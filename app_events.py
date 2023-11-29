from flask_socketio import SocketIO
from threading import Thread
import app_obd, app_account, time, threading

socketio = SocketIO()
uptime_lock = threading.Lock()
os_type = ["Linux","Windows"]

@socketio.on('connect')
def connect_event():
    print('Client connected')
    print('Getting OBD status...')
    socketio.emit("connect", "connected with server")
    # uptime()

def uptime():
    thread = Thread(target=loop_uptime(os_type[1]))
    thread.daemon = True
    thread.start()

def loop_uptime(os):
    loop = True
    uptime_lock.acquire()
    if os == "Linux":
        try:
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
    elif os == "Windows":
        while loop == True:
            time.sleep(1)
            socketio.emit("rpi_uptime", "1")
            print("[+] sent uptime windows (1) packet")
            
        

    

