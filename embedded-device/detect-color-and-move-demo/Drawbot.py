from jetbot import Robot
import time
class Drawbot:
    def __init__(self) -> None:
        super().__init__()
        self.robot = Robot()

    def stop(self):
        self.robot.stop()

    def step_forward(self,speed=0.3):
        self.robot.forward(speed)

    def step_backward(self, speed=0.3):
        self.robot.backward(speed)

    def step_left(self, speed=0.3):
        self.robot.left(speed)

    def step_right(self, speed =0.3):
        self.robot.right(speed)

    def wait(self, time_to_wait=0.5):
        time.sleep(time_to_wait)

    def stop(self):
        self.robot.stop()