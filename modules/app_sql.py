import csv, os
import app_obd, app_car, app_account, app_gps
from datetime import datetime

currentday = datetime.today().strftime("%d%m%Y")
currenttime = datetime.now().strftime("%H_%M_%S")
account = app_account.Account
car = app_car.Car
sCarModel = ''.join(letter for letter in car.model if letter.isalnum())
sql_name = account.name + "_" + sCarModel + "_" + currentday + ".sql"
sql_path = "../db/sql/"



#         ## VN, NAME, DATE, TIME, GPS_X, GPS_Y, SPEED, ODOMETER
#          (["VN", "NAME", "DATE", "TIME", "GPSX", "GPSY", "SPEED", "ODOMETER"])
#          ([car.model, account.name, currentday, currenttime, GPSX, GPSY, SPEED, ODOMETER])