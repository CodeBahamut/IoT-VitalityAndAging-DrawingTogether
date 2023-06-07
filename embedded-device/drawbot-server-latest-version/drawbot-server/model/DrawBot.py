from queue import Queue
from model.Command import Command
from time import sleep
from threading import Thread
from jetbot import Robot
from model.PenServo import PenServo as Servo
from model.ColorDetector import ColorDetector

class DrawBot():
    def __init__(self):
        JETSON_SERVO_PIN = 7
        self._priorityQueue = Queue()
        self._is_controller_on = False
        self._is_moving = False
        self._should_detect_shape = False
        self.servo = Servo(JETSON_SERVO_PIN)
        self.servo.up()
        self.robot = Robot()
        self.color_detector = ColorDetector()
        
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
    def start_controller(self):
        self._is_controller_on= True

    # Check if Drawbot is currently running
    def is_controller_on(self):
        return self._is_controller_on
    
    # Enable/Disable shape detection
    def set_should_detect_shape(self, value):
        self._should_detect_shape = value

    # Enable manual controls
    def enable_manual_controls(self):
        while self._is_controller_on:
            if not self._priorityQueue.empty():
                self.handleQueue()

    # Stops the Drawbot from moving
    def stop_controller(self):
        self.robot.stop()
        self._is_controller_on = False

    def start_moving(self, speed=0.3):
        self.robot.stop()
        self.robot.forward(speed)
        self._is_moving = True
        
    def is_moving(self):
        return self._is_moving
    
    def stop_moving(self):
        self._is_moving = False
        self.robot.stop()
        
    # Move the Drawbot forwards
    def step_forward(self,speed=0.3):
        self.robot.forward(speed)
        sleep(1.0)
        self.robot.stop()
        
    # Move the Drawbot backwards
    def step_backward(self, speed=0.3):
        self.robot.stop()
        self.robot.backward(speed)
        sleep(1.0)
        self.robot.stop()

    # Turn the Drawbot to the left
    def step_left(self, speed=0.3):
        self.robot.stop()
        self.robot.left(speed)
        sleep(0.5)
        self.robot.stop()
        
         # Turn the Drawbot to the left
    def turn_180(self, speed=0.3):
        self.robot.stop()
        self.robot.left(speed)
        sleep(1.0)
        self.robot.stop()
        self.start_moving()
        
    # Turn the Drawbot to the right
    def step_right(self, speed =0.3):
        self.robot.stop()
        self.robot.right(speed)
        sleep(0.5)
        self.robot.stop()
        
        
    # Make the Drawbot wait
    def wait(self, time_to_wait=0.5):
        sleep(time_to_wait)
        
    # Handles a single command of the Drawbot Command queue
    def handleQueue(self):
        self.robot.stop()
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
            elif command == Command.Turn180:
                self.turn_180()
                print("Turn around baby")
                
    # Draw a single leaf of a sunflower
    def drawSunflowerLeaf(self):
        self.robot.stop()
        self.servo.down()
        INITIAL_SPEED = 0.4
        TIMEOUT = 0.25

        self.robot.forward(INITIAL_SPEED)
        sleep(TIMEOUT)

        self.robot.backward(INITIAL_SPEED)
        sleep(TIMEOUT)

        self.robot.left(INITIAL_SPEED)
        sleep(TIMEOUT)

        self.robot.stop()
        self.servo.up()
        
    # Draw an entire sunflower
    def drawSunflower(self):
        AMOUNT_OF_LEAVES = 13
        
        for i in range(AMOUNT_OF_LEAVES):
            self.drawSunflowerLeaf() 
    
    def draw_triangle_side(self):
        self.robot.stop()
        self.servo.down()
        
        INITIAL_SPEED = 0.4
        TIMEOUT = 0.4
        
        self.robot.forward(INITIAL_SPEED)
        sleep(TIMEOUT)
        
        self.servo.up()

        self.robot.set_motors(0, INITIAL_SPEED)
        sleep(TIMEOUT)
        self.robot.set_motors(INITIAL_SPEED, 0)
        sleep(TIMEOUT)    
    
    # To draw when a triangle is recognized
    def drawTriangle(self):
        for i in range(3):
            self.draw_triangle_side()
        
    def drawRectangle(self):
        self.drawTriangle()
        
    # Lift up the pencil
    def setPenUp(self):
        self.servo.up()
    
    # Put down the pencil
    def setPenDown(self):
        self.servo.down()
    
    def toggle_pen(self):    
        if self.servo.is_up:
            self.servo.down()
        else:
            self.servo.up()
    
    # Draw a pointy leaf
    def drawLeaf(self):
        self.robot.stop()
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

        self.setPenUp()
        self.robot.stop()
    
    def detect_color(self, image):
        return self.color_detector.detect_color(image)
    
    # Draw a single leaf
    def drawTurnLeafLeaf(self):
        self.robot.stop()
        self.setPenDown()
        INITIAL_SPEED = 0.6
        LEAVE_CURVE_TIMEOUT = 0.5
        TIMEOUT_TURN = 2.5
        SLOW_SPEED = INITIAL_SPEED * 0.3

        # Quick turn
        self.robot.set_motors(0, INITIAL_SPEED)
        sleep(LEAVE_CURVE_TIMEOUT)

        self.robot.set_motors(-INITIAL_SPEED, 0)
        sleep(LEAVE_CURVE_TIMEOUT)

        self.setPenUp()
        self.robot.stop()
        
    
    # Draw a turn leaf flower
    def drawTurnLeaf(self):
        for i in range(3):
            self.drawTurnLeafLeaf()

    def isServoUp(self):
        return self.servo.is_up
    
    def shouldDetectShape(self):
        return self._should_detect_shape