from agentverse.agents import HapticAgent
from agentverse.env import HapticEnv
from agentverse.training import Trainer


def main() -> None:
    trainer = Trainer(HapticEnv(), HapticAgent())
    print(trainer.train_step())


if __name__ == "__main__":
    main()

