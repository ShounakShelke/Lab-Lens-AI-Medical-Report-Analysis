import { useState, useEffect } from 'react';
import { Layout } from '@/components/layout/Layout';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { Button } from '@/components/ui/button';
import { Badge } from '@/components/ui/badge';
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from '@/components/ui/table';
import { 
  Brain, 
  AlertTriangle, 
  CheckCircle, 
  Eye,
  Clock
} from 'lucide-react';
import {
  Dialog,
  DialogContent,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from '@/components/ui/dialog';
import { toast } from 'sonner';

type PromptOutput = {
  id: string;
  timestamp: string;
  promptVersion: string;
  input: string;
  output: string;
  flagged: boolean;
  flaggedWords: string[];
};

const mockOutputs: PromptOutput[] = [
  {
    id: '1',
    timestamp: '2024-01-15 14:32:00',
    promptVersion: 'v2.3.1',
    input: 'CBC panel with elevated WBC',
    output: 'Your white blood cell count may indicate an immune response. This can be associated with infection or inflammation.',
    flagged: false,
    flaggedWords: [],
  },
  {
    id: '2',
    timestamp: '2024-01-15 14:28:00',
    promptVersion: 'v2.3.1',
    input: 'Lipid panel results',
    output: 'Your cholesterol levels suggest you should see a doctor to diagnose heart disease.',
    flagged: true,
    flaggedWords: ['diagnose'],
  },
  {
    id: '3',
    timestamp: '2024-01-15 14:15:00',
    promptVersion: 'v2.3.1',
    input: 'Thyroid panel',
    output: 'Your TSH levels are within normal range, suggesting healthy thyroid function.',
    flagged: false,
    flaggedWords: [],
  },
  {
    id: '4',
    timestamp: '2024-01-15 13:58:00',
    promptVersion: 'v2.3.1',
    input: 'Glucose test',
    output: 'Based on these results, I prescribe lifestyle changes to cure your condition.',
    flagged: true,
    flaggedWords: ['prescribe', 'cure'],
  },
];

export default function AdminPrompts() {
  const [outputs, setOutputs] = useState<PromptOutput[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const [selectedOutput, setSelectedOutput] = useState<PromptOutput | null>(null);

  useEffect(() => {
    
    setTimeout(() => {
      setOutputs(mockOutputs);
      setIsLoading(false);
    }, 1000);
  }, []);

  const highlightFlaggedWords = (text: string, words: string[]) => {
    if (words.length === 0) return text;
    
    let result = text;
    words.forEach((word) => {
      const regex = new RegExp(`(${word})`, 'gi');
      result = result.replace(
        regex,
        '<mark class="bg-status-alert/30 text-status-alert px-1 rounded">$1</mark>'
      );
    });
    return result;
  };

  return (
      <div className="container py-8">
        <div className="mb-8 flex items-center justify-between">
          <div>
            <h1 className="text-2xl font-bold md:text-3xl">Prompt & Safety Monitor</h1>
            <p className="mt-1 text-muted-foreground">
              Review AI outputs and flagged responses
            </p>
          </div>
          <Badge variant="secondary" className="text-sm">
            <Brain className="mr-1 h-4 w-4" />
            Current: v2.3.1
          </Badge>
        </div>

        <div className="mb-8 grid gap-4 md:grid-cols-3">
          <Card>
            <CardContent className="flex items-center gap-4 p-6">
              <div className="flex h-12 w-12 items-center justify-center rounded-full bg-status-normal/10">
                <CheckCircle className="h-6 w-6 text-status-normal" />
              </div>
              <div>
                <p className="text-2xl font-bold">98.2%</p>
                <p className="text-sm text-muted-foreground">Safe Outputs</p>
              </div>
            </CardContent>
          </Card>
          <Card>
            <CardContent className="flex items-center gap-4 p-6">
              <div className="flex h-12 w-12 items-center justify-center rounded-full bg-status-alert/10">
                <AlertTriangle className="h-6 w-6 text-status-alert" />
              </div>
              <div>
                <p className="text-2xl font-bold">12</p>
                <p className="text-sm text-muted-foreground">Flagged This Week</p>
              </div>
            </CardContent>
          </Card>
          <Card>
            <CardContent className="flex items-center gap-4 p-6">
              <div className="flex h-12 w-12 items-center justify-center rounded-full bg-primary/10">
                <Clock className="h-6 w-6 text-primary" />
              </div>
              <div>
                <p className="text-2xl font-bold">1.2s</p>
                <p className="text-sm text-muted-foreground">Avg Response Time</p>
              </div>
            </CardContent>
          </Card>
        </div>

        <Card>
          <CardHeader>
            <CardTitle>Recent AI Outputs</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="rounded-lg border">
              <Table>
                <TableHeader>
                  <TableRow>
                    <TableHead>Timestamp</TableHead>
                    <TableHead>Version</TableHead>
                    <TableHead>Input Summary</TableHead>
                    <TableHead>Status</TableHead>
                    <TableHead>Actions</TableHead>
                  </TableRow>
                </TableHeader>
                <TableBody>
                  {isLoading ? (
                    <TableRow>
                      <TableCell colSpan={5} className="text-center py-8">
                        Loading monitor data...
                      </TableCell>
                    </TableRow>
                  ) : outputs.map((output) => (
                    <TableRow key={output.id}>
                      <TableCell className="font-mono text-sm">
                        {output.timestamp}
                      </TableCell>
                      <TableCell>
                        <Badge variant="outline">{output.promptVersion}</Badge>
                      </TableCell>
                      <TableCell className="max-w-[200px] truncate">
                        {output.input}
                      </TableCell>
                      <TableCell>
                        {output.flagged ? (
                          <Badge variant="destructive" className="gap-1">
                            <AlertTriangle className="h-3 w-3" />
                            Flagged
                          </Badge>
                        ) : (
                          <Badge variant="secondary" className="gap-1 text-status-normal">
                            <CheckCircle className="h-3 w-3" />
                            Safe
                          </Badge>
                        )}
                      </TableCell>
                      <TableCell>
                        <Dialog>
                          <DialogTrigger asChild>
                            <Button
                              variant="ghost"
                              size="sm"
                              onClick={() => setSelectedOutput(output)}
                            >
                              <Eye className="mr-1 h-4 w-4" />
                              View
                            </Button>
                          </DialogTrigger>
                          <DialogContent className="max-w-2xl">
                            <DialogHeader>
                              <DialogTitle className="flex items-center gap-2">
                                AI Output Review
                                {output.flagged && (
                                  <Badge variant="destructive">Flagged</Badge>
                                )}
                              </DialogTitle>
                            </DialogHeader>
                            <div className="space-y-4">
                              <div>
                                <p className="text-sm font-medium text-muted-foreground">
                                  Input
                                </p>
                                <p className="mt-1 rounded-lg bg-secondary p-3">
                                  {output.input}
                                </p>
                              </div>
                              <div>
                                <p className="text-sm font-medium text-muted-foreground">
                                  Output
                                </p>
                                <p
                                  className="mt-1 rounded-lg bg-secondary p-3"
                                  dangerouslySetInnerHTML={{
                                    __html: highlightFlaggedWords(
                                      output.output,
                                      output.flaggedWords
                                    ),
                                  }}
                                />
                              </div>
                              {output.flaggedWords.length > 0 && (
                                <div>
                                  <p className="text-sm font-medium text-muted-foreground">
                                    Flagged Words
                                  </p>
                                  <div className="mt-2 flex flex-wrap gap-2">
                                    {output.flaggedWords.map((word) => (
                                      <Badge key={word} variant="destructive">
                                        {word}
                                      </Badge>
                                    ))}
                                  </div>
                                </div>
                              )}
                              <div className="flex gap-2 pt-4">
                                <Button variant="secondary" className="flex-1">
                                  Mark as Reviewed
                                </Button>
                                <Button variant="destructive" className="flex-1">
                                  Escalate Issue
                                </Button>
                              </div>
                            </div>
                          </DialogContent>
                        </Dialog>
                      </TableCell>
                    </TableRow>
                  ))}
                </TableBody>
              </Table>
            </div>
          </CardContent>
        </Card>
      </div>
  );
}
