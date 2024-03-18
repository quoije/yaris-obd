from app_events import socketio
from threading import Thread

class GPS:
    def __init__(self):
        self.LocationX = None
        self.LocationY= None

@socketio.on('gps')
def get_gps():
    global LocationX
    global LocationY
    
    LocationX = "45.5202844"
    LocationY = "-73.5493208"
    Location = [LocationX, LocationY]

    socketio.emit('gps_location', Location)
    
    print("websocket should be sent now")

    return print("socket.io emitted")