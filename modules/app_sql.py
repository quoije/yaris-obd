import sqlite3
import app_obd, app_car, app_account, app_gps
from datetime import datetime
from sqlite3 import Error

currentdatetime = datetime.now()
account = app_account.Account
car = app_car.Car
sCarModel = ''.join(letter for letter in car.model if letter.isalnum())
sql_file = account.name + "_" + sCarModel + ".db"
sql_path = "../db/sql/" + sql_file

def create_conn(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def main():
    db = sql_path

    sql_create_tracking_table = """CREATE TABLE IF NOT EXISTS tracking (
                                    id integer PRIMARY KEY,
                                    VN text NOT NULL,
                                    NAME text NOT NULL,
                                    DATETIME datetime,
                                    GPSX float,
                                    GPSY float,
                                    SPEED float,
                                    ODOMETER float
                                );"""
    
    sql_create_dtc_table = """CREATE TABLE IF NOT EXISTS dtc (
                                    id integer PRIMARY KEY,
                                    NAME text NOT NULL,
                                    STATUS text,
                                    DTC_ID text
                                );"""

    # create a database connection
    conn = create_conn(db)

    # create tables
    if conn is not None:
        # create diagnostics table
        create_table(conn, sql_create_tracking_table)

        # create diagnostics table
        create_table(conn, sql_create_dtc_table)

    else:
        print("Error! cannot create the database connection.")

if __name__ == '__main__':
    create_conn(sql_path)



#         ## VN, NAME, DATE, TIME, GPS_X, GPS_Y, SPEED, ODOMETER
#          (["VN", "NAME", "DATE", "TIME", "GPSX", "GPSY", "SPEED", "ODOMETER"])
#          ([car.model, account.name, currentday, currenttime, GPSX, GPSY, SPEED, ODOMETER])