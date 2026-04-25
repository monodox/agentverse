from agentverse.haptics import ForceSimulator, SensorSimulator, TouchSimulator


def test_force_simulator() -> None:
    assert ForceSimulator().compute_force(2.0, 3.0) == 6.0


def test_touch_and_sensor_simulators() -> None:
    assert TouchSimulator().detect_contact(0.2)
    assert SensorSimulator().read()["pressure"] == 0.0

