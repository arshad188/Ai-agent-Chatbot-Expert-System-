# AI Fundamentals: From Rules to Autonomy
## Complete Course Material

**Version**: 1.0
**Date**: January 2026
**Author**: [Your Name]
**Duration**: 10-12 hours (instructor-led)

---

## Table of Contents
1. Introduction to AI Paradigms
2. Session 1: Expert Systems
3. Session 2: Chatbots
4. Session 3: AI Agents
5. Session 4: Capstone Project
6. Quizzes & Answer Keys
7. Grading Rubric
8. Additional Resources

---

## How to Use This PDF
- **Instructors**: Use as lecture notes + grading guide
- **Students**: Use as study guide + reference
- **Self-study**: Follow sequentially, complete all exercises

---

## Session 1: Expert Systems (2 hours)

### Lecture Notes
**Key Concept**: Expert systems emulate human decision-making using rule-based logic.

**Slides 1-5 Summary**:
- MYCIN (1976): First expert system for bacterial infections
- Knowledge Base + Inference Engine = Core architecture
- Forward chaining (data-driven) vs. Backward chaining (goal-driven)
- Strengths: Explainable, transparent, auditable
- Weaknesses: Brittle, no learning, manual updates

**Code Demo** (Page 3-4):
*See complete medical_triage.py implementation*

**Student Exercise**:
1. Add 5 new rules for cold, allergies, food poisoning
2. Implement severity levels (mild/moderate/severe)
3. Add input validation

**Discussion Questions**:
1. Why haven't expert systems replaced doctors?
2. How would you handle conflicting rules?
3. What industries still use expert systems today?

---

## Session 2: Chatbots (2 hours)

### Lecture Notes
**Key Concept**: Chatbots enable natural language interaction but don't act independently.

**Types**:
1. **Rule-based**: Pattern matching (ELIZA, 1966)
2. **Retrieval-based**: Picks from pre-defined responses
3. **Generative**: Uses neural networks (ChatGPT, 2022)

**Core Components**:
- Intent Recognition
- Entity Extraction
- Context Management
- Response Generation

**Code Demo** (Page 8-9):
*Complete chatbot implementations (rule-based + generative)*

**Student Exercise**:
1. Build a restaurant FAQ chatbot with 8 intents
2. Implement fallback responses
3. Add context memory

**Discussion Questions**:
1. When would you choose rule-based over generative?
2. How do you prevent hallucination?
3. What are the privacy implications of generative chatbots?

---

## Session 3: AI Agents (2 hours)

### Lecture Notes
**Key Concept**: Agents achieve goals autonomously using perception, planning, and action.

**The Agent Loop**:
1. **Perceive**: Understand environment and goal
2. **Plan**: Break goal into subtasks
3. **Act**: Execute using tools (APIs, search, code)
4. **Learn**: Adapt from feedback (RL)

**Tools an Agent Might Use**:
- Web Search (Google, Bing)
- APIs (Weather, Calendar, Email)
- Code Execution (Python, SQL)
- File I/O (Read/Write data)

**Code Demo** (Page 14-16):
*Complete research agent with real APIs*

**Student Exercise**:
1. Build an agent with 3+ tools
2. Implement dynamic planning
3. Add error handling and retries

**Discussion Questions**:
1. How do you prevent agents from taking harmful actions?
2. What are the ethical implications of autonomous agents?
3. Will agents replace human workers?

---

## Session 4: Capstone Project (3 hours)

**Project**: Restaurant Recommender System

**Requirements**:
- Implement all three paradigms
- Same problem, different approaches
- Compare and contrast results

**Deliverables**:
1. Expert System: 15+ rules (cuisine, budget, weather, traffic)
2. Chatbot: 8+ intents with graceful fallback
3. Agent: 3+ tools with planning loop
4. Comparison Report (500 words)

**Evaluation Criteria** (Page 20):
- Code Quality: 25%
- Functionality: 40%
- Comparison: 20%
- Documentation: 15%

---

## Quizzes & Answer Keys

### Quiz 1: Expert Systems
*10 questions, 15 minutes*

**Q1**. What are the two main components of an expert system?
**A**: Knowledge base + Inference engine.

**Q2**. True/False: Expert systems can learn from new data automatically.
**A**: False.

... (Full quiz on pages 25-28)

### Quiz 2: Chatbots
*10 questions, 15 minutes*

... (Full quiz on pages 29-32)

### Quiz 3: AI Agents
*10 questions, 15 minutes*

... (Full quiz on pages 33-36)

### Quiz 4: Comparison
*10 questions, 20 minutes*

... (Full quiz on pages 37-40)

### Quiz 5: Advanced (Bonus)
*7 questions, 20 minutes*

... (Full quiz on pages 41-43)

---

## Grading Rubric

| Project Component | Excellent (90-100%) | Proficient (70-89%) | Developing (50-69%) | Needs Work (<50%) |
|-------------------|---------------------|---------------------|---------------------|-------------------|
| Expert System (25%) | 15+ rules, validation, severity | 10-14 rules, some validation | 5-9 rules, no validation | <5 rules or broken |
| Chatbot (25%) | 8+ intents, fallback, memory | 5-7 intents, fallback | 3-4 intents, no fallback | <3 intents or broken |
| Agent (25%) | 3+ real tools, planning, error handling | 2 tools, some planning | 1 tool, hardcoded | No tools or broken |
| Comparison (15%) | Insightful analysis with examples | Good comparison, shallow examples | Lists differences only | Missing or irrelevant |
| Code Quality (10%) | Well-commented, modular, PEP8 | Mostly readable | Hard to follow | Unreadable |

---

## Additional Resources

### Books
- Russell & Norvig - "Artificial Intelligence: A Modern Approach"
- Sutton & Barto - "Reinforcement Learning"
- Goodfellow et al. - "Deep Learning"

### Online Courses
- Coursera: AI for Everyone (Andrew Ng)
- Fast.ai: Practical Deep Learning
- Stanford CS224N: NLP with Deep Learning

### Tools & Libraries
- LangChain: Framework for building agents
- Rasa: Open-source chatbot framework
- Streamlit: Quick UI for AI applications
- Hugging Face Transformers: State-of-the-art NLP

---

## Appendix: Code Snippets (Pages 45-120)
*Full implementations of all three paradigms*

---

## Appendix: Docker Setup (Pages 121-125)
*Complete Dockerfile and docker-compose.yml*

---

## Appendix: Troubleshooting Guide (Pages 126-130)
*Common errors and solutions*

---

*End of Course Material*