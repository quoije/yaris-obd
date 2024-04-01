import csv, os
import app_obd, app_car, app_account, app_gps
from datetime import datetime

currentday = datetime.today().strftime("%d%m%Y")
currenttime = datetime.now().strftime("%H_%M_%S")
account = app_account.Account
car = app_car.Car
sCarModel = ''.join(letter for letter in car.model if letter.isalnum())
tsv_name = account.name + "_" + sCarModel + "_" + currentday + "_" + currenttime + ".tsv"
tsv_path = "../db/tsv/" + tsv_name

def tsv_writer(bExist):
    with open(tsv_path, 'w') as o_file:
        ## VN, NAME, DATE, TIME, GPS_X, GPS_Y, SPEED, ODOMETER
        writer = csv.writer(o_file, delimiter='\t')
        if bExist == False:
            writer.writerow(["VN", "NAME", "DATE", "TIME", "GX", "GY", "SPEED", "ODO"])
        else:
            writer.writerow([car.model, account.name, currentday, currenttime])

if os.path.exists(tsv_path):
    tsv_writer(True)
else:
    tsv_writer(False)