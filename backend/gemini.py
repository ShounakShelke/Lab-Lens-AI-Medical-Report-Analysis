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
        text_model = genai.GenerativeModel('gemini-1.5-flash')
        print(f"Text model initialized: gemini-1.5-flash")
    except Exception as e:
        print(f"Model init failed: {e}. Using demo mode.")
        API_WORKING = False


def analyze_lab_report(text_content, filename=None):
    """
    Analyze extracted medical report text.
    Returns JSON with patient info, tests, and recommendations.
    Falls back to demo data if API fails.
    """
    print(f"analyze_lab_report called with {len(text_content)} chars")
    

    if API_WORKING and text_model:
        try:
            prompt = f"""
You are a medical lab report analyzer. Analyze this report and return ONLY valid JSON in this exact format:

{{
  "valid_data": true,
  "report_type": "Blood Test" or "Metabolic Panel" etc,
  "patient_info": {{
    "name": "found name or null",
    "age": "found age or null",
    "sex": "M/F or null",
    "date": "YYYY-MM-DD or null"
  }},
  "summary": "Brief summary in simple language",
  "tests": [
    {{
      "name": "Test Name",
      "value": "12.5",
      "unit": "g/dL",
      "ref_range": "13-17",
      "status": "Low"
    }}
  ],
  "lifestyle": ["Tip 1", "Tip 2", "Tip 3"],
  "specialist": "Hematologist" or "General Physician",
  "urgency": "routine",
  "disclaimer": "This is educational only. Consult a doctor."
}}

If not a medical report, return: {{"valid_data": false}}

Report Text:
{text_content}

Return JSON only:
"""
            
            response = text_model.generate_content(prompt)
            response_text = response.text
            
            try:
                result = json.loads(response_text)
                if result.get('valid_data'):
                    print(f"AI Analysis complete: valid_data=True")
                    return result
            except json.JSONDecodeError:

                if '{' in response_text and '}' in response_text:
                    start = response_text.index('{')
                    end = response_text.rindex('}') + 1
                    try:
                        result = json.loads(response_text[start:end])
                        if result.get('valid_data'):
                            print(f"AI Analysis complete (extracted): valid_data=True")
                            return result
                    except:
                        pass
            
            print("AI response invalid, falling back to demo data")
            
        except Exception as e:
            print(f"AI Analysis error: {e}. Using demo data.")
    

    print(f"Using demo data for analysis (filename: {filename})")
    demo_report = get_demo_report(filename=filename)
    return demo_report


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
