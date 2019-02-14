import random
import json
import time


def getPatientInfo():

    # get patient info
    patientId = random.randint(1000,9000)

    patientDict = {}
    patientDict[patientId] = {
                 'name': random.choice(['Alex', 'SeoYoung', 'Jason', 'Tony', 'Betty', 'Steven', 'James']),
                 'gender': random.choice(['Male', 'Female']),
                 'age': random.randint(20, 90)
                 }

    json_string = json.dumps(patientDict)
    print(json_string)
    return json_string


def readSensorData(PatientInfo):
    pi = json.loads(PatientInfo)
    patientId = next(iter(pi))

    data_dict = {}

    data_dict[patientId] = {
                 'pulse': random.randint(60,150),
                 'bloodPressure': random.randint(10,150),
                 'bloodOx': random.randint(30,140),
                 'time': time.ctime(),
                 'pulseRangeLower': 90,
                 'pulseRangeUpper': 120,
                 'pressureRangeLower': 30,
                 'pressureRangeUpper': 100,
                 'oxRangeLower': 60,
                 'oxRangeUpper': 90,
                 }

    sensordata = json.dumps(data_dict)
    print(sensordata)
    return sensordata


if __name__ == "__main__":
    getPatientInfo()
    readSensorData()
