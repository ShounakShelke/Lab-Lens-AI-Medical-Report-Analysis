import { useEffect, useState } from 'react';
import { useLocation, useParams, Link } from 'react-router-dom';
import { Layout } from '@/components/layout/Layout';
import { StatusBadge, StatusType } from '@/components/StatusBadge';
import { Button } from '@/components/ui/button';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from '@/components/ui/table';
import { 
  FileText, 
  Download, 
  Share2, 
  Lightbulb, 
  Heart, 
  Stethoscope,
  AlertCircle,
  CheckCircle,
  Loader2,
  MessageSquare
} from 'lucide-react';
import { resultsAPI } from '@/services/api';
import { toast } from 'sonner';

export default function Results() {
  const { state } = useLocation();
  const { reportId } = useParams();
  const [data, setData] = useState<any>(state?.analysis || null);
  const [loading, setLoading] = useState(!state?.analysis);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    if (!data && reportId) {
      setLoading(true);
      resultsAPI.getResults(reportId)
        .then(res => {
          if (res.data.success) {
            setData(res.data.data.analysis || res.data.data);
          } else {
            setError("Failed to load results");
          }
        })
        .catch(err => {
          console.error(err);
          setError("Error loading results");
        })
        .finally(() => setLoading(false));
    } else if (!data && !reportId) {
      setError("No report data found. Please upload a report.");
      setLoading(false);
    }
  }, [reportId, data]);

  if (loading) {
    return (
      <Layout>
        <div className="flex h-[50vh] items-center justify-center">
          <Loader2 className="h-10 w-10 animate-spin text-primary" />
          <span className="ml-3 text-lg">Loading results...</span>
        </div>
      </Layout>
    );
  }

  if (error || !data) {
    return (
      <Layout>
         <div className="flex h-[50vh] flex-col items-center justify-center gap-4 text-center">
            <AlertCircle className="h-12 w-12 text-destructive" />
            <h2 className="text-xl font-bold">{error || "No results available"}</h2>
            <Button asChild>
              <Link to="/upload">Upload New Report</Link>
            </Button>
         </div>
      </Layout>
    );
  }

  const riskSummary = data.riskSummary || { overallRisk: "Low", bannerMessage: "", severityBannerColor: "green" };
  const overallRisk = riskSummary.overallRisk;
  
  const getBannerStyles = (color: string) => {
      switch(color) {
          case 'red': return "bg-red-100 border-red-500 text-red-800";
          case 'yellow': return "bg-yellow-100 border-yellow-500 text-yellow-800";
          default: return "bg-green-100 border-green-500 text-green-800";
      }
  };

  const getTestRowStyles = (status: string) => {
      const s = status.toLowerCase();
      if (s === 'high' || s.includes('risk')) return "bg-red-50 text-red-900 font-medium";
      if (s === 'borderline') return "bg-yellow-50 text-yellow-900";
      return "";
  };

  const mapStatus = (status: string): StatusType => {
      const s = status?.toLowerCase() || "";
      if (s.includes('high') || s.includes('alert') || s.includes('critical') || s.includes('risk')) return 'alert';
      if (s.includes('borderline') || s.includes('monitor')) return 'borderline';
      return 'normal';
  };

  const testResults = data.tests || [];
  const lifestyleGuidance = data.lifestyle || [];
  
  const handleDownload = () => {
    window.print();
  };

  return (
    <Layout>
      <div className="container py-8 md:py-12 print:p-0">
        
        {/* Print-only Header */}
        <div className="hidden print:block mb-8 text-center border-b pb-6">
            <h1 className="text-3xl font-bold text-primary">Lab-Lens Analysis Report</h1>
            <p className="text-sm text-muted-foreground mt-2">Generated on {new Date().toLocaleDateString()} • Secure AI Laboratory Interpretation</p>
        </div>

        {overallRisk !== 'Low' && (
            <div className={`mb-8 flex items-center gap-4 rounded-xl border-l-4 p-6 shadow-sm ${getBannerStyles(riskSummary.severityBannerColor)} print:border`}>
                <AlertCircle className="h-8 w-8 shrink-0" />
                <div>
                    <h2 className="text-xl font-bold uppercase tracking-tight">{riskSummary.bannerMessage || "ATTENTION NEEDED"}</h2>
                    <p className="mt-1 font-medium opacity-90">
                        Based on your results, we detected patterns associated with {overallRisk}.
                        Please see the specialist recommendation below.
                    </p>
                </div>
            </div>
        )}

        <div className="mb-8 flex flex-col gap-4 md:flex-row md:items-center md:justify-between print:hidden">
          <div>
            <h1 className="text-2xl font-bold md:text-3xl">Your Results</h1>
            <p className="mt-1 text-muted-foreground">
              Analysis completed • {new Date().toLocaleDateString()}
            </p>
          </div>
          <div className="flex gap-3">
            <Button variant="outline" size="sm" asChild>
                <Link to="/chat" state={{ reportId: reportId || state?.reportId, analysis: data }}>
                    <MessageSquare className="mr-2 h-4 w-4" />
                    Ask Assistant
                </Link>
            </Button>
            <Button variant="outline" size="sm" onClick={handleDownload}>
              <Download className="mr-2 h-4 w-4" />
              Download / Print
            </Button>
          </div>
        </div>

        <div className="grid gap-8 lg:grid-cols-3">
          <div className="space-y-8 lg:col-span-2">
            
            <Card>
              <CardHeader>
                <CardTitle className="flex items-center gap-2">
                  <FileText className="h-5 w-5 text-primary" />
                  Clinical Data
                </CardTitle>
              </CardHeader>
              <CardContent>
                <div className="rounded-lg border">
                  <Table>
                    <TableHeader>
                      <TableRow>
                        <TableHead>Test Name</TableHead>
                        <TableHead>Value</TableHead>
                        <TableHead>Reference Range</TableHead>
                        <TableHead>Status</TableHead>
                      </TableRow>
                    </TableHeader>
                    <TableBody>
                      {testResults.length > 0 ? (
                        testResults.map((test: any, index: number) => (
                          <TableRow key={index} className={getTestRowStyles(test.status)}>
                            <TableCell className="font-medium">{test.name}</TableCell>
                            <TableCell>
                              {test.value} <span className="text-muted-foreground text-xs">{test.unit}</span>
                            </TableCell>
                            <TableCell className="text-muted-foreground">{test.ref_range || test.referenceRange || test.range}</TableCell>
                            <TableCell>
                              <StatusBadge status={mapStatus(test.status)} size="sm" />
                            </TableCell>
                          </TableRow>
                        ))
                      ) : (
                        <TableRow>
                          <TableCell colSpan={4} className="text-center">No tests detected</TableCell>
                        </TableRow>
                      )}
                    </TableBody>
                  </Table>
                </div>
              </CardContent>
            </Card>

            <Card>
              <CardHeader>
                <CardTitle className="flex items-center gap-2">
                  <Lightbulb className="h-5 w-5 text-primary" />
                  Interpretation
                </CardTitle>
              </CardHeader>
              <CardContent className="space-y-4">
                <p className="text-muted-foreground leading-relaxed">
                  {data.summary || "No summary available."}
                </p>
              </CardContent>
            </Card>
          </div>

          <div className="space-y-6">
            <Card className={`border-2 ${overallRisk === 'High' ? 'border-red-500/50 bg-red-50/10' : 'border-primary/20 bg-primary/5'}`}>
              <CardHeader>
                <CardTitle className="flex items-center gap-2 text-lg">
                  <Stethoscope className={`h-5 w-5 ${overallRisk === 'High' ? 'text-red-600' : 'text-primary'}`} />
                  Recommended Specialist
                </CardTitle>
              </CardHeader>
              <CardContent className="space-y-3">
                 <div className="rounded-lg bg-card p-4 shadow-sm">
                  <p className="text-sm font-medium text-muted-foreground">Based on severity:</p>
                  <p className={`text-xl font-bold ${overallRisk === 'High' ? 'text-red-600' : 'text-primary'}`}>
                      {data.recommendedSpecialist || data.specialist || "General Physician"}
                  </p>
                </div>
                <p className="text-xs text-muted-foreground">
                  *This recommendation is based on the specific abnormalities detected in your report.
                </p>
              </CardContent>
            </Card>

            <Card>
              <CardHeader>
                <CardTitle className="flex items-center gap-2 text-lg">
                  <Heart className="h-5 w-5 text-accent" />
                  Lifestyle Tips
                </CardTitle>
              </CardHeader>
              <CardContent className="space-y-4">
                {lifestyleGuidance.length > 0 ? (
                  lifestyleGuidance.map((tip: string, index: number) => (
                    <div key={index} className="flex gap-3">
                      <div className="flex h-10 w-10 shrink-0 items-center justify-center rounded-lg bg-accent/10">
                        <Heart className="h-5 w-5 text-accent" />
                      </div>
                      <div>
                        <p className="font-medium">Tip {index + 1}</p>
                        <p className="mt-1 text-sm text-muted-foreground">
                          {tip}
                        </p>
                      </div>
                    </div>
                  ))
                ) : (
                  <p className="text-sm text-muted-foreground">No specific lifestyle tips generated.</p>
                )}
              </CardContent>
            </Card>

            <Card>
              <CardContent className="space-y-3 p-4">
                <Button asChild variant="default" className="w-full">
                  <Link to="/upload">
                    Upload Another Report
                  </Link>
                </Button>
                <Button asChild variant="outline" className="w-full">
                  <Link to="/history">
                    View History
                  </Link>
                </Button>
              </CardContent>
            </Card>
          </div>
        </div>

        <div className="mt-8 rounded-xl border border-border bg-secondary/30 p-6">
          <div className="flex items-start gap-4">
            <AlertCircle className="mt-0.5 h-5 w-5 shrink-0 text-primary" />
            <div className="text-sm">
              <p className="font-medium text-foreground">Important Disclaimer</p>
              <p className="mt-1 text-muted-foreground">
                {data.disclaimer || "This analysis is generated by AI for educational purposes only. It does not constitute medical advice, diagnosis, or treatment recommendations."}
              </p>
            </div>
          </div>
        </div>
      </div>
    </Layout>
  );
}
