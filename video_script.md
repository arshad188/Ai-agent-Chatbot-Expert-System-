# Video Script: "3 AI Paradigms in 10 Minutes"

**Tone**: Energetic, accessible, with visual demonstrations
**Audience**: Beginners to intermediate AI learners
**Format**: Talking head + screen recordings

---

### [0:00-0:30] Intro
**[VISUAL]** Title card: "AI Paradigms: Expert Systems vs Chatbots vs Agents"

**SPEAKER (on camera):**
"Hey everyone! Today we're going to demystify three fundamental AI paradigms. Think of them as different ways AI can think and act - from rigid rule-followers to autonomous problem-solvers. Let's dive in!"

---

### [0:30-2:30] Expert Systems
**[VISUAL]** Split screen: Speaker + screen showing code from medical_triage.py

**SPEAKER:**
"First up: Expert Systems. These are the OGs of AI - they've been around since the 1970s. The idea is simple: encode human expertise as IF-THEN rules."

**[VISUAL]** Shows rule diagram: IF fever AND cough THEN possible flu

**SPEAKER:**
"Let me show you a quick demo. Here's a medical triage system. Notice how it asks for symptoms one by one, then applies rules to give a diagnosis. It's transparent - you can see exactly why it made its decision."

**[SCREEN RECORDING]** Run the medical triage script

**SPEAKER:**
"But the downside? It's brittle. Add a new symptom? You need to write a new rule. No learning, no adaptation. It's like a cookbook - great for known recipes, useless for new dishes."

---

### [2:30-4:30] Chatbots
**[VISUAL]** Split screen: Speaker + screen showing chatbot demo

**SPEAKER:**
"Now let's talk Chatbots. Instead of rigid rules, they focus on conversation. There are two types:"

**[VISUAL]** Animation showing rule-based vs generative

**SPEAKER:**
"Rule-based chatbots use pattern matching - like ELIZA from the 1960s. They're predictable but limited. Then we have generative chatbots like ChatGPT - they use neural networks to create original responses."

**[SCREEN RECORDING]** Run rule-based and generative chatbots side by side

**SPEAKER:**
"See the difference? The generative bot sounds more natural, but it can hallucinate - make things up. The rule-based bot is safer but boring. Trade-offs everywhere!"

**[VISUAL]** Shows intent/entity diagram

**SPEAKER:**
"Key concepts for chatbots: Intent - what does the user want? And Entities - specific details like dates or locations. Get these right, and your bot can understand complex requests."

---

### [4:30-7:00] AI Agents
**[VISUAL]** Speaker + screen showing agent planning animation

**SPEAKER:**
"Finally, the most exciting paradigm: AI Agents. These aren't just responders - they're DOERS. They perceive their environment, plan actions, and execute them autonomously."

**[VISUAL]** Perception-Planning-Action loop animation

**SPEAKER:**
"Here's the key difference: A chatbot answers questions. An agent ACHIEVES GOALS. Let me show you."

**[SCREEN RECORDING]** Run research_agent.py - show it searching papers, summarizing, and saving

**SPEAKER:**
"Watch this: I give it one goal - 'Find recent papers on AI bias.' It breaks that down, searches academic databases, summarizes findings, and saves them - all without my step-by-step guidance."

**[VISUAL]** Shows tools the agent uses

**SPEAKER:**
"Agents use tools - web search, APIs, calculators. They're like digital workers. But they can also go wrong - infinite loops, high costs, unpredictability. They need guardrails."

---

### [7:00-8:30] Comparison
**[VISUAL]** Comparison table graphic

**SPEAKER:**
"Let's put them side by side:"

**TEXT OVERLAY:**
- **Expert System**: Rule-based, explainable, no learning
- **Chatbot**: Conversational, natural UI, can hallucinate
- **AI Agent**: Goal-driven, autonomous, can use tools

**SPEAKER:**
"When to use which? Medical diagnosis? Expert System - you need clarity. Customer service? Chatbot - friendly interface. Research automation? Agent - gets the job done."

**[VISUAL]** Hybrid system diagram

**SPEAKER:**
"But the future is hybrid. Imagine: An agent with a chatbot interface, supervised by an expert system for safety. That's where we're heading - combining the best of all worlds."

---

### [8:30-9:30] Capstone Demo
**[VISUAL]** Show Streamlit restaurant app

**SPEAKER:**
"In our course, you'll build all three systems for a restaurant recommender. Here's the final Streamlit app - see how you can switch between paradigms for the SAME problem?"

**[SCREEN RECORDING]** Flicking through Expert, Chatbot, Agent tabs

**SPEAKER:**
"Same input - 'Italian food, low budget.' Expert gives a rule-based answer. Chatbot has a conversation. Agent checks weather and traffic first. Which one would YOU trust?"

---

### [9:30-10:00] Outro
**SPEAKER (on camera):**
"So there you have it - from rigid rules to autonomous action. The evolution of AI is moving toward more flexible, capable systems. But remember: each paradigm has its place.

**[VISUAL]** Course info slide

**SPEAKER:**
"Ready to build these yourself? Check out our GitHub repo - link below. You'll get Jupyter notebooks, quizzes, and a full capstone project. Hit subscribe, and happy coding!"

**[VISUAL]** End card with links, social media

**SPEAKER:**
"Next video: How to build an AI agent from scratch with LangChain. See you there!"