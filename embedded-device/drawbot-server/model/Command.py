from enum import Enum, unique


@unique
class Command(str,Enum):
    Forward = "forward"
    Backward = "backward"
    Right = "right"
    Left = "left"
    Idle = "idle"