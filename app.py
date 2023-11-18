import app_obd, app_car, app_account, time, app_events, threading
from flask import Flask, render_template, make_response, json
from app_events import socketio

port_number = 8000

app = Flask(__name__)
@app.route('/')
def index():
    print("hello")
    return render_template('index.html')

@app.route('/dtc')
def dtc():
    return render_template('dtc.html')

# not sure if im gonna use this
@app.route('/api/obd_speed')
def data():
    data = app_obd.speed
    response = make_response(json.dumps(data))
    response.content_type = 'application/json'
    return response

if __name__ == '__main__':  
    socketio.init_app(app)

    p_obd_connection = threading.Thread(target=app_obd.obd_connection)
    p_obd_connection.start()

    print("allo?")
    
    ##
    ## only debug, remove in prod
    ##
    app.run(host='localhost', port=port_number)
    ##
