#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: AlexLin
"""

import pymysql
import json


def read_json(jsonfile):
    # change json file to dictionary
    dict = json.loads(jsonfile)
    return dict

def connect_db():
    # connect to MySQL database
    db = pymysql.connect(host='localhost', port=3306, user='root', passwd='yourpassword', db='patientinfo')
    print('connected')
    return db


def create_table(db):
    cursor = db.cursor()

    sql = """CREATE TABLE PatientInfo(
            id VARCHAR (255),
            patientName VARCHAR(255),
            gender VARCHAR(255),
            age int(255),
            time VARCHAR (255),
            blood_pressure VARCHAR(255),
            blood_Oxygen VARCHAR(255),
            pulse VARCHAR(255))"""

    cursor.execute(sql)
    db.commit()

    cursor.execute("SHOW TABLES")
    for x in cursor:
        print(x)


def insert_db(db, PatientInfo, SensorData):
    cursor = db.cursor()

    PatientInfo = read_json(PatientInfo)
    SensorData = read_json(SensorData)

    dict = {}

    for id in PatientInfo:
        dict['PatientID'] = id
        for i, j in PatientInfo[id].items():
            dict[i] = j
        for i, j in SensorData[id].items():
            dict[i] = j

    sql = """INSERT INTO PatientInfo(id, patientName, gender, age, time, blood_pressure, blood_oxygen, pulse)
         VALUES ('%s', '%s', '%s', %s, '%s', '%s', '%s', '%s')"""\
          % (dict['PatientID'], dict['name'], dict['gender'], dict['age'],
             dict['time'], dict['bloodPressure'], dict['bloodOx'], dict['pulse'])

    try:
        cursor.execute(sql)
        db.commit()

    except Exception:
        # Rollback in case there is any error
        db.rollback()


def search_db(db):
    cursor = db.cursor()
    # select to search based on the Patient's id
    sql = "SELECT * FROM PatientInfo"

    try:
        cursor.execute(sql)
        # obtain all recorded data
        results = cursor.fetchall()
        print(results)

        for row in results:
            id = row[0]
            patientName = row[1]
            gender = row[2]
            age = row[3]
            time = row[4]
            blood_pressure = row[5]
            blood_oxygen = row[6]
            pulse = row[7]

            print(("id: %s, patientName: %s, gender: %s, age: %s, time: %s, "
                  "blood_pressure: %s, blood_oxygen: %s, pulse: %s") % \
                (id, patientName, gender, age, time, blood_pressure, blood_oxygen, pulse))

    except Exception:
        print("Error: unable to fecth data")


def delete_db(db):
    cursor = db.cursor()

    # delete whole table
    sql = "DELETE FROM PatientInfo"

    # delete element from the table
    # sql="DELETE FROM PatientInfo WHERE id >'1234'"

    try:
        cursor.execute(sql)
        db.commit()

    except Exception:
        db.rollback()
    cursor.close()
    db.close()


def update_db(db):
    cursor = db.cursor()

    # example of updating one element from the table
    sql = "UPDATE PatientInfo SET age=age + 10"

    try:
        cursor.execute(sql)
        db.commit()

    except Exception:
        db.rollback()

def main():
    db = connect_db()    # connect MySQL database
    create_table(db)     # create table
    insert_db(db)        # insert values
    search_db(db)        # obtain records
    delete_db(db)        # delete table
    update_db(db)        # update data


if __name__ == '__main__':
    main()
