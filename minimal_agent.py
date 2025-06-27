class SimpleAgent:
    def __init__(self, goal):
        self.goal = goal
        self.history = []

    def think(self):
        thought = f"To achieve '{self.goal}', I need to gather information."
        self.history.append(thought)
        return thought

    def act(self):
        print("Thinking...")
        thought = self.think()
        print("Thought:", thought)
        print("with memory:", self.history)
        print("Action: Searching online (simulated)")

agent = SimpleAgent( "learn about AI agents")
agent.act()
agent.act()


