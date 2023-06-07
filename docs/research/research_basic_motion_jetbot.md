## Step 1 Connect to the jetbot

To learn how to connect to the jetbot go to [connect jetbot to pc](..\documentation\connect_jetbot_computer.md)

## Step 2 Import Robot from jetbot

Assuming that we are using the Jetbot pre-built OS then its not that difficult to control the robot. 

First we should add the robot class from the jetbot package using the following line. 

```
from jetbot import Robot
```

The next step is to initilize it as an instance

```
robot = Robot()
```

## Step 3 Making the Jetbot move

### Giving simple movement commands to the Jetbot

The robot class has 4 basic automatized methods for movement (``left``, ``right``, ``forward`` and ``backward``). It also has a ``stop`` function. 

An example of using the forward method is:

```
robot.forward(0.1)
```

In this example 0.1 means 10% of its max speed. 

You can use the stop method in a similiar fashion:

```
robot.stop()
```

An example where you would make the robot go forward then stop using a short command would be:

```
robot.forward(0.5)
time.sleep(0.5)
robot.stop()
```

### Controlling motors individually

There are a few methods in the robot class to control the motors individually.

The first is ``set_motors``. Using this method you can give two values with the method. The first parameter is the value for the left motor and the second parameter is for the right motor. 

An example is as follows:

```
robot.set_motors(0.3, 0.1)
time.sleep(3.0)
robot.stop()
```

In this example the robot should go slowly to the right for 3 seconds then stop. 

Another method to to control the motors seperatly is by changing the values of the attributes of the motors inside of the robot class. The attributes for the motors are ``left_motor`` and ``right_motor``. So an example similiar to the one from eariler but using this method would be:

```
robot.left_motor.value = 0.3
robot.right_motor.value = 0.1
time.sleep(3.0)
robot.left_motor.value = 0.0
robot.right_motor.value = 0.0
```

