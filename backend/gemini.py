"""
LAB-LENS AI Analysis Module  
Uses Google Gemini for medical report analysis and chat
With robust fallback to demo data when API unavailable
"""
import os
import json
import google.generativeai as genai
from dotenv import load_dotenv
from demo_data import get_demo_report, get_demo_chat_response

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY") or os.getenv("API_KEY")
API_WORKING = False

if not API_KEY:
    print("WARNING: No API key found. Using demo mode.")
else:
    try:
        genai.configure(api_key=API_KEY)
        print("Gemini AI configured successfully")
        API_WORKING = True
    except Exception as e:
        print(f"Gemini config failed: {e}. Using demo mode.")


text_model = None
if API_WORKING:
    try:
        # Using a lower temperature for medical analysis to ensure consistency and reduce hallucinations
        generation_config = {
            "temperature": 0.1,
            "top_p": 0.95,
            "top_k": 40,
            "max_output_tokens": 2048,
        }
        text_model = genai.GenerativeModel(
            model_name='gemini-1.5-flash',
            generation_config=generation_config
        )
        print(f"Text model initialized: gemini-1.5-flash (Low Temp)")
    except Exception as e:
        print(f"Model init failed: {e}. Using demo mode.")
        API_WORKING = False


def analyze_lab_report(text_content, filename=None):
    """
    Analyze extracted medical report text.
    Returns JSON with patient info, tests, and recommendations.
    Falls back to demo data if API fails.
    """
    print(f"analyze_lab_report called with {len(text_content)} characters")

    if API_WORKING and text_model:
        try:
            prompt = f"""
You are an expert Medical Laboratory Scientist using the Lab-Lens Precision Engine. 
Analyze the following extracted text from a medical lab report with 100% accuracy.

### CRITICAL EXTRACTION RULES:
1. **ZERO HALLUCINATION**: ONLY extract tests that are explicitly written in the text. DO NOT assume or fabricate values for missing tests (e.g., if MCV is not in the text, do not include it).
2. **UNIT NORMALIZATION**: Convert values to standard concentrations if necessary.
   - If WBC is 9,600 /µL, extract as 9.6 (Unit: x10^9/L).
   - If Platelets are 250,000 /µL, extract as 250 (Unit: x10^9/L).
   - Always extract numeric values exactly as they appear for Hemoglobin.
3. **MAPPING**: Capture "Test Name", "Result", "Unit", and "Reference Range" as separate fields.
4. **STATUS**: Assign "Normal", "Low", "High", or "Borderline" based on the provided reference ranges.
5. **COMPLETENESS**: Ensure Biochemistry (Sugar, Urea, Creatinine), Serology, and Microscopy are all captured if present.

### ANALYTICAL RULES:
1. **NO DIAGNOSTIC LABELING**: DO NOT use disease names (e.g., Anemia, Diabetes, Hypothyroidism, Lupus). Instead, describe the result objectively (e.g., "reduced oxygen-carrying markers", "elevated metabolic values").
2. **Risk Level**: 
  - "Low": All markers optimal.
  - "Moderate": Minor deviations or common imbalances.
  - "High": Critical values detected (e.g., extremely high Creatinine, Troponin, or PSA).
3. **Specialist**: Recommend ONE specific specialist based on the most abnormal marker.
4. **Summary**: Concise explanation. Use "Your results show..." and avoid definitive medical terms.

### RESPONSE FORMAT (STRICT JSON ONLY):
{{
  "valid_data": true,
  "report_type": "Exact type detected",
  "patient_info": {{
    "name": "Full Name",
    "age": "Age",
    "sex": "M/F/Unknown",
    "date": "YYYY-MM-DD"
  }},
  "overall_risk": "Low" | "Moderate" | "High",
  "summary": "2-3 sentences max.",
  "tests": [
    {{
      "name": "Exact Test Name",
      "value": "Numeric Value",
      "unit": "Unit",
      "ref_range": "Reference Range",
      "status": "Level"
    }}
  ],
  "lifestyle": ["Tip 1", "Tip 2", "Tip 3"],
  "specialist": "Specialist Name",
  "urgency": "routine" | "follow-up" | "urgent"
}}

REPORT TEXT:
{text_content}

JSON Response:
"""
            
            response = text_model.generate_content(prompt)
            response_text = response.text
            
            # Extract JSON from response if it's wrapped in markers
            if "```json" in response_text:
                response_text = response_text.split("```json")[1].split("```")[0].strip()
            elif "```" in response_text:
                response_text = response_text.split("```")[1].split("```")[0].strip()

            try:
                result = json.loads(response_text)
                if result.get('valid_data'):
                    print(f"AI Analysis complete: valid_data=True, risk={result.get('overall_risk')}")
                    return result
            except json.JSONDecodeError:
                # Fallback extraction logic
                if '{' in response_text and '}' in response_text:
                    start = response_text.index('{')
                    end = response_text.rindex('}') + 1
                    try:
                        result = json.loads(response_text[start:end])
                        if result.get('valid_data'):
                             print(f"AI Analysis complete (extracted): risk={result.get('overall_risk')}")
                             return result
                    except:
                        pass
            
            print("AI response invalid, falling back to demo data")
            
        except Exception as e:
            print(f"AI Analysis error: {e}. Using demo data.")
    
    # Fallback to demo data
    print(f"Using demo data for analysis (filename: {filename})")
    from demo_data import get_demo_report
    
    # Improved filename matching for demo
    risk_lvl = None
    if filename:
        fn = filename.lower()
        if 'high' in fn or 'critical' in fn: risk_lvl = 'high'
        elif 'low' in fn or 'normal' in fn: risk_lvl = 'low'
        elif 'moderate' in fn or 'medium' in fn: risk_lvl = 'moderate'
        
    return get_demo_report(filename=filename, risk_level=risk_lvl)


def chat_with_context(message, report_context):
    """
    Medical Q&A chatbot with report context.
    Falls back to demo responses if API unavailable.
    """
    print(f"chat_with_context called with message: {message[:50]}...")
    

    if API_WORKING and text_model:
        try:
            context = ""
            if report_context and isinstance(report_context, dict):
                context = f"""
REPORT CONTEXT:
Patient: {report_context.get('patient', {}).get('name', 'User')}
Type: {report_context.get('report_type', 'Medical Report')}
Risk: {report_context.get('riskSummary', {}).get('overallRisk', 'Unknown')}

Tests (sample):
"""
                tests = report_context.get('tests', [])[:3]
                for t in tests:
                    if isinstance(t, dict):
                        context += f"- {t.get('name')}: {t.get('value')} {t.get('unit')}\n"
            
            full_prompt = f"""{context}

USER QUESTION: {message}

Respond in this JSON format:
{{
  "reply": "Your helpful medical explanation in simple terms",
  "suggestions": ["Question 1?", "Question 2?", "Question 3?"]
}}

Rules:
- Be warm and educational
- Never diagnose or prescribe
- Refer to report values when relevant
- End with: "Consult your doctor for medical advice."

JSON Response:
"""
            
            response = text_model.generate_content(full_prompt)
            text = response.text
            
            if '{' in text and '}' in text:
                start = text.index('{')
                end = text.rindex('}') + 1
                result = json.loads(text[start:end])
                
                if "reply" in result:
                    if "suggestions" not in result:
                        result["suggestions"] = ["What do my results mean?", "Should I be worried?", "What can I do to improve?"]
                    print(f"✓ AI Chat response generated")
                    return result
        
        except Exception as e:
            print(f"⚠️ AI Chat error: {e}. Using demo response.")
    

    print(f"💬 Using demo chat response")
    return get_demo_chat_response(message, report_context)
