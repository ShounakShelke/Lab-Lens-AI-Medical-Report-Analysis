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
    "specialist": "General Physician",
    "urgency": "routine",
    "overall_risk": "Low",
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
    "specialist": "Internal Medicine",
    "urgency": "follow-up",
    "overall_risk": "Moderate",
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
    "specialist": "Nephrologist",
    "urgency": "urgent",
    "overall_risk": "High",
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
    "urgency": "follow-up",
    "overall_risk": "Moderate",
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
    "specialist": "Gastroenterologist",
    "urgency": "follow-up",
    "overall_risk": "Moderate",
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
    "urgency": "follow-up",
    "overall_risk": "Moderate",
    "disclaimer": "This is an AI-generated analysis for educational purposes. High cholesterol is a modifiable risk factor. Please consult your healthcare provider."
}


ABS_REPORT = {
    "valid_data": True,
    "report_type": "Hematology & Basic Screening",
    "patient_info": {"name": "Demo Patient", "age": "45", "sex": "M", "date": None},
    "summary": "The hematology report shows significant anemia with low hemoglobin (8.0 g/dL), low red blood cell count (3.32 million/cu mm), and low packed cell volume (26.3%). These findings may indicate iron deficiency anemia.",
    "tests": [
        {"name": "Haemoglobin", "value": "8.0", "unit": "g/dL", "ref_range": "12-14", "status": "Low"},
        {"name": "RBC Count", "value": "3.32", "unit": "million/cu mm", "ref_range": "3.80-5.80", "status": "Low"},
        {"name": "WBC Count", "value": "5000", "unit": "/cu mm", "ref_range": "4,000-11,000", "status": "Normal"},
        {"name": "Neutrophils", "value": "55", "unit": "%", "ref_range": "40-70", "status": "Normal"},
        {"name": "Lymphocytes", "value": "38", "unit": "%", "ref_range": "20-50", "status": "Normal"},
        {"name": "PCV", "value": "26.3", "unit": "%", "ref_range": "36-56", "status": "Low"},
        {"name": "MCV", "value": "79.2", "unit": "fL", "ref_range": "80-100", "status": "Low"},
        {"name": "MCH", "value": "24.0", "unit": "pg", "ref_range": "27-32", "status": "Low"},
        {"name": "MCHC", "value": "30.0", "unit": "g/dL", "ref_range": "32-36", "status": "Low"},
        {"name": "Sr. Creatinine", "value": "0.8", "unit": "mg/dL", "ref_range": "0.6-1.4", "status": "Normal"}
    ],
    "lifestyle": [
        "Increase intake of iron-rich foods like spinach, lentils, and red meat.",
        "Consider vitamin C rich foods to enhance iron absorption.",
        "Avoid tea and coffee around meal times.",
        "Schedule follow-up blood tests."
    ],
    "specialist": "Hematologist",
    "urgency": "follow-up",
    "overall_risk": "Moderate"
}

DIABETES_REPORT = {
    "valid_data": True,
    "report_type": "Diabetes Panel",
    "summary": "Blood glucose levels are elevated indicating prediabetes or early Type 2 diabetes. Your HbA1c of 6.8% shows average blood sugar has been high.",
    "tests": [
        {"name": "Fasting Blood Sugar", "value": "126", "unit": "mg/dL", "ref_range": "70-100", "status": "High"},
        {"name": "HbA1c", "value": "6.8", "unit": "%", "ref_range": "<5.7", "status": "High"}
    ],
    "lifestyle": ["Follow a low-carbohydrate, high-fiber diet.", "Exercise at least 30 minutes daily.", "Monitor blood sugar levels regularly."],
    "specialist": "Endocrinologist",
    "overall_risk": "Moderate"
}

KIDNEY_REPORT = {
    "valid_data": True,
    "report_type": "Kidney Function",
    "summary": "Kidney function tests indicate moderately reduced kidney function (Stage 3 CKD) with elevated creatinine and reduced eGFR.",
    "tests": [
        {"name": "Serum Creatinine", "value": "1.8", "unit": "mg/dL", "ref_range": "0.6-1.2", "status": "High"},
        {"name": "eGFR", "value": "52", "unit": "mL/min", "ref_range": ">90", "status": "Low"}
    ],
    "lifestyle": ["Limit sodium/salt intake.", "Moderate protein consumption.", "Stay well hydrated."],
    "specialist": "Nephrologist",
    "overall_risk": "High"
}

VITAMIN_REPORT = {
    "valid_data": True,
    "report_type": "Vitamin Panel",
    "summary": "Significant nutritional deficiencies detected. Vitamin D is severely deficient and B12 is below optimal.",
    "tests": [
        {"name": "Vitamin D (25-OH)", "value": "12", "unit": "ng/mL", "ref_range": "30-100", "status": "Low"},
        {"name": "Vitamin B12", "value": "180", "unit": "pg/mL", "ref_range": "200-900", "status": "Low"}
    ],
    "lifestyle": ["Get 15-20 minutes of morning sunlight.", "Take Vitamin D3 supplements as prescribed.", "Include B12 sources - meat, eggs, dairy."],
    "specialist": "General Physician",
    "overall_risk": "Moderate"
}

ALL_DEMO_REPORTS = [
    LOW_RISK_REPORT,
    MODERATE_RISK_REPORT,
    HIGH_RISK_REPORT,
    THYROID_REPORT,
    LIVER_REPORT,
    LIPID_REPORT,
    ABS_REPORT,
    DIABETES_REPORT,
    KIDNEY_REPORT,
    VITAMIN_REPORT
]

# --- EXTENDED DEMO KNOWLEDGE BASE (NotebookLM-style) ---
# This dictionary contains pre-fixed answers for standard questions for each demo report.
DEMO_KNOWLEDGE_BASE = {
    "Low": {
        "questions": [
            "What does a 'Low Risk' profile mean?",
            "Is my hemoglobin level 14.5 g/dL good?",
            "What do white blood cells (WBC) indicate?",
            "Why is my platelet count important?",
            "What is the standard range for blood pressure?",
            "How can I maintain these healthy levels?",
            "What does Hematocrit (PCV) measure?",
            "Are there any specific diet recommendations?",
            "When should I get my next check-up?",
            "What symptoms should I watch out for?"
        ],
        "answers": {
            "What does a 'Low Risk' profile mean?": "A 'Low Risk' profile means all your vital biomarkers are within the standard clinical reference ranges. It suggests your body is functioning optimally in the areas tested.",
            "Is my hemoglobin level 14.5 g/dL good?": "Yes, 14.5 g/dL is an excellent level for an adult (standard range 13-17 g/dL for men, 12-15 g/dL for women), indicating good oxygen-carrying capacity in your blood.",
            "What do white blood cells (WBC) indicate?": "WBCs are part of your immune system. Your level of 7500 /µL is normal, suggesting no active infection or significant inflammatory response at the time of testing.",
            "Why is my platelet count important?": "Platelets help your blood clot. Your count of 250,000 /µL is well within the healthy 150k-400k range, ensuring proper wound healing.",
            "What is the standard range for blood pressure?": "Standard healthy blood pressure is typically around 120/80 mmHg. Consistent readings above 130/80 are usually considered elevated.",
            "How can I maintain these healthy levels?": "Consistent sleep (7-8 hours), balanced nutrition (low processed sugar), and at least 150 minutes of moderate activity per week are the pillars of maintenance.",
            "What does Hematocrit (PCV) measure?": "Hematocrit measures the percentage of your blood volume made up of red blood cells. Your 44% is optimal for energy and endurance.",
            "Are there any specific diet recommendations?": "Focus on 'Whole Foods'—plenty of leafy greens, lean proteins, and complex carbohydrates to keep these markers stable.",
            "When should I get my next check-up?": "For a low-risk profile, an annual screening is usually sufficient unless you develop new symptoms.",
            "What symptoms should I watch out for?": "Even with good labs, watch for unexplained fatigue, sudden weight changes, or persistent pain, and consult a doctor if they occur."
        }
    },
    "Moderate": {
        "questions": [
            "Why is my risk level 'Moderate'?",
            "What does 'Borderline' status mean?",
            "How can I lower my cholesterol naturally?",
            "Is a blood sugar of 118 mg/dL dangerous?",
            "What foods should I avoid for better liver health?",
            "What is the standard range for blood pressure?",
            "Can stress affect my lab results?",
            "How much exercise do I need to see improvement?",
            "What is the difference between LDL and HDL?",
            "How soon should I retest?"
        ],
        "answers": {
            "Why is my risk level 'Moderate'?": "Your risk is 'Moderate' because some values (like glucose or cholesterol) are 'Borderline' or slightly 'High'. This is a 'wait and watch' stage where lifestyle changes can prevent future issues.",
            "What does 'Borderline' status mean?": "'Borderline' means your value is at the very edge of the normal range. It's a warning sign that the marker is moving in an unhealthy direction.",
            "How can I lower my cholesterol naturally?": "Increase soluble fiber (oats, beans), eliminate trans fats, and increase healthy fats (omega-3s from fish or flaxseed).",
            "Is a blood sugar of 118 mg/dL dangerous?": "It's not an immediate emergency, but 118 mg/dL (fasting) is in the 'Prediabetes' range (100-125 mg/dL). It's a critical time to adjust your sugar intake.",
            "What foods should I avoid for better liver health?": "Avoid high-fructose corn syrup, excessive alcohol, and highly processed 'white' flours which can cause liver stress.",
            "What is the standard range for blood pressure?": "Standard healthy blood pressure is 120/80. For moderate risk individuals, keeping it below 130/80 is vital to protect your heart and kidneys.",
            "Can stress affect my lab results?": "Yes, chronic stress raises cortisol, which can indirectly increase blood sugar and blood pressure markers.",
            "How much exercise do I need to see improvement?": "Aim for 30 minutes of brisk walking 5 days a week. It significantly improves how your body processes sugar and fats.",
            "What is the difference between LDL and HDL?": "LDL is 'Bad' cholesterol—it builds plaques. HDL is 'Good'—it acts like a vacuum cleaner, removing fat from your arteries.",
            "How soon should I retest?": "Usually, 3 months is the standard window to see if lifestyle changes have positively impacted your markers."
        }
    },
    "High": {
        "questions": [
            "What makes these results 'High Risk'?",
            "What is Creatinine and why is 2.8 mg/dL high?",
            "What is eGFR and why is 45 mL/min low?",
            "Are my kidneys in danger?",
            "What is the standard range for blood pressure?",
            "How can I take better care of my health now?",
            "What is HbA1c and what does 8.2% mean?",
            "Should I go to the emergency room?",
            "What questions should I ask my specialist?",
            "Can these results be reversed?"
        ],
        "answers": {
            "What makes these results 'High Risk'?": "High Risk is assigned when markers like Creatinine or Potassium are significantly outside safe zones, indicating that an organ system (like kidneys) is struggling.",
            "What is Creatinine and why is 2.8 mg/dL high?": "Creatinine is a waste product. 2.8 mg/dL is high because it suggests your kidneys aren't filtering waste efficiently (normal is typically 0.6-1.2).",
            "What is eGFR and why is 45 mL/min low?": "eGFR measures kidney filtration rate. 45 mL/min suggests Stage 3 kidney disease. Values above 90 are considered normal.",
            "Are my kidneys in danger?": "These results suggest your kidneys are under significant stress. Immediate consultation with a Nephrologist is essential to prevent further decline.",
            "What is the standard range for blood pressure?": "For high-risk individuals, the standard goal is usually under 120/80. High blood pressure is a primary driver of kidney and heart damage.",
            "How can I take better care of my health now?": "Strictly follow a low-sodium diet, avoid NSAIDs (like Ibuprofen), and manage your blood sugar with religious discipline.",
            "What is HbA1c and what does 8.2% mean?": "HbA1c shows your average blood sugar over 3 months. 8.2% indicates poorly controlled diabetes which can damage your organs.",
            "Should I go to the emergency room?": "If you experience severe shortness of breath, chest pain, or sudden confusion along with these results, seek emergency care immediately.",
            "What questions should I ask my specialist?": "Ask: 'What is my current CKD stage?', 'Which medications should I stop?', and 'What is the target for my blood pressure?'",
            "Can these results be reversed?": "While some kidney damage is permanent, strict management can often stabilize the condition and prevent the need for dialysis."
        }
    },
    "General": {
        "questions": [
            "What is the standard range of blood pressure?",
            "How can I take better care of my health in general?",
            "How often should I get blood tests?",
            "What should I do before a fasting blood test?",
            "Can vitamins change my test results?",
            "How do I read a lab report?",
            "What's the difference between a lab and a doctor?",
            "Are home test kits accurate?",
            "What does 'Reference Range' mean?",
            "Why do ranges differ between labs?"
        ],
        "answers": {
            "What is the standard range of blood pressure?": "Healthy blood pressure is generally considered 120/80 mmHg or lower. 130/80+ is Stage 1 Hypertension.",
            "How can I take better care of my health in general?": "Prioritize 'The Big Three': Consistent sleep, unprocessed food, and daily movement. Small changes compounded over time lead to the best results.",
            "How often should I get blood tests?": "Most healthy adults should have a basic screening once a year. If you have chronic conditions, every 3-6 months is common.",
            "What should I do before a fasting blood test?": "Do not eat or drink anything except water for 8-12 hours. Avoid exercise and caffeine as well, as they can spike certain markers.",
            "Can vitamins change my test results?": "Yes, especially Biotin (Vitamin B7), which can interfere with thyroid and heart tests. Always tell your lab which supplements you take.",
            "How do I read a lab report?": "Look at the 'Value' column, compare it to the 'Reference Range', and check the 'Status' or 'Flag' column for H (High) or L (Low).",
            "What's the difference between a lab and a doctor?": "A lab performs the technical measurement. A doctor provides the clinical interpretation based on your symptoms and history.",
            "Are home test kits accurate?": "Many are reliable for screening, but clinical lab tests are much more precise and should be used for actual diagnosis.",
            "What does 'Reference Range' mean?": "It's the range of values found in 95% of the healthy population. Being slightly outside doesn't always mean you are sick.",
            "Why do ranges differ between labs?": "Different labs use different equipment and chemical methods, which leads to slight variations in their 'Normal' benchmarks."
        }
    }
}

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
        elif 'abs' in filename_lower:
            report = ABS_REPORT.copy()
        elif 'reports-1' in filename_lower:
            report = DIABETES_REPORT.copy()
        elif 'reports-4' in filename_lower:
            report = KIDNEY_REPORT.copy()
        elif 'reports-6' in filename_lower:
            report = VITAMIN_REPORT.copy()
    

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

        if report['patient_info']['name'] in ['Healthy Individual', 'Sample Patient', 'Demo Patient']:
            report['patient_info']['name'] = random.choice(SAMPLE_NAMES)
            

    risk_val = report.get('overall_risk', 'Low')
    report['suggested_questions'] = DEMO_KNOWLEDGE_BASE.get(risk_val, {}).get("questions", [])[:4]
    
    return report


def get_demo_chat_response(message, report_context=None):
    """
    Generate a demo chat response when AI is unavailable.
    Includes Prefix answers for known questions.
    """
    message_lower = message.lower().strip()
    

    risk_group = "General"
    if report_context:
        risk_val = report_context.get('riskSummary', {}).get('overallRisk', 'Low')
        if risk_val in ["High", "Moderate", "Low"]:
            risk_group = risk_val


    target_groups = [risk_group, "General"] if risk_group != "General" else ["General"]
    
    for group in target_groups:
        qa_data = DEMO_KNOWLEDGE_BASE.get(group, {})
        for question, answer in qa_data.get("answers", {}).items():

            if message_lower in question.lower() or question.lower() in message_lower:
                return {
                    "reply": f"{answer}",
                    "suggestions": [q for q in qa_data["questions"] if q != question][:3]
                }


    suggestions = DEMO_KNOWLEDGE_BASE.get(risk_group, {}).get("questions", [])[:4]
    
    if 'hemoglobin' in message_lower or 'hb' in message_lower:
        reply = """Hemoglobin is a protein in your red blood cells that carries oxygen throughout your body. 

Normal ranges are typically:
- Men: 13.0-17.0 g/dL
- Women: 12.0-15.5 g/dL

Low hemoglobin may indicate anemia, which can cause fatigue, weakness, and shortness of breath. High hemoglobin might indicate dehydration or other conditions.

Consult your doctor for personalized medical advice."""
        suggestions = ["What foods are rich in iron?", "What causes low hemoglobin?", "What are anemia symptoms?"]
    
    elif 'cholesterol' in message_lower or 'lipid' in message_lower:
        reply = """Cholesterol is a waxy substance your body needs, but too much can be harmful.

Key values to understand:
- Total Cholesterol: Should be under 200 mg/dL
- LDL ("Bad"): Should be under 100 mg/dL  
- HDL ("Good"): Should be over 40 mg/dL (higher is better)

High cholesterol increases heart disease risk but is manageable through diet and regular exercise.

Consult your doctor for personalized medical advice."""
        suggestions = ["What foods lower cholesterol?", "Is my HDL too low?", "Should I take statins?"]
    
    elif 'sugar' in message_lower or 'glucose' in message_lower or 'diabetes' in message_lower:
        reply = """Blood sugar (glucose) levels are important indicators of diabetes risk.

Key values:
- Fasting Blood Sugar: 70-100 mg/dL is normal, 100-125 is prediabetes, 126+ indicates diabetes
- HbA1c: Under 5.7% is normal, 5.7-6.4% is prediabetes, 6.5%+ indicates diabetes

Prediabetes can often be reversed with lifestyle changes!

Consult your doctor for personalized medical advice."""
        suggestions = ["What foods spike blood sugar?", "How can I reverse prediabetes?", "What is HbA1c?"]
    
    elif 'diet' in message_lower or 'food' in message_lower or 'eat' in message_lower:
        reply = """A healthy diet is one of the most powerful tools for improving lab results!

General guidelines:
🥗 **Eat More:** Leafy greens, whole grains, lean proteins, healthy fats.
🚫 **Eat Less:** Added sugars, processed foods, trans fats, excess sodium.

Consult your doctor for personalized medical advice."""
        suggestions = ["What foods improve hemoglobin?", "Best foods for heart health?", "Should I take supplements?"]
    
    else:
        reply = f"""I'm scanning your report data to provide the most relevant answer. Based on your current analysis ({risk_group} Risk profile), I can help you decode these clinical values in plain English.

While I'm an AI assistant designed to provide educational insights, I can certainly explain:
• Reference Ranges: Why some values are flagged and what "Normal" actually means.
• Clinical Significance: The role of specific markers in your body.
• General Advice: Standard lifestyle adjustments recommended for various medical deviations.

Would you like me to break down a specific test result, or would you prefer a general summary of your health markers?"""
    
    return {
        "reply": reply,
        "suggestions": suggestions
    }
