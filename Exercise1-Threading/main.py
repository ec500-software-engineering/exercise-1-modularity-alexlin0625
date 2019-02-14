from time import sleep
from threading import *
from storage_mysqldb import *
from input_thread import *
import alert_system
import output


def run_threads():
    while True:
        db = connect_db()
        PatientInfo = getPatientInfo()
        SensorData = readSensorData(PatientInfo)

        # create_table(db) #create table only the first target
        insert_db(db, PatientInfo, SensorData)
        # search_db(db)
        # delete_db(db) #only use it if you want to delete table data for the patient
        # update_db(db)
        sleep(2)
        alert_json = alert_system.alertCheck(SensorData)
        patient1 = output.patient()
        patient1.recieveFromAlert(alert_json)
        patient1.send_alert_to_UI()
        sleep(2)


t1 = Thread(target=run_threads())
t1.start()




