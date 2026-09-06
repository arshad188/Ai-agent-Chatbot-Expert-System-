import random
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

class RestaurantChatbot:
    def __init__(self):
        self.bot = ChatBot("RestaurantBot")
        trainer = ListTrainer(self.bot)
        
        # Training with conversational flow
        conv = [
            "Hi", "Hello! I can help you find a restaurant. What cuisine do you like?",
            "Italian", "Great! What's your budget? (low/medium/high)",
            "low", "I recommend Pizza Hut. Would you like directions?",
            "medium", "Try Olive Garden - they have great pasta!",
            "high", "Fancy Trattoria is perfect for special occasions.",
            "vegan", "Green Leaf Cafe has excellent plant-based options.",
            "gluten-free", "Pure Kitchen offers many GF dishes.",
            "weather", "Let me check... It's sunny today! Great for patios.",
            "parking", "Most places have parking. Do you need valet?",
            "bye", "Goodbye! Enjoy your meal!",
        ]
        trainer.train(conv)
    
    def chat(self):
        print("🍽️ Restaurant Chatbot - Ask me anything!")
        while True:
            user = input("You: ")
            if user.lower() in ["exit", "quit", "bye"]:
                print("Bot: Goodbye!")
                break
            print("Bot:", self.bot.get_response(user))

if __name__ == "__main__":
    bot = RestaurantChatbot()
    bot.chat()