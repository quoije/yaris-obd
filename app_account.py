import app_car as Car
import threading, app_events
from threading import Thread

socketio = app_events.SocketIO()
account_name = "quoije"
account_pp_image = "static\img\image.png"
account_car = Car
account_car.model = "YARIS" 
account_lock = threading.Lock()

class Account:
    def __init__(self):
        self.name = account_name
        self.pp_image = account_pp_image
        self.car = account_car
    def info():
        return [name, pp_image, car.model]