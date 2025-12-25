import { Layout } from '@/components/layout/Layout';
import { MetricCard } from '@/components/MetricCard';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { 
  FileText, 
  Users, 
  Brain, 
  AlertTriangle,
  CheckCircle,
  XCircle,
  TrendingUp
} from 'lucide-react';
import { PieChart, Pie, Cell, ResponsiveContainer, BarChart, Bar, XAxis, YAxis, Tooltip, Legend } from 'recharts';


const severityData = [
  { name: 'Normal', value: 65, color: 'hsl(142, 76%, 36%)' },
  { name: 'Borderline', value: 25, color: 'hsl(38, 92%, 50%)' },
  { name: 'Alert', value: 10, color: 'hsl(0, 84%, 60%)' },
];

const weeklyData = [
  { day: 'Mon', reports: 45 },
  { day: 'Tue', reports: 52 },
  { day: 'Wed', reports: 49 },
  { day: 'Thu', reports: 63 },
  { day: 'Fri', reports: 58 },
  { day: 'Sat', reports: 32 },
  { day: 'Sun', reports: 28 },
];

const recentActivity = [
  { id: 1, type: 'report', message: 'New report analyzed', time: '2 min ago', status: 'normal' },
  { id: 2, type: 'flag', message: 'AI output flagged for review', time: '15 min ago', status: 'alert' },
  { id: 3, type: 'report', message: 'New report analyzed', time: '32 min ago', status: 'borderline' },
  { id: 4, type: 'user', message: 'New user registered', time: '1 hour ago', status: 'normal' },
];

export default function AdminDashboard() {
  return (
      <div className="container py-8">
        <div className="mb-8">
          <h1 className="text-2xl font-bold md:text-3xl">Admin Dashboard</h1>
          <p className="mt-1 text-muted-foreground">
            Monitor system health and AI performance
          </p>
        </div>

        <div className="mb-8 grid gap-6 md:grid-cols-2 lg:grid-cols-4">
          <MetricCard
            title="Reports Processed"
            value="1,247"
            subtitle="This month"
            icon={FileText}
            trend={{ value: 12, label: 'vs last month' }}
            variant="primary"
          />
          <MetricCard
            title="Active Users"
            value="328"
            subtitle="Unique users"
            icon={Users}
            trend={{ value: 8, label: 'vs last month' }}
            variant="default"
          />
          <MetricCard
            title="Gemini API Calls"
            value="3,842"
            subtitle="This month"
            icon={Brain}
            trend={{ value: 15, label: 'vs last month' }}
            variant="default"
          />
          <MetricCard
            title="Flagged Outputs"
            value="12"
            subtitle="Pending review"
            icon={AlertTriangle}
            trend={{ value: -5, label: 'vs last month' }}
            variant="warning"
          />
        </div>

        <div className="mb-8 grid gap-6 lg:grid-cols-2">
          <Card>
            <CardHeader>
              <CardTitle className="text-lg">Severity Distribution</CardTitle>
            </CardHeader>
            <CardContent>
              <div className="flex items-center gap-8">
                <div className="h-48 w-48">
                  <ResponsiveContainer width="100%" height="100%">
                    <PieChart>
                      <Pie
                        data={severityData}
                        cx="50%"
                        cy="50%"
                        innerRadius={40}
                        outerRadius={70}
                        paddingAngle={5}
                        dataKey="value"
                      >
                        {severityData.map((entry, index) => (
                          <Cell key={`cell-${index}`} fill={entry.color} />
                        ))}
                      </Pie>
                    </PieChart>
                  </ResponsiveContainer>
                </div>
                <div className="space-y-3">
                  {severityData.map((item) => (
                    <div key={item.name} className="flex items-center gap-3">
                      <div
                        className="h-3 w-3 rounded-full"
                        style={{ backgroundColor: item.color }}
                      />
                      <span className="text-sm text-muted-foreground">{item.name}</span>
                      <span className="font-semibold">{item.value}%</span>
                    </div>
                  ))}
                </div>
              </div>
            </CardContent>
          </Card>

          <Card>
            <CardHeader>
              <CardTitle className="text-lg">Reports This Week</CardTitle>
            </CardHeader>
            <CardContent>
              <div className="h-48">
                <ResponsiveContainer width="100%" height="100%">
                  <BarChart data={weeklyData}>
                    <XAxis dataKey="day" axisLine={false} tickLine={false} />
                    <YAxis axisLine={false} tickLine={false} />
                    <Tooltip 
                      contentStyle={{ 
                        borderRadius: '8px',
                        border: '1px solid hsl(var(--border))',
                        boxShadow: 'var(--shadow-md)'
                      }}
                    />
                    <Bar 
                      dataKey="reports" 
                      fill="hsl(var(--primary))" 
                      radius={[4, 4, 0, 0]}
                    />
                  </BarChart>
                </ResponsiveContainer>
              </div>
            </CardContent>
          </Card>
        </div>

        <Card>
          <CardHeader>
            <CardTitle className="flex items-center gap-2 text-lg">
              <TrendingUp className="h-5 w-5 text-primary" />
              Recent Activity
            </CardTitle>
          </CardHeader>
          <CardContent>
            <div className="space-y-4">
              {recentActivity.map((activity) => (
                <div
                  key={activity.id}
                  className="flex items-center gap-4 rounded-lg border border-border p-4"
                >
                  <div
                    className={`flex h-10 w-10 items-center justify-center rounded-full ${
                      activity.status === 'normal'
                        ? 'bg-status-normal/10 text-status-normal'
                        : activity.status === 'borderline'
                        ? 'bg-status-borderline/10 text-status-borderline'
                        : 'bg-status-alert/10 text-status-alert'
                    }`}
                  >
                    {activity.status === 'normal' ? (
                      <CheckCircle className="h-5 w-5" />
                    ) : activity.status === 'borderline' ? (
                      <AlertTriangle className="h-5 w-5" />
                    ) : (
                      <XCircle className="h-5 w-5" />
                    )}
                  </div>
                  <div className="flex-1">
                    <p className="font-medium">{activity.message}</p>
                    <p className="text-sm text-muted-foreground">{activity.time}</p>
                  </div>
                </div>
              ))}
            </div>
          </CardContent>
        </Card>
      </div>
  );
}
