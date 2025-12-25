import { Link, useNavigate } from 'react-router-dom';
import { Button } from '@/components/ui/button';
import { useAuth } from '@/hooks/useAuth';
import { 
  Shield, 
  LogOut, 
  Settings, 
  FileText,
  LayoutDashboard,
  MessageSquare,
  AlertTriangle
} from 'lucide-react';
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuSeparator,
  DropdownMenuTrigger,
} from '@/components/ui/dropdown-menu';
import { Avatar, AvatarFallback, AvatarImage } from '@/components/ui/avatar';

export function AdminNavbar() {
  const { user, logout } = useAuth();
  const navigate = useNavigate();

  const handleLogout = async () => {
    await logout();
    navigate('/login');
  };

  return (
    <header className="sticky top-0 z-50 w-full border-b border-border/40 bg-zinc-950/95 backdrop-blur supports-[backdrop-filter]:bg-zinc-950/60 text-white">
      <div className="container flex h-16 items-center justify-between">
        <Link to="/admin/dashboard" className="flex items-center gap-2 transition-opacity hover:opacity-80">
          <div className="flex h-9 w-9 items-center justify-center rounded-lg bg-red-600">
            <Shield className="h-5 w-5 text-white" />
          </div>
          <span className="text-xl font-semibold tracking-tight">Lab-Lens Admin</span>
        </Link>

        <nav className="hidden items-center gap-6 md:flex">
          <Link 
            to="/admin/dashboard" 
            className="text-sm font-medium text-zinc-400 transition-colors hover:text-white"
          >
            Dashboard
          </Link>
          <Link 
            to="/admin/prompts" 
            className="text-sm font-medium text-zinc-400 transition-colors hover:text-white"
          >
            Prompts
          </Link>
          <Link 
            to="/admin/rules" 
            className="text-sm font-medium text-zinc-400 transition-colors hover:text-white"
          >
            Rules
          </Link>
          <Link 
            to="/admin/feedback" 
            className="text-sm font-medium text-zinc-400 transition-colors hover:text-white"
          >
            Feedback
          </Link>
        </nav>

        <div className="flex items-center gap-3">
          <DropdownMenu>
            <DropdownMenuTrigger asChild>
              <Button variant="ghost" className="relative h-10 w-10 rounded-full hover:bg-zinc-800">
                <Avatar className="h-9 w-9 border border-zinc-700">
                  <AvatarImage src={user?.avatar} alt={user?.name} />
                  <AvatarFallback className="bg-red-600 text-white">
                    A
                  </AvatarFallback>
                </Avatar>
              </Button>
            </DropdownMenuTrigger>
            <DropdownMenuContent className="w-56" align="end" forceMount>
              <div className="flex items-center gap-2 p-2">
                <div className="flex flex-col space-y-1 leading-none">
                  <p className="font-medium">Administrator</p>
                  <p className="text-xs text-muted-foreground">{user?.email}</p>
                </div>
              </div>
              <DropdownMenuSeparator />
              <DropdownMenuItem asChild>
                <Link to="/" className="flex items-center gap-2">
                  <LogOut className="h-4 w-4" />
                  Exit Admin Mode
                </Link>
              </DropdownMenuItem>
              <DropdownMenuSeparator />
              <DropdownMenuItem 
                onClick={handleLogout}
                className="flex items-center gap-2 text-destructive focus:text-destructive"
              >
                <LogOut className="h-4 w-4" />
                Log out
              </DropdownMenuItem>
            </DropdownMenuContent>
          </DropdownMenu>
        </div>
      </div>
    </header>
  );
}
