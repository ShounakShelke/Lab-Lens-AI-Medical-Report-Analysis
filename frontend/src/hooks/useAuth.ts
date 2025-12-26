import { useState, useEffect, useCallback } from 'react';
import { authAPI } from '@/services/api';

export interface User {
  id: string;
  email: string;
  name: string;
  avatar?: string;
  role: 'user' | 'admin';
}

export function useAuth() {
  const [user, setUser] = useState<User | null>(null);
  const [isLoading, setIsLoading] = useState(true);
  const [isAuthenticated, setIsAuthenticated] = useState(false);

  useEffect(() => {
    const storedUser = sessionStorage.getItem('user');
    const token = sessionStorage.getItem('auth_token');
    
    if (storedUser && token) {
      try {
        const parsedUser = JSON.parse(storedUser);
        setUser(parsedUser);
        setIsAuthenticated(true);
      } catch {
        sessionStorage.removeItem('user');
        sessionStorage.removeItem('auth_token');
      }
    }
    setIsLoading(false);
  }, []);

  const login = useCallback(async (credential: string) => {
    if (credential.startsWith("demo-token")) {
      const isAdmin = credential.includes("admin");
      return demoLogin(isAdmin);
    }

    try {
      const response = await authAPI.googleLogin(credential);
      const { user: userData, token } = response.data;

      sessionStorage.setItem('auth_token', token);
      sessionStorage.setItem('user', JSON.stringify(userData));

      setUser(userData);
      setIsAuthenticated(true);

      return { success: true, user: userData };
    } catch (error) {
      console.error('Login failed:', error);
      return { success: false, error: 'Login failed' };
    }
  }, []);

  const logout = useCallback(async () => {
    try {
      await authAPI.logout();
    } catch {
  }
    
    sessionStorage.removeItem('auth_token');
    sessionStorage.removeItem('user');
    setUser(null);
    setIsAuthenticated(false);
  }, []);

  const demoLogin = useCallback((isAdmin = false) => {
    const demoUser: User = {
      id: 'demo-user-123',
      email: isAdmin ? 'admin@lablens.demo' : 'user@lablens.demo',
      name: isAdmin ? 'Demo Admin' : 'Demo User',
      role: isAdmin ? 'admin' : 'user',
    };
    
    sessionStorage.setItem('auth_token', 'demo-token');
    sessionStorage.setItem('user', JSON.stringify(demoUser));
    
    setUser(demoUser);
    setIsAuthenticated(true);
    
    return { success: true, user: demoUser };
  }, []);

  return {
    user,
    isLoading,
    isAuthenticated,
    isAdmin: user?.role === 'admin',
    login,
    logout,
    demoLogin,
  };
}
