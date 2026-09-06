# Instructor Teaching Guide

## 📅 Course Schedule (4 sessions)

### Session 1: Expert Systems (2 hours)
- **0-15 min**: Lecture - What are expert systems?
- **15-30 min**: Demo - Medical triage system
- **30-60 min**: Hands-on - Students build their own rule system
- **60-90 min**: Challenge - Add 5 new rules
- **90-120 min**: Discussion - Limitations and real-world applications

### Session 2: Chatbots (2 hours)
- **0-15 min**: Lecture - Rule-based vs. generative
- **15-30 min**: Demo - ELIZA-style chatbot
- **30-60 min**: Hands-on - Build FAQ bot
- **60-90 min**: Demo - Generative chatbot with Transformers
- **90-120 min**: Discussion - When to use which type

### Session 3: AI Agents (2 hours)
- **0-15 min**: Lecture - Perception-Planning-Action loop
- **15-30 min**: Demo - Simple goal-based agent
- **30-60 min**: Hands-on - Build research agent
- **60-90 min**: Demo - Tool-using agent with real APIs
- **90-120 min**: Discussion - Safety and limitations

### Session 4: Capstone (3 hours)
- **0-30 min**: Project introduction
- **30-120 min**: Build all three systems
- **120-150 min**: Testing and comparison
- **150-180 min**: Presentations and discussion

## 🎓 Grading Breakdown
- Quizzes: 20% (5 quizzes × 4%)
- Notebooks: 30% (10% each)
- Capstone: 40%
- Reflection Essay: 10%

## 🛠 Common Issues & Solutions
1. **Transformers not installing**: Use `pip install transformers torch --no-cache-dir`
2. **Port conflicts**: Change ports in docker-compose.yml
3. **API rate limits**: Add delays between requests
4. **Memory issues**: Reduce batch sizes in generative models

## 📖 Additional Resources
- Russell & Norvig - Artificial Intelligence: A Modern Approach
- Sutton & Barto - Reinforcement Learning
- LangChain Documentation
- OpenAI API Documentation