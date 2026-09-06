import requests
import json
import random

class RestaurantAgent:
    def __init__(self):
        self.tools = {
            "check_weather": self.get_weather,
            "find_nearby": self.search_places,
            "check_traffic": self.get_traffic,
            "suggest": self.suggest_restaurant
        }
    
    def get_weather(self, city="Islamabad"):
        """Simulated weather - would use OpenWeatherMap API"""
        weathers = ["sunny ☀️", "rainy 🌧️", "cloudy ☁️", "clear 🌤️"]
        return random.choice(weathers)
    
    def search_places(self, cuisine="any", radius="5km"):
        """Simulated - would use Google Places API"""
        places = {
            "Italian": ["Pizza Hut", "Olive Garden", "Trattoria Roma"],
            "Chinese": ["Panda Express", "Dragon Wok", "Beijing House"],
            "Pakistani": ["Kabul Restaurant", "Taste of Lahore", "BBQ Tonight"]
        }
        return random.choice(places.get(cuisine, ["Local Diner", "Cafe Metro"]))
    
    def get_traffic(self, destination):
        """Simulated traffic check"""
        statuses = ["light traffic 🚗", "moderate 🚗🚗", "heavy 🚗🚗🚗"]
        return random.choice(statuses)
    
    def suggest_restaurant(self, preferences):
        """Autonomous planner - decides which tools to use"""
        print("🤖 Agent thinking...")
        
        # Step 1: Check weather
        weather = self.tools["check_weather"]()
        print(f"   🌤️ Weather: {weather}")
        
        # Step 2: Find places based on cuisine
        cuisine = preferences.get("cuisine", "any")
        place = self.tools["find_nearby"](cuisine)
        print(f"   📍 Found: {place}")
        
        # Step 3: Check traffic
        traffic = self.tools["check_traffic"](place)
        print(f"   🚦 Traffic: {traffic}")
        
        # Step 4: Final recommendation with reasoning
        advice = f"Recommend {place} - "
        if "rainy" in weather:
            advice += "it's indoors and has covered parking. "
        else:
            advice += "great weather for dining out. "
        advice += f"Traffic is {traffic}, so allow extra time."
        
        return advice

# Test
agent = RestaurantAgent()
result = agent.suggest_restaurant({"cuisine": "Italian", "location": "downtown"})
print("\n✅ Final Recommendation:", result)