# Assembly Guide

In this chapter there will be instructons on how to put the DrawBot together. Once you have reached this chapter you should already have all the items from the bill of materials including the items necessary to construct the JetBot (You can see how to put the JetBot together [here](https://jetbot.org/master/hardware_setup.html)). If you're interested in how we came up with the design you can go to the [pen holder attachment](documentation/pen_holder_doc.md) and [pen location research](research/research_pen_location.md) pages.

You will need some tools to make the Drawbot. These are a **screwdriver**, a **tap set** with M5 and M6 bits and a **soldering iron**.

![Tap bits](../images/Manual9.jpeg){width=300}

### Step 1 - Clean printed parts
Once you have printed all the parts for the DrawBot and created the JetBot you can start by cleaning the supports off of all the parts. Be careful with some areas as they are sometimes thinner than the supports and will easily break. 

3D printed parts are always a challenge due to the fact that not all printers have the same amount of accuracy and quality. You may need to adjust some parts to make them fit. This can be easily done by using sandpaper, a file or some clippers.

### Step 2 - Attach camera mount to JetBot

![Camera Extension](../images/Manual1.jpeg){width=266} 
![Camera Mount](../images/Manual2.jpeg){width=266}
![Camera Mount 2](../images/Manual3.jpeg){width=266}
![Diagonal Supports](../images/Manual4.jpeg){width=266}
![Diagonal Supports](../images/Manual5.jpeg){width=266}

1. Mount the camera extension to the JetBot using 4 screws   

2. Attach the camera mount to the extension using the M3x40 bolt and nut

3. Attach the 2 diagonal supports to the camera extension using 4 M2x10 screws and to the JetBot using 4 M2x20 screws

### Step 3 - Mount Pen Holder

![Hole tap left](../images/Manual6.jpeg){width=250}
![Hole tap right](../images/Manual7.jpeg){width=250}
![Tap pen holder](../images/Manual8.jpeg){width=250}
![feed bolts](../images/Manual10.jpeg){width=250}
![Attach holder](../images/Manual11.jpeg){width=250}
![Attach screw](../images/Manual12.jpeg){width=250}

4. Attach the pen holder to the camera extension by first tapping the two holes in the camera extension with an M6 bit. 
5. Next tap the hole in the front of the pen holder with an M5 bit
6. To attach the holder to the extension feed the 2 M6x40 bolts through the pen holder and screw them in the camera extension from underneath

    !!! warning
        The holes of the pen holder might be too small for the bolt: To overcome this roll up a piece of sandpaper and feed it through the holes several times. This should be enough to make the holes slightly bigger.

7. Screw the M5x20 bolt into the front hole of the holder
8. Attach the camera to the mount with 4 M2x10 screws and put a pen in the holder and you are all finished!

<p align="center">
  <img width="400" height="400" src="../images/Manual13.jpeg">
</p>


### Step 4 - Assemble the floor

![Attach Servo](../images/Manual15.jpeg){width=250}
![Attach WeMos](../images/Manual16.jpeg){width=250}
![Soldered wire](../images/Manual17.jpeg){width=250}
<p align="center">
  <img width="400" height="400" src="..\images\Wiring-diagram-servo.png">
</p>


1. Attach the servo to the floor with 2 M2x10 screws. Make sure the servo has a far enough reach to point at least 135 degrees up.
2. Mount the WeMos using one or two M2x10 screws (depends on the kind of Wemos you have).
3. Follow the instructions in the wiring diagram above to connect these components to the Jetson Nano. 
4. You also need to solder the ground wire like in the image above so that it can connect on 2 pins and in the plug to the servo.
5. Finally attach the floor to the JetBot using 4 M2x10 screws

6. When the floor is done it should look like this

    ![Finished Floor](../images/Manual18.jpeg){width=375}
    ![Finished Floor2](../images/Manual19.jpeg){width=375}

To finish up follow the wiring diagram to attach the two jump wires and plug the usb cable in one of the ports.
