from time import sleep
import threading
from storage_mysqldb import connect_db, create_table, insert_db
from input_thread import getPatientInfo, readSensorData
import alert_system
import output
import queue


def getAllInfo():
    while True:
        sleep(2)
        # get data
        PatientInfo = getPatientInfo()
        SensorData = readSensorData(PatientInfo)
        # putting data into queues.
        patientInfoQueue.put(PatientInfo)
        sensorDataQueue.put(SensorData)
        alertQueue.put(SensorData)


def manageDatabase():
    while True:
        PatientInfo = patientInfoQueue.get()
        SensorData = sensorDataQueue.get()
        # insert data from the queues to database.
        insert_db(db, PatientInfo, SensorData)
        print("Insert data successful")


def alert():
    while True:
        SensorData = alertQueue.get()
        # output alert messages
        alert_json = alert_system.alertCheck(SensorData)
        patient1 = output.patient()
        patient1.recieveFromAlert(alert_json)
        patient1.send_alert_to_UI()


db = connect_db()
create_table(db)  # only use this for the first time
patientInfoQueue = queue.Queue()
sensorDataQueue = queue.Queue()
alertQueue = queue.Queue()
threadGetInfo = threading.Thread(target=getAllInfo)
threadManageDatabase = threading.Thread(target=manageDatabase)
threadAlert = threading.Thread(target=alert)
threadGetInfo.start()
threadManageDatabase.start()
threadAlert.start()
