import { cn } from '@/lib/utils';
import { Check, Loader2, Circle } from 'lucide-react';

interface Step {
  id: string;
  label: string;
  description?: string;
}

interface LoadingStepperProps {
  steps: Step[];
  currentStep: number;
  className?: string;
}

export function LoadingStepper({ steps, currentStep, className }: LoadingStepperProps) {
  return (
    <div className={cn('space-y-4', className)}>
      {steps.map((step, index) => {
        const isCompleted = index < currentStep;
        const isActive = index === currentStep;
        const isPending = index > currentStep;

        return (
          <div
            key={step.id}
            className={cn(
              'flex items-start gap-4 rounded-lg border p-4 transition-all duration-300',
              isCompleted && 'border-status-normal/30 bg-status-normal/5',
              isActive && 'border-primary/50 bg-primary/5 shadow-soft',
              isPending && 'border-border bg-card opacity-60'
            )}
          >
            <div
              className={cn(
                'flex h-8 w-8 shrink-0 items-center justify-center rounded-full transition-all duration-300',
                isCompleted && 'bg-status-normal text-primary-foreground',
                isActive && 'bg-primary text-primary-foreground',
                isPending && 'bg-secondary text-muted-foreground'
              )}
            >
              {isCompleted ? (
                <Check className="h-4 w-4" />
              ) : isActive ? (
                <Loader2 className="h-4 w-4 animate-spin" />
              ) : (
                <Circle className="h-4 w-4" />
              )}
            </div>

            <div className="flex-1 space-y-1">
              <p
                className={cn(
                  'font-medium transition-colors',
                  isCompleted && 'text-status-normal',
                  isActive && 'text-foreground',
                  isPending && 'text-muted-foreground'
                )}
              >
                {step.label}
              </p>
              {step.description && (
                <p className="text-sm text-muted-foreground">{step.description}</p>
              )}
            </div>

            {isCompleted && (
              <span className="text-xs font-medium text-status-normal">Complete</span>
            )}
            {isActive && (
              <span className="text-xs font-medium text-primary animate-pulse-soft">
                Processing...
              </span>
            )}
          </div>
        );
      })}
    </div>
  );
}
