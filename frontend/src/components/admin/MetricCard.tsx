import { ReactNode } from 'react';
import { cn } from '@/lib/utils';
import { TrendingUp, TrendingDown, Minus } from 'lucide-react';

interface MetricCardProps {
  title: string;
  value: string | number;
  icon: ReactNode;
  trend?: {
    value: number;
    label: string;
  };
  variant?: 'default' | 'success' | 'warning' | 'danger';
  className?: string;
}

const variantStyles = {
  default: {
    icon: 'bg-primary/10 text-primary',
    trend: 'text-muted-foreground',
  },
  success: {
    icon: 'bg-status-normal-bg text-status-normal',
    trend: 'text-status-normal',
  },
  warning: {
    icon: 'bg-status-borderline-bg text-status-borderline',
    trend: 'text-status-borderline',
  },
  danger: {
    icon: 'bg-status-alert-bg text-status-alert',
    trend: 'text-status-alert',
  },
};

export function MetricCard({
  title,
  value,
  icon,
  trend,
  variant = 'default',
  className
}: MetricCardProps) {
  const styles = variantStyles[variant];

  const TrendIcon = trend
    ? trend.value > 0
      ? TrendingUp
      : trend.value < 0
        ? TrendingDown
        : Minus
    : null;

  return (
    <div className={cn(
      "bg-card rounded-xl p-5 shadow-card border border-border animate-fade-in",
      className
    )}>
      <div className="flex items-start justify-between">
        <div className="space-y-3">
          <p className="text-sm font-medium text-muted-foreground">{title}</p>
          <p className="text-3xl font-display font-bold text-foreground">{value}</p>
          {trend && (
            <div className="flex items-center gap-1.5">
              {TrendIcon && (
                <TrendIcon className={cn("w-4 h-4", styles.trend)} />
              )}
              <span className={cn("text-sm font-medium", styles.trend)}>
                {trend.value > 0 ? '+' : ''}{trend.value}%
              </span>
              <span className="text-sm text-muted-foreground">{trend.label}</span>
            </div>
          )}
        </div>
        <div className={cn("w-12 h-12 rounded-xl flex items-center justify-center", styles.icon)}>
          {icon}
        </div>
      </div>
    </div>
  );
}
