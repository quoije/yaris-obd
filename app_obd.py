import obd, time, threading
from datetime import datetime
from app_events import socketio
from threading import Thread

status = None
speed = 0
rpm = None

class OBD:
    def __init__(self):
        self.status = status
        self.rpm = rpm
        self.speed = speed

obd_status = ["Disconnected", "Connected", "Connection...", "wtf"]
obd_speed_lock = threading.Lock()

try:
    print(obd_status[2])
    connection = obd.OBD()  # put linux /dev/rfi... something in () for the rpi bluetooth adpater

except Exception as e:
    print("An error occurred:", str(e))

def get_speedtime():
    global speed
    date = datetime.now()
    today = str(date.today())
    time_now = str(date.strftime("%H:%M:%S"))
    return [str(time_now), speed]

@socketio.on('obd')
def obd_connection():
        
    if connection.is_connected():
        print(obd_status[1])
        socketio.emit('obd_status', obd_status[1])
        print("OBD connection established.")

    else:
        print(obd_status[0])
        socketio.emit('obd_status', obd_status[0])
        socketio.emit('obd_speed', "-")
        socketio.emit('obd_error', "-")

        # test speed while offline
        print("OBD connection failed.")
        thread = Thread(target=obd_speed)
        thread.daemon = True
        thread.start()
            
def obd_speed():
    obd_speed_lock.acquire()
    cmd = obd.commands.SPEED  # select an OBD command (sensor)
    response = connection.query(cmd)  # send the command and parse the response
    loop = True
    try:
        while loop == True:
            global speed
            speed = speed + 1
            time.sleep(1)
            if response.is_null():
                    print("No data received. #"+ str(get_speedtime()))
                    socketio.emit('obd_speed', get_speedtime())
            else:
                    print("Original value:", response.value) 
                    print("Value in kph:", response.value.to("kph"))
                    socketio.emit('obd_speed', response.value.to("kph"))
    finally:
        obd_speed_lock.release()
        

