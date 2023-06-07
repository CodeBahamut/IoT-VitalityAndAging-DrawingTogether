# Pick up where we left off

For the next team we advise to go through all the research and documentation we have made. Learn from our mistakes and
improve the DrawBot.

## Project code

[Here](https://gitlab.fdmci.hva.nl/IoT/2022-2023-sep-jan/group-project/vitalityandaging-drawing-together/-/tree/main/embedded-device/drawbot-server-latest-version/drawbot-server)
you can find the code.

## Our issues

- The power, we noticed that when you're trying to draw and detect shapes at the same time the Drawbot has power issues.
  For more info on the power issues please look into [Power issues](documentation/power_issue.md)
- When we first got the Jetbot it was really hard to connect to it. We have made this way easier, have a look
  into [Jetbot configuration](documentation/jetbot_configuration.md) to set it up.

## Our advice

- We noticed that it is really hard for the Drawbot to make accurate drawings. The motors are not precise enough and
  there is too much fluctuation in the results. Our advice for this would be to use stepper motors. With stepper motors
  you can tell the Drawbot the exact amount of steps it should make. Which should result in more accurate drawings.
