# Lab-Lens: Technical Approach & Architecture

## 1. Project Vision
**Lab-Lens** is designed to bridge the gap between complex medical diagnostics and patient understanding. Our goal is to empower users with clear, actionable insights from their lab reports *without* replacing the role of a doctor. 

We prioritize **Responsible AI**, ensuring that while we use advanced models for explanation, we rely on deterministic, medical-standard logic for risk assessment to minimize hallucinations.

---

## 2. Core Architecture

### **The Hybrid AI Engine (Our USP)**
Unlike generic wrappers that send everything to an LLM, we use a **Hybrid Pipeline** to ensure accuracy and safety:

1.  **Extraction (OCR)**: We use **EasyOCR** (running locally on CPU) to extract raw text from images. This ensures we can handle scanned, skewed, or low-quality report images.
2.  **Structuring (Generative AI)**: We pass the raw messy text to **Google Gemini 1.5 Flash**. Its specific role is *Data Structuring* and *Contextualization*. It converts unstructured text into a standard JSON schema (`Test Name`, `Value`, `Unit`, `Reference Range`).
3.  **Risk Evaluation (Deterministic Code)**: We do **NOT** rely solely on the LLM to decide if a value is "High Risk". We feed the structured data into our strictly coded `severity.py` engine. This module evaluates key markers (e.g., Cholesterol > 240 mg/dL) against hard-coded medical standards to determine the "Status" tags (Normal/Borderline/Alert).
4.  **Explanation (Generative AI)**: Once risk is calculated, Gemini is used again to generate "Plain English" summaries and lifestyle tips based on the confirmed data.

### **Tech Stack**
*   **Frontend**: React + Vite + TypeScript.
    *   *Styling*: Tailwind CSS + Shadcn UI for a premium, trustworthy medical aesthetic.
    *   *State*: React Query for async data management.
*   **Backend**: Flask (Python).
    *   *Reason*: Seamless integration with PyTorch (EasyOCR) and Google GenAI SDK.
*   **Data**: File-based JSON Database (`reports.json`, `users.json`) for portability and ease of setup during the hackathon phase.
*   **Auth**: Google OAuth 2.0 + Custom Demo Auth for judges.

---

## 3. User Flow

1.  **Secure Login**: User authenticates via Google or Demo credentials.
2.  **Upload**: User uploads a lab report (Image/PDF).
3.  **Processing Stages**:
    *   *Stage 1*: Image preprocessing (Greyscale/Contrast enhancement).
    *   *Stage 2*: Text Extraction (OCR).
    *   *Stage 3*: Clinical Entity Recognition (Gemini).
    *   *Stage 4*: Risk Scoring (Python Logic).
4.  **Results**: User sees a dashboard with:
    *   **Severity Banner**: Immediate visual cue (Green/Yellow/Red).
    *   **Simplified Metrics**: "Badges" instead of just numbers.
    *   **AI Chat Assistant**: A context-aware chatbot (RAG-lite) that knows the specific report details and can answer follow-up questions.

---

## 4. Safety & Ethics Guardrails
*   **Probabilistic Language**: The System Prompt strictly forces the AI to use phrases like "may indicate" rather than "you have".
*   **No Diagnosis**: The system is hard-coded to refuse diagnosis requests.
*   **Privacy**: Analysis is stateless where possible; we do not use patient data for model training.
*   **Visual Disclaimers**: Every page includes warnings that this is an educational tool, not a medical device.

---

## 5. Directory Structure
*   `/frontend`: React application (UI/UX).
*   `/backend`: Flask server, AI logic, and OCR handling.
*   `/ml_model`: Placeholder for future fine-tuned LayoutLMv3 model training scripts.
