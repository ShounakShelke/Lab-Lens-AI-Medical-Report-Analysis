# Lab-Lens - Intelligent Lab Report Analyzer

AI-powered medical lab report analyzer that provides easy-to-understand insights from your blood tests and medical reports.


## Features

- **Upload & Analyze**: Upload lab reports (PDF, JPG, PNG) for AI-powered analysis
- **OCR Extraction**: Automatic text extraction using EasyOCR
- **Gemini AI Integration**: Advanced analysis using Google's Gemini 1.5 Flash
- **Safety Rules**: Ethical AI guardrails prevent diagnosis and prescription
- **Severity Calculation**: Automatic risk level assessment (Low/Moderate/High)
- **History Storage**: Persistent report history
- **Demo Endpoints**: Pre-built demo data for testing
- **Interactive Chat**: AI-powered Q&A about lab results
- **Authentication**: Email/Password and Google OAuth support

## Project Structure

```
Cortex-LMH-main/
├── backend/
│   ├── app.py          # Main Flask application
│   ├── gemini.py       # Gemini AI integration
│   ├── ocr.py          # OCR text extraction
│   ├── severity.py     # Risk calculation logic
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── pages/      # React pages
│   │   ├── components/ # UI components
│   │   └── services/   # API services
│   └── package.json
├── Procfile            # Render deployment
├── render.yaml         # Render blueprint
└── README.md
```



**Disclaimer**: This is an AI-powered educational tool. It is not a medical diagnosis. Always consult a healthcare professional for medical advice.


### Built with Love by Team Cortex LMH 🧡

## Team Cortex LMH - Shounak Shelke | Shravani Parte | Sahil Kesarkar
