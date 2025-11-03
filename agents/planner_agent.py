from agents.base_agent import BaseAgent

class PlannerAgent(BaseAgent):
    def plan_task(self, user_input):
        if "schedule" in user_input.lower():
            return "Schedule a reminder or event."
        elif "summarize" in user_input.lower():
            return "Summarize the provided text or data."
        elif "weather" in user_input.lower():
            return "Fetch weather information."
        else:
            return "Engage in general conversation."
