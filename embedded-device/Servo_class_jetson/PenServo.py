# import RPi.GPIO as GPIO
# import time   
# class PenServo:
    
#     def __init__(self, pin):
#         self.pin = pin
#         # Optional cleanup which resets GPIO states
#         GPIO.setmode(GPIO.BOARD)
#         GPIO.cleanup(pin)
#         # Setup
#         GPIO.setup(pin,GPIO.OUT)
#         self.is_up = True
        
#     def up(self, delay = 0):
#         GPIO.output(self.pin,True)
#         time.sleep(delay)
#         self.is_up = True
        
#     def down(self, delay = 0):
#         GPIO.output(self.pin,False)
#         time.sleep(delay)
#         self.is_up = False