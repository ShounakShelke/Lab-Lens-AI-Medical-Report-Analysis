import { ReactNode } from 'react';
import { Navbar } from './Navbar';
import { AdminNavbar } from './AdminNavbar';
import { Footer } from './Footer';

interface LayoutProps {
  children: ReactNode;
  hideFooter?: boolean;
  admin?: boolean;
}

export function Layout({ children, hideFooter = false, admin = false }: LayoutProps) {
  return (
    <div className="flex min-h-screen flex-col">
      {admin ? <AdminNavbar /> : <Navbar />}
      <main className="flex-1">{children}</main>
      {!hideFooter && <Footer />}
    </div>
  );
}
