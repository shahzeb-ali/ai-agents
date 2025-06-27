from agent_memory_03 import AgentMemory

class SimpleAgent:
    def __init__(self, goal, user_id="user1"):
        self.goal = goal
        self.user_id = user_id
        self.memory = AgentMemory(user_id=user_id)


    def think(self) -> str:
        thought = f"Thinking about goal: {self.goal}"
        self.memory.add(thought, metadata={"type": "thought"})
        return thought

    def decide(self) -> str:
        action = f"Decide to search for '{self.goal}'"
        self.memory.add(action, metadata={"type": "action"})
        return action

    def act(self, action) -> str:
        result = f"Executed: {action}"
        self.memory.add(result, metadata={"type": "executed"})
        return result

    def loop(self, steps=3):
            for i in range(steps):
                print(f"\n --- Step --- {i+1}")
                thought = self.think()
                print(f"{thought}")

                action = self.decide()
                print(f"{action}")

                result = self.act(action)
                print(f"{result}")

                print("\nRecalling top 2 past thoughts...")
                memory_hits = self.memory.search("think", n_results=2)
                for m in memory_hits:
                    print(f"Retrieved: {m['document']} (type: {m['metadata'].get('type')})")



if __name__ == "__main__":
    agent = SimpleAgent(goal="learn about vector databases", user_id="user1")
    agent.loop(steps=3)
