import time
from flask import Flask,request

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello World!'

# @app.route('/api/pins/on', methods = ['POST'])
# def on():
#     if request.method == 'POST':
#         json = request.json
#         print(json['pin'])
#         GPIO.setup(json['pin'], GPIO.OUT)
#         GPIO.output(json['pin'], GPIO.HIGH)
#         return '{} ON'.format(json['pin'])

# @app.route('/api/pins/off', methods = ['POST'])
# def off():
#     if request.method == 'POST':
#         json = request.json
#         print(json['pin'])
#         GPIO.output(json['pin'], GPIO.LOW)
#         return '{} OFF'.format(json['pin'])


# @app.route('/reset/pins')
# def reset():
#     GPIO.cleanup()
#     return 'GPIO RESET'
