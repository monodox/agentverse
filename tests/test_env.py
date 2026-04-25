from agentverse.env import BaseEnv, HapticEnv, RobotEnv


def test_base_env_step() -> None:
    env = BaseEnv()
    state, reward, done, info = env.step({"move": "noop"})
    assert state == {}
    assert reward == 0.0
    assert done is False
    assert info["action"] == {"move": "noop"}


def test_specialized_envs() -> None:
    assert HapticEnv().get_feedback()["force"] == 0.0
    assert RobotEnv().get_robot_state()["z"] == 0.0

