import { Link } from 'react-router-dom';
import { Layout } from '@/components/layout/Layout';
import { Button } from '@/components/ui/button';
import { 
  Activity, 
  Shield, 
  FileText, 
  Sparkles, 
  ArrowRight,
  CheckCircle,
  Clock,
  Lock
} from 'lucide-react';

const features = [
  {
    icon: FileText,
    title: 'Upload Any Lab Report',
    description: 'Support for PDF, JPG, and PNG formats. Your data stays private.',
  },
  {
    icon: Sparkles,
    title: 'AI-Powered Analysis',
    description: 'Get plain-language explanations using advanced AI technology.',
  },
  {
    icon: Shield,
    title: 'Safety First',
    description: 'Built with ethical safeguards. We never diagnose or prescribe.',
  },
];

const stats = [
  { label: 'Reports Analyzed', value: '10K+' },
  { label: 'Accuracy Rate', value: '99.2%' },
  { label: 'Avg. Processing', value: '<30s' },
];

export default function Landing() {
  return (
    <Layout>
      <section className="relative overflow-hidden">
        <div className="absolute inset-0 -z-10 gradient-subtle" />
        <div className="absolute -top-40 right-0 -z-10 h-96 w-96 rounded-full bg-primary/10 blur-3xl" />
        <div className="absolute -bottom-40 left-0 -z-10 h-96 w-96 rounded-full bg-accent/10 blur-3xl" />

        <div className="container py-20 md:py-32">
          <div className="mx-auto max-w-4xl text-center">
            <div className="mb-6 inline-flex items-center gap-2 rounded-full bg-primary/10 px-4 py-1.5 text-sm font-medium text-primary">
              <Sparkles className="h-4 w-4" />
              Powered by Google AI
            </div>

            <h1 className="mb-6 text-4xl font-bold tracking-tight md:text-5xl lg:text-6xl">
              Understand your lab reports.{' '}
              <span className="text-primary">Clearly. Responsibly.</span>
            </h1>

            <p className="mx-auto mb-8 max-w-2xl text-lg text-muted-foreground md:text-xl">
              Lab-Lens uses AI to translate complex medical lab results into clear, 
              easy-to-understand insights — without ever replacing your doctor.
            </p>

            <div className="flex flex-col items-center justify-center gap-4 sm:flex-row">
              <Button asChild variant="hero" size="xl">
                <Link to="/login">
                  Upload Lab Report
                  <ArrowRight className="ml-1 h-5 w-5" />
                </Link>
              </Button>
              <Button asChild variant="heroOutline" size="xl">
                <Link to="/login?demo=true">
                  Try Demo
                </Link>
              </Button>
            </div>

            <div className="mt-12 flex flex-wrap items-center justify-center gap-8 text-sm text-muted-foreground">
              <div className="flex items-center gap-2">
                <CheckCircle className="h-4 w-4 text-status-normal" />
                <span>No diagnosis claims</span>
              </div>
              <div className="flex items-center gap-2">
                <Lock className="h-4 w-4 text-primary" />
                <span>Encrypted & private</span>
              </div>
              <div className="flex items-center gap-2">
                <Clock className="h-4 w-4 text-accent" />
                <span>Results in seconds</span>
              </div>
            </div>
          </div>
        </div>
      </section>

      <section className="border-y border-border/40 bg-card/50">
        <div className="container py-12">
          <div className="grid grid-cols-1 gap-8 md:grid-cols-3">
            {stats.map((stat, index) => (
              <div 
                key={stat.label}
                className="text-center animate-fade-in"
                style={{ animationDelay: `${index * 100}ms` }}
              >
                <p className="text-4xl font-bold text-primary">{stat.value}</p>
                <p className="mt-1 text-muted-foreground">{stat.label}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      <section className="py-20 md:py-32">
        <div className="container">
          <div className="mx-auto mb-16 max-w-2xl text-center">
            <h2 className="mb-4 text-3xl font-bold md:text-4xl">
              How Lab-Lens Works
            </h2>
            <p className="text-lg text-muted-foreground">
              Simple, transparent, and designed with your safety in mind.
            </p>
          </div>

          <div className="grid gap-8 md:grid-cols-3">
            {features.map((feature, index) => (
              <div
                key={feature.title}
                className="group rounded-2xl border border-border bg-card p-8 transition-all duration-300 hover:border-primary/30 hover:shadow-large animate-slide-up"
                style={{ animationDelay: `${index * 100}ms` }}
              >
                <div className="mb-6 flex h-14 w-14 items-center justify-center rounded-xl bg-primary/10 transition-colors group-hover:bg-primary/20">
                  <feature.icon className="h-7 w-7 text-primary" />
                </div>
                <h3 className="mb-3 text-xl font-semibold">{feature.title}</h3>
                <p className="text-muted-foreground">{feature.description}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      <section className="py-20 md:py-32">
        <div className="container">
          <div className="mx-auto max-w-4xl rounded-3xl gradient-hero p-8 text-center text-primary-foreground md:p-16">
            <div className="mb-6 inline-flex h-16 w-16 items-center justify-center rounded-2xl bg-primary-foreground/20">
              <Activity className="h-8 w-8" />
            </div>
            <h2 className="mb-4 text-3xl font-bold md:text-4xl">
              Ready to understand your health?
            </h2>
            <p className="mx-auto mb-8 max-w-xl text-lg text-primary-foreground/90">
              Upload your lab report and get clear, responsible insights in seconds. 
              No account required to try.
            </p>
            <Button asChild size="xl" className="bg-primary-foreground text-primary hover:bg-primary-foreground/90">
              <Link to="/login">
                Get Started Free
                <ArrowRight className="ml-1 h-5 w-5" />
              </Link>
            </Button>
          </div>
        </div>
      </section>


    </Layout>
  );
}
