import { useState, useRef, useEffect } from "react";
import { Link, useLocation } from "react-router-dom";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { ScrollArea } from "@/components/ui/scroll-area";
import { Badge } from "@/components/ui/badge";
import {
  Activity,
  Send,
  MessageSquare,
  ChevronLeft,
  ChevronRight,
  User,
  Bot,
  Stethoscope,
  FileText
} from "lucide-react";
import { useAuth } from "@/hooks/useAuth";
import { chatAPI } from "@/services/api";
import { toast } from "sonner";
import { Layout } from "@/components/layout/Layout";

interface Message {
    id: string;
    type: 'user' | 'assistant';
    content: string;
    timestamp: Date;
}

const LabChat = () => {
  const { state } = useLocation();
  const [sidebarCollapsed, setSidebarCollapsed] = useState(false);
  const [message, setMessage] = useState("");
  const [isTyping, setIsTyping] = useState(false);
  const [messages, setMessages] = useState<Message[]>([]);
  const messagesEndRef = useRef<HTMLDivElement>(null);
  
  const { user } = useAuth();
  
  const reportId = state?.reportId;
  const analysis = state?.analysis;

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  useEffect(() => {
    if (analysis) {
        setMessages([{
            id: 'init',
            type: 'assistant',
            content: `I've analyzed your report. You can ask me about your ${analysis.riskSummary?.overallRisk || ''} risk factors or specific test results.`,
            timestamp: new Date()
        }]);
    }
  }, [analysis]);

  const handleSendMessage = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!message.trim()) return;

    const userMsg: Message = {
        id: Date.now().toString(),
        type: 'user',
        content: message,
        timestamp: new Date()
    };
    
    setMessages(prev => [...prev, userMsg]);
    setMessage("");
    setIsTyping(true);

    try {
      const response = await chatAPI.sendMessage(userMsg.content, reportId);
      
      const botMsg: Message = {
          id: (Date.now() + 1).toString(),
          type: 'assistant',
          content: response.data.reply,
          timestamp: new Date()
      };
      setMessages(prev => [...prev, botMsg]);
    } catch (error) {
      console.error("Chat Error:", error);
      toast.error("Failed to get response");
      setMessages(prev => [...prev, {
          id: Date.now().toString(),
          type: 'assistant',
          content: "I'm having trouble connecting to the medical database right now.",
          timestamp: new Date()
      }]);
    } finally {
        setIsTyping(false);
    }
  };

  return (
    <Layout>
      <div className="flex h-[calc(100vh-4rem)] border-t bg-background">
        <aside 
          className={`bg-slate-50 border-r border-border transition-all duration-300 relative ${
            sidebarCollapsed ? 'w-16' : 'w-72'
          }`}
        >
          <button
            onClick={() => setSidebarCollapsed(!sidebarCollapsed)}
            className="absolute -right-3 top-6 w-6 h-6 rounded-full bg-primary text-primary-foreground flex items-center justify-center shadow-md hover:bg-primary/90 z-10"
          >
            {sidebarCollapsed ? <ChevronRight className="w-3 h-3" /> : <ChevronLeft className="w-3 h-3" />}
          </button>

          <div className="p-4 h-full flex flex-col">
             {!sidebarCollapsed && (
                 <div className="mb-6">
                     <h2 className="font-semibold text-lg flex items-center gap-2">
                         <Activity className="h-5 w-5 text-primary" />
                         Active Session
                     </h2>
                     <p className="text-xs text-muted-foreground mt-1">
                         Report ID: {reportId ? reportId.slice(0, 8) : 'None'}
                     </p>
                 </div>
             )}

             <div className="flex-1">
                 {!sidebarCollapsed && (
                     <div className="rounded-lg bg-white p-3 border shadow-sm mb-4">
                         <div className="flex items-center gap-2 mb-2">
                             <FileText className="h-4 w-4 text-primary" />
                             <span className="font-medium text-sm">Report Summary</span>
                         </div>
                         <div className="space-y-2">
                             {analysis?.riskSummary?.overallRisk && (
                                 <Badge variant={analysis.riskSummary.overallRisk === 'High' ? 'destructive' : 'outline'}>
                                     {analysis.riskSummary.overallRisk} Risk
                                 </Badge>
                             )}
                             <p className="text-xs text-muted-foreground line-clamp-3">
                                 {analysis?.summary || "No active report context."}
                             </p>
                         </div>
                     </div>
                 )}
             </div>

             <div className="mt-auto">
                 <Button variant="ghost" className="w-full justify-start gap-2" asChild>
                     <Link to="/history">
                        <ChevronLeft className="h-4 w-4" />
                        {!sidebarCollapsed && "Back to History"}
                     </Link>
                 </Button>
             </div>
          </div>
        </aside>

        <main className="flex-1 flex flex-col bg-background">
          <header className="h-16 border-b flex items-center justify-between px-6 bg-white/50 backdrop-blur">
            <div className="flex items-center gap-3">
              <div className="h-8 w-8 rounded-full bg-primary/10 flex items-center justify-center">
                  <Stethoscope className="h-4 w-4 text-primary" />
              </div>
              <h1 className="font-semibold">Medical Assistant AI</h1>
            </div>
            {analysis && (
                <Badge variant="outline" className="text-xs hidden md:flex">
                    Context Active: {analysis.tests?.length || 0} biomarkers
                </Badge>
            )}
          </header>

          <ScrollArea className="flex-1 p-6">
            <div className="max-w-3xl mx-auto space-y-6">
              {messages.map((msg) => (
                <div key={msg.id} className={`flex gap-4 ${msg.type === 'user' ? 'justify-end' : ''} animate-in fade-in slide-in-from-bottom-2`}>
                  {msg.type !== 'user' && (
                    <div className="w-8 h-8 rounded-full bg-primary flex items-center justify-center shrink-0">
                      <Bot className="w-4 h-4 text-primary-foreground" />
                    </div>
                  )}
                  
                  <div className={`max-w-[80%] rounded-2xl p-4 ${
                    msg.type === 'user' 
                      ? 'bg-primary text-primary-foreground rounded-tr-none' 
                      : 'bg-muted rounded-tl-none'
                  }`}>
                    <p className="text-sm leading-relaxed whitespace-pre-wrap">{msg.content}</p>
                  </div>

                  {msg.type === 'user' && (
                    <div className="w-8 h-8 rounded-full bg-muted flex items-center justify-center shrink-0">
                      <User className="w-4 h-4 text-muted-foreground" />
                    </div>
                  )}
                </div>
              ))}

              {isTyping && (
                <div className="flex gap-4">
                  <div className="w-8 h-8 rounded-full bg-primary flex items-center justify-center">
                    <Bot className="w-4 h-4 text-primary-foreground" />
                  </div>
                  <div className="bg-muted rounded-2xl p-4 rounded-tl-none">
                    <div className="flex gap-1 h-5 items-center">
                      <span className="w-2 h-2 bg-primary/40 rounded-full animate-bounce" style={{ animationDelay: '0ms' }} />
                      <span className="w-2 h-2 bg-primary/40 rounded-full animate-bounce" style={{ animationDelay: '150ms' }} />
                      <span className="w-2 h-2 bg-primary/40 rounded-full animate-bounce" style={{ animationDelay: '300ms' }} />
                    </div>
                  </div>
                </div>
              )}
              <div ref={messagesEndRef} />
            </div>
          </ScrollArea>

          <div className="p-4 border-t bg-background">
            <form onSubmit={handleSendMessage} className="max-w-3xl mx-auto flex gap-3">
              <Input
                value={message}
                onChange={(e) => setMessage(e.target.value)}
                placeholder="Ask about your results, diet recommendations, or next steps..."
                className="flex-1"
                disabled={isTyping}
              />
              <Button type="submit" disabled={!message.trim() || isTyping}>
                <Send className="w-4 h-4" />
              </Button>
            </form>
            <p className="text-xs text-center text-muted-foreground mt-2">
                AI can make mistakes. Please consult a doctor for medical advice.
            </p>
          </div>
        </main>
      </div>
    </Layout>
  );
};

export default LabChat;
