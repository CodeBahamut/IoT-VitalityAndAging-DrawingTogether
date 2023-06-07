# Controlling the GPIO pins on the Jetson Nano 

### RPi GPIO

After following the guide below we managed to figure out how to control the GPIO pins on the Jetson nano. The OS comes with the RPi.GPIO library and if not you need to install it.

<iframe width="280" height="160" 
src="https://www.youtube.com/embed/BBKpEgJKF0s" 
title="YouTube video player" frameborder="0" allow="accelerometer;
autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Using this video I came up with the code for the next example.

```python
import RPi.GPIO as GPIO
import time   
class PenServo:
    
    def __init__(self, pin):
        self.pin = pin
        # Optional cleanup which resets GPIO states
        GPIO.setmode(GPIO.BOARD)
        GPIO.cleanup(pin)
        # Setup
        GPIO.setup(pin,GPIO.OUT)
        self.is_up = True
        
    def up(self, delay = 0):
        GPIO.output(self.pin,True)
        time.sleep(delay)
        self.is_up = True
        
    def down(self, delay = 0):
        GPIO.output(self.pin,False)
        time.sleep(delay)
        self.is_up = False
```

Here we use the RPi GPIO library to control the pins. Then we set the mode to board mode. Which means that you give it the pin numbers that are visible on the actual board. 
We cleanup the code to make sure its hasn't been configured or used for something else at the same time. We then set it as an output pin. We also add a state variable in the form of is_up to keep track of weather the servo is facing up or down. According to the code that we have on the Wemos if the pin is positive it will go up and if its negative it will go down. 

Below is an example using Jetson GPIO but we found this to be less intuitive than RPi.GPIO so we didn't use but it might prove handy for someone else. 

[NVIDIA/jetson-gpio](https://github.com/NVIDIA/jetson-gpio)

