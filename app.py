from flask import Flask, render_template, make_response, json
import app_obd, app_car, app_account, time
from app_events import socketio
from gevent.pywsgi import WSGIServer

app = Flask(__name__)
socketio.init_app(app)

account = app_account.Account()
obd = app_obd.OBD()
car = app_car.Car()

@app.route('/')
def index():
    print("hello "+account.name)
    return render_template('index.html', account = account)

@app.route('/dtc')
def dtc():
    return render_template('dtc.html')

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
    