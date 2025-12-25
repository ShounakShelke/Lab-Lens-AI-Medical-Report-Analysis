"""
Universal Severity & Risk Logic for Lab-Lens
A comprehensive reference engine for clinical values across all common report types.
Acts as a grounding layer for AI-extracted data.
"""

import re


MASTER_REFERENCE_DICTIONARY = {

    "hemoglobin": {"M": [13, 17], "F": [12, 15], "unit": "g/dL"},
    "haemoglobin": {"M": [13, 17], "F": [12, 15], "unit": "g/dL"},
    "rbcount": [4.2, 5.9, "million/µL"],
    "wbc": [4000, 11000, "per µL"],
    "platelets": [150000, 450000, "per µL"],
    "neutrophils": [40, 70, "%"],
    "lymphocytes": [20, 45, "%"],
    "pcv": [36, 52, "%"],
    "hematocrit": [36, 52, "%"],
    

    "fasting sugar": [70, 99, "mg/dL"],
    "blood sugar": [70, 140, "mg/dL"],
    "glucose": [70, 140, "mg/dL"],
    "hba1c": [0, 5.7, "%"],
    "urea": [15, 45, "mg/dL"],
    "creatinine": [0.6, 1.3, "mg/dL"],
    "uric acid": [2.4, 7.0, "mg/dL"],
    "calcium": [8.5, 10.5, "mg/dL"],
    "sodium": [135, 145, "mmol/L"],
    "potassium": [3.5, 5.0, "mmol/L"],
    

    "bilirubin": [0.3, 1.2, "mg/dL"],
    "ast": [5, 40, "U/L"],
    "alt": [5, 45, "U/L"],
    "sgot": [5, 40, "U/L"],
    "sgpt": [5, 45, "U/L"],
    "alkaline phosphatase": [40, 120, "U/L"],
    "albumin": [3.5, 5.5, "g/dL"],
    

    "cholesterol": [0, 200, "mg/dL"],
    "ldl": [0, 100, "mg/dL"],
    "hdl": [40, 100, "mg/dL"],
    "triglycerides": [0, 150, "mg/dL"],
    
    "tsh": [0.4, 4.0, "µIU/mL"],
    "t3": [80, 200, "ng/dL"],
    "t4": [5, 12, "µg/dL"],
    

    "crp": [0, 1.0, "mg/L"],
    "hs-crp": [0, 1.0, "mg/L"],
}

def clean_value(val_str):
    """Extracts numeric value from string."""
    try:
        match = re.search(r"(\d+(\.\d+)?)", str(val_str))
        return float(match.group(1)) if match else None
    except:
        return None

def get_status(test_name, val, sex="M"):
    """
    Compares a test value against the master dictionary.
    Returns: status, is_abnormal
    """
    name_key = test_name.lower()
    

    ref = None
    for key in MASTER_REFERENCE_DICTIONARY:
        if key in name_key:
            ref = MASTER_REFERENCE_DICTIONARY[key]
            break
            
    if not ref:
        return "Not Classified", False


    if isinstance(ref, dict):
        ranges = ref.get(sex, [0, 1000])
    else:
        ranges = ref[:2]

    num_val = clean_value(val)
    if num_val is None:
        return "Invalid Data", False

    low, high = ranges
    if num_val < low: return "Low", True
    if num_val > high: return "High", True
    

    if num_val <= low * 1.1 or num_val >= high * 0.9:
        return "Borderline", True
        
    return "Normal", False

def calculate_risk_level(tests_list):
    """
    Analyzes the entire set of tests to determine overall severity.
    """
    processed = []
    abnormal_count = 0
    severe_flags = []
    
    for test in tests_list:
        name = test.get('name', 'Unknown')
        val = test.get('value', '0')
        
        status, is_abnormal = get_status(name, val)
        

        if status == "Not Classified":
            status = test.get('status', 'Normal')
            is_abnormal = status.lower() not in ['normal', 'optimal']
            
        test['status'] = status
        processed.append(test)
        
        if is_abnormal:
            abnormal_count += 1

            if any(x in name.lower() for x in ['crp', 'creatinine', 'hiv', 'hbsag', 'troponin']):
                severe_flags.append(name)


    if len(severe_flags) > 0:
        overall = "High Risk"
        msg = "CRITICAL MARKERS DETECTED"
        color = "red"
        specialist = "Specialist Consultation Required"
    elif abnormal_count >= 3:
        overall = "Moderate Risk"
        msg = "MULTIPLE ABNORMALITIES DETECTED"
        color = "yellow"
        specialist = "Internal Medicine"
    elif abnormal_count > 0:
        overall = "Mild Risk"
        msg = "MINOR DEVIATIONS FOUND"
        color = "yellow"
        specialist = "General Physician"
    else:
        overall = "Low Risk"
        msg = "OPTIMAL HEALTH PROFILE"
        color = "green"
        specialist = "General Wellness"

    summary = {
        "overallRisk": overall,
        "bannerMessage": msg,
        "severityBannerColor": color,
        "recommendedSpecialist": specialist,
        "abnormalCount": abnormal_count
    }
    
    return summary, processed
