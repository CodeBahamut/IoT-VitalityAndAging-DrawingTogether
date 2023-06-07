from flask import Flask, request, json, jsonify, make_response, render_template, Response
# from serialtest import get_dist
from threading import Thread
from time import sleep
from model.DrawBot import DrawBot
from model.Command import Command
from util.TypeConverters import CommandTypeConverter

from IPython.display import display
import ipywidgets.widgets as widgets
from jetbot import Camera, bgr8_to_jpeg
import cv2


app = Flask(__name__)
draw_bot = DrawBot()
app.url_map.converters.update(command_type=CommandTypeConverter)

thread:Thread=None
    
camera = Camera.instance(width=224, height=224)

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
    global thread
    thread = Thread(target=draw_bot.run)
    thread.start()

    responseBody = {"isDrawBotOn ": draw_bot.is_on()}
    return make_response(jsonify(responseBody), 200)

@app.route('/stop', methods=('GET','POST'))
def stop():
    draw_bot.stop()
    responseBody = {"isDrawBotOn ": draw_bot.is_on()}
    thread.join()
    return make_response(jsonify(responseBody), 200)
        
        
@app.route('/command/enqueue/<command_type:command>', methods=('POST', 'GET'))
def insertCommand(command: Command):
    isEnqueued = draw_bot.enqueue(command)
    responseBody = {"isEnqueued": isEnqueued}
    return make_response(jsonify(responseBody), 201)


# @app.route("/command/dequeue", methods=['GET'])
# def getNextCommand():
#     responseBody = {"command": draw_bot.dequeue().value}
#     return make_response(jsonify(responseBody), 200)

## testing purposes
@app.route("/draw-bot-state", methods=['GET'])
def get_daraw_bot_status():
    is_draw_bot_on = False
    if thread is not None and thread.is_alive():
        is_draw_bot_on = True
    responseBody = {"isDrawBotOn": is_draw_bot_on}
    return make_response(jsonify(responseBody), 200)


# @app.route('/comamnd', methods=['POST'])
# def to_process_json_example():
#     content_type = request.headers.get('Content-Type')
#     if content_type == 'application/json':
#         json = request.json
#         return json



if __name__ == '__main__':
#     app.run(host='192.168.178.29', port=5000, debug=False, threaded=True, use_reloader=False)
#     app.run(host='10.10.10.1', port=5000, debug=False)
    app.run(host='0.0.0.0', port=5000, debug=False)