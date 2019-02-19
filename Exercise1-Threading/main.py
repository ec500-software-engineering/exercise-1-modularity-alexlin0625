from time import sleep
from threading import Thread
from storage_mysqldb import connect_db, create_table, insert_db
from input_thread import getPatientInfo, readSensorData
import alert_system
import output


from storage_mysqldb import connect_db, create_table, insert_db, search_db, update_db
from input import getPatientInfo, readSensorData

def run_threads(PatientInfo, SensorData):
    db = connect_db()
    create_table(db) # create table only the first time
    insert_db(db, PatientInfo, SensorData)
    # search_db(db) # search for patient's current information
    # delete_db(db) # only use it if you want to delete table data for the patient
    # update_db(db) # update elements in patient's current information
    alert_json = alert_system.alertCheck(SensorData)
    patient1 = output.patient()
    patient1.recieveFromAlert(alert_json)
    patient1.send_alert_to_UI()


while True:
    PatientInfo = getPatientInfo()
    SensorData = readSensorData(PatientInfo)
    t1 = Thread(target=run_threads, args=(PatientInfo, SensorData))
    t1.start()
    sleep(3)





