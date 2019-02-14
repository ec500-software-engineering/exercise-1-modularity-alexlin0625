'''
Created on 02/10/2019
@author: Xiangkun Ye
Source code copied from https://github.com/alexlin0625/EC500_Spring19/blob/alert-system/alert_system.py.
With lots of modifications to make it work.
Basically I rewrited the whole file.
'''

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 09:29:32 2019

@author: mohitbeniwal
"""
import json


def sendToUI(msg,j):
    ui_dict={"alert_message":msg,"bloodPressure":j["bloodPressure"],"pulse":j["pulse"],"bloodOx":j["bloodOx"]}
    ui_json=json.dumps(ui_dict)
    return ui_json
    #call_output_method


def alertCheck(Sensordata):
    j=json.loads(Sensordata)
    alert_message = ""

    for value in j.values():
        val = value

    if(val["bloodPressure"] < val["pressureRangeLower"]):
        alert_message+="BloodPressure is Too low, "
    elif(val["bloodPressure"]>val["pressureRangeUpper"]):
        alert_message="BloodPressure is Too high, "
    if(val["pulse"]<val["pulseRangeLower"]):
        alert_message+="Pulse is Too low, "
    elif(val["pulse"]>val["pulseRangeUpper"]):
        alert_message+="Pulse is Too high, "
    if(val["bloodOx"]<val["oxRangeLower"]):
        alert_message+="BloodOx is Too low, "
    elif(val["bloodOx"]>val["oxRangeUpper"]):
        alert_message+="BloodOx is Too high, "
    return sendToUI(alert_message, val)
