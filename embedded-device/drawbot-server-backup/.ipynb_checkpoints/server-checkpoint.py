from flask import Flask, request, json, jsonify, make_response, render_template, Response
from flask_socketio import SocketIO
# from serialtest import get_dist
from threading import Thread, Lock
from time import sleep
from model.DrawBot import DrawBot
from model.Command import Command
from util.TypeConverters import CommandTypeConverter

from IPython.display import display
import ipywidgets.widgets as widgets
from jetbot import Camera, bgr8_to_jpeg
import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from teachable_machine import TeachableMachine
import os

script_dir = os.path.dirname(__file__)

# Load the model
model_path = os.path.join(script_dir, "shapes_model.h5")
labels_path =  os.path.join(script_dir, "labels.txt")

model = load_model(model_path, compile=False)

# Grab the labels from the labels.txt file. This will be used later.
labels = open(labels_path, 'r').readlines()

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins='*')
draw_bot = DrawBot()
camera = Camera.instance(width=224, height=224)

app.url_map.converters.update(command_type=CommandTypeConverter)

commands_thread:Thread=None
ml_thread:Thread=None # is used to run the the prediciton on this thread
thread_lock = Lock()


def generate_frames():
    while True:
        ret, buffer = cv2.imencode('.jpg', camera.value)
        frame = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

    
@app.route('/', methods=('GET','POST'))
def index():
    return render_template("index.html", title = 'Jetbot')


@app.route('/video')
def video():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/start', methods=('GET','POST'))
def start():
    draw_bot.start()
    global commands_thread
    commands_thread = Thread(target=draw_bot.enable_manual_controls)
    commands_thread.start()

    responseBody = {"isDrawBotOn ": draw_bot.is_on()}
    return make_response(jsonify(responseBody), 200)

@app.route('/pen-up', methods=('GET','POST'))
def set_pen_up():
    draw_bot.setPenUp()
    responseBody = {"isPenUp ": False}
    return make_response(jsonify(responseBody), 200)

@app.route('/pen-down', methods=('GET','POST'))
def set_pen_down():
    draw_bot.setPenDown()
    responseBody = {"isPenUp ": True}
    return make_response(jsonify(responseBody), 200)

@app.route('/flower-1', methods=('GET','POST'))
def flower_1():
    draw_bot.drawSunflower()
    responseBody = {"drawing-flower-1": True}
    return make_response(jsonify(responseBody), 200)

@app.route('/flower-2', methods=('GET','POST'))
def flower_2():
    draw_bot.drawLeaf()
    responseBody = {"drawing-flower-2": True}
    return make_response(jsonify(responseBody), 200)

@app.route('/flower-3', methods=('GET','POST'))
def flower_3():
    draw_bot.drawTurnLeaf()
    responseBody = {"drawing-flower-3": True}
    return make_response(jsonify(responseBody), 200)

@app.route('/stop', methods=('GET','POST'))
def stop():
    draw_bot.stop()
    responseBody = {"isDrawBotOn ": draw_bot.is_on()}
    commands_thread.join()
    return make_response(jsonify(responseBody), 200)

@app.route('/start-shape-detection', methods=('GET','POST'))
def start_shape_detection():
    draw_bot.set_should_detect_shape(True)
    responseBody = {"shouldDetectShape ": draw_bot.should_detect_shape()}
    return make_response(jsonify(responseBody), 200)

@app.route('/stop-shape-detection', methods=('GET','POST'))
def stop_shape_detection():
    draw_bot.set_should_detect_shape(False)
    responseBody = {"shouldDetectShape ": draw_bot.should_detect_shape()}
    return make_response(jsonify(responseBody), 200)
        
@app.route('/command/enqueue/<command_type:command>', methods=('POST', 'GET'))
def insertCommand(command: Command):
    isEnqueued = draw_bot.enqueue(command)
    responseBody = {"isEnqueued": isEnqueued}
    return make_response(jsonify(responseBody), 201)

## testing purposes
@app.route("/draw-bot-state", methods=['GET'])
def get_daraw_bot_status():
    is_draw_bot_on = False
    if commands_thread is not None and commands_thread.is_alive():
        is_draw_bot_on = True
    responseBody = {"isDrawBotOn": is_draw_bot_on}
    return make_response(jsonify(responseBody), 200)



def socket_thread():
    while True:
        if draw_bot.should_detect_shape():
            # Resize the raw image into (224-height,224-width) pixels.
            image = cv2.resize(camera.value, (224, 224), interpolation=cv2.INTER_AREA)
            # Make the image a numpy array and reshape it to the models input shape.
            image = np.asarray(image, dtype=np.float32).reshape(1, 224, 224, 3)
            # Normalize the image array
            image = (image / 127.5) - 1
            # Have the model predict what the current image is. Model.predict
            # returns an array of percentages. Example:[0.2,0.8] meaning its 20% sure
            # it is the first label and 80% sure its the second label.
            probabilities = model.predict(image)
            socketio.emit('onShapeIsDetected', {'shapeName': labels[np.argmax(probabilities)]})
            socketio.sleep(1)

@socketio.on('connect')
def connect():
    global ml_thread
    with thread_lock: ## this is equivalent to acquire and release
        if ml_thread is None:
            ml_thread = socketio.start_background_task(socket_thread)

            
@socketio.on('disconnect')
def disconnect():
    print('Client disconnected',  request.sid)
    if ml_thread is not None and ml_thread.is_alive():
        ml_thread.join()


if __name__ == '__main__':
#     app.run(host='192.168.178.29', port=5000, debug=False, threaded=True, use_reloader=False)
#     app.run(host='', port=5000, debug=False)
    app.run(host='0.0.0.0', port=5000, debug=False)