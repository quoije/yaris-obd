import app_car as Car

account_car = Car()
account_car.model = "YARIS"
account_pp_image = "static\img\image.png"
account_info = ["name","pp_image", "car_model"]

class Account:
    def __init__(self):
        self.name = "quoije"
        self.pp_image = None
        self.car = account_car.model

def account_info():
    obd_speed_lock.acquire()
    cmd = obd.commands.GET_DTC  # select an OBD command (sensor)
    response = connection.query(cmd)  # send the command and parse the response
    try:
            if response.is_null():
                    error_txt = "No data received."
                    print(error_txt)
                    socketio.emit('obd_dtc', error_txt)
            else:   
                    print(response.value) 
                    socketio.emit('obd_dtc', response.value)
    finally:
        obd_rpm_lock.release()