from flask_socketio import SocketIO
from threading import Thread
from modules import app_obd
import time, threading

socketio = SocketIO()
uptime_lock = threading.Lock()

@socketio.on('connect')
def connect_event():
    print('Client connected')
    print('Getting OBD status...')
    app_obd.obd_connection()
    uptime()

def uptime():
    thread = Thread(target=loop_uptime)
    thread.daemon = True
    thread.start()

def loop_uptime():
    uptime_lock.acquire()
    try:
        loop = True
        while loop == True:
            boottime = time.clock_gettime(time.CLOCK_BOOTTIME)
            # Convert to hours, minutes, and seconds
            seconds = int(boottime)
            minutes, seconds = divmod(seconds, 60)
            hours, minutes = divmod(minutes, 60)
            time.sleep(1)
            uptime = f"{hours:02d}:{minutes:02d}:{seconds:02d}"   
            socketio.emit("rpi_uptime", uptime)
    finally:
        uptime_lock.release()

    

