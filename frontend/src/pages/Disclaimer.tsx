import { Layout } from '@/components/layout/Layout';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { 
  Shield, 
  AlertTriangle, 
  CheckCircle, 
  XCircle, 
  Brain,
  Stethoscope,
  Lock,
  FileWarning
} from 'lucide-react';

const sections = [
  {
    icon: CheckCircle,
    title: 'What Lab-Lens Does',
    color: 'text-status-normal',
    bgColor: 'bg-status-normal/10',
    items: [
      'Extracts test values from uploaded lab report images and PDFs',
      'Compares values against standard reference ranges',
      'Provides plain-language explanations of what results may indicate',
      'Offers general lifestyle guidance for health maintenance',
      'Suggests relevant medical specialties for further consultation',
    ],
  },
  {
    icon: XCircle,
    title: 'What Lab-Lens Does NOT Do',
    color: 'text-status-alert',
    bgColor: 'bg-status-alert/10',
    items: [
      'Provide medical diagnoses or clinical assessments',
      'Recommend specific treatments or medications',
      'Replace the expertise of healthcare professionals',
      'Store or share your personal health information',
      'Make predictions about health outcomes',
    ],
  },
];

const aiLimitations = [
  {
    title: 'Context Limitations',
    description: 'AI cannot consider your complete medical history, current medications, symptoms, or other factors that doctors use for proper interpretation.',
  },
  {
    title: 'Reference Range Variations',
    description: 'Reference ranges can vary between laboratories and may need adjustment based on age, sex, ethnicity, and other individual factors.',
  },
  {
    title: 'Complex Interactions',
    description: 'Multiple test results may interact in complex ways that require professional medical judgment to properly understand.',
  },
  {
    title: 'Evolving Medical Knowledge',
    description: 'Medical understanding continuously evolves, and AI models may not always reflect the most current clinical guidelines.',
  },
];

export default function Disclaimer() {
  return (
    <Layout>
      <div className="container py-8 md:py-12">
        <div className="mx-auto mb-12 max-w-3xl text-center">
          <div className="mx-auto mb-4 flex h-16 w-16 items-center justify-center rounded-2xl bg-primary/10">
            <Shield className="h-8 w-8 text-primary" />
          </div>
          <h1 className="mb-4 text-3xl font-bold md:text-4xl">
            Understanding Lab-Lens
          </h1>
          <p className="text-lg text-muted-foreground">
            Our commitment to your health safety
          </p>
        </div>

        <Card className="mx-auto mb-12 max-w-3xl border-status-borderline/30 bg-status-borderline/5">
          <CardContent className="p-6">
            <div className="flex items-start gap-4">
              <div className="flex h-12 w-12 shrink-0 items-center justify-center rounded-xl bg-status-borderline/20">
                <AlertTriangle className="h-6 w-6 text-status-borderline" />
              </div>
              <div>
                <h2 className="text-lg font-semibold">Medical Disclaimer</h2>
                <p className="mt-2 text-muted-foreground">
                  Lab-Lens is an educational tool designed to help you better understand your lab 
                  results. It is <strong className="text-foreground">not a substitute for professional 
                  medical advice, diagnosis, or treatment</strong>. Always seek the advice of your 
                  physician or other qualified health provider with any questions you may have 
                  regarding a medical condition.
                </p>
              </div>
            </div>
          </CardContent>
        </Card>

        <div className="mb-12 grid gap-8 md:grid-cols-2">
          {sections.map((section) => (
            <Card key={section.title}>
              <CardHeader>
                <CardTitle className="flex items-center gap-3">
                  <div className={`flex h-10 w-10 items-center justify-center rounded-lg ${section.bgColor}`}>
                    <section.icon className={`h-5 w-5 ${section.color}`} />
                  </div>
                  {section.title}
                </CardTitle>
              </CardHeader>
              <CardContent>
                <ul className="space-y-3">
                  {section.items.map((item, index) => (
                    <li key={index} className="flex items-start gap-2 text-sm">
                      <div className={`mt-1.5 h-1.5 w-1.5 shrink-0 rounded-full ${section.color.replace('text-', 'bg-')}`} />
                      <span className="text-muted-foreground">{item}</span>
                    </li>
                  ))}
                </ul>
              </CardContent>
            </Card>
          ))}
        </div>

        <Card className="mx-auto mb-12 max-w-3xl">
          <CardHeader>
            <CardTitle className="flex items-center gap-3">
              <div className="flex h-10 w-10 items-center justify-center rounded-lg bg-primary/10">
                <Stethoscope className="h-5 w-5 text-primary" />
              </div>
              Why Doctor Consultation Matters
            </CardTitle>
          </CardHeader>
          <CardContent className="prose prose-sm max-w-none text-muted-foreground">
            <p>
              While Lab-Lens can help you understand what your test values mean in general terms, 
              a healthcare professional considers many factors that our AI cannot:
            </p>
            <ul className="mt-4 space-y-2">
              <li>Your complete medical history and family background</li>
              <li>Current symptoms and how you're feeling</li>
              <li>Medications and supplements you're taking</li>
              <li>Previous test results and trends over time</li>
              <li>Physical examination findings</li>
              <li>Your individual health goals and concerns</li>
            </ul>
            <p className="mt-4">
              These factors are essential for accurate interpretation and appropriate medical guidance. 
              Lab results are just one piece of the health puzzle.
            </p>
          </CardContent>
        </Card>

        <div className="mx-auto max-w-3xl">
          <div className="mb-6 flex items-center gap-3">
            <div className="flex h-10 w-10 items-center justify-center rounded-lg bg-secondary">
              <Brain className="h-5 w-5 text-muted-foreground" />
            </div>
            <h2 className="text-xl font-semibold">AI Limitations</h2>
          </div>
          
          <div className="grid gap-4 sm:grid-cols-2">
            {aiLimitations.map((limitation) => (
              <Card key={limitation.title}>
                <CardContent className="p-4">
                  <h3 className="font-medium">{limitation.title}</h3>
                  <p className="mt-2 text-sm text-muted-foreground">
                    {limitation.description}
                  </p>
                </CardContent>
              </Card>
            ))}
          </div>
        </div>

        <Card className="mx-auto mt-12 max-w-3xl">
          <CardHeader>
            <CardTitle className="flex items-center gap-3">
              <div className="flex h-10 w-10 items-center justify-center rounded-lg bg-primary/10">
                <Lock className="h-5 w-5 text-primary" />
              </div>
              Your Privacy & Security
            </CardTitle>
          </CardHeader>
          <CardContent className="space-y-4 text-sm text-muted-foreground">
            <p>
              We take your privacy seriously. When you upload a lab report:
            </p>
            <ul className="space-y-2">
              <li className="flex items-start gap-2">
                <CheckCircle className="mt-0.5 h-4 w-4 shrink-0 text-status-normal" />
                Your report is processed in a temporary, secure environment
              </li>
              <li className="flex items-start gap-2">
                <CheckCircle className="mt-0.5 h-4 w-4 shrink-0 text-status-normal" />
                Original files are deleted immediately after analysis
              </li>
              <li className="flex items-start gap-2">
                <CheckCircle className="mt-0.5 h-4 w-4 shrink-0 text-status-normal" />
                All data transmission is encrypted using industry standards
              </li>
              <li className="flex items-start gap-2">
                <CheckCircle className="mt-0.5 h-4 w-4 shrink-0 text-status-normal" />
                We do not sell or share your health information
              </li>
            </ul>
          </CardContent>
        </Card>

        <div className="mx-auto mt-12 max-w-3xl rounded-xl border border-status-alert/30 bg-status-alert/5 p-6">
          <div className="flex items-start gap-4">
            <FileWarning className="h-6 w-6 shrink-0 text-status-alert" />
            <div>
              <h3 className="font-semibold text-status-alert">Emergency Notice</h3>
              <p className="mt-2 text-sm text-muted-foreground">
                If you are experiencing a medical emergency, please call emergency services 
                immediately or go to your nearest emergency room. Do not rely on this tool 
                for urgent health matters.
              </p>
            </div>
          </div>
        </div>
      </div>
    </Layout>
  );
}
