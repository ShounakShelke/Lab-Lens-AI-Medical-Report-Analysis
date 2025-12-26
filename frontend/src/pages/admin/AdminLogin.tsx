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
              I agree and continue
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
