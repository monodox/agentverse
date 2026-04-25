from agentverse.agents import BaseAgent, HapticAgent, TeacherAgent


def test_base_agent_act() -> None:
    action = BaseAgent("test").act({"value": 1})
    assert action["agent"] == "test"


def test_haptic_and_teacher_agents() -> None:
    assert HapticAgent().process_touch({"pressure": 1.0})["pressure"] == 1.0
    assert TeacherAgent().demonstrate({})["agent"] == "agent"

