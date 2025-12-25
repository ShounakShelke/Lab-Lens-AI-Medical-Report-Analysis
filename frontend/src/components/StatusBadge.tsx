import { cn } from '@/lib/utils';
import { CheckCircle, AlertCircle, XCircle } from 'lucide-react';

export type StatusType = 'normal' | 'borderline' | 'alert';

interface StatusBadgeProps {
  status: StatusType;
  label?: string;
  size?: 'sm' | 'md' | 'lg';
  showIcon?: boolean;
}

const statusConfig = {
  normal: {
    label: 'Normal',
    icon: CheckCircle,
    className: 'bg-status-normal/10 text-status-normal border-status-normal/30',
  },
  borderline: {
    label: 'Borderline',
    icon: AlertCircle,
    className: 'bg-status-borderline/10 text-status-borderline border-status-borderline/30',
  },
  alert: {
    label: 'Consult Doctor',
    icon: XCircle,
    className: 'bg-status-alert/10 text-status-alert border-status-alert/30',
  },
};

const sizeConfig = {
  sm: 'px-2 py-0.5 text-xs',
  md: 'px-2.5 py-1 text-sm',
  lg: 'px-3 py-1.5 text-sm',
};

export function StatusBadge({ 
  status, 
  label, 
  size = 'md',
  showIcon = true 
}: StatusBadgeProps) {
  const config = statusConfig[status];
  const Icon = config.icon;

  return (
    <span
      className={cn(
        'inline-flex items-center gap-1.5 rounded-full border font-medium',
        config.className,
        sizeConfig[size]
      )}
    >
      {showIcon && <Icon className={cn(
        size === 'sm' ? 'h-3 w-3' : size === 'lg' ? 'h-4 w-4' : 'h-3.5 w-3.5'
      )} />}
      {label || config.label}
    </span>
  );
}
