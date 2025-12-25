# 🚀 Render Deployment Guide

## Backend Deployment

1. **Create New Web Service** on Render
   - Connect your GitHub repo
   - Root Directory: `backend`
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`

2. **Environment Variables**
   ```
   GEMINI_API_KEY=AIzaSy...
   PORT=10000
   ```

3. **Settings**
   - Instance Type: Free
   - Python Version: 3.11

## Frontend Deployment (Vercel)

1. **Import Project** to Vercel
   - Root Directory: `frontend`
   - Framework: Vite
   - Build Command: `npm run build`
   - Output Directory: `dist`

2. **Environment Variables**
   ```
   VITE_API_URL=https://your-backend.onrender.com
   ```

## Testing

Backend: `https://your-backend.onrender.com/health`  
Frontend: Upload a test image

## Troubleshooting

- **Backend won't start**: Check GEMINI_API_KEY is set
- **Frontend API errors**: Verify VITE_API_URL
- **CORS issues**: Check backend CORS config
