### API reference

In this table below are all the API calls that can be made to the Drawbot server and some info about them.
Once connected to the hotspot, the Drawbot's server can be reached on jetbot.local:5000

| Endpoint                           | HTTP METHOD | Description                                                                                                        |                           Response                            |                            
|:-----------------------------------|:------------|:-------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------:|
| /                                  | GET         | This will return the index page                                                                                    |  HTTP/1.1 200 OK<br>rendered html template (index.html page)  |
| /video                             | GET         | This will push dynamically updated content to the web browser, which is used for streaming the camera's frames     | HTTP/1.1 200 OK<br> multipart/x-mixed-replace; boundary=frame |
| /start                             | POST        | This will kick off the Drawbot, by starting a separate thread that will handle the controllers                     |          HTTP/1.1 200 OK<br>{"isDrawBotOn ": "True"}          |
| /stop                              | POST        | This will dispose the running thread that is responsible for handling the controllers                              |         HTTP/1.1 200 OK<br>{"isDrawBotOn ": "False"}          |
| /start-shape-detection             | POST        | This will start the shape detection mode, by starting a separate thread that is used to run the shape recognition  |       HTTP/1.1 200 OK<br>{"shouldDetectShape ": "True"}       |
| /stop-shape-detection              | POST        | This will stop the shape detection mode, by disposing the thread that is used to run the shape recognition         |      HTTP/1.1 200 OK<br>{"shouldDetectShape ": "False"}       |
| /command/enqueue<br/>/command-type | POST        | This will either enqueue or directly fire a certain command, (command-type can be: left, right, forward, backward) |       HTTP/1.1 201 OK<br>{"isEnqueued ": "True/False"}        |
| /draw-bot-state                    | GET         | This will return the status of the Drawbot                                                                         |       HTTP/1.1 200 OK<br>{"isDrawBotOn ": "True/False"}       |
| /pen-up                            | POST        | This will send a signal to the Wemose, to set the pen up                                                           |            HTTP/1.1 200 OK<br>{"isPenUp ": False}             |
| /pen-down                          | POST        | This will send a signal to the Wemose, to set the pen down                                                         |             HTTP/1.1 200 OK<br>{"isPenUp ": True}             |
| /flower-1                          | POST        | This will make the Drawbot to draw a flower v1                                                                     |         HTTP/1.1 200 OK<br>{"drawing-flower-1": True}         |
| /flower-2                          | POST        | This will make the Drawbot to draw a flower v2                                                                     |         HTTP/1.1 200 OK<br>{"drawing-flower-2": True}         |
| /flower-3                          | POST        | This will make the Drawbot to draw a flower v3                                                                     |         HTTP/1.1 200 OK<br>{"drawing-flower-3": True}         |

