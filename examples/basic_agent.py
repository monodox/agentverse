from agentverse.agents import BaseAgent
from agentverse.env import BaseEnv


def main() -> None:
    env = BaseEnv()
    agent = BaseAgent()
    observation = env.reset()
    action = agent.act(observation)
    print(action)


if __name__ == "__main__":
    main()

