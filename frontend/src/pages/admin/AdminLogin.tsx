import { useState } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import { Layout } from '@/components/layout/Layout';
import { Button } from '@/components/ui/button';
import { Checkbox } from '@/components/ui/checkbox';
import { useAuth } from '@/hooks/useAuth';
import { Activity, Shield, AlertTriangle } from 'lucide-react';

export default function AdminLogin() {
  const [hasConsented, setHasConsented] = useState(false);
  const [isLoading, setIsLoading] = useState(false);
  const { demoLogin } = useAuth();
  const navigate = useNavigate();

  const handleAdminLogin = async () => {
    if (!hasConsented) return;
    setIsLoading(true);
    
    try {
      const result = demoLogin(true);
      if (result.success) {
        navigate('/admin/dashboard');
      }
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <Layout hideFooter>
      <div className="container flex min-h-[calc(100vh-4rem)] items-center justify-center py-12">
        <div className="mx-auto w-full max-w-md">
          <div className="mb-8 text-center">
            <div className="mx-auto mb-4 flex h-16 w-16 items-center justify-center rounded-2xl bg-primary">
              <Activity className="h-8 w-8 text-primary-foreground" />
            </div>
            <h1 className="text-2xl font-bold">Admin Access</h1>
            <p className="mt-2 text-muted-foreground">
              Authorized personnel only
            </p>
          </div>

          <div className="rounded-2xl border border-border bg-card p-8 shadow-medium">
            <div className="mb-6 rounded-lg border border-status-alert/30 bg-status-alert/5 p-4">
              <div className="flex gap-3">
                <Shield className="mt-0.5 h-5 w-5 shrink-0 text-status-alert" />
                <div className="text-sm">
                  <p className="font-medium text-foreground">Restricted Access</p>
                  <p className="mt-1 text-muted-foreground">
                    This area is for authorized Lab-Lens administrators only. 
                    Unauthorized access attempts are logged.
                  </p>
                </div>
              </div>
            </div>

            <div className="mb-6 flex items-start gap-3 rounded-lg border border-border bg-secondary/30 p-4">
              <Checkbox
                id="admin-consent"
                checked={hasConsented}
                onCheckedChange={(checked) => setHasConsented(checked === true)}
                className="mt-0.5"
              />
              <label
                htmlFor="admin-consent"
                className="cursor-pointer text-sm leading-relaxed text-muted-foreground"
              >
                I confirm that I am an authorized administrator and will handle 
                all data in accordance with privacy regulations.
              </label>
            </div>

            <Button
              variant="default"
              size="lg"
              className="w-full"
              onClick={handleAdminLogin}
              disabled={!hasConsented || isLoading}
            >
              <svg className="mr-2 h-5 w-5" viewBox="0 0 24 24">
                <path
                  fill="currentColor"
                  d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z"
                />
                <path
                  fill="currentColor"
                  d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z"
                />
                <path
                  fill="currentColor"
                  d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.07H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.93l2.85-2.22.81-.62z"
                />
                <path
                  fill="currentColor"
                  d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.07l3.66 2.84c.87-2.6 3.3-4.53 6.16-4.53z"
                />
              </svg>
              Sign in with Google
            </Button>

            <div className="mt-6 text-center">
              <Link
                to="/login"
                className="text-sm text-muted-foreground transition-colors hover:text-foreground"
              >
                ← Back to User Login
              </Link>
            </div>
          </div>

          <div className="mt-6 flex items-center justify-center gap-2 text-sm text-muted-foreground">
            <AlertTriangle className="h-4 w-4 text-status-borderline" />
            <span>All admin actions are logged and audited</span>
          </div>
        </div>
      </div>
    </Layout>
  );
}
