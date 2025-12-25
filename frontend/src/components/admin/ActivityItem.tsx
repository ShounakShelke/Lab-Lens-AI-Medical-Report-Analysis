import { FileText, AlertTriangle, Users, MessageSquare, CheckCircle } from 'lucide-react';
import { cn } from '@/lib/utils';

interface ActivityItemProps {
  type: 'report' | 'flag' | 'user' | 'review' | 'system';
  message: string;
  time: string;
}

const typeConfig = {
  report: {
    icon: FileText,
    color: 'text-status-normal',
    bgColor: 'bg-status-normal-bg',
  },
  flag: {
    icon: AlertTriangle,
    color: 'text-status-alert',
    bgColor: 'bg-status-alert-bg',
  },
  user: {
    icon: Users,
    color: 'text-status-normal',
    bgColor: 'bg-status-normal-bg',
  },
  review: {
    icon: CheckCircle,
    color: 'text-status-normal',
    bgColor: 'bg-status-normal-bg',
  },
  system: {
    icon: MessageSquare,
    color: 'text-muted-foreground',
    bgColor: 'bg-muted',
  },
};

export function ActivityItem({ type, message, time }: ActivityItemProps) {
  const config = typeConfig[type];
  const Icon = config.icon;

  return (
    <div className="flex items-start gap-3 py-3">
      <div className={cn('flex h-8 w-8 items-center justify-center rounded-full', config.bgColor)}>
        <Icon className={cn('h-4 w-4', config.color)} />
      </div>
      <div className="flex-1 min-w-0">
        <p className="text-sm text-foreground">{message}</p>
        <p className="text-xs text-muted-foreground mt-1">{time}</p>
      </div>
    </div>
  );
}
