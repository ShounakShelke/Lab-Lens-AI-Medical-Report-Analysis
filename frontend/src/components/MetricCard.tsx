import { cn } from '@/lib/utils';
import { LucideIcon, TrendingUp, TrendingDown, Minus } from 'lucide-react';

interface MetricCardProps {
  title: string;
  value: string | number;
  subtitle?: string;
  icon: LucideIcon;
  trend?: {
    value: number;
    label: string;
  };
  variant?: 'default' | 'primary' | 'success' | 'warning' | 'danger';
}

const variantStyles = {
  default: 'bg-card border-border',
  primary: 'bg-primary/5 border-primary/20',
  success: 'bg-status-normal/5 border-status-normal/20',
  warning: 'bg-status-borderline/5 border-status-borderline/20',
  danger: 'bg-status-alert/5 border-status-alert/20',
};

const iconVariantStyles = {
  default: 'bg-secondary text-foreground',
  primary: 'bg-primary/10 text-primary',
  success: 'bg-status-normal/10 text-status-normal',
  warning: 'bg-status-borderline/10 text-status-borderline',
  danger: 'bg-status-alert/10 text-status-alert',
};

export function MetricCard({
  title,
  value,
  subtitle,
  icon: Icon,
  trend,
  variant = 'default',
}: MetricCardProps) {
  const getTrendIcon = () => {
    if (!trend) return null;
    if (trend.value > 0) return TrendingUp;
    if (trend.value < 0) return TrendingDown;
    return Minus;
  };

  const TrendIcon = getTrendIcon();

  return (
    <div
      className={cn(
        'rounded-xl border p-6 transition-all duration-200 hover:shadow-medium',
        variantStyles[variant]
      )}
    >
      <div className="flex items-start justify-between">
        <div className="space-y-2">
          <p className="text-sm font-medium text-muted-foreground">{title}</p>
          <p className="text-3xl font-bold tracking-tight">{value}</p>
          {subtitle && (
            <p className="text-sm text-muted-foreground">{subtitle}</p>
          )}
        </div>
        <div
          className={cn(
            'flex h-12 w-12 items-center justify-center rounded-lg',
            iconVariantStyles[variant]
          )}
        >
          <Icon className="h-6 w-6" />
        </div>
      </div>
      
      {trend && TrendIcon && (
        <div className="mt-4 flex items-center gap-1 text-sm">
          <TrendIcon
            className={cn(
              'h-4 w-4',
              trend.value > 0 && 'text-status-normal',
              trend.value < 0 && 'text-status-alert',
              trend.value === 0 && 'text-muted-foreground'
            )}
          />
          <span
            className={cn(
              'font-medium',
              trend.value > 0 && 'text-status-normal',
              trend.value < 0 && 'text-status-alert',
              trend.value === 0 && 'text-muted-foreground'
            )}
          >
            {trend.value > 0 ? '+' : ''}
            {trend.value}%
          </span>
          <span className="text-muted-foreground">{trend.label}</span>
        </div>
      )}
    </div>
  );
}
