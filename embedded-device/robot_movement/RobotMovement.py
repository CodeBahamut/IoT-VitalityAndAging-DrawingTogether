from jetbot import Robot
import time
class RobotMovement(Robot):
    
    def __init__(self) -> None:
        super().__init__()
        
    def left_curve(self, speed):
        self.left_motor.value = speed / 2
        self.right_motor.value = speed
    
    def right_curve(self, speed):
        self.left_motor.value = speed / 2
        self.right_motor.value = speed
        
    def calculate_time(self, degree = 10):
        time = degree * 0.0109
        return time
        
    def turn_set_degrees_right(self, degree = 10, speed = 0.3):
        self.left_motor.value = speed
        self.right_motor.value = -speed
        timer = self.calculate_time(degree)
        time.sleep(timer)
        self.stop()
        
    def turn_set_degrees_left(self, degree = 10, speed = 0.3):
        self.left_motor.value = -speed
        self.right_motor.value = speed
        timer = self.calculate_time(degree)
        time.sleep(timer)
        self.stop()
        
    def turn_45_degree_right(self, speed = 0.3):
        self.left_motor.value = speed
        self.right_motor.value = -speed
        time.sleep(0.49)
        self.stop()
        
    def turn_45_degree_left(self, speed = 0.3):
        self.left_motor.value = -speed
        self.right_motor.value = speed
        time.sleep(0.49)
        self.stop()
        
    def turn_90_degree_right(self, speed = 0.3):
        self.left_motor.value = speed
        self.right_motor.value = -speed
        time.sleep(0.95)
        self.stop() 
        
    def turn_90_degree_left(self, speed = 0.3):
        self.left_motor.value = -speed
        self.right_motor.value = speed
        time.sleep(0.95)
        self.stop() 
        
    def turn_180_degree_right(self, speed = 0.3):
        self.left_motor.value = speed
        self.right_motor.value = -speed
        time.sleep(1.9)
        self.stop()
        
    def turn_180_degree_left(self, speed = 0.3):
        self.left_motor.value = -speed
        self.right_motor.value = speed
        time.sleep(1.9)
        self.stop()
        
    def turn_360_degree_right(self, speed = 0.3):
        self.left_motor.value = speed
        self.right_motor.value = -speed
        time.sleep(3.68)
        self.stop()
        
    def turn_360_degree_left(self, speed = 0.3):
        self.left_motor.value = -speed
        self.right_motor.value = speed
        time.sleep(3.68)
        self.stop()
        
        
    # ALl the curves at normal speeds.
    def right_curve_forward(self, speed = 0.3):
        self.left_motor.value = speed
        self.right_motor.value = speed / 2
        
    def left_curve_forward(self, speed = 0.3):
        self.left_motor.value = speed / 2
        self.right_motor.value = speed 
        
    def right_curve_backward(self, speed = -0.3):
        self.left_motor.value = speed
        self.right_motor.value = speed / 2
    
    def left_curve_backward(self, speed = -0.3):
        self.left_motor.value = speed / 2
        self.right_motor.value = speed 
        
    # ALl the curves at fast speeds.
    def right_curve_forward_fast(self, speed = 0.8):
        self.left_motor.value = speed
        self.right_motor.value = speed / 2
        
    def left_curve_forward_fast(self, speed = 0.8):
        self.left_motor.value = speed / 2
        self.right_motor.value = speed 
        
    def right_curve_backward_fast(self, speed = -0.8):
        self.left_motor.value = speed
        self.right_motor.value = speed / 2
    
    def left_curve_backward_fast(self, speed = -0.8):
        self.left_motor.value = speed / 2
        self.right_motor.value = speed
    
        
#     left_motor = traitlets.Instance(Motor)
#     right_motor = traitlets.Instance(Motor)

#     # config
#     i2c_bus = traitlets.Integer(default_value=1).tag(config=True)
#     left_motor_channel = traitlets.Integer(default_value=1).tag(config=True)
#     left_motor_alpha = traitlets.Float(default_value=1.0).tag(config=True)
#     right_motor_channel = traitlets.Integer(default_value=2).tag(config=True)
#     right_motor_alpha = traitlets.Float(default_value=1.0).tag(config=True)
    
#     def __init__(self, *args, **kwargs):
#         super(Robot, self).__init__(*args, **kwargs)
#         self.motor_driver = Adafruit_MotorHAT(i2c_bus=self.i2c_bus)
#         self.left_motor = Motor(self.motor_driver, channel=self.left_motor_channel, alpha=self.left_motor_alpha)
#         self.right_motor = Motor(self.motor_driver, channel=self.right_motor_channel, alpha=self.right_motor_alpha)
        
#     def set_motors(self, left_speed, right_speed):
#         self.left_motor.value = left_speed
#         self.right_motor.value = right_speed
        
#     def forward(self, speed=1.0, duration=None):
#         self.left_motor.value = speed
#         self.right_motor.value = speed

#     def backward(self, speed=1.0):
#         self.left_motor.value = -speed
#         self.right_motor.value = -speed

#     def left(self, speed=1.0):
#         self.left_motor.value = -speed
#         self.right_motor.value = speed

#     def right(self, speed=1.0):
#         self.left_motor.value = speed
#         self.right_motor.value = -speed

#     def stop(self):
#         self.left_motor.value = 0
#         self.right_motor.value = 0
        

    
