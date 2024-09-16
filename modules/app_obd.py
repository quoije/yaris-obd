from modules import app_gps, app_sql, app_events
import obd, time, threading
from datetime import datetime
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
obd_rpm_lock = threading.Lock()

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

def obd_connection():  
    if connection.is_connected():
        print(obd_status[1])
        app_events.socketio.emit('obd_status', obd_status[1])
        print("OBD connection established.")

    else:
        print("OBD connection failed.")
        print(obd_status[0])

        app_events.socketio.emit('obd_status', obd_status[0])
        app_events.socketio.emit('obd_speed', "-")
        app_events.socketio.emit('obm_error', "-")
        app_events.socketio.emit('obd_rpm', "-")

        # debug speed for testing
        thread_speed = Thread(target=obd_speed)
        thread_speed.daemon = True
        thread_speed.start()

        # debug rpm for testing
        thread_rpm = Thread(target=obd_rpm)
        thread_rpm.daemon = True
        thread_rpm.start()
            
def obd_speed():
    obd_speed_lock.acquire()
    cmd = obd.commands.SPEED  # select an OBD command (sensor)
    response = connection.query(cmd)  # send the command and parse the response
    loop = True
    try:
        while loop == True:
            global speed
            speed = speed + 1
            time.sleep(10)
            if response.is_null():
                    print("No data received. #"+ str(get_speedtime()))
                    print(app_gps.get_gps())
                    app_events.socketio.emit('obd_speed', get_speedtime())
            else:
                    print("Original value:", response.value) 
                    print("Value in kph:", response.value.to("kph"))
                    app_events.socketio.emit('obd_speed', response.value.to("kph"))
    finally:
        obd_speed_lock.release()
        
def obd_rpm():
    obd_speed_lock.acquire()
    cmd = obd.commands.RPM  # select an OBD command (sensor)
    response = connection.query(cmd)  # send the command and parse the response
    loop = True
    try:
        while loop == True:
            global rpm
            speed = speed + 1
            time.sleep(1)
            if response.is_null():
                    print("No data received. #"+ str(get_speedtime()))
                    app_events.socketio.emit('obd_speed', get_speedtime())
            else:   
                    print("RPM:", response.value) 
                    app_events.socketio.emit('obd_speed', response.value.to("kph"))
    finally:
        obd_rpm_lock.release()

def kill_obd(obd_type):
    if obd_type == "speed":
        obd_speed.loop = False
    elif obd_type == "rpm":
        obd_rpm.loop = False
