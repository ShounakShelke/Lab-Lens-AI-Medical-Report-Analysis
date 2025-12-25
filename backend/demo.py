"""
Demo Endpoints for Lab-Lens
Provides pre-configured demo data for testing and demonstrations.
"""

from flask import Blueprint, jsonify

demo_bp = Blueprint("demo", __name__)


DEMO_LOW_RISK = {
    "id": "demo-low-001",
    "tests": [
        {"name": "Hemoglobin", "value": "14.5", "unit": "g/dL", "ref_range": "12-16", "status": "Normal"},
        {"name": "RBC Count", "value": "4.8", "unit": "million/cu mm", "ref_range": "4.5-5.5", "status": "Normal"},
        {"name": "WBC Count", "value": "7000", "unit": "/cu mm", "ref_range": "4000-11000", "status": "Normal"},
        {"name": "Platelets", "value": "250000", "unit": "/cu mm", "ref_range": "150000-400000", "status": "Normal"},
        {"name": "Fasting Blood Sugar", "value": "92", "unit": "mg/dL", "ref_range": "70-100", "status": "Normal"},
        {"name": "Total Cholesterol", "value": "180", "unit": "mg/dL", "ref_range": "<200", "status": "Normal"},
        {"name": "HDL Cholesterol", "value": "55", "unit": "mg/dL", "ref_range": ">40", "status": "Normal"},
    ],
    "riskSummary": {
        "overallRisk": "Low",
        "bannerMessage": "LOW RISK PROFILE",
        "severityBannerColor": "green",
        "normalCount": 7,
        "borderlineCount": 0,
        "highCount": 0,
        "recommendedSpecialist": "General Physician"
    },
    "summary": "All your lab values are within normal ranges. Your blood count, blood sugar, and lipid profile all show healthy levels. Continue maintaining your current healthy lifestyle with regular exercise, balanced nutrition, and adequate sleep.",
    "lifestyle": [
        "Continue with regular physical activity (30 minutes daily)",
        "Maintain a balanced diet rich in fruits, vegetables, and whole grains",
        "Stay hydrated with 8 glasses of water daily",
        "Get 7-8 hours of quality sleep each night",
        "Schedule routine annual check-ups to maintain good health"
    ],
    "recommendedSpecialist": "General Physician",
    "disclaimer": "This is a demo report. For actual medical advice, consult a healthcare professional."
}

DEMO_MODERATE_RISK = {
    "id": "demo-moderate-001",
    "tests": [
        {"name": "Total Cholesterol", "value": "215", "unit": "mg/dL", "ref_range": "<200", "status": "Borderline"},
        {"name": "LDL Cholesterol", "value": "135", "unit": "mg/dL", "ref_range": "<100", "status": "Borderline"},
        {"name": "HDL Cholesterol", "value": "42", "unit": "mg/dL", "ref_range": ">40", "status": "Normal"},
        {"name": "Triglycerides", "value": "165", "unit": "mg/dL", "ref_range": "<150", "status": "Borderline"},
        {"name": "Fasting Blood Sugar", "value": "108", "unit": "mg/dL", "ref_range": "70-100", "status": "Borderline"},
        {"name": "Hemoglobin", "value": "13.5", "unit": "g/dL", "ref_range": "12-16", "status": "Normal"},
        {"name": "hs-CRP", "value": "1.8", "unit": "mg/L", "ref_range": "<1.0", "status": "Borderline"},
    ],
    "riskSummary": {
        "overallRisk": "Moderate",
        "bannerMessage": "MODERATE RISK - LIFESTYLE CHANGES RECOMMENDED",
        "severityBannerColor": "yellow",
        "normalCount": 2,
        "borderlineCount": 5,
        "highCount": 0,
        "recommendedSpecialist": "Internal Medicine"
    },
    "summary": "Your lipid profile shows borderline elevated levels of Total Cholesterol, LDL (bad cholesterol), and Triglycerides. Your fasting blood sugar is also slightly above the optimal range. These patterns may indicate early metabolic changes that can be managed effectively with lifestyle modifications. The mild elevation in hs-CRP suggests low-grade inflammation.",
    "lifestyle": [
        "Reduce intake of saturated fats and processed foods",
        "Increase consumption of omega-3 rich foods (fish, walnuts, flaxseed)",
        "Aim for 45 minutes of moderate cardio exercise 5 days a week",
        "Limit refined carbohydrates and sugary beverages",
        "Consider adding fiber supplements or oatmeal to your diet",
        "Schedule a follow-up lipid panel in 3 months"
    ],
    "recommendedSpecialist": "Internal Medicine",
    "disclaimer": "This is a demo report. For actual medical advice, consult a healthcare professional."
}

DEMO_HIGH_RISK = {
    "id": "demo-high-001",
    "tests": [
        {"name": "Total Cholesterol", "value": "285", "unit": "mg/dL", "ref_range": "<200", "status": "High"},
        {"name": "LDL Cholesterol", "value": "195", "unit": "mg/dL", "ref_range": "<100", "status": "High"},
        {"name": "HDL Cholesterol", "value": "32", "unit": "mg/dL", "ref_range": ">40", "status": "Low"},
        {"name": "Triglycerides", "value": "280", "unit": "mg/dL", "ref_range": "<150", "status": "High"},
        {"name": "hs-CRP", "value": "4.5", "unit": "mg/L", "ref_range": "<1.0", "status": "High"},
        {"name": "Homocysteine", "value": "18", "unit": "micromol/L", "ref_range": "<15", "status": "High"},
        {"name": "Lp(a)", "value": "55", "unit": "mg/dL", "ref_range": "<30", "status": "High"},
    ],
    "riskSummary": {
        "overallRisk": "High",
        "bannerMessage": "HIGH CARDIOVASCULAR RISK DETECTED",
        "severityBannerColor": "red",
        "normalCount": 0,
        "borderlineCount": 0,
        "highCount": 7,
        "recommendedSpecialist": "Cardiologist"
    },
    "summary": "Your lipid panel reveals significantly elevated cardiovascular risk markers. Total Cholesterol, LDL, and Triglycerides are all substantially above recommended levels, while HDL (protective cholesterol) is low. Inflammatory markers hs-CRP and Homocysteine are elevated, suggesting active vascular inflammation. Elevated Lp(a) is an independent genetic risk factor. URGENT consultation with a cardiologist is strongly recommended.",
    "lifestyle": [
        "URGENT: Schedule an appointment with a cardiologist immediately",
        "Adopt a strict Mediterranean or DASH diet",
        "Complete elimination of trans fats and limit saturated fats",
        "Begin supervised cardiovascular exercise program",
        "Avoid smoking and limit alcohol consumption",
        "Monitor blood pressure regularly",
        "Consider discussing statin therapy with your doctor"
    ],
    "recommendedSpecialist": "Cardiologist",
    "disclaimer": "This is a demo report showing high-risk markers. For actual medical emergencies, seek immediate medical attention."
}


@demo_bp.route("/low-risk")
def demo_low():
    """Returns a demo report with low risk profile"""
    return jsonify({
        "success": True,
        "data": DEMO_LOW_RISK
    })


@demo_bp.route("/moderate-risk")
def demo_moderate():
    """Returns a demo report with moderate risk profile"""
    return jsonify({
        "success": True,
        "data": DEMO_MODERATE_RISK
    })


@demo_bp.route("/high-risk")
def demo_high():
    """Returns a demo report with high cardiovascular risk profile"""
    return jsonify({
        "success": True,
        "data": DEMO_HIGH_RISK
    })


@demo_bp.route("/all")
def demo_all():
    """Returns all demo profiles for testing"""
    return jsonify({
        "success": True,
        "data": {
            "low": DEMO_LOW_RISK,
            "moderate": DEMO_MODERATE_RISK,
            "high": DEMO_HIGH_RISK
        }
    })
