from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import json
import os
import uuid
import datetime
from dotenv import load_dotenv

load_dotenv()

from gemini import analyze_lab_report, chat_with_context
from ocr import extract_text_from_image
from severity import calculate_risk_level

app = Flask(__name__)

# Production CORS setup
allowed_origins = os.getenv("ALLOWED_ORIGINS", "*").split(",")
CORS(app, resources={r"/api/*": {"origins": allowed_origins}}, supports_credentials=True)
# Also apply to other routes if needed
CORS(app) 

import pymongo
from pymongo import MongoClient

REPORTS_FILE = 'reports.json'
MONGO_URI = os.getenv("MONGO_URI")
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME", "cortex_lmh")

# Initialize MongoDB
db_client = None
reports_collection = None

if MONGO_URI:
    try:
        db_client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
        # Force a connection check
        db_client.server_info()
        db = db_client[MONGO_DB_NAME]
        reports_collection = db['reports']
        print(f"✅ Connected to MongoDB Atlas: {MONGO_DB_NAME}")
    except Exception as e:
        print(f"⚠️ MongoDB Connection failed: {e}. Falling back to local JSON.")

def get_all_reports():
    """Fetch all reports from MongoDB or local JSON fallback."""
    if reports_collection is not None:
        try:
            return list(reports_collection.find({}, {'_id': 0}).sort('createdAt', -1))
        except Exception as e:
            print(f"Error reading from MongoDB: {e}")
    
    # Fallback to local JSON
    if os.path.exists(REPORTS_FILE):
         with open(REPORTS_FILE, 'r') as f:
            try: return json.load(f)
            except: return []
    return []

def save_report_data(data):
    """Save report to MongoDB or local JSON fallback."""
    if reports_collection is not None:
        try:
            reports_collection.insert_one(data.copy())
            print(f"✓ Report saved to MongoDB Atlas")
            return True
        except Exception as e:
            print(f"Error saving to MongoDB: {e}")

    # Fallback to local JSON
    try:
        reports = []
        if os.path.exists(REPORTS_FILE):
            with open(REPORTS_FILE, 'r') as f:
                reports = json.load(f)
        reports.append(data)
        with open(REPORTS_FILE, 'w') as f:
            json.dump(reports, f, indent=4)
        return True
    except Exception as e:
        print(f"Error saving report locally: {e}")
        return False

def get_report_by_id(report_id):
    """Retrieve a single report by ID."""
    if reports_collection is not None:
        try:
            return reports_collection.find_one({"id": report_id}, {'_id': 0})
        except Exception as e:
            print(f"Error finding report in MongoDB: {e}")

    # Fallback to local JSON
    reports = get_all_reports()
    return next((r for r in reports if r.get('id') == report_id), None)


@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "healthy", "team": "Cortex LMH"})

@app.route('/api/history', methods=['GET'])
def get_history():
    reports = get_all_reports()
    return jsonify({"success": True, "data": reports[::-1]})

@app.route('/api/reports/<report_id>', methods=['GET'])
def get_report(report_id):
    report = get_report_by_id(report_id)
    if report:
        return jsonify({"success": True, "data": report})
    return jsonify({"error": "Report not found"}), 404

@app.route('/api/analyze', methods=['POST'])
def analyze():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    
    file = request.files['file']
    filename = file.filename
    safe_filename = str(uuid.uuid4()) + "_" + filename 
    
    if not os.path.exists('uploads'):
         os.makedirs('uploads')
         
    filepath = os.path.join('uploads', safe_filename)
    file.save(filepath)

    try:
        text = extract_text_from_image(filepath)
        
        # We no longer force demo mode based on filenames to avoid confusion with real reports
        # Only analyze with AI
        print(f"Running Lab-Lens AI Intelligence for: {filename}")
        raw_analysis = analyze_lab_report(text, filename=filename)

        # Safety Fallback: Do not show a scary demo report if real analysis fails.
        if not raw_analysis or not raw_analysis.get('tests'):
            print("⚠️ Analysis failed. Using neutral safety fallback.")
            raw_analysis = {
                "valid_data": True,
                "report_type": "Report Analysis Unavailable",
                "summary": "We were able to process your file, but our AI couldn't generate a confident clinical summary for this specific format. Please review the raw values with a healthcare professional.",
                "tests": [],
                "overall_risk": "Low",
                "specialist": "General Physician",
                "urgency": "routine",
                "lifestyle": ["Ask your doctor to help interpret these results.", "Maintain a regular health check-up schedule."]
            }

        # Standard Processing
        tests = raw_analysis.get('tests', [])
        risk_summary, processed_tests = calculate_risk_level(tests)
        
        # Priority 1: Use AI's explicit overall_risk if available
        # Priority 2: Use calculated risk from severity.py
        ai_risk = raw_analysis.get('overall_risk')
        if ai_risk:
            risk_summary['overallRisk'] = ai_risk
            # Align banner colors with AI risk
            if "High" in ai_risk:
                risk_summary['severityBannerColor'] = "red"
                risk_summary['bannerMessage'] = "CRITICAL FINDINGS DETECTED"
            elif "Moderate" in ai_risk:
                risk_summary['severityBannerColor'] = "yellow"
                risk_summary['bannerMessage'] = "MODERATE DEVIATIONS DETECTED"
            else:
                risk_summary['severityBannerColor'] = "green"
                risk_summary['bannerMessage'] = "OPTIMAL HEALTH PROFILE"

        report_id = str(uuid.uuid4())
        final_report = {
            "id": report_id,
            "reportId": report_id,
            "patient": raw_analysis.get('patient_info', {"name": "Patient", "age": "--", "sex": "--"}),
            "tests": processed_tests,
            "riskSummary": risk_summary,
            "recommendedSpecialist": raw_analysis.get('specialist') or risk_summary['recommendedSpecialist'],
            "summary": raw_analysis.get('summary', 'Analysis completed.'),
            "lifestyle": raw_analysis.get('lifestyle', []),
            "urgency": raw_analysis.get('urgency', 'routine'),
            "reportType": raw_analysis.get('report_type', 'Medical Report'),
            "disclaimer": "This is not a medical diagnosis. Consult a doctor.",
            "createdAt": datetime.datetime.now().isoformat(),
            "imageUrl": f"/uploads/{safe_filename}",
            "filename": filename
        }

        save_report_data(final_report)
        print(f"Analysis complete! Report ID: {report_id} | Risk: {risk_summary['overallRisk']}")

        return jsonify({"success": True, "data": final_report, "reportId": report_id})
        
    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({"error": str(e), "success": False}), 500

@app.route('/uploads/<path:filename>')
def serve_upload(filename):
    return send_from_directory('uploads', filename)

@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        user_msg = data.get('message', '')
        report_id = data.get('reportId')
        context = get_report_by_id(report_id)
        response_data = chat_with_context(user_msg, context)
        return jsonify({"success": True, "reply": response_data.get('reply', 'I can help you understand your lab results.'), "suggestions": response_data.get('suggestions', ["What do my results mean?", "Should I be worried?"])})
    except Exception as e:
        return jsonify({"success": True, "reply": "I'm here to help you understand your lab results. Consult your doctor for medical advice.", "suggestions": ["What do my results mean?", "Should I be worried?"]})

@app.route('/api/demo/low-risk', methods=['GET'])
def demo_low():
    return jsonify({"success": True, "data": {"tests": [{"name": "Total Cholesterol", "value": 180, "unit": "mg/dL", "status": "Normal"}], "riskSummary": {"overallRisk": "Low", "bannerMessage": "LOW RISK PROFILE", "severityBannerColor": "green"}, "recommendedSpecialist": "General Physician", "summary": "All values are within normal limits."}})

@app.route('/api/demo/moderate-risk', methods=['GET'])
def demo_moderate():
    return jsonify({"success": True, "data": {"tests": [{"name": "Total Cholesterol", "value": 210, "unit": "mg/dL", "status": "Borderline"}], "riskSummary": {"overallRisk": "Moderate", "bannerMessage": "MODERATE CARDIOVASCULAR RISK DETECTED", "severityBannerColor": "yellow"}, "recommendedSpecialist": "Internal Medicine", "summary": "Borderline lipid levels detected."}})

@app.route('/api/demo/high-risk', methods=['GET'])
def demo_high():
    return jsonify({"success": True, "data": {"tests": [{"name": "Total Cholesterol", "value": 260, "unit": "mg/dL", "status": "High"}], "riskSummary": {"overallRisk": "High", "bannerMessage": "HIGH CARDIOVASCULAR RISK DETECTED", "severityBannerColor": "red"}, "recommendedSpecialist": "Cardiologist", "summary": "Critical markers detected."}})


if __name__ == '__main__':
    if not os.path.exists(REPORTS_FILE): 
        with open(REPORTS_FILE, 'w') as f: json.dump([], f)
    
    is_production = os.environ.get('RENDER', False) or os.environ.get('PRODUCTION', False)
    port = int(os.environ.get('PORT', 5000))
    
    print("=" * 60)
    print("LAB-LENS BACKEND v1.17")
    print("=" * 60)
    print(f"Mode: {'PRODUCTION' if is_production else 'DEVELOPMENT'}")
    print(f"Port: {port}")
    print("PNG Demo: high_risk, moderate, low_risk, abs")
    print("PDF Demo: reports-1 to reports-6")
    print("=" * 60)
    
    app.run(host='0.0.0.0', debug=not is_production, port=port)
