class Memory:
    def __init__(self):
        self.history = []

    def add(self, message):
        self.history.append(message)

    def recall(self):
        return "\n".join(self.history[-5:])  # short-term memory

class SimpleAgent:
    def __init__(self, goal):
        self.goal = goal
        self.memory = Memory()

    def think(self):
        thought = f"Thinking about goal: {self.goal}"
        self.memory.add(f"Thought: {thought}")
        return thought

    def decide(self):
        action = f"Action: Search for '{self.goal}'"
        self.memory.add(action)
        return action

    def act(self, action):
        print(action)
        self.memory.add(f"Executed: {action}")

    def loop(self, steps=3):
        for _ in range(steps):
            print(self.think())
            action = self.decide()
            self.act(action)
            print("--- Memory Snapshot ---")
            print(self.memory.recall())

agent = SimpleAgent("learn about vector databases")
agent.loop()
