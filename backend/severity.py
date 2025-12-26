"""
Universal Severity & Risk Logic for Lab-Lens
A comprehensive reference engine for clinical values across all common report types.
Acts as a grounding layer for AI-extracted data.
"""

import re


# --- RADIALLY EXPANDED MEDICAL DATASET (100+ TESTS) ---
# Format: "key": {"M": [low, high], "F": [low, high], "unit": "unit", "category": "cat", "specialist": "spec", "priority": "P"}

MASTER_REFERENCE_DICTIONARY = {
    # 🩸 HEMATOLOGY (1-30)
    "wbc": {"M": [4.0, 11.0], "F": [4.0, 11.0], "unit": "x10^9/L", "category": "Hematology", "specialist": "Hematologist", "priority": "Medium", "purpose": "Leukocyte count. High indicates infection/inflammation."},
    "rbc": {"M": [4.5, 5.9], "F": [4.1, 5.1], "unit": "x10^12/L", "category": "Hematology", "specialist": "Hematologist", "priority": "Routine", "purpose": "Red blood cell count. Low indicates anemia."},
    "hemoglobin": {"M": [13.2, 16.6], "F": [11.6, 15.0], "unit": "g/dL", "category": "Hematology", "specialist": "Hematologist", "priority": "High", "purpose": "Oxygen carrying protein."},
    "haemoglobin": {"M": [13.2, 16.6], "F": [11.6, 15.0], "unit": "g/dL", "category": "Hematology", "specialist": "Hematologist", "priority": "High"},
    "hematocrit": {"M": [38.3, 48.6], "F": [35.5, 44.9], "unit": "%", "category": "Hematology", "specialist": "Hematologist", "priority": "Routine", "purpose": "Packed cell volume (PCV)."},
    "pcv": {"M": [38.3, 48.6], "F": [35.5, 44.9], "unit": "%", "category": "Hematology", "specialist": "Hematologist", "priority": "Routine"},
    "platelet": {"M": [150, 450], "F": [150, 450], "unit": "x10^9/L", "category": "Hematology", "specialist": "Hematologist", "priority": "High", "purpose": "Thrombocyte count. Essential for clotting."},
    "esr": {"M": [0, 22], "F": [0, 29], "unit": "mm/hr", "category": "Hematology", "specialist": "Rheumatologist", "priority": "Routine", "purpose": "Erythrocyte Sedimentation Rate. Inflammation marker."},
    "reticulocyte": {"M": [0.5, 2.5], "F": [0.5, 2.5], "unit": "%", "category": "Hematology", "specialist": "Hematologist", "priority": "Routine", "purpose": "Immature red blood cell count."},
    "mcv": {"M": [80, 100], "F": [80, 100], "unit": "fL", "category": "Hematology", "specialist": "Hematologist", "priority": "Routine", "purpose": "Mean Corpuscular Volume. Sizing of RBCs."},
    "mch": {"M": [27, 33], "F": [27, 33], "unit": "pg", "category": "Hematology", "specialist": "Hematologist", "priority": "Routine", "purpose": "Mean Corpuscular Hemoglobin."},
    "mchc": {"M": [32, 36], "F": [32, 36], "unit": "g/dL", "category": "Hematology", "specialist": "Hematologist", "priority": "Routine", "purpose": "Mean Corpuscular Hemoglobin Conc."},
    "anc": {"M": [1500, 7500], "F": [1500, 7500], "unit": "cells/mcL", "category": "Hematology", "specialist": "Hematologist", "priority": "High", "purpose": "Absolute Neutrophil Count."},
    "alc": {"M": [1300, 3500], "F": [1300, 3500], "unit": "cells/mcL", "category": "Hematology", "specialist": "Hematologist", "priority": "Medium", "purpose": "Absolute Lymphocyte Count."},
    "absolute monocyte": {"M": [200, 950], "F": [200, 950], "unit": "cells/mcL", "category": "Hematology", "specialist": "Hematologist", "priority": "Routine"},
    "absolute eosinophil": {"M": [0, 500], "F": [0, 500], "unit": "cells/mcL", "category": "Hematology", "specialist": "Allergist", "priority": "Routine"},
    "absolute basophil": {"M": [0, 300], "F": [0, 300], "unit": "cells/mcL", "category": "Hematology", "specialist": "Hematologist", "priority": "Routine"},
    "segmented neutrophils": {"M": [50, 62], "F": [50, 62], "unit": "%", "category": "Hematology", "specialist": "Hematopathologist", "priority": "Medium"},
    "mpv": {"M": [7.8, 11.0], "F": [7.8, 11.0], "unit": "fL", "category": "Hematology", "specialist": "Hematologist", "priority": "Routine", "purpose": "Mean Platelet Volume."},
    "pct": {"M": [0.12, 0.50], "F": [0.12, 0.50], "unit": "%", "category": "Hematology", "specialist": "Hematologist", "priority": "Routine", "purpose": "Plateletcrit."},
    "pdw": {"M": [9, 17], "F": [9, 17], "unit": "%", "category": "Hematology", "specialist": "Hematologist", "priority": "Routine", "purpose": "Platelet Distribution Width."},
    "rdw-cv": {"M": [11, 15], "F": [11, 15], "unit": "%", "category": "Hematology", "specialist": "Hematologist", "priority": "Routine"},
    "rdw-sd": {"M": [39, 46], "F": [39, 46], "unit": "fL", "category": "Hematology", "specialist": "Hematologist", "priority": "Routine"},

    # 🧪 BIOCHEMISTRY & DIABETES (31-60)
    "fasting glucose": {"M": [70, 99], "F": [70, 99], "unit": "mg/dL", "category": "Biochemistry", "specialist": "Endocrinologist", "priority": "High", "purpose": "Diabetes screening."},
    "random glucose": {"M": [80, 140], "F": [80, 140], "unit": "mg/dL", "category": "Biochemistry", "specialist": "Endocrinologist", "priority": "High"},
    "glucose": {"M": [70, 140], "F": [70, 140], "unit": "mg/dL", "category": "Biochemistry", "specialist": "Endocrinologist", "priority": "High"},
    "hba1c": {"M": [4.0, 5.6], "F": [4.0, 5.6], "unit": "%", "category": "Biochemistry", "specialist": "Endocrinologist", "priority": "High", "purpose": "Average sugar."},
    "insulin": {"M": [2, 25], "F": [2, 25], "unit": "µIU/mL", "category": "Biochemistry", "specialist": "Endocrinologist", "priority": "Medium"},
    "c-peptide": {"M": [0.5, 2.0], "F": [0.5, 2.0], "unit": "ng/mL", "category": "Biochemistry", "specialist": "Endocrinologist", "priority": "Medium"},
    "creatinine": {"M": [0.7, 1.3], "F": [0.6, 1.1], "unit": "mg/dL", "category": "Biochemistry", "specialist": "Nephrologist", "priority": "High"},
    "urea": {"M": [15, 50], "F": [15, 50], "unit": "mg/dL", "category": "Biochemistry", "specialist": "Nephrologist", "priority": "Medium"},
    "bun": {"M": [7, 20], "F": [7, 20], "unit": "mg/dL", "category": "Biochemistry", "specialist": "Nephrologist", "priority": "Medium"},
    "uric acid": {"M": [3.4, 7.0], "F": [2.4, 6.0], "unit": "mg/dL", "category": "Biochemistry", "specialist": "Rheumatologist", "priority": "Medium"},
    "total protein": {"M": [6.0, 8.3], "F": [6.0, 8.3], "unit": "g/dL", "category": "Biochemistry", "specialist": "Internal Medicine", "priority": "Routine"},
    "ast": {"M": [8, 48], "F": [8, 48], "unit": "U/L", "category": "LFT", "specialist": "Hepatologist", "priority": "Medium"},
    "alt": {"M": [7, 56], "F": [7, 56], "unit": "U/L", "category": "LFT", "specialist": "Hepatologist", "priority": "Medium"},
    "alp": {"M": [40, 129], "F": [40, 129], "unit": "U/L", "category": "LFT", "specialist": "Gastroenterologist", "priority": "Medium"},
    "ggt": {"M": [9, 48], "F": [9, 48], "unit": "U/L", "category": "LFT", "specialist": "Hepatologist", "priority": "Routine"},
    "total bilirubin": {"M": [0.3, 1.9], "F": [0.3, 1.9], "unit": "mg/dL", "category": "LFT", "specialist": "Hepatologist", "priority": "Medium"},
    "direct bilirubin": {"M": [0.0, 0.3], "F": [0.0, 0.3], "unit": "mg/dL", "category": "LFT", "specialist": "Hepatologist", "priority": "Medium"},
    "albumin": {"M": [3.5, 5.5], "F": [3.5, 5.5], "unit": "g/dL", "category": "LFT", "specialist": "Hepatologist", "priority": "Routine"},
    "globulin": {"M": [2.0, 3.5], "F": [2.0, 3.5], "unit": "g/dL", "category": "LFT", "specialist": "Hepatologist", "priority": "Routine"},
    "ldh": {"M": [140, 280], "F": [140, 280], "unit": "U/L", "category": "LFT", "specialist": "Hepatologist", "priority": "Routine"},

    # 🧪 TOXICOLOGY & DRUG SCREENING (61-90)
    "noroxycodone": {"M": [0, 50], "F": [0, 50], "unit": "ng/mL", "category": "Toxicology", "specialist": "Toxicologist", "priority": "High", "purpose": "Oxycodone metabolite."},
    "oxycodone": {"M": [0, 50], "F": [0, 50], "unit": "ng/mL", "category": "Toxicology", "specialist": "Toxicologist", "priority": "High"},
    "morphine": {"M": [0, 95], "F": [0, 95], "unit": "ng/mL", "category": "Toxicology", "specialist": "Toxicologist", "priority": "High"},
    "oxymorphone": {"M": [0, 50], "F": [0, 50], "unit": "ng/mL", "category": "Toxicology", "specialist": "Toxicologist", "priority": "High"},
    "ethyl sulfate": {"M": [0, 200], "F": [0, 200], "unit": "ng/mL", "category": "Toxicology", "specialist": "Addiction Medicine Specialist", "priority": "Medium", "purpose": "Alcohol metabolite (EtS)."},
    "ets": {"M": [0, 200], "F": [0, 200], "unit": "ng/mL", "category": "Toxicology", "specialist": "Addiction Medicine Specialist", "priority": "Medium"},
    "ethyl glucuronide": {"M": [0, 500], "F": [0, 500], "unit": "ng/mL", "category": "Toxicology", "specialist": "Addiction Medicine Specialist", "priority": "Medium", "purpose": "Alcohol metabolite (EtG)."},
    "etg": {"M": [0, 500], "F": [0, 500], "unit": "ng/mL", "category": "Toxicology", "specialist": "Addiction Medicine Specialist", "priority": "Medium"},
    "thc": {"M": [0, 50], "F": [0, 50], "unit": "ng/mL", "category": "Toxicology", "specialist": "Addiction Medicine Specialist", "priority": "High", "purpose": "Cannabis screening."},
    "opiates": {"M": [0, 300], "F": [0, 300], "unit": "ng/mL", "category": "Toxicology", "specialist": "Toxicologist", "priority": "High"},
    "urine ph": {"M": [5.0, 9.0], "F": [5.0, 9.0], "unit": "pH", "category": "Urinalysis", "specialist": "Urologist", "priority": "Routine"},
    "specific gravity": {"M": [1.003, 1.030], "F": [1.003, 1.030], "unit": "sg", "category": "Urinalysis", "specialist": "Nephrologist", "priority": "Routine"},
    "oxidants": {"M": [0, 200], "F": [0, 200], "unit": "µg/mL", "category": "Toxicology", "specialist": "Toxicologist", "priority": "Medium"},
    "benzodiazepines": {"M": [0, 200], "F": [0, 200], "unit": "ng/mL", "category": "Toxicology", "specialist": "Addiction Medicine Specialist", "priority": "High"},
    "barbiturates": {"M": [0, 200], "F": [0, 200], "unit": "ng/mL", "category": "Toxicology", "specialist": "Toxicologist", "priority": "High"},
    "fentanyl": {"M": [0, 1.0], "F": [0, 1.0], "unit": "ng/mL", "category": "Toxicology", "specialist": "Toxicologist", "priority": "High"},
    "methadone": {"M": [0, 300], "F": [0, 300], "unit": "ng/mL", "category": "Toxicology", "specialist": "Addiction Medicine Specialist", "priority": "High"},
    "mdma": {"M": [0, 500], "F": [0, 500], "unit": "ng/mL", "category": "Toxicology", "specialist": "Toxicologist", "priority": "High"},
    "lsd": {"M": [0, 0.5], "F": [0, 0.5], "unit": "ng/mL", "category": "Toxicology", "specialist": "Toxicologist", "priority": "High"},
    "cocaine": {"M": [0, 150], "F": [0, 150], "unit": "ng/mL", "category": "Toxicology", "specialist": "Toxicologist", "priority": "High"},
    "ketamine": {"M": [0, 50], "F": [0, 50], "unit": "ng/mL", "category": "Toxicology", "specialist": "Toxicologist", "priority": "High"},

    # 🧬 AUTOIMMUNE & RHEUMATOLOGY (91-120)
    "ana": {"M": [0, 1.0], "F": [0, 1.0], "unit": "titer/index", "category": "Autoimmune", "specialist": "Rheumatologist", "priority": "High", "purpose": "Antinuclear Antibody. Lupus screening."},
    "anti-dsdna": {"M": [0, 30], "F": [0, 30], "unit": "IU/mL", "category": "Autoimmune", "specialist": "Rheumatologist", "priority": "High"},
    "anti-ccp": {"M": [0, 20], "F": [0, 20], "unit": "U/mL", "category": "Autoimmune", "specialist": "Rheumatologist", "priority": "High", "purpose": "Rheumatoid Arthritis marker."},
    "rf": {"M": [0, 14], "F": [0, 14], "unit": "IU/mL", "category": "Autoimmune", "specialist": "Rheumatologist", "priority": "Medium", "purpose": "Rheumatoid Factor."},
    "hla-b27": {"M": [0, 0], "F": [0, 0], "unit": "Binary", "category": "Autoimmune", "specialist": "Rheumatologist", "priority": "High"},
    "complement c3": {"M": [80, 180], "F": [80, 180], "unit": "mg/dL", "category": "Autoimmune", "specialist": "Immunologist", "priority": "Medium"},
    "complement c4": {"M": [15, 45], "F": [15, 45], "unit": "mg/dL", "category": "Autoimmune", "specialist": "Immunologist", "priority": "Medium"},
    "anti-smith": {"M": [0, 1.0], "F": [0, 1.0], "unit": "Index", "category": "Autoimmune", "specialist": "Rheumatologist", "priority": "High"},
    "anti-mitochondrial": {"M": [0, 0.1], "F": [0, 0.1], "unit": "Titer", "category": "Autoimmune", "specialist": "Hepatologist", "priority": "High"},

    # 🦠 INFECTIOUS DISEASE (121-150)
    "hiv viral load": {"M": [0, 20], "F": [0, 20], "unit": "copies/mL", "category": "Infectious Disease", "specialist": "HIV/AIDS Care Specialist", "priority": "High"},
    "hbv-dna": {"M": [0, 10], "F": [0, 10], "unit": "IU/mL", "category": "Infectious Disease", "specialist": "Hepatologist", "priority": "High"},
    "hcv rna": {"M": [0, 15], "F": [0, 15], "unit": "IU/mL", "category": "Infectious Disease", "specialist": "Hepatologist", "priority": "High"},
    "tb quantiferon": {"M": [0, 0.35], "F": [0, 0.35], "unit": "IU/mL", "category": "Infectious Disease", "specialist": "Pulmonologist", "priority": "High"},
    "malaria pcr": {"M": [0, 0], "F": [0, 0], "unit": "Binary", "category": "Infectious Disease", "specialist": "Travel & Tropical Medicine Expert", "priority": "High"},
    "leptospira": {"M": [0, 1.0], "F": [0, 1.0], "unit": "Index", "category": "Infectious Disease", "specialist": "Infectious Disease Specialist", "priority": "Medium"},
    "brucella": {"M": [0, 1.0], "F": [0, 1.0], "unit": "Index", "category": "Infectious Disease", "specialist": "Infectious Disease Specialist", "priority": "Medium"},
    "chlamydia": {"M": [0, 0], "F": [0, 0], "unit": "Binary", "category": "Infectious Disease", "specialist": "Sexual Medicine Specialist", "priority": "High"},
    "gonorrhea": {"M": [0, 0], "F": [0, 0], "unit": "Binary", "category": "Infectious Disease", "specialist": "Sexual Medicine Specialist", "priority": "High"},
    "syphilis": {"M": [0, 1.0], "F": [0, 1.0], "unit": "Index/Titer", "category": "Infectious Disease", "specialist": "Infectious Disease Specialist", "priority": "High"},
    "hsv 1": {"M": [0, 0.9], "F": [0, 0.9], "unit": "Index", "category": "Infectious Disease", "specialist": "Infectious Disease Specialist", "priority": "Medium"},
    "hsv 2": {"M": [0, 0.9], "F": [0, 0.9], "unit": "Index", "category": "Infectious Disease", "specialist": "Infectious Disease Specialist", "priority": "Medium"},

    # 🧠 NEUROLOGICAL (151-170)
    "csf glucose": {"M": [40, 70], "F": [40, 70], "unit": "mg/dL", "category": "Neurological", "specialist": "Neurologist", "priority": "High"},
    "csf protein": {"M": [15, 45], "F": [15, 45], "unit": "mg/dL", "category": "Neurological", "specialist": "Neurologist", "priority": "High"},
    "tau protein": {"M": [0, 300], "F": [0, 300], "unit": "pg/mL", "category": "Neurological", "specialist": "Geriatric Specialist", "priority": "High", "purpose": "Alzheimer marker."},
    "amyloid beta": {"M": [500, 1500], "F": [500, 1500], "unit": "pg/mL", "category": "Neurological", "specialist": "Neurologist", "priority": "High"},
    "nse": {"M": [0, 16.3], "F": [0, 16.3], "unit": "ng/mL", "category": "Neurological", "specialist": "Oncologist", "priority": "Medium", "purpose": "Neuron Specific Enolase."},
    "myelin basic protein": {"M": [0, 4.0], "F": [0, 4.0], "unit": "ng/mL", "category": "Neurological", "specialist": "Neurologist", "priority": "High"},

    # 🧬 GENETIC & ONCOLOGY (171-190)
    "psa": {"M": [0, 4.0], "F": [0, 0], "unit": "ng/mL", "category": "Oncology", "specialist": "Urologist", "priority": "High"},
    "ca-125": {"M": [0, 35], "F": [0, 35], "unit": "U/mL", "category": "Oncology", "specialist": "Gynecologist", "priority": "High"},
    "cea": {"M": [0, 3.0], "F": [0, 3.0], "unit": "ng/mL", "category": "Oncology", "specialist": "Oncologist", "priority": "High"},
    "afp": {"M": [0, 8.0], "F": [0, 8.0], "unit": "ng/mL", "category": "Oncology", "specialist": "Hepatologist", "priority": "High"},
    "brca1": {"M": [0, 0], "F": [0, 0], "unit": "Binary", "category": "Genetics", "specialist": "Clinical Geneticist", "priority": "High"},
    "brca2": {"M": [0, 0], "F": [0, 0], "unit": "Binary", "category": "Genetics", "specialist": "Clinical Geneticist", "priority": "High"},
    "kras mutation": {"M": [0, 0], "F": [0, 0], "unit": "Binary", "category": "Genetics", "specialist": "Molecular Pathologist", "priority": "High"},
    "nras mutation": {"M": [0, 0], "F": [0, 0], "unit": "Binary", "category": "Genetics", "specialist": "Molecular Pathologist", "priority": "High"},
    "tp53": {"M": [0, 0], "F": [0, 0], "unit": "Binary", "category": "Genetics", "specialist": "Molecular Pathologist", "priority": "High"},
    "egfr mutation": {"M": [0, 0], "F": [0, 0], "unit": "Binary", "category": "Genetics", "specialist": "Pulmonary Critical Care Specialist", "priority": "High"},
    "her2/neu": {"M": [0, 1.0], "F": [0, 1.0], "unit": "Index", "category": "Oncology", "specialist": "Breast Cancer Surgeon", "priority": "High"},

    # 🥚 REPRODUCTIVE & FERTILITY (191-205)
    "amh": {"M": [0.7, 7.0], "F": [0.7, 7.0], "unit": "ng/mL", "category": "Fertility", "specialist": "IVF & Fertility Consultant", "priority": "Medium", "purpose": "Anti-Mullerian Hormone."},
    "fsh": {"M": [1.5, 12.4], "F": [4.7, 21.5], "unit": "mIU/mL", "category": "Fertility", "specialist": "Reproductive Endocrinologist", "priority": "Medium"},
    "lh": {"M": [1.7, 8.6], "F": [2.4, 12.6], "unit": "mIU/mL", "category": "Fertility", "specialist": "Reproductive Endocrinologist", "priority": "Medium"},
    "progesterone": {"M": [0, 1.0], "F": [0.1, 25.0], "unit": "ng/mL", "category": "Fertility", "specialist": "Obstetrician (OB/GYN)", "priority": "Medium"},
    "estradiol": {"M": [10, 50], "F": [30, 400], "unit": "pg/mL", "category": "Fertility", "specialist": "Gynecologist", "priority": "Medium"},
    "shbg": {"M": [10, 80], "F": [20, 130], "unit": "nmol/L", "category": "Fertility", "specialist": "Andrologist", "priority": "Routine"},

    # 👶 PEDIATRIC & NEONATAL (206-215)
    "newborn screening": {"M": [0, 0], "F": [0, 0], "unit": "Binary", "category": "Pediatric", "specialist": "Neonatal Intensivist", "priority": "High"},
    "g6pd": {"M": [7.0, 20.5], "F": [7.0, 20.5], "unit": "U/g Hb", "category": "Pediatric", "specialist": "Pediatric Hematologist", "priority": "High"},
    "pku": {"M": [0, 2.0], "F": [0, 2.0], "unit": "mg/dL", "category": "Pediatric", "specialist": "Clinical Geneticist", "priority": "High"},
    "neonatal bilirubin": {"M": [0.1, 12.0], "F": [0.1, 12.0], "unit": "mg/dL", "category": "Pediatric", "specialist": "Neonatologist", "priority": "High"},
    "irt": {"M": [0, 70], "F": [0, 70], "unit": "ng/mL", "category": "Pediatric", "specialist": "Pediatric Endocrinologist", "priority": "High", "purpose": "Cystic Fibrosis screening."},
}

def clean_value(val_str):
    """Extracts numeric value from string, handling 'lakhs' and other notations."""
    try:
        val_str = str(val_str).lower().replace(",", "")
        # Handle 'lakh' (common in Indian reports: 2.48 lakhs = 248,000)
        multiplier = 1.0
        if "lakh" in val_str:
            multiplier = 100000.0
            val_str = val_str.replace("lakh", "").replace("s", "").strip()
        
        match = re.search(r"(\d+(\.\d+)?)", val_str)
        if match:
            return float(match.group(1)) * multiplier
        return None
    except:
        return None

def get_status(test_name, val, sex="M"):
    """
    Compares a test value against the master dictionary.
    Returns: status, is_abnormal
    """
    name_key = test_name.lower().replace("(f)", "fasting").replace("(pp)", "random")
    
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
    
    # --- AUTO-NORMALIZATION OF MAGNITUDE ---
    # Many labs use /µL (e.g. 9600) while ref uses 10^9/L (9.6)
    # If the value is > 100x the high range, we assume it's in a smaller unit scale
    if num_val > high * 100:
        normalized_val = num_val / 1000.0
    else:
        normalized_val = num_val

    if normalized_val < low: return "Low", True
    if normalized_val > high: return "High", True
    
    # Borderline is 10% near the edges
    if normalized_val <= low * 1.1 or normalized_val >= high * 0.9:
        return "Borderline", True
        
    return "Normal", False

def calculate_risk_level(tests_list):
    """
    Analyzes the entire set of tests to determine overall severity.
    """
    processed = []
    abnormal_count = 0
    severe_flags = []
    potential_specialists = []
    
    for test in tests_list:
        name = test.get('name', 'Unknown')
        val = test.get('value', '0')
        
        status, is_abnormal = get_status(name, val)
        
        # Get metadata if available
        meta = None
        for key in MASTER_REFERENCE_DICTIONARY:
            if key in name.lower():
                meta = MASTER_REFERENCE_DICTIONARY[key]
                break

        if status == "Not Classified":
            status = test.get('status', 'Normal')
            is_abnormal = status.lower() not in ['normal', 'optimal']
            
        test['status'] = status
        processed.append(test)
        
        if is_abnormal:
            abnormal_count += 1
            if meta and meta.get('specialist'):
                potential_specialists.append(meta['specialist'])

            if any(x in name.lower() for x in ['crp', 'creatinine', 'hiv', 'hbsag', 'troponin', 'psa', 'cea']):
                severe_flags.append(name)


    # Determine Specialist
    if potential_specialists:
        # Pick the most common or first specialist noted for abnormal results
        recommended_specialist = potential_specialists[0]
    else:
        recommended_specialist = "General Physician"

    if len(severe_flags) > 0:
        overall = "High"
        msg = "CRITICAL MARKERS DETECTED"
        color = "red"
        specialist = recommended_specialist
    elif abnormal_count >= 3:
        overall = "Moderate"
        msg = "MULTIPLE ABNORMALITIES DETECTED"
        color = "yellow"
        specialist = recommended_specialist
    elif abnormal_count > 0:
        overall = "Moderate"
        msg = "MINOR DEVIATIONS FOUND"
        color = "yellow"
        specialist = recommended_specialist
    else:
        overall = "Low"
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
