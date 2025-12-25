# Lab-Lens: Project Report

**Team:** Cortex LMH
**Project Name:** Lab-Lens
**Theme:** Healthcare & AI

---

## 1. Executive Summary
**Lab-Lens** is an intelligent medical lab report analyzer designed to bridge the communication gap between patients and their diagnostic data. By leveraging state-of-the-art Generative AI (Google Gemini) alongside deterministic medical logic, Lab-Lens transforms complex, jargon-heavy pathology reports into clear, simplified, and actionable insights.

---

## 2. Problem Statement
Medical lab reports are the gold standard for diagnosis, but they are often unintelligible to the average patient. 
- **Complexity**: Reports are filled with abbreviations (e.g., "hs-CRP", "HbA1c") and numerical ranges that are hard to interpret without medical training.
- **Anxiety**: "borderline" or "high" values often cause unnecessary panic before a doctor's consultation.
- **Accessibility**: Patients struggle to aggregate their history or ask follow-up questions about their own data.

---

## 3. Proposed Solution
Lab-Lens provides a secure, web-based platform where users can upload photos or PDFs of their reports. 

### Key Capabilities:
1.  **Instant Simplification**: Translates medical terms into plain English.
2.  **Visual Risk Assessment**: Uses a color-coded "Semaphore System" (Green/Yellow/Red) to highlight areas of concern immediately.
3.  **Strict Safety Guardrails**: Unlike generic chatbots, our hybrid engine prevents dangerous hallucinations by validating critical values against hard-coded medical standards before generation.
4.  **Interactive Assistant**: A built-in RAG-lite chatbot allows users to ask, "What foods should I avoid with high cholesterol?" specific to *their* results.

---

## 4. Technical Architecture

### 4.1. The Hybrid AI Pipeline
We devised a unique **"Trust-but-Verify"** architecture:
1.  **Extraction**: **EasyOCR** extracts raw text from user uploads locally, ensuring privacy and handling noisy images.
2.  **Structuring**: **Gemini 1.5 Flash** organizes this messy text into a structured JSON format.
3.  **Evaluation (The "Judge")**: A determinstic Python module (`severity.py`) validates the extracted values against standard reference ranges (e.g., American Heart Association guidelines). It overrides the AI if the AI's hallucination probability is non-zero.
4.  **Presentation**: The frontend renders these verified results, while a secondary AI call generates the "Lifestyle Tips" summary.

### 4.2. Tech Stack
-   **Frontend**: React, TypeScript, Vite, Tailwind CSS, Shadcn UI (for accessibility and premium design).
-   **Backend**: Flask (Python), Google GenAI SDK, EasyOCR, PyTorch.
-   **Storage**: Lightweight JSON store (Prototype) / scalable to PostgreSQL.
-   **Authentication**: Google OAuth 2.0 (Secure & Familiar).

---

## 5. Features & USP
*   **Medical-Grade UI**: A clean, calming interface designed to reduce user anxiety.
*   **Demo Mode included**: Pre-loaded High/Moderate/Low risk scenarios to demonstrate the engine's capability without needing fresh blood work.
*   **Admin Dashboard**: A hidden view for medical professionals to review AI outputs and flag errors (Human-in-the-Loop reinforcement learning).

---

## 6. Future Scope
1.  **Multi-Modal Support**: Analyzing X-Rays and MRI reports using Gemini Pro Vision.
2.  **Longitudinal Tracking**: Graphing a patient's cholesterol over 5 years.
3.  **EHR Integration**: Direct connection with Hospital systems (FHIR standards).
4.  **Local LLM Support**: Running a distilled Med-PaLM model locally for offline capability.

---

## 7. Conclusion
Lab-Lens represents the future of patient empowerment. By combining the empathy of user-centric design with the power of Large Language Models, we are not just reading reports—we are translating data into health.
