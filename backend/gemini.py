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
You are an expert Medical Laboratory Scientist. Analyze the following extracted text from a medical lab report. 
Your goal is to provide a structured, accurate, and consistent analysis.

### INSTRUCTIONS:
1. Extract all tests, values, units, and reference ranges.
2. For each test, determine its status: "Normal", "Low", "High", or "Borderline".
3. Calculate an Overall Risk Level based on the abnormalities:
   - "Low Risk": All or almost all values are normal.
   - "Moderate Risk": Multiple minor deviations (Borderline/Mild Low/High) or 1-2 significant deviations.
   - "High Risk": Critical markers (e.g., Creatinine, Troponin, CRP) are high, or many values are severely abnormal.
4. Provide a "summary" that is consistent with the Overall Risk. If you mark it as "High Risk", the summary must reflect that.
5. Identify the "specialist" most relevant to the abnormalities (e.g., Cardiologist for heart, Endocrinologist for sugar/thyroid, Nephrologist for kidney, Hematologist for blood).
6. Ensure the "urgency" matches the Risk Level: "routine" for Low, "follow-up" for Moderate, "urgent" for High.

### RESPONSE FORMAT (STRICT JSON ONLY):
{{
  "valid_data": true,
  "report_type": "e.g., Complete Blood Count, Metabolic Panel",
  "patient_info": {{
    "name": "Full Name",
    "age": "Age with unit",
    "sex": "M/F",
    "date": "YYYY-MM-DD"
  }},
  "overall_risk": "Low" | "Moderate" | "High",
  "summary": "A cohesive 2-3 sentence explanation of the findings.",
  "tests": [
    {{
      "name": "Exact Test Name",
      "value": "Numeric Value",
      "unit": "Unit",
      "ref_range": "Range",
      "status": "Normal" | "Low" | "High" | "Borderline"
    }}
  ],
  "lifestyle": ["Specific actionable tip 1", "Specific actionable tip 2", "Specific actionable tip 3"],
  "specialist": "Most appropriate single medical specialty",
  "urgency": "routine" | "follow-up" | "urgent",
  "disclaimer": "Educational purposes only. Consult a physician."
}}

If the text does not look like a medical lab report or is completely unreadable, return: {{"valid_data": false}}

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
