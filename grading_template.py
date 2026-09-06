# instructor/grading_template.py
class ProjectGrader:
    def __init__(self):
        self.criteria = {
            "expert_system": {
                "rules_count": 15,
                "severity_levels": 3,
                "input_validation": True,
                "docstrings": True,
                "error_handling": True
            },
            "chatbot": {
                "training_data": True,
                "intents": 8,
                "fallback": True,
                "context_memory": True,
                "exit_condition": True
            },
            "agent": {
                "tools_count": 3,
                "planning_loop": True,
                "error_handling": True,
                "real_apis": 1,
                "save_function": True
            }
        }
    
    def grade_expert(self, code: str) -> int:
        score = 25
        # Check each criterion
        if "def diagnose" not in code:
            score -= 8
        if "severity" not in code:
            score -= 5
        if "validation" not in code:
            score -= 4
        # ... etc
        return max(0, score)