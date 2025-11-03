class BaseAgent:
    def __init__(self, name, role):
        self.name = name
        self.role = role
        self.memory = []

    def remember(self, note):
        self.memory.append(note)
        with open("data/memory_log.txt", "a") as f:
            f.write(note + "\n")
