from storage_mysqldb import *
from input import *
import alert_system
import output

PatientInfo = getPatientInfo()
SensorData = readSensorData()
db = connect_db()
create_table(db)
insert_db(db, PatientInfo, SensorData)
search_db(db)
# delete_db(db) #only use it if you want to delete table data for the patient
update_db(db)
alert_json = alert_system.alertCheck(SensorData)
patient1 = output.patient()
patient1.recieveFromAlert(alert_json)
patient1.send_alert_to_UI()
