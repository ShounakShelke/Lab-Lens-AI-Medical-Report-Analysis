import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import {
  Activity,
  Mail,
  Lock,
  ArrowRight,
  Eye,
  EyeOff,
  Shield,
  User,
  CheckCircle2,
} from "lucide-react";
import { useAuth } from "@/hooks/useAuth";
import { toast } from "sonner";

export default function Login() {
  const [loginType, setLoginType] = useState<"user" | "admin">("user");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [showPassword, setShowPassword] = useState(false);
  const [isLoading, setIsLoading] = useState(false);

  const navigate = useNavigate();
  const { login } = useAuth();

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setIsLoading(true);

    try {
      const credential =
        loginType === "admin" ? "demo-token-admin" : "demo-token-user";

      const result = await login(credential);

      if (result.success) {
        toast.success("Login successful");

        setTimeout(() => {
          if (loginType === "admin") {
            
            navigate("/admin/login");
          } else {
            navigate("/upload");
          }
        }, 300);
      } else {
        toast.error("Login failed");
      }
    } catch (err) {
      toast.error("Unexpected error");
    } finally {
      setIsLoading(false);
    }
  };

  const fillDemo = (type: "user" | "admin") => {
    setLoginType(type);
    setEmail(type === "admin" ? "admin@lablens.demo" : "user@lablens.demo");
    setPassword(type === "admin" ? "admin123" : "user123");
    toast.info(`${type === "admin" ? "Admin" : "User"} demo filled`);
  };

  return (
    <div className="min-h-screen flex bg-background">
      {}
      <div className="hidden lg:flex lg:w-1/2 bg-gradient-to-br from-blue-900 via-slate-900 to-black text-white">
        <div className="m-auto text-center max-w-md">
          <div className="mx-auto mb-6 w-20 h-20 rounded-2xl bg-white/10 flex items-center justify-center">
            <Activity className="w-10 h-10 text-blue-400" />
          </div>
          <h1 className="text-4xl font-bold mb-4">Lab-Lens</h1>
          <p className="text-blue-100/80 mb-10">
            AI-assisted medical report understanding with ethical safeguards
          </p>

          {[
            "Instant lab insights",
            "Safety-first AI",
            "No diagnosis or prescriptions",
          ].map((t) => (
            <div key={t} className="flex items-center gap-3 justify-center mb-3">
              <CheckCircle2 className="w-4 h-4 text-blue-400" />
              <span>{t}</span>
            </div>
          ))}
        </div>
      </div>

      {}
      <div className="flex-1 flex items-center justify-center p-8">
        <Card className="w-full max-w-md border-none shadow-none">
          <CardHeader>
            <CardTitle className="text-3xl">Sign In</CardTitle>
            <CardDescription>
              Demo login for hackathon showcase
            </CardDescription>
          </CardHeader>

          <CardContent>
            {}
            <div className="flex mb-6 bg-muted rounded-lg p-1">
              <Button
                type="button"
                variant="ghost"
                onClick={() => fillDemo("user")}
                className={`flex-1 ${
                  loginType === "user" && "bg-background shadow"
                }`}
              >
                <User className="w-4 h-4 mr-2" />
                User
              </Button>
              <Button
                type="button"
                variant="ghost"
                onClick={() => fillDemo("admin")}
                className={`flex-1 ${
                  loginType === "admin" && "bg-background shadow"
                }`}
              >
                <Shield className="w-4 h-4 mr-2" />
                Admin
              </Button>
            </div>

            <form onSubmit={handleSubmit} className="space-y-5">
              <div>
                <Label>Email</Label>
                <div className="relative">
                  <Mail className="absolute left-3 top-3 w-4 h-4 text-muted-foreground" />
                  <Input
                    className="pl-10"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                    required
                  />
                </div>
              </div>

              <div>
                <Label>Password</Label>
                <div className="relative">
                  <Lock className="absolute left-3 top-3 w-4 h-4 text-muted-foreground" />
                  <Input
                    className="pl-10 pr-10"
                    type={showPassword ? "text" : "password"}
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    required
                  />
                  <button
                    type="button"
                    onClick={() => setShowPassword(!showPassword)}
                    className="absolute right-3 top-3"
                  >
                    {showPassword ? (
                      <EyeOff className="w-4 h-4" />
                    ) : (
                      <Eye className="w-4 h-4" />
                    )}
                  </button>
                </div>
              </div>

              <Button className="w-full" disabled={isLoading}>
                {isLoading ? "Signing in..." : "Sign In"}
                <ArrowRight className="ml-2 w-4 h-4" />
              </Button>
            </form>

            <div className="mt-6 text-xs text-muted-foreground flex justify-center gap-2">
              <Shield className="w-3 h-3" />
              Demo mode • No real authentication
            </div>
          </CardContent>
        </Card>
      </div>
    </div>
  );
}
