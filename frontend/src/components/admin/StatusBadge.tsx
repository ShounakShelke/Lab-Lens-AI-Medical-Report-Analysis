import { cn } from '@/lib/utils';

interface StatusBadgeProps {
  status: 'new' | 'reviewed' | 'flagged' | 'safe' | 'flagged';
  className?: string;
}

const statusConfig = {
  new: {
    label: 'New',
    className: 'bg-blue-50 text-blue-700 border-blue-200',
  },
  reviewed: {
    label: 'Reviewed',
    className: 'bg-green-50 text-green-700 border-green-200',
  },
  flagged: {
    label: 'Flagged',
    className: 'bg-red-50 text-red-700 border-red-200',
  },
  safe: {
    label: 'Safe',
    className: 'bg-green-50 text-green-700 border-green-200',
  },
};

export function StatusBadge({ status, className }: StatusBadgeProps) {
  const config = statusConfig[status];

  return (
    <span
      className={cn(
        'inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium border',
        config.className,
        className
      )}
    >
      {config.label}
    </span>
  );
}
