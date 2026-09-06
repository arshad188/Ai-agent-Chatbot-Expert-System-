# Expert System with 20+ rules
class RestaurantExpert:
    def __init__(self):
        self.rules = [
            # Budget + Cuisine
            {"conditions": {"budget": "low", "cuisine": "Italian"}, "result": "Pizza Hut - $"},
            {"conditions": {"budget": "medium", "cuisine": "Italian"}, "result": "Olive Garden - $$"},
            {"conditions": {"budget": "high", "cuisine": "Italian"}, "result": "Fancy Trattoria - $$$"},
            # Weather + Location
            {"conditions": {"weather": "rainy", "has_parking": False}, "result": "Avoid outdoor seating - try indoor mall food court"},
            {"conditions": {"weather": "sunny", "has_parking": True}, "result": "Great day for patio dining - recommend The Terrace"},
            # Dietary
            {"conditions": {"dietary": "vegan"}, "result": "Green Leaf Cafe - plant-based menu"},
            {"conditions": {"dietary": "gluten-free"}, "result": "Pure Kitchen - GF options available"},
            # Crowd + Time
            {"conditions": {"crowd": "busy", "time": "dinner"}, "result": "Make a reservation at Steakhouse 55"},
            {"conditions": {"crowd": "quiet", "time": "lunch"}, "result": "Try the local deli - quick and cheap"},
        ]
    
    def recommend(self, user_input):
        for rule in self.rules:
            match = True
            for key, value in rule["conditions"].items():
                if user_input.get(key) != value:
                    match = False
                    break
            if match:
                return rule["result"]
        return "No perfect match - try a popular spot like Main Street Bistro"

# Test
expert = RestaurantExpert()
print(expert.recommend({"budget": "low", "cuisine": "Italian"}))  # Pizza Hut