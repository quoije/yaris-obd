from flask import Flask, render_template, make_response, json
import app_obd, app_car, app_account, time, app_events
from app_events import socketio

app = Flask(__name__)
socketio.init_app(app)
app_obd.obd_connection()

@app.route('/')
def index():
    print("hello")
    return render_template('index.html')

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

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Run the Flask application with a custom port."
    )
    parser.add_argument(
        "--port", type=int, default=5000, help="Port number (default is 5000)"
    )
    args = parser.parse_args()

    app.run(debug=True, port=args.port)