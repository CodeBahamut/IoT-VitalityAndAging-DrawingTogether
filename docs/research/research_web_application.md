# Research Web-application

## Requirements web-app

- Must have a page which can be used to control the Drawbot
- Can send commands to the jetbot
- Jetbot should be able to persist these commands

## Possible Solutions

1. The Jetbot hosts a network. This network can be accessed by wifi. Go to a specific URL to control te Jetbot. Any
   commands can be sent to the Jetbot using a python queue.

2. The web-app has a back-end which handles the Jetbot commands coming from actions in the Front-end. Posts them to a
   database. Jetbot can fetch current commands waiting in queue. Jetbot fetches a single command per iteration and
   executes it.

3. Front-end sends commands to a queue waiting on the back-end side. Jetbot can ```poll()``` this queue through an API.
   FIFO (queue).

4. Front-end sends commands to the back-end which has socket functionality. The Drawbot hosts a queue which its content
   is managed by the socket.

## Chosen solution

### Solution 3: Front-end sends commands to a queue waiting on the back-end side. Jetbot can ```poll()``` this queue through an API. FIFO (queue).

We chose this solution because it requires the least resources, but meets all requirements.

### How can we apply this solution?

#### Front-end

We require a single page which contains buttons to operate the Jetbot. Each time a button is pressed, the command is
sent to the database which is hosted using X (Heroku?).

- Static HTML pages
- CSS for styling
- Using Javascript controller to send commands

#### Back-end and Drawbot

Consists of a model layer which is used to store all commands using a queue. An API is set up which is used to control
this queue. For example: Front-end sends a POST request with a command to the API, which adds the cmomand to the queue.
Drawbot sends a GET request to the API which sends the command back to the Drawbot. Drawbot can execute the command.
Once finished, it fetches again.

- Class DrawbotQueue
- Model: 'Command', containing command information
- Model: 'Drawbot', containing a queue<DrawbotQueue> of commands<Command>
- Repository communicating with model queue
- Controller calls repository methods

### API overview

| Method | Action          | Endpoint        | Body                 | Response |
|--------|-----------------|-----------------|----------------------|----------|
| GET    | Get all commands        | /commands       |              | 200      |
| POST   | Enqueue command | /insertCommand  | {  "command": stop } | 201      |
| GET    | Dequeue command | /getNextCommand |                      | 200      |


