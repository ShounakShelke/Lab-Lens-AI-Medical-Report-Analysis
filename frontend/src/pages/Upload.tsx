import { useState, useCallback } from 'react';
import { useNavigate } from 'react-router-dom';
import { Layout } from '@/components/layout/Layout';
import { UploadCard } from '@/components/UploadCard';
import { Shield, FileText, Zap } from 'lucide-react';
import { uploadAPI } from '@/services/api';
import { toast } from 'sonner';

export default function Upload() {
  const [uploadProgress, setUploadProgress] = useState(0);
  const [isUploading, setIsUploading] = useState(false);
  const navigate = useNavigate();

  const handleFileSelect = useCallback(async (file: File) => {
    setIsUploading(true);
    setUploadProgress(0);
    
    try {
      const response = await uploadAPI.uploadReport(file, (progress) => {
        setUploadProgress(progress);
      });

      if (response.data.success) {
        setUploadProgress(100);
        toast.success("Analysis Complete!");
        
        setTimeout(() => {
          navigate('/results', { 
            state: { 
              analysis: response.data.data, 
              reportId: response.data.reportId,
              fileName: file.name
            } 
          });
        }, 500);
      } else {
        throw new Error(response.data.error || "Analysis failed");
      }
      
    } catch (error) {
      console.error("Upload failed", error);
      toast.error("Failed to upload/analyze report. Please try again.");
      setUploadProgress(0);
    } finally {
      setIsUploading(false);
    }
  }, [navigate]);

  const tips = [
    {
      icon: FileText,
      title: 'Supported Formats',
      description: 'PDF, JPG, or PNG files from any lab provider',
    },
    {
      icon: Shield,
      title: 'Privacy First',
      description: 'Files are processed in memory and never stored',
    },
    {
      icon: Zap,
      title: 'Quick Analysis',
      description: 'Get results in under 30 seconds',
    },
  ];

  return (
    <Layout>
      <div className="container py-12 md:py-20">
        <div className="mx-auto max-w-3xl">
          <div className="mb-8 text-center">
            <h1 className="mb-3 text-3xl font-bold md:text-4xl">
              Upload Your Lab Report
            </h1>
            <p className="text-lg text-muted-foreground">
              Drag and drop your report or click to browse
            </p>
          </div>

          <UploadCard
            onFileSelect={handleFileSelect}
            uploadProgress={uploadProgress}
            isUploading={isUploading}
          />

          <div className="mt-12 grid gap-6 md:grid-cols-3">
            {tips.map((tip) => (
              <div
                key={tip.title}
                className="flex items-start gap-3 rounded-lg border border-border bg-card p-4"
              >
                <div className="flex h-10 w-10 shrink-0 items-center justify-center rounded-lg bg-primary/10">
                  <tip.icon className="h-5 w-5 text-primary" />
                </div>
                <div>
                  <h3 className="font-medium">{tip.title}</h3>
                  <p className="mt-1 text-sm text-muted-foreground">
                    {tip.description}
                  </p>
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>
    </Layout>
  );
}
