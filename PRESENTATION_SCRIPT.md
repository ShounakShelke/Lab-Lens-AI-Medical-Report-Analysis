# Lab-Lens: Presentation Script

**Time Limit:** ~3-5 Minutes
**Speaker:** [Your Name]

---

### [0:00 - 0:45] Introduction & Hook
"Good [Morning/Afternoon] Judges.

We've all been there—or know someone who has. You get a blood test result back, and it's 5 pages of numbers, acronyms, and bold text. You frantically Google 'High Eosinophils' and convince yourself you have a rare tropical disease, only to find out later it was just a seasonal allergy.

This gap—between **Medical Data** and **Patient Understanding**—is where anxiety lives.

I am proud to present **Lab-Lens**: An intelligent companion that translates your lab reports into clear, actionable, and safe insights."

---

### [0:45 - 1:30] The Solution (Live Demo Start)
*(Switch screen to Lab-Lens Landing Page)*

"Lab-Lens is a secure web platforms built with React and powered by Google Gemini. Let me show you how it works.

We start by logging in securely with Google.
*(Click 'Continue with Google' or use Demo Login)*

Here on the dashboard, I can upload a standard photo of a lipid profile.
*(Upload 'report_high_risk.png')*

While this processes, let me explain what's happening under the hood. We aren't just sending the image to ChatGPT and hoping for the best. That would be dangerous.

We use a **Hybrid Pipeline**. 
1. First, we use computer vision to extract text.
2. Then, we use Generative AI to *structure* that data.
3. But crucially, we pass that structured data through a **Deterministic Medical Rule Engine**. We verify risky values like Cholesterol against hard-coded medical standards. This guarantees that if a value is 'Critical', the AI *cannot* hallucinate and call it 'Normal'."

---

### [1:30 - 2:30] Results Walkthrough (The "Wow" Moment)
*(Screen shows Results Page)*

"And here is the result.

Notice the difference? No confused clutter.
- At the top, a **Clinical Severity Banner** tells me exactly where I stand: 'High Cardiovascular Risk'.
- Below, my results are converted into clear **Status Badges**.
- I get a plain-English summary, and specific **Lifestyle Tips**—like reducing saturated fats—customized to *these* specific numbers.

But questions rarely stop at the report. 
*(Click 'Ask Assistant')*

I can chat with Lab-Lens. 'What should I eat for breakfast given these results?'
The bot has the context of my report and answers instantly. It's like having a knowledgeable friend explain the doctor's notes."

---

### [2:30 - 3:00] Admin & Safety
*(Briefly mention or show Admin Dashboard if time permits)*

"We also built an **Admin Layer** for 'Human-in-the-Loop' verification. Doctors can review the AI's generated summaries to ensure safety and improve the model over time.

We prioritize safety: disclaimers are everywhere, and we explicitly block diagnosis attempts."

---

### [3:00 - End] Conclusion
"Lab-Lens is strictly an educational tool, not a doctor replacement. But it empowers patients to walk into their next appointment informed, calm, and ready to ask the right questions.

Thank you. We are Team Cortex LMH, and we are ready for your questions."
