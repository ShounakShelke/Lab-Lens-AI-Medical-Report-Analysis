import { useState } from 'react';
import { Layout } from '@/components/layout/Layout';
import { Card, CardContent, CardHeader, CardTitle, CardDescription } from '@/components/ui/card';
import { Button } from '@/components/ui/button';
import { Textarea } from '@/components/ui/textarea';
import { Input } from '@/components/ui/input';
import { Badge } from '@/components/ui/badge';
import { 
  Shield, 
  Save, 
  Plus, 
  X, 
  AlertTriangle,
  CheckCircle 
} from 'lucide-react';
import { useToast } from '@/hooks/use-toast';

export default function AdminRules() {
  const { toast } = useToast();
  
  const [disclaimer, setDisclaimer] = useState(
    `Lab-Lens does not provide medical diagnosis, treatment recommendations, or clinical advice. This tool is for educational and informational purposes only. Always consult a qualified healthcare professional for medical decisions. Never disregard professional medical advice or delay seeking it because of something you have learned from this tool.`
  );

  const [allowedPhrases, setAllowedPhrases] = useState([
    'may indicate',
    'can be associated with',
    'might suggest',
    'could be related to',
    'is often seen with',
    'consider consulting',
    'general wellness tips',
    'educational purposes',
  ]);

  const [blockedWords, setBlockedWords] = useState([
    'diagnose',
    'cure',
    'prescribe',
    'treat',
    'medicine',
    'medication',
    'drug',
    'therapy',
    'definitely',
    'certainly',
    'guaranteed',
  ]);

  const [newAllowedPhrase, setNewAllowedPhrase] = useState('');
  const [newBlockedWord, setNewBlockedWord] = useState('');

  const handleAddAllowedPhrase = () => {
    if (newAllowedPhrase.trim()) {
      setAllowedPhrases([...allowedPhrases, newAllowedPhrase.trim()]);
      setNewAllowedPhrase('');
    }
  };

  const handleAddBlockedWord = () => {
    if (newBlockedWord.trim()) {
      setBlockedWords([...blockedWords, newBlockedWord.trim()]);
      setNewBlockedWord('');
    }
  };

  const handleRemoveAllowedPhrase = (phrase: string) => {
    setAllowedPhrases(allowedPhrases.filter((p) => p !== phrase));
  };

  const handleRemoveBlockedWord = (word: string) => {
    setBlockedWords(blockedWords.filter((w) => w !== word));
  };

  const handleSave = () => {
    toast({
      title: 'Rules Updated',
      description: 'Safety rules have been saved successfully.',
    });
  };

  return (
      <div className="container py-8">
        <div className="mb-8 flex items-center justify-between">
          <div>
            <h1 className="text-2xl font-bold md:text-3xl">Disclaimer & Rules</h1>
            <p className="mt-1 text-muted-foreground">
              Configure safety guidelines and content filtering
            </p>
          </div>
          <Button onClick={handleSave}>
            <Save className="mr-2 h-4 w-4" />
            Save Changes
          </Button>
        </div>

        <div className="grid gap-8 lg:grid-cols-2">
          <Card className="lg:col-span-2">
            <CardHeader>
              <CardTitle className="flex items-center gap-2">
                <Shield className="h-5 w-5 text-primary" />
                Medical Disclaimer
              </CardTitle>
              <CardDescription>
                This disclaimer is shown to users throughout the application
              </CardDescription>
            </CardHeader>
            <CardContent>
              <Textarea
                value={disclaimer}
                onChange={(e) => setDisclaimer(e.target.value)}
                rows={5}
                className="resize-none"
              />
              <p className="mt-2 text-sm text-muted-foreground">
                {disclaimer.length} characters
              </p>
            </CardContent>
          </Card>

          <Card>
            <CardHeader>
              <CardTitle className="flex items-center gap-2">
                <CheckCircle className="h-5 w-5 text-status-normal" />
                Allowed Phrases
              </CardTitle>
              <CardDescription>
                Safe phrases the AI is encouraged to use
              </CardDescription>
            </CardHeader>
            <CardContent>
              <div className="mb-4 flex gap-2">
                <Input
                  value={newAllowedPhrase}
                  onChange={(e) => setNewAllowedPhrase(e.target.value)}
                  placeholder="Add new phrase..."
                  onKeyDown={(e) => e.key === 'Enter' && handleAddAllowedPhrase()}
                />
                <Button onClick={handleAddAllowedPhrase} size="icon">
                  <Plus className="h-4 w-4" />
                </Button>
              </div>
              <div className="flex flex-wrap gap-2">
                {allowedPhrases.map((phrase) => (
                  <Badge
                    key={phrase}
                    variant="secondary"
                    className="gap-1 bg-status-normal/10 text-status-normal hover:bg-status-normal/20"
                  >
                    {phrase}
                    <button
                      onClick={() => handleRemoveAllowedPhrase(phrase)}
                      className="ml-1 rounded-full p-0.5 hover:bg-status-normal/20"
                    >
                      <X className="h-3 w-3" />
                    </button>
                  </Badge>
                ))}
              </div>
            </CardContent>
          </Card>

          <Card>
            <CardHeader>
              <CardTitle className="flex items-center gap-2">
                <AlertTriangle className="h-5 w-5 text-status-alert" />
                Blocked Words
              </CardTitle>
              <CardDescription>
                Words that trigger AI output flagging
              </CardDescription>
            </CardHeader>
            <CardContent>
              <div className="mb-4 flex gap-2">
                <Input
                  value={newBlockedWord}
                  onChange={(e) => setNewBlockedWord(e.target.value)}
                  placeholder="Add blocked word..."
                  onKeyDown={(e) => e.key === 'Enter' && handleAddBlockedWord()}
                />
                <Button onClick={handleAddBlockedWord} size="icon" variant="destructive">
                  <Plus className="h-4 w-4" />
                </Button>
              </div>
              <div className="flex flex-wrap gap-2">
                {blockedWords.map((word) => (
                  <Badge
                    key={word}
                    variant="destructive"
                    className="gap-1"
                  >
                    {word}
                    <button
                      onClick={() => handleRemoveBlockedWord(word)}
                      className="ml-1 rounded-full p-0.5 hover:bg-destructive-foreground/20"
                    >
                      <X className="h-3 w-3" />
                    </button>
                  </Badge>
                ))}
              </div>
            </CardContent>
          </Card>
        </div>

        <Card className="mt-8">
          <CardHeader>
            <CardTitle>Preview</CardTitle>
            <CardDescription>
              How the disclaimer appears to users
            </CardDescription>
          </CardHeader>
          <CardContent>
            <div className="rounded-lg border border-primary/20 bg-primary/5 p-4">
              <div className="flex items-start gap-3">
                <Shield className="mt-0.5 h-5 w-5 shrink-0 text-primary" />
                <p className="text-sm text-muted-foreground">{disclaimer}</p>
              </div>
            </div>
          </CardContent>
        </Card>
      </div>
  );
}
