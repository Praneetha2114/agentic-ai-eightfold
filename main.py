# main.py
"""
Agentic AI – Eightfold Project
Author: [Your Full Name]
Roll No: [Your Roll Number]
CMR Institute of Technology, Hyderabad
Batch: 2026
"""

import requests
import json
import time

class Agent:
    def __init__(self, name, role):
        self.name = name
        self.role = role
        self.memory = []

    def think(self, task):
        """Generate a reasoning trace for the task."""
        thought = f"[{self.name} Thinking] -> Task received: '{task}'"
        self.memory.append(thought)
        print(thought)
        time.sleep(0.5)
        return f"{self.name} decided to: {self.plan(task)}"

    def plan(self, task):
        """Basic reasoning / planning logic."""
        if "news" in task.lower():
            return "fetch latest tech headlines"
        elif "weather" in task.lower():
            return "get current weather info"
        else:
            return "respond conversationally"

    def act(self, plan):
        """Perform a simple simulated action or API call."""
        print(f"[{self.name} Acting] Executing plan: {plan}")
        if "weather" in plan:
            # Example API call (replace with your own key if needed)
            try:
                city = "Hyderabad"
                url = f"https://wttr.in/{city}?format=3"
                response = requests.get(url)
                return f"Weather in {city}: {response.text.strip()}"
            except Exception as e:
                return f"API error: {e}"
        elif "news" in plan:
            return "Today's trending tech: AI agents revolutionize automation!"
        else:
            return "Hello! I’m your Agentic AI assistant. How can I help?"

    def run(self, task):
        """Full reasoning + action cycle."""
        thought = self.think(task)
        result = self.act(self.plan(task))
        summary = f"{self.name} completed the task with result: {result}"
        self.memory.append(summary)
        return result

if __name__ == "__main__":
    print("🤖 Agentic AI – Eightfold Demo")
    agent = Agent("Orion", "Conversational AI Agent")

    while True:
        user_input = input("\nEnter your request (or type 'exit' to stop): ")
        if user_input.lower() == "exit":
            print("Goodbye! 👋")
            break
        output = agent.run(user_input)
        print(f"✅ Result: {output}")
