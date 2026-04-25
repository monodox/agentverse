from agentverse.agents import BaseAgent, TeacherAgent


def main() -> None:
    agents = [BaseAgent("student"), TeacherAgent("teacher")]
    for agent in agents:
        print(agent.act({"task": "demo"}))


if __name__ == "__main__":
    main()

