from flask import Flask, render_template, make_response, json
import app_obd, app_car, app_account, time
from app_events import socketio

app = Flask(__name__)
socketio.init_app(app)

account = app_account.Account()
obd = app_obd.OBD()
car = app_car.Car()

@app.route('/')
def index():
    print("hello "+account.name)
    return render_template('index.html', account = account)

# not sure if im gonna use this
@app.route('/api/obd_speed/')
def data():
    data = app_obd.speed
    response = make_response(json.dumps(data))
    response.content_type = 'application/json'
    return response