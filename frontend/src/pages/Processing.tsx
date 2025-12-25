import { useState, useEffect } from 'react';
import { useNavigate, useLocation } from 'react-router-dom';
import { Layout } from '@/components/layout/Layout';
import { LoadingStepper } from '@/components/LoadingStepper';
import { Shield, AlertCircle } from 'lucide-react';

const processingSteps = [
  {
    id: 'extract',
    label: 'Extracting Values',
    description: 'Reading test results from your report using OCR',
  },
  {
    id: 'normalize',
    label: 'Normalizing Ranges',
    description: 'Comparing values against standard reference ranges',
  },
  {
    id: 'generate',
    label: 'Generating Explanation',
    description: 'Creating plain-language insights using AI',
  },
];

export default function Processing() {
  const [currentStep, setCurrentStep] = useState(0);
  const navigate = useNavigate();
  const location = useLocation();
  const fileName = location.state?.fileName || 'your report';

  useEffect(() => {
    const stepDurations = [2000, 2500, 3000];
    let timeoutId: NodeJS.Timeout;

    const advanceStep = (step: number) => {
      if (step < processingSteps.length) {
        setCurrentStep(step);
        timeoutId = setTimeout(() => advanceStep(step + 1), stepDurations[step] || 2000);
      } else {
        setTimeout(() => {
          navigate('/results', { state: { fileName } });
        }, 500);
      }
    };

    advanceStep(0);

    return () => {
      if (timeoutId) clearTimeout(timeoutId);
    };
  }, [navigate, fileName]);

  return (
    <Layout hideFooter>
      <div className="container flex min-h-[calc(100vh-4rem)] items-center justify-center py-12">
        <div className="mx-auto w-full max-w-xl">
          <div className="mb-8 text-center">
            <div className="mx-auto mb-4 flex h-16 w-16 items-center justify-center rounded-2xl bg-primary/10">
              <div className="h-8 w-8 animate-spin-slow rounded-full border-4 border-primary border-t-transparent" />
            </div>
            <h1 className="text-2xl font-bold">Analyzing Your Report</h1>
            <p className="mt-2 text-muted-foreground">
              Processing: {fileName}
            </p>
          </div>

          <div className="mb-8 rounded-xl border border-primary/20 bg-primary/5 p-4">
            <div className="flex items-start gap-3">
              <Shield className="mt-0.5 h-5 w-5 shrink-0 text-primary" />
              <div className="text-sm">
                <p className="font-medium text-foreground">Safety Notice</p>
                <p className="mt-1 text-muted-foreground">
                  This analysis is for informational purposes only and does not 
                  constitute medical advice, diagnosis, or treatment recommendations.
                </p>
              </div>
            </div>
          </div>

          <LoadingStepper steps={processingSteps} currentStep={currentStep} />

          <div className="mt-8 flex items-start gap-3 rounded-lg bg-secondary/50 p-4 text-sm text-muted-foreground">
            <AlertCircle className="mt-0.5 h-4 w-4 shrink-0 text-primary" />
            <p>
              Your report is being analyzed locally and will not be stored on our servers. 
              All processing is done in a secure, temporary environment.
            </p>
          </div>
        </div>
      </div>
    </Layout>
  );
}
