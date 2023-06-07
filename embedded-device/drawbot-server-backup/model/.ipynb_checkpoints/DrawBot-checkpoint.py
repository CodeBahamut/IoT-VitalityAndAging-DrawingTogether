from queue import Queue
from model.Command import Command
from time import sleep
from threading import Thread
from jetbot import Robot
from model.PenServo import PenServo as Servo

class DrawBot():
    def __init__(self):
        JETSON_SERVO_PIN = 7
        # Call the Thread class's init function
        # Thread.__init__(self)
        self._priorityQueue = Queue()
        self._is_on = True
        self._should_detect_shape = False
        self.robot = Robot()
        self.servo = Servo(JETSON_SERVO_PIN)
        self.servo.up()

    # Insert a command into the queue.
    def enqueue(self, command: Command) -> bool:
        self._priorityQueue.put(command)
        return True

    # Remove a command from the queue.
    def dequeue(self) -> Command:
        if not self._priorityQueue.empty():
            return self._priorityQueue.get()
        return Command.Idle

    # Start the drawbot
    def start(self):
        self._is_on = True

    # Check if Drawbot is currently running
    def is_on(self):
        return self._is_on
    
    # Check if Drawbot is currently detecting shapes
    def should_detect_shape(self):
        return self._should_detect_shape
    
    # Enable/Disable shape detection
    def set_should_detect_shape(self, value):
        self._should_detect_shape = value

    # Enable manual controls
    def enable_manual_controls(self):
        while self.is_on():
            if not self._priorityQueue.empty():
                self.handleQueue()

    # Stops the Drawbot from moving
    def stop(self):
        self.robot.stop()
        self._is_on = False

    # Move the Drawbot forwards
    def step_forward(self,speed=0.3):
        self.robot.forward(speed)
        sleep(1.0)
        self.robot.stop()
        
    # Move the Drawbot backwards
    def step_backward(self, speed=0.3):
        self.robot.backward(speed)
        sleep(1.0)
        self.robot.stop()

    # Turn the Drawbot to the left
    def step_left(self, speed=0.3):
        self.robot.left(speed)
        sleep(1.0)
        self.robot.stop()

    # Turn the Drawbot to the right
    def step_right(self, speed =0.3):
        self.robot.right(speed)
        sleep(1.0)
        self.robot.stop()

    # Make the Drawbot wait
    def wait(self, time_to_wait=0.5):
        sleep(time_to_wait)
        
    # Handles a single command of the Drawbot Command queue
    def handleQueue(self):
        command = self.dequeue()
        if not command == Command.Idle:
#             self.robot.stop() ## stop either way if the queue is not empty
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
                
    # Draw a single leaf of a sunflower
    def drawSunflowerLeaf(self):
        INITIAL_SPEED = 0.4
        TIMEOUT = 0.25

        self.robot.forward(INITIAL_SPEED)
        sleep(TIMEOUT)

        self.robot.backward(INITIAL_SPEED)
        sleep(TIMEOUT)

        self.robot.left(INITIAL_SPEED)
        sleep(TIMEOUT)

        self.robot.stop()
        
    # Draw an entire sunflower
    def drawSunflower(self):
        AMOUNT_OF_LEAVES = 13
        
        for i in range(AMOUNT_OF_LEAVES):
            self.drawSunflowerLeaf()
        
    # Lift up the pencil
    def setPenUp(self):
        self.servo.up()
    
    # Pick up the pencil
    def setPenDown(self):
        self.servo.down()
        
    # Draw a pointy leaf
    def drawLeaf(self):
        INITIAL_SPEED = 0.6
        LEAVE_CURVE_TIMEOUT = 0.5
        TIMEOUT_TURN = 2.5
        SLOW_SPEED = INITIAL_SPEED * 0.3

        # Curve forward
        self.robot.set_motors(SLOW_SPEED, INITIAL_SPEED * 0.8)
        sleep(LEAVE_CURVE_TIMEOUT)

        self.setPenUp()
        self.robot.stop()
        sleep(2)

        # Turn
        self.robot.set_motors(0, INITIAL_SPEED)
        sleep(LEAVE_CURVE_TIMEOUT)
        self.robot.set_motors(-INITIAL_SPEED, 0)
        sleep(LEAVE_CURVE_TIMEOUT)

        self.setPenDown()
        self.robot.stop()
        sleep(2)

        # Curve forward
        self.robot.set_motors(SLOW_SPEED, INITIAL_SPEED * 0.8)
        sleep(LEAVE_CURVE_TIMEOUT)

        self.robot.stop()
    
    # Draw a single leaf
    def drawTurnLeafLeaf(self):
        INITIAL_SPEED = 0.6
        LEAVE_CURVE_TIMEOUT = 0.5
        TIMEOUT_TURN = 2.5
        SLOW_SPEED = INITIAL_SPEED * 0.3

        # Quick turn
        self.robot.set_motors(0, INITIAL_SPEED)
        sleep(LEAVE_CURVE_TIMEOUT)

        self.robot.set_motors(-INITIAL_SPEED, 0)
        sleep(LEAVE_CURVE_TIMEOUT)

        self.robot.stop()
    
    # Draw a turn leaf flower
    def drawTurnLeaf(self):
        for i in range(3):
            self.drawTurnLeafLeaf()