import { useState, useEffect } from 'react';
import { Layout } from '@/components/layout/Layout';
import { Button } from '@/components/ui/button';
import { Card, CardContent } from '@/components/ui/card';
import { StatusBadge, StatusType } from '@/components/StatusBadge';
import { FileText, Calendar, ChevronRight, Plus, Loader2 } from 'lucide-react';
import { Link } from 'react-router-dom';
import { resultsAPI } from '@/services/api';
import { toast } from 'sonner';

interface Report {
  id: string;
  createdAt: string;
  filename?: string;
  summary?: string;
  riskSummary?: {
    overallRisk: string;
    severityBannerColor?: string;
  };
  tests?: any[];
}

export default function History() {
  const [reports, setReports] = useState<Report[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchHistory = async () => {
      try {
        const response = await resultsAPI.getHistory();
        if (response.data.success) {
          setReports(response.data.data || []);
        }
      } catch (error) {
        console.error('Failed to fetch history:', error);
        toast.error('Failed to load report history');
      } finally {
        setLoading(false);
      }
    };

    fetchHistory();
  }, []);

  const mapRiskToStatus = (risk: string): StatusType => {
    const r = risk?.toLowerCase() || '';
    if (r.includes('high') || r.includes('severe')) return 'alert';
    if (r.includes('moderate') || r.includes('borderline')) return 'borderline';
    return 'normal';
  };

  const getReportCategory = (report: Report): string => {
    if (report.filename) {
      if (report.filename.toLowerCase().includes('lipid')) return 'Lipid Panel';
      if (report.filename.toLowerCase().includes('cbc')) return 'Complete Blood Count';
      if (report.filename.toLowerCase().includes('metabolic')) return 'Metabolic Panel';
    }
    if (report.tests && report.tests.length > 0) {
      const testNames = report.tests.map(t => t.name?.toLowerCase() || '').join(' ');
      if (testNames.includes('cholesterol') || testNames.includes('triglycerides')) return 'Lipid Panel';
      if (testNames.includes('hemoglobin') || testNames.includes('rbc')) return 'Hematology Panel';
      if (testNames.includes('glucose') || testNames.includes('sugar')) return 'Metabolic Panel';
    }
    return 'Lab Report Analysis';
  };

  if (loading) {
    return (
      <Layout>
        <div className="container py-8 md:py-12">
          <div className="flex h-[50vh] items-center justify-center">
            <Loader2 className="h-10 w-10 animate-spin text-primary" />
            <span className="ml-3 text-lg">Loading history...</span>
          </div>
        </div>
      </Layout>
    );
  }

  return (
    <Layout>
      <div className="container py-8 md:py-12">
        <div className="mb-8 flex flex-col gap-4 md:flex-row md:items-center md:justify-between">
          <div>
            <h1 className="text-2xl font-bold md:text-3xl">Report History</h1>
            <p className="mt-1 text-muted-foreground">
              View your previous lab report analyses
            </p>
          </div>
          <Button asChild>
            <Link to="/upload">
              <Plus className="mr-2 h-4 w-4" />
              Upload New Report
            </Link>
          </Button>
        </div>

        {reports.length > 0 ? (
          <div className="space-y-4">
            {reports.map((report) => (
              <Card
                key={report.id}
                className="transition-all duration-200 hover:border-primary/30 hover:shadow-medium"
              >
                <CardContent className="flex items-center gap-4 p-6">
                  <div className="flex h-12 w-12 shrink-0 items-center justify-center rounded-xl bg-primary/10">
                    <FileText className="h-6 w-6 text-primary" />
                  </div>
                  
                  <div className="flex-1 min-w-0">
                    <div className="flex items-center gap-3">
                      <h3 className="font-semibold truncate">{getReportCategory(report)}</h3>
                      <StatusBadge 
                        status={mapRiskToStatus(report.riskSummary?.overallRisk || 'normal')} 
                        size="sm" 
                      />
                    </div>
                    <p className="mt-1 text-sm text-muted-foreground truncate">
                      {report.summary || 'Analysis completed'}
                    </p>
                    <div className="mt-2 flex items-center gap-1 text-xs text-muted-foreground">
                      <Calendar className="h-3 w-3" />
                      {new Date(report.createdAt).toLocaleDateString('en-US', {
                        year: 'numeric',
                        month: 'long',
                        day: 'numeric',
                      })}
                    </div>
                  </div>

                  <Button asChild variant="ghost" size="sm">
                    <Link to={`/results/${report.id}`} state={{ analysis: report }}>
                      View Summary
                      <ChevronRight className="ml-1 h-4 w-4" />
                    </Link>
                  </Button>
                </CardContent>
              </Card>
            ))}
          </div>
        ) : (
          <Card>
            <CardContent className="flex flex-col items-center justify-center py-16 text-center">
              <div className="mb-4 flex h-16 w-16 items-center justify-center rounded-2xl bg-secondary">
                <FileText className="h-8 w-8 text-muted-foreground" />
              </div>
              <h3 className="text-lg font-semibold">No reports yet</h3>
              <p className="mt-1 text-muted-foreground">
                Upload your first lab report to get started
              </p>
              <Button asChild className="mt-4">
                <Link to="/upload">
                  <Plus className="mr-2 h-4 w-4" />
                  Upload Report
                </Link>
              </Button>
            </CardContent>
          </Card>
        )}

        <div className="mt-8 rounded-lg bg-secondary/50 p-4 text-sm text-muted-foreground">
          <p>
            <strong className="text-foreground">Privacy Note:</strong> For your security, 
            we only store analysis summaries and dates. Your original lab reports are not 
            retained on our servers.
          </p>
        </div>
      </div>
    </Layout>
  );
}
