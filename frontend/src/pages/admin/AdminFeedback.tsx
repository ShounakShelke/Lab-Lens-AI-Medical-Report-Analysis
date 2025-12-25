import { useState } from 'react';
import { Layout } from '@/components/layout/Layout';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { Button } from '@/components/ui/button';
import { Badge } from '@/components/ui/badge';
import { Textarea } from '@/components/ui/textarea';
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from '@/components/ui/table';
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from '@/components/ui/select';
import { 
  MessageSquare, 
  Flag, 
  CheckCircle, 
  Clock,
  AlertTriangle,
  Star
} from 'lucide-react';
import {
  Dialog,
  DialogContent,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from '@/components/ui/dialog';
import { useToast } from '@/hooks/use-toast';


const feedbackItems = [
  {
    id: '1',
    date: '2024-01-15',
    user: 'user***@email.com',
    type: 'accuracy',
    message: 'The explanation for my glucose levels was very helpful and easy to understand.',
    rating: 5,
    status: 'reviewed',
    notes: '',
  },
  {
    id: '2',
    date: '2024-01-14',
    user: 'user***@email.com',
    type: 'concern',
    message: 'The AI suggested I "definitely have" a condition. This seems too absolute.',
    rating: 2,
    status: 'flagged',
    notes: 'Investigated prompt v2.3.0 - issue fixed in v2.3.1',
  },
  {
    id: '3',
    date: '2024-01-14',
    user: 'user***@email.com',
    type: 'feature',
    message: 'Would love to be able to compare results over time.',
    rating: 4,
    status: 'new',
    notes: '',
  },
  {
    id: '4',
    date: '2024-01-13',
    user: 'user***@email.com',
    type: 'accuracy',
    message: 'Reference ranges didn\'t match my lab\'s ranges exactly.',
    rating: 3,
    status: 'reviewed',
    notes: 'Expected behavior - ranges vary by lab',
  },
];

const statusColors = {
  new: 'bg-primary/10 text-primary',
  reviewed: 'bg-status-normal/10 text-status-normal',
  flagged: 'bg-status-alert/10 text-status-alert',
};

const typeColors = {
  accuracy: 'bg-blue-500/10 text-blue-600',
  concern: 'bg-status-alert/10 text-status-alert',
  feature: 'bg-purple-500/10 text-purple-600',
};

export default function AdminFeedback() {
  const { toast } = useToast();
  const [feedback, setFeedback] = useState(feedbackItems);
  const [selectedFeedback, setSelectedFeedback] = useState<typeof feedbackItems[0] | null>(null);
  const [notes, setNotes] = useState('');

  const handleStatusChange = (id: string, newStatus: string) => {
    setFeedback(feedback.map((item) =>
      item.id === id ? { ...item, status: newStatus } : item
    ));
    toast({
      title: 'Status Updated',
      description: `Feedback marked as ${newStatus}`,
    });
  };

  const handleSaveNotes = (id: string) => {
    setFeedback(feedback.map((item) =>
      item.id === id ? { ...item, notes } : item
    ));
    toast({
      title: 'Notes Saved',
      description: 'Your notes have been saved.',
    });
  };

  const getStatusIcon = (status: string) => {
    switch (status) {
      case 'new':
        return <Clock className="h-3 w-3" />;
      case 'reviewed':
        return <CheckCircle className="h-3 w-3" />;
      case 'flagged':
        return <Flag className="h-3 w-3" />;
      default:
        return null;
    }
  };

  const renderStars = (rating: number) => {
    return (
      <div className="flex gap-0.5">
        {[1, 2, 3, 4, 5].map((star) => (
          <Star
            key={star}
            className={`h-4 w-4 ${
              star <= rating ? 'fill-status-borderline text-status-borderline' : 'text-muted'
            }`}
          />
        ))}
      </div>
    );
  };

  const newCount = feedback.filter((f) => f.status === 'new').length;
  const flaggedCount = feedback.filter((f) => f.status === 'flagged').length;

  return (
      <div className="container py-8">
        <div className="mb-8">
          <h1 className="text-2xl font-bold md:text-3xl">Feedback Review</h1>
          <p className="mt-1 text-muted-foreground">
            Monitor and respond to user feedback
          </p>
        </div>

        <div className="mb-8 grid gap-4 md:grid-cols-4">
          <Card>
            <CardContent className="flex items-center gap-4 p-6">
              <div className="flex h-12 w-12 items-center justify-center rounded-full bg-primary/10">
                <MessageSquare className="h-6 w-6 text-primary" />
              </div>
              <div>
                <p className="text-2xl font-bold">{feedback.length}</p>
                <p className="text-sm text-muted-foreground">Total Feedback</p>
              </div>
            </CardContent>
          </Card>
          <Card>
            <CardContent className="flex items-center gap-4 p-6">
              <div className="flex h-12 w-12 items-center justify-center rounded-full bg-primary/10">
                <Clock className="h-6 w-6 text-primary" />
              </div>
              <div>
                <p className="text-2xl font-bold">{newCount}</p>
                <p className="text-sm text-muted-foreground">New / Pending</p>
              </div>
            </CardContent>
          </Card>
          <Card>
            <CardContent className="flex items-center gap-4 p-6">
              <div className="flex h-12 w-12 items-center justify-center rounded-full bg-status-alert/10">
                <Flag className="h-6 w-6 text-status-alert" />
              </div>
              <div>
                <p className="text-2xl font-bold">{flaggedCount}</p>
                <p className="text-sm text-muted-foreground">Flagged</p>
              </div>
            </CardContent>
          </Card>
          <Card>
            <CardContent className="flex items-center gap-4 p-6">
              <div className="flex h-12 w-12 items-center justify-center rounded-full bg-status-borderline/10">
                <Star className="h-6 w-6 text-status-borderline" />
              </div>
              <div>
                <p className="text-2xl font-bold">4.2</p>
                <p className="text-sm text-muted-foreground">Avg Rating</p>
              </div>
            </CardContent>
          </Card>
        </div>

        <Card>
          <CardHeader>
            <CardTitle>User Feedback</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="rounded-lg border">
              <Table>
                <TableHeader>
                  <TableRow>
                    <TableHead>Date</TableHead>
                    <TableHead>Type</TableHead>
                    <TableHead>Rating</TableHead>
                    <TableHead className="max-w-[300px]">Message</TableHead>
                    <TableHead>Status</TableHead>
                    <TableHead>Actions</TableHead>
                  </TableRow>
                </TableHeader>
                <TableBody>
                  {feedback.map((item) => (
                    <TableRow key={item.id}>
                      <TableCell className="text-sm">{item.date}</TableCell>
                      <TableCell>
                        <Badge className={typeColors[item.type as keyof typeof typeColors]}>
                          {item.type}
                        </Badge>
                      </TableCell>
                      <TableCell>{renderStars(item.rating)}</TableCell>
                      <TableCell className="max-w-[300px] truncate text-sm">
                        {item.message}
                      </TableCell>
                      <TableCell>
                        <Badge className={`gap-1 ${statusColors[item.status as keyof typeof statusColors]}`}>
                          {getStatusIcon(item.status)}
                          {item.status}
                        </Badge>
                      </TableCell>
                      <TableCell>
                        <Dialog>
                          <DialogTrigger asChild>
                            <Button
                              variant="ghost"
                              size="sm"
                              onClick={() => {
                                setSelectedFeedback(item);
                                setNotes(item.notes);
                              }}
                            >
                              Review
                            </Button>
                          </DialogTrigger>
                          <DialogContent className="max-w-lg">
                            <DialogHeader>
                              <DialogTitle>Feedback Details</DialogTitle>
                            </DialogHeader>
                            <div className="space-y-4">
                              <div className="flex items-center justify-between">
                                <div className="flex items-center gap-2">
                                  <Badge className={typeColors[item.type as keyof typeof typeColors]}>
                                    {item.type}
                                  </Badge>
                                  {renderStars(item.rating)}
                                </div>
                                <span className="text-sm text-muted-foreground">
                                  {item.date}
                                </span>
                              </div>

                              <div className="rounded-lg bg-secondary p-4">
                                <p className="text-sm">{item.message}</p>
                              </div>

                              <div className="space-y-2">
                                <label className="text-sm font-medium">Status</label>
                                <Select
                                  value={item.status}
                                  onValueChange={(value) => handleStatusChange(item.id, value)}
                                >
                                  <SelectTrigger>
                                    <SelectValue />
                                  </SelectTrigger>
                                  <SelectContent>
                                    <SelectItem value="new">New</SelectItem>
                                    <SelectItem value="reviewed">Reviewed</SelectItem>
                                    <SelectItem value="flagged">Flagged</SelectItem>
                                  </SelectContent>
                                </Select>
                              </div>

                              <div className="space-y-2">
                                <label className="text-sm font-medium">Notes</label>
                                <Textarea
                                  value={notes}
                                  onChange={(e) => setNotes(e.target.value)}
                                  placeholder="Add internal notes..."
                                  rows={3}
                                />
                              </div>

                              <Button
                                className="w-full"
                                onClick={() => handleSaveNotes(item.id)}
                              >
                                Save Notes
                              </Button>
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
