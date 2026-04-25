"""AgentVerse by Haptis: haptics-first agentic simulation."""

from agentverse.agents import BaseAgent, HapticAgent, TeacherAgent
from agentverse.env import BaseEnv, HapticEnv, RobotEnv
from agentverse.haptics import ForceSimulator, SensorSimulator, TouchSimulator

# Stable top-level aliases for downstream imports.
SimEnv = HapticEnv
Agent = HapticAgent
HapticLayer = ForceSimulator

__version__ = "0.1.0"
__author__ = "Monodox"

__all__ = [
    "Agent",
    "BaseAgent",
    "BaseEnv",
    "ForceSimulator",
    "HapticAgent",
    "HapticEnv",
    "HapticLayer",
    "RobotEnv",
    "SensorSimulator",
    "SimEnv",
    "TeacherAgent",
    "TouchSimulator",
]
