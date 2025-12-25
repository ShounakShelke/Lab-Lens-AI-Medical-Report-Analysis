import { Link } from 'react-router-dom';
import { Activity, Shield, ExternalLink } from 'lucide-react';

export function Footer() {
  return (
    <footer className="border-t border-border/40 bg-secondary/30">
      <div className="container py-8">
        <div className="mb-6 rounded-lg border border-border/60 bg-card p-4">
          <div className="flex items-start gap-3">
            <Shield className="mt-0.5 h-5 w-5 shrink-0 text-primary" />
            <p className="text-sm text-muted-foreground">
              <span className="font-medium text-foreground">Important: </span>
              Lab-Lens does not provide medical diagnosis, treatment recommendations, or clinical advice. 
              This tool is for educational and informational purposes only. Always consult a qualified 
              healthcare professional for medical decisions.
            </p>
          </div>
        </div>

        <div className="flex flex-col items-center justify-between gap-6 md:flex-row">
          <div className="flex items-center gap-2">
            <div className="flex h-8 w-8 items-center justify-center rounded-lg bg-primary">
              <Activity className="h-4 w-4 text-primary-foreground" />
            </div>
            <span className="font-semibold">Lab-Lens</span>
            <span className="text-sm text-muted-foreground">
              Responsible Medical AI
            </span>
          </div>

          <nav className="flex flex-wrap items-center justify-center gap-6 text-sm">
            <Link 
              to="/disclaimer" 
              className="text-muted-foreground transition-colors hover:text-foreground"
            >
              Disclaimer
            </Link>
            <Link 
              to="/disclaimer" 
              className="text-muted-foreground transition-colors hover:text-foreground"
            >
              Privacy Policy
            </Link>
            <Link 
              to="/disclaimer" 
              className="text-muted-foreground transition-colors hover:text-foreground"
            >
              Terms of Use
            </Link>
          </nav>

          <div className="flex items-center gap-4 text-sm text-muted-foreground">
            <span className="flex items-center gap-1.5">
              Powered by Google AI
              <ExternalLink className="h-3 w-3" />
            </span>
          </div>
        </div>

        <div className="mt-6 text-center text-xs text-muted-foreground">
          © {new Date().getFullYear()} Lab-Lens. Built with ethical AI principles.
        </div>
      </div>
    </footer>
  );
}
