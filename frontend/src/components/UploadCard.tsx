import { useState, useCallback } from 'react';
import { cn } from '@/lib/utils';
import { Upload, FileText, X, AlertCircle, CheckCircle } from 'lucide-react';
import { Button } from '@/components/ui/button';
import { Progress } from '@/components/ui/progress';

interface UploadCardProps {
  onFileSelect: (file: File) => void;
  uploadProgress?: number;
  isUploading?: boolean;
  acceptedTypes?: string[];
  maxSizeMB?: number;
}

export function UploadCard({
  onFileSelect,
  uploadProgress = 0,
  isUploading = false,
  acceptedTypes = ['application/pdf', 'image/jpeg', 'image/png'],
  maxSizeMB = 10,
}: UploadCardProps) {
  const [isDragging, setIsDragging] = useState(false);
  const [selectedFile, setSelectedFile] = useState<File | null>(null);
  const [error, setError] = useState<string | null>(null);

  const validateFile = useCallback(
    (file: File): string | null => {
      if (!acceptedTypes.includes(file.type)) {
        return 'Invalid file type. Please upload a PDF, JPG, or PNG file.';
      }
      if (file.size > maxSizeMB * 1024 * 1024) {
        return `File size exceeds ${maxSizeMB}MB limit.`;
      }
      return null;
    },
    [acceptedTypes, maxSizeMB]
  );

  const handleFile = useCallback(
    (file: File) => {
      const validationError = validateFile(file);
      if (validationError) {
        setError(validationError);
        return;
      }
      setError(null);
      setSelectedFile(file);
      onFileSelect(file);
    },
    [validateFile, onFileSelect]
  );

  const handleDrop = useCallback(
    (e: React.DragEvent) => {
      e.preventDefault();
      setIsDragging(false);
      const file = e.dataTransfer.files[0];
      if (file) handleFile(file);
    },
    [handleFile]
  );

  const handleDragOver = useCallback((e: React.DragEvent) => {
    e.preventDefault();
    setIsDragging(true);
  }, []);

  const handleDragLeave = useCallback((e: React.DragEvent) => {
    e.preventDefault();
    setIsDragging(false);
  }, []);

  const handleInputChange = useCallback(
    (e: React.ChangeEvent<HTMLInputElement>) => {
      const file = e.target.files?.[0];
      if (file) handleFile(file);
    },
    [handleFile]
  );

  const clearFile = useCallback(() => {
    setSelectedFile(null);
    setError(null);
  }, []);

  const formatFileSize = (bytes: number) => {
    if (bytes < 1024) return `${bytes} B`;
    if (bytes < 1024 * 1024) return `${(bytes / 1024).toFixed(1)} KB`;
    return `${(bytes / (1024 * 1024)).toFixed(1)} MB`;
  };

  return (
    <div className="w-full space-y-4">
      <div
        onDrop={handleDrop}
        onDragOver={handleDragOver}
        onDragLeave={handleDragLeave}
        className={cn(
          'relative flex min-h-[280px] flex-col items-center justify-center rounded-xl border-2 border-dashed p-8 transition-all duration-200',
          isDragging
            ? 'border-primary bg-primary/5 shadow-glow'
            : 'border-border bg-card hover:border-primary/50 hover:bg-secondary/30',
          isUploading && 'pointer-events-none opacity-70'
        )}
      >
        {selectedFile ? (
          <div className="flex w-full max-w-sm flex-col items-center gap-4">
            <div className="flex h-16 w-16 items-center justify-center rounded-xl bg-primary/10">
              <FileText className="h-8 w-8 text-primary" />
            </div>
            <div className="text-center">
              <p className="font-medium">{selectedFile.name}</p>
              <p className="text-sm text-muted-foreground">
                {formatFileSize(selectedFile.size)}
              </p>
            </div>
            {isUploading ? (
              <div className="w-full space-y-3">
                <Progress value={uploadProgress} className="h-2" />
                <div className="text-center space-y-1">
                  <p className="text-sm font-medium text-foreground">
                    {uploadProgress < 100 ? 'Uploading & Analyzing...' : 'Finishing analysis...'}
                  </p>
                  <p className="text-xs text-muted-foreground">
                    {uploadProgress < 30 && 'Uploading your report...'}
                    {uploadProgress >= 30 && uploadProgress < 60 && 'Extracting text from image...'}
                    {uploadProgress >= 60 && uploadProgress < 90 && 'AI analyzing your results...'}
                    {uploadProgress >= 90 && 'Preparing your report...'}
                  </p>
                </div>
              </div>
            ) : uploadProgress === 100 ? (
              <div className="flex items-center gap-2 text-status-normal">
                <CheckCircle className="h-5 w-5" />
                <span className="font-medium">Analysis complete! Redirecting...</span>
              </div>
            ) : (
              <div className="flex gap-2">
                <Button variant="ghost" size="sm" onClick={clearFile}>
                  <X className="mr-1 h-4 w-4" />
                  Remove
                </Button>
              </div>
            )}
          </div>
        ) : (
          <>
            <div className="mb-4 flex h-16 w-16 items-center justify-center rounded-xl bg-primary/10">
              <Upload className="h-8 w-8 text-primary" />
            </div>
            <div className="text-center">
              <p className="text-lg font-medium">
                Drop your lab report here
              </p>
              <p className="mt-1 text-sm text-muted-foreground">
                or click to browse files
              </p>
            </div>
            <div className="mt-4 flex flex-wrap items-center justify-center gap-2 text-xs text-muted-foreground">
              <span className="rounded-full bg-secondary px-2 py-1">PDF</span>
              <span className="rounded-full bg-secondary px-2 py-1">JPG</span>
              <span className="rounded-full bg-secondary px-2 py-1">PNG</span>
              <span>• Max {maxSizeMB}MB</span>
            </div>
            <input
              type="file"
              accept={acceptedTypes.join(',')}
              onChange={handleInputChange}
              className="absolute inset-0 cursor-pointer opacity-0"
              disabled={isUploading}
            />
          </>
        )}
      </div>

      {error && (
        <div className="flex items-center gap-2 rounded-lg border border-status-alert/30 bg-status-alert/5 p-3 text-sm text-status-alert">
          <AlertCircle className="h-4 w-4 shrink-0" />
          {error}
        </div>
      )}

      <div className="flex items-start gap-2 rounded-lg bg-secondary/50 p-3 text-xs text-muted-foreground">
        <AlertCircle className="mt-0.5 h-4 w-4 shrink-0 text-primary" />
        <p>
          Your reports are processed temporarily and are not stored on our servers. 
          All data is encrypted during transmission.
        </p>
      </div>
    </div>
  );
}
