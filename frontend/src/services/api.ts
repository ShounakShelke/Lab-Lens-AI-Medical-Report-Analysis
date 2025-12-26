import axios from 'axios';

const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:5000/api';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

api.interceptors.request.use((config) => {
  const token = sessionStorage.getItem('auth_token');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

api.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      sessionStorage.removeItem('auth_token');
      sessionStorage.removeItem('user');
      window.location.href = '/login';
    }
    return Promise.reject(error);
  }
);

export const authAPI = {
  googleLogin: (credential: string) => 
    api.post('/auth/google', { credential }),
  logout: () => 
    api.post('/auth/logout'),
  getUser: () => 
    api.get('/auth/user'),
};

export const uploadAPI = {
  uploadReport: (file: File, onProgress?: (progress: number) => void) => {
    const formData = new FormData();
    formData.append('file', file);
    return api.post('/analyze', formData, {
      headers: { 'Content-Type': 'multipart/form-data' },
      onUploadProgress: (progressEvent) => {
        if (onProgress && progressEvent.total) {
          const progress = Math.round((progressEvent.loaded * 100) / progressEvent.total);
          onProgress(progress);
        }
      },
    });
  },
  getProcessingStatus: (reportId: string) => 
    api.get(`/upload/status/${reportId}`),
};

export const resultsAPI = {
  getResults: (reportId: string) => 
    api.get(`/reports/${reportId}`),
  getHistory: () => 
    api.get('/history'),
};

export const chatAPI = {
  sendMessage: (message: string, reportId?: string) => 
    api.post('/chat', { message, reportId }),
};

export const adminAPI = {
  getSummary: () => api.get('/admin/summary'),
  getDashboard: () => 
    api.get('/admin/dashboard'),
  getPrompts: () => 
    api.get('/admin/prompts'),
  updatePrompt: (id: string, data: { version: string; content: string }) => 
    api.put(`/admin/prompts/${id}`, data),
  getRules: () => 
    api.get('/admin/rules'),
  updateRules: (data: { disclaimer: string; allowedPhrases: string[]; blockedWords: string[] }) => 
    api.put('/admin/rules', data),
  getFeedback: () => 
    api.get('/admin/feedback'),
  updateFeedbackStatus: (id: string, status: string) => 
    api.put(`/admin/feedback/${id}`, { status }),
};

export default api;
