# How to determine the best location for a pen/marker on the JetBot?

In this piece of text I will research and conclude the best location for a pen/marker holder on the JetBot. To do this I'm going to find sources of working drawing robots and see where and why they placed the pen/marker the way they placed it. 

First of all I have some pictures of the JetBot we are working with: 

![JetBot rear](../images/JetBot-rear.jpeg){width=270}
![JetBot top](../images/JetBot-top.jpeg){width=270}
![JetBot front](../images/JetBot-front.jpeg){width=270}

From left to right it is the rear, the top and the front view of the vehicle.

I did some research on finished driving drawing robots and from that I can conclude that most of the pens are attached on the axle of the rotating wheels. This is because if the robot wants to draw a 90 degree angle it can do so by simply rotating the wheel at the same speed in opposite directions. If the pen is more forward or back it will draw a rounded shape with those same wheel settings. It is also less accurate with the pen at the rear of the machine. With our JetBot the rear swings out so it is very difficult to get accurate drawings. Here is an example of one of those drawing robots below.

<iframe width="815" height="400" src="https://www.youtube.com/embed/Uo2aUUNhdKs" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

So if we want to place the pen/marker on the axle of our JetBot we have to move some of the hardware to the rear which is the battery and the Jetson nano chip. But if we want ot achieve the same effect of perfect 90 degree angles with the pen in front of the axle (so we don't have to remake the chassis) we can also achieve this by coding the turns so that the wheels spin at different speeds in different directions. This is something we need to discuss because there might be no need for 90 degree angles. 

One thing is certain in adjusting the design for the pen/marker. And that is that we need to move the camera further to the front so it streches further than the pen. We can do this by adjusting the existing camera mount in 3D printing software. The file for this is provided in the JetBot documentation.

In conclusion, we need to place the pen or marker as close to the axle as possible. The best thing is to place it on the axle but having to move all the hardware it just doesn't seem practical. To place the pen on the front we must also move the camera to the front and print a different mount.


