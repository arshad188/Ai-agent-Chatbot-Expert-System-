import streamlit as st
from expert_rules import RestaurantExpert
from chatbot_ui import RestaurantChatbot
from agent_tools import RestaurantAgent

st.title("🍽️ Restaurant Recommender - 3 Paradigms")

paradigm = st.selectbox("Choose AI Paradigm", ["Expert System", "Chatbot", "Agent"])

if paradigm == "Expert System":
    st.subheader("Rule-Based Expert")
    budget = st.selectbox("Budget", ["low", "medium", "high"])
    cuisine = st.selectbox("Cuisine", ["Italian", "Chinese", "Pakistani"])
    if st.button("Recommend"):
        expert = RestaurantExpert()
        result = expert.recommend({"budget": budget, "cuisine": cuisine})
        st.success(result)

elif paradigm == "Chatbot":
    st.subheader("Conversational Interface")
    user_input = st.text_input("Ask about restaurants:")
    if user_input:
        bot = RestaurantChatbot()
        response = bot.bot.get_response(user_input)
        st.write(f"🤖 {response}")

else:  # Agent
    st.subheader("Autonomous Goal-Driven Agent")
    goal = st.text_area("Describe what you want:", "Find an Italian place for dinner")
    if st.button("Run Agent"):
        agent = RestaurantAgent()
        with st.spinner("Agent thinking..."):
            result = agent.suggest_restaurant({"cuisine": "Italian"})
        st.success(result)