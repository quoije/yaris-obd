from flask import Flask, render_template, make_response, json
import modules.app_obd, modules.app_car, modules.app_account, modules.app_gps, time
from modules.app_events import socketio
from gevent.pywsgi import WSGIServer

app = Flask(__name__)
socketio.init_app(app)

account = modules.app_account.Account()
obd = modules.app_obd.OBD()
car = modules.app_car.Car()
gps = modules.app_gps.get_gps()

@app.route('/')
def index():
    print("hello "+ account.name)
    print("you're car model is:" + car.model)
    return render_template('index.html', account = account, car = car)

@app.route('/dtc')
def dtc():
    return render_template('dtc.html', account = account, car = car)

@app.route('/dash')
def dash():
    return render_template('dash.html', account = account, car = car)

# not sure if im gonna use this
@app.route('/api/obd_speed/')
def data():
    data = app_obd.speed
    response = make_response(json.dumps(data))
    response.content_type = 'application/json'
    return response

if __name__ == '__main__':
    # Debug/Development
    # app.run(debug=True, host="0.0.0.0", port="5000")
    # Production
    http_server = WSGIServer(('', 5000), app)
    print("server on :5000")
    http_server.serve_forever()
    