"""
Demo/Fallback Data for Lab-Lens
Pre-configured medical report analysis results for reliable demo experience
"""

import random
from datetime import datetime


SAMPLE_NAMES = ["John Smith", "Sarah Johnson", "Michael Chen", "Emily Davis", "Raj Patel", "Lisa Wong"]

def get_random_patient():
    return {
        "name": random.choice(SAMPLE_NAMES),
        "age": str(random.randint(25, 65)),
        "sex": random.choice(["M", "F"]),
        "date": datetime.now().strftime("%Y-%m-%d")
    }


LOW_RISK_REPORT = {
    "valid_data": True,
    "report_type": "Complete Blood Count (CBC)",
    "patient_info": {"name": "Healthy Individual", "age": "32", "sex": "M", "date": None},
    "summary": "Your blood test results look excellent! All major parameters are within healthy ranges. Your hemoglobin, white blood cells, and platelet counts are all optimal, indicating good overall health.",
    "tests": [
        {"name": "Hemoglobin", "value": "14.5", "unit": "g/dL", "ref_range": "13.0-17.0", "status": "Normal"},
        {"name": "RBC Count", "value": "5.2", "unit": "million/µL", "ref_range": "4.5-5.5", "status": "Normal"},
        {"name": "WBC Count", "value": "7500", "unit": "/µL", "ref_range": "4000-11000", "status": "Normal"},
        {"name": "Platelet Count", "value": "250000", "unit": "/µL", "ref_range": "150000-400000", "status": "Normal"},
        {"name": "Hematocrit (PCV)", "value": "44", "unit": "%", "ref_range": "38-50", "status": "Normal"},
        {"name": "MCV", "value": "88", "unit": "fL", "ref_range": "80-100", "status": "Normal"},
        {"name": "MCH", "value": "29", "unit": "pg", "ref_range": "27-33", "status": "Normal"},
        {"name": "MCHC", "value": "33", "unit": "g/dL", "ref_range": "32-36", "status": "Normal"},
    ],
    "lifestyle": [
        "Continue your current healthy lifestyle and balanced diet",
        "Stay hydrated with 8-10 glasses of water daily",
        "Maintain regular physical activity of 30 minutes daily",
        "Get 7-8 hours of quality sleep each night"
    ],
    "specialist": "General Wellness",
    "urgency": "routine",
    "disclaimer": "This is an AI-generated analysis for educational purposes. Always consult your healthcare provider."
}


MODERATE_RISK_REPORT = {
    "valid_data": True,
    "report_type": "Comprehensive Metabolic Panel",
    "patient_info": {"name": "Sample Patient", "age": "45", "sex": "F", "date": None},
    "summary": "Your metabolic panel shows some values that need attention. Your blood sugar and cholesterol levels are slightly elevated, which may benefit from lifestyle modifications. Consider dietary changes and regular monitoring.",
    "tests": [
        {"name": "Fasting Blood Sugar", "value": "118", "unit": "mg/dL", "ref_range": "70-100", "status": "High"},
        {"name": "Total Cholesterol", "value": "225", "unit": "mg/dL", "ref_range": "0-200", "status": "High"},
        {"name": "LDL Cholesterol", "value": "145", "unit": "mg/dL", "ref_range": "0-100", "status": "High"},
        {"name": "HDL Cholesterol", "value": "42", "unit": "mg/dL", "ref_range": "40-60", "status": "Borderline"},
        {"name": "Triglycerides", "value": "165", "unit": "mg/dL", "ref_range": "0-150", "status": "High"},
        {"name": "Creatinine", "value": "0.9", "unit": "mg/dL", "ref_range": "0.6-1.2", "status": "Normal"},
        {"name": "Urea", "value": "32", "unit": "mg/dL", "ref_range": "15-45", "status": "Normal"},
        {"name": "Uric Acid", "value": "5.8", "unit": "mg/dL", "ref_range": "2.4-7.0", "status": "Normal"},
    ],
    "lifestyle": [
        "Reduce refined carbohydrates and sugary foods",
        "Include more fiber-rich vegetables and whole grains",
        "Engage in 45 minutes of moderate exercise 5 days a week",
        "Consider reducing saturated fat intake",
        "Schedule a follow-up test in 3 months"
    ],
    "specialist": "Internal Medicine / Endocrinologist",
    "urgency": "follow-up recommended",
    "disclaimer": "This is an AI-generated analysis for educational purposes. Always consult your healthcare provider."
}


HIGH_RISK_REPORT = {
    "valid_data": True,
    "report_type": "Complete Health Profile",
    "patient_info": {"name": "Priority Care Patient", "age": "55", "sex": "M", "date": None},
    "summary": "Several critical markers in your report require immediate medical attention. Your kidney function markers and blood sugar levels are significantly elevated. Please consult a specialist promptly for proper evaluation and treatment planning.",
    "tests": [
        {"name": "Creatinine", "value": "2.8", "unit": "mg/dL", "ref_range": "0.6-1.2", "status": "High"},
        {"name": "Blood Urea", "value": "78", "unit": "mg/dL", "ref_range": "15-45", "status": "High"},
        {"name": "eGFR", "value": "45", "unit": "mL/min", "ref_range": "90-120", "status": "Low"},
        {"name": "Fasting Glucose", "value": "186", "unit": "mg/dL", "ref_range": "70-100", "status": "High"},
        {"name": "HbA1c", "value": "8.2", "unit": "%", "ref_range": "4.0-5.6", "status": "High"},
        {"name": "Potassium", "value": "5.8", "unit": "mEq/L", "ref_range": "3.5-5.0", "status": "High"},
        {"name": "Hemoglobin", "value": "10.5", "unit": "g/dL", "ref_range": "13.0-17.0", "status": "Low"},
        {"name": "CRP", "value": "12.5", "unit": "mg/L", "ref_range": "0-3.0", "status": "High"},
    ],
    "lifestyle": [
        "URGENT: Schedule an appointment with a nephrologist",
        "Monitor blood pressure daily and maintain records",
        "Follow a renal-friendly diet (low sodium, low potassium)",
        "Strict blood sugar monitoring is essential",
        "Avoid NSAIDs and over-the-counter pain medications",
        "Stay well hydrated unless advised otherwise by doctor"
    ],
    "specialist": "Nephrologist / Endocrinologist - Urgent",
    "urgency": "urgent",
    "disclaimer": "This is an AI-generated analysis for educational purposes. These results indicate conditions requiring immediate medical attention. Please consult your healthcare provider promptly."
}


THYROID_REPORT = {
    "valid_data": True,
    "report_type": "Thyroid Function Test",
    "patient_info": {"name": "Thyroid Check", "age": "38", "sex": "F", "date": None},
    "summary": "Your thyroid panel shows elevated TSH with low T4, which may indicate hypothyroidism (underactive thyroid). Common symptoms include fatigue, weight gain, and feeling cold. This condition is very manageable with proper treatment.",
    "tests": [
        {"name": "TSH", "value": "8.5", "unit": "µIU/mL", "ref_range": "0.4-4.0", "status": "High"},
        {"name": "Free T4", "value": "0.6", "unit": "ng/dL", "ref_range": "0.8-1.8", "status": "Low"},
        {"name": "Free T3", "value": "1.8", "unit": "pg/mL", "ref_range": "2.0-4.4", "status": "Low"},
        {"name": "Total T4", "value": "4.2", "unit": "µg/dL", "ref_range": "5.0-12.0", "status": "Low"},
        {"name": "Anti-TPO", "value": "85", "unit": "IU/mL", "ref_range": "0-35", "status": "High"},
    ],
    "lifestyle": [
        "Consult an endocrinologist for proper thyroid medication",
        "Take thyroid medication on empty stomach in the morning",
        "Include selenium-rich foods like Brazil nuts",
        "Regular exercise can help manage symptoms",
        "Get thyroid levels rechecked after 6-8 weeks of treatment"
    ],
    "specialist": "Endocrinologist",
    "urgency": "follow-up recommended",
    "disclaimer": "This is an AI-generated analysis for educational purposes. Thyroid conditions are very treatable. Please consult your healthcare provider."
}


LIVER_REPORT = {
    "valid_data": True,
    "report_type": "Liver Function Test",
    "patient_info": {"name": "Liver Panel", "age": "42", "sex": "M", "date": None},
    "summary": "Your liver enzymes are elevated, which may indicate liver stress. This could be due to various factors including diet, medications, or lifestyle. Further evaluation is recommended to determine the cause.",
    "tests": [
        {"name": "SGPT (ALT)", "value": "85", "unit": "U/L", "ref_range": "7-56", "status": "High"},
        {"name": "SGOT (AST)", "value": "72", "unit": "U/L", "ref_range": "10-40", "status": "High"},
        {"name": "Alkaline Phosphatase", "value": "145", "unit": "U/L", "ref_range": "44-147", "status": "Borderline"},
        {"name": "Total Bilirubin", "value": "1.4", "unit": "mg/dL", "ref_range": "0.1-1.2", "status": "High"},
        {"name": "Direct Bilirubin", "value": "0.4", "unit": "mg/dL", "ref_range": "0-0.3", "status": "High"},
        {"name": "Albumin", "value": "3.8", "unit": "g/dL", "ref_range": "3.5-5.0", "status": "Normal"},
        {"name": "Total Protein", "value": "7.2", "unit": "g/dL", "ref_range": "6.0-8.3", "status": "Normal"},
    ],
    "lifestyle": [
        "Avoid alcohol completely until liver enzymes normalize",
        "Reduce fatty and fried foods",
        "Stay hydrated with plenty of water",
        "Consider liver-protective foods like garlic and green tea",
        "Review all medications with your doctor",
        "Retest liver function in 4-6 weeks"
    ],
    "specialist": "Gastroenterologist / Hepatologist",
    "urgency": "follow-up recommended",
    "disclaimer": "This is an AI-generated analysis for educational purposes. Elevated liver enzymes require medical evaluation. Please consult your healthcare provider."
}


LIPID_REPORT = {
    "valid_data": True,
    "report_type": "Lipid Profile",
    "patient_info": {"name": "Cardiac Risk Assessment", "age": "50", "sex": "M", "date": None},
    "summary": "Your lipid profile shows elevated cholesterol levels indicating increased cardiovascular risk. The good news is that cholesterol can often be managed effectively with lifestyle changes and, if needed, medication.",
    "tests": [
        {"name": "Total Cholesterol", "value": "265", "unit": "mg/dL", "ref_range": "0-200", "status": "High"},
        {"name": "LDL Cholesterol", "value": "175", "unit": "mg/dL", "ref_range": "0-100", "status": "High"},
        {"name": "HDL Cholesterol", "value": "38", "unit": "mg/dL", "ref_range": "40-60", "status": "Low"},
        {"name": "VLDL Cholesterol", "value": "52", "unit": "mg/dL", "ref_range": "5-40", "status": "High"},
        {"name": "Triglycerides", "value": "260", "unit": "mg/dL", "ref_range": "0-150", "status": "High"},
        {"name": "LDL/HDL Ratio", "value": "4.6", "unit": "", "ref_range": "0-3.5", "status": "High"},
    ],
    "lifestyle": [
        "Follow a heart-healthy Mediterranean diet",
        "Increase omega-3 fatty acids (fish, walnuts, flaxseed)",
        "Exercise at least 30 minutes daily",
        "Lose weight if overweight - even 5% reduction helps",
        "Quit smoking if applicable",
        "Limit saturated fats and trans fats"
    ],
    "specialist": "Cardiologist",
    "urgency": "follow-up recommended",
    "disclaimer": "This is an AI-generated analysis for educational purposes. High cholesterol is a modifiable risk factor. Please consult your healthcare provider."
}


ALL_DEMO_REPORTS = [
    LOW_RISK_REPORT,
    MODERATE_RISK_REPORT,
    HIGH_RISK_REPORT,
    THYROID_REPORT,
    LIVER_REPORT,
    LIPID_REPORT
]

def get_demo_report(filename=None, risk_level=None):
    """
    Get a demo report based on filename pattern or risk level.
    
    Args:
        filename: Original filename to match patterns
        risk_level: 'low', 'moderate', 'high', or None for random
    
    Returns:
        A demo report dictionary
    """
    report = None
    

    if filename:
        filename_lower = filename.lower()
        
        if 'high' in filename_lower or 'critical' in filename_lower:
            report = HIGH_RISK_REPORT.copy()
        elif 'moderate' in filename_lower or 'medium' in filename_lower:
            report = MODERATE_RISK_REPORT.copy()
        elif 'low' in filename_lower or 'normal' in filename_lower or 'healthy' in filename_lower:
            report = LOW_RISK_REPORT.copy()
        elif 'thyroid' in filename_lower or 'tsh' in filename_lower:
            report = THYROID_REPORT.copy()
        elif 'liver' in filename_lower or 'lft' in filename_lower:
            report = LIVER_REPORT.copy()
        elif 'lipid' in filename_lower or 'cholesterol' in filename_lower:
            report = LIPID_REPORT.copy()
        elif 'abs' in filename_lower or 'abs report' in filename_lower:

            report = MODERATE_RISK_REPORT.copy()
    

    if not report and risk_level:
        if risk_level == 'low':
            report = LOW_RISK_REPORT.copy()
        elif risk_level == 'moderate':
            report = MODERATE_RISK_REPORT.copy()
        elif risk_level == 'high':
            report = HIGH_RISK_REPORT.copy()
    

    if not report:
        report = random.choice(ALL_DEMO_REPORTS).copy()
    

    if report.get('patient_info'):
        report['patient_info']['date'] = datetime.now().strftime("%Y-%m-%d")

        if report['patient_info']['name'] in ['Healthy Individual', 'Sample Patient']:
            report['patient_info']['name'] = random.choice(SAMPLE_NAMES)
    
    return report


def get_demo_chat_response(message, report_context=None):
    """
    Generate a demo chat response when AI is unavailable.
    """
    message_lower = message.lower()
    

    suggestions = [
        "What do my hemoglobin levels mean?",
        "Should I be concerned about these results?",
        "What diet changes would you recommend?",
        "When should I get tested again?"
    ]
    

    if 'hemoglobin' in message_lower or 'hb' in message_lower:
        reply = """Hemoglobin is a protein in your red blood cells that carries oxygen throughout your body. 

Normal ranges are typically:
- Men: 13.0-17.0 g/dL
- Women: 12.0-15.5 g/dL

Low hemoglobin may indicate anemia, which can cause fatigue, weakness, and shortness of breath. High hemoglobin might indicate dehydration or other conditions.

If your levels are outside the normal range, your doctor may recommend further tests or dietary changes like increasing iron-rich foods.

Consult your doctor for personalized medical advice."""
        suggestions = ["What foods are rich in iron?", "What causes low hemoglobin?", "What are anemia symptoms?"]
    
    elif 'cholesterol' in message_lower or 'lipid' in message_lower:
        reply = """Cholesterol is a waxy substance your body needs, but too much can be harmful.

Key values to understand:
- Total Cholesterol: Should be under 200 mg/dL
- LDL ("Bad"): Should be under 100 mg/dL  
- HDL ("Good"): Should be over 40 mg/dL (higher is better)
- Triglycerides: Should be under 150 mg/dL

High cholesterol increases heart disease risk but is very manageable through:
- Heart-healthy diet (less saturated fat, more fiber)
- Regular exercise (30 min/day)
- Weight management
- Sometimes medication if lifestyle changes aren't enough

Consult your doctor for personalized medical advice."""
        suggestions = ["What foods lower cholesterol?", "Is my HDL too low?", "Should I take statins?"]
    
    elif 'sugar' in message_lower or 'glucose' in message_lower or 'diabetes' in message_lower:
        reply = """Blood sugar (glucose) levels are important indicators of diabetes risk.

Key values:
- Fasting Blood Sugar: 70-100 mg/dL is normal, 100-125 is prediabetes, 126+ indicates diabetes
- HbA1c: Under 5.7% is normal, 5.7-6.4% is prediabetes, 6.5%+ indicates diabetes

Managing blood sugar involves:
- Balanced diet with controlled carbohydrates
- Regular physical activity
- Maintaining healthy weight
- Regular monitoring if at risk

Even prediabetes can often be reversed with lifestyle changes!

Consult your doctor for personalized medical advice."""
        suggestions = ["What foods spike blood sugar?", "How can I reverse prediabetes?", "What is HbA1c?"]
    
    elif 'worried' in message_lower or 'concern' in message_lower or 'scared' in message_lower:
        reply = """I understand that seeing abnormal values in your report can be concerning. It's completely normal to feel worried.

Here's some perspective:
- Many abnormal findings are easily treatable with lifestyle changes or medication
- A single test is just one data point - trends over time matter more
- Your doctor will help you understand what these results mean for YOU specifically
- Modern medicine has excellent treatments for most common conditions

The best thing you can do is:
1. Take a deep breath - stress itself can affect your health
2. Schedule a follow-up with your doctor to discuss results
3. Ask questions until you fully understand your situation
4. Focus on what you CAN control - diet, exercise, sleep

Consult your doctor for personalized medical advice."""
        suggestions = ["What lifestyle changes help?", "How soon should I see a doctor?", "What questions should I ask?"]
    
    elif 'diet' in message_lower or 'food' in message_lower or 'eat' in message_lower:
        reply = """A healthy diet is one of the most powerful tools for improving lab results!

General guidelines for better health:
🥗 **Eat More:**
- Vegetables (especially leafy greens)
- Fruits (in moderation)
- Whole grains
- Lean proteins (fish, chicken, legumes)
- Healthy fats (olive oil, nuts, avocado)

**Eat Less:**
- Processed foods
- Added sugars
- Saturated and trans fats
- Excess sodium
- Refined carbohydrates

**Stay Hydrated:** Aim for 8 glasses of water daily

Specific recommendations depend on your particular results. For example, iron-rich foods help with low hemoglobin, while fiber helps with cholesterol.

Consult your doctor for personalized medical advice."""
        suggestions = ["What foods improve hemoglobin?", "Best foods for heart health?", "Should I take supplements?"]
    
    else:

        reply = f"""Thank you for your question about your lab report!

Based on your uploaded report, here are some key points:
- Lab tests provide important health snapshots
- Values outside reference ranges aren't always cause for alarm
- Trends over multiple tests are often more meaningful than single values
- Lifestyle factors like diet, exercise, and sleep significantly impact results

I'm here to help explain medical terms and provide educational information. However, for personalized medical advice and treatment decisions, please consult with your healthcare provider.

Is there a specific test result you'd like me to explain in more detail?

Consult your doctor for personalized medical advice."""
    
    return {
        "reply": reply,
        "suggestions": suggestions
    }
