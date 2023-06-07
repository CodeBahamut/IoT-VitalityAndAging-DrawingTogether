from queue import Queue
from model.Command import Command
from time import sleep
from threading import Thread
from jetbot import Robot

class DrawBot():

    def __init__(self):
        # Call the Thread class's init function
        # Thread.__init__(self)
        self._priorityQueue = Queue()
        self._is_on = True
        self._should_detect_shape = False
        self.robot = Robot()

    def enqueue(self, command: Command) -> bool:
        self._priorityQueue.put(command)
        return True

    def dequeue(self) -> Command:
        if not self._priorityQueue.empty():
            return self._priorityQueue.get()
        return Command.Idle

    def start(self):
        self._is_on = True

    def is_on(self):
        return self._is_on
    
    def should_detect_shape(self):
        return self._should_detect_shape
    
    def set_should_detect_shape(self, value):
        self._should_detect_shape = value

    def run(self):
#         self.step_forward()
        while self.is_on():
            if not self._priorityQueue.empty():
                self.handleQueue()
        print("\nStopped running")
        # self.turn_off()

    def stop(self):
        self.robot.stop()
#         self._priorityQueue.clear()
        self._is_on = False

    def step_forward(self,speed=0.3):
        self.robot.forward(speed)

    def step_backward(self, speed=0.3):
        self.robot.backward(speed)

    def step_left(self, speed=0.3):
        self.robot.left(speed)

    def step_right(self, speed =0.3):
        self.robot.right(speed)

    def wait(self, time_to_wait=0.5):
        sleep(time_to_wait)
        
    def handleQueue(self):
        command = self.dequeue()
        if not command == Command.Idle:
            self.robot.stop() ## stop either way if the queue is not empty
            if command == Command.Forward:
                self.step_forward()
                print("Forward is called")
            elif command == Command.Backward:
                self.step_backward()
                print("Backward is called")
            elif command == Command.Right:
                self.step_right()
                print("Right is called")
            elif command == Command.Left:
                self.step_left()
                print("Left is called")
        
        
        
    