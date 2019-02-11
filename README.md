# EC500 exercise 1 Modulartiy
modules selected from https://github.com/alexlin0625/EC500_Spring19 in branches

  * Input_module selected from Sunitha Sampath

  * Alert_module selected from XiangKun Ye

  * Output_module selected from ZhiZhou Qiu

  * Storage_module from Alex Jeffrey Lin (myself)
  
# Implementation

  * Input.py: this is input module that return patient information and sersor data as json formate. Patientinfo contains patient's ID, name, gender and age. Sensordata contains time, pulse, pulse range(upper/lower), blood pressure, blood pressure range(upper/lower), blood oxygen and blood oxygen range(upper/lower).
  
  patientdetails.csv: contains testing data for Patientinfo.
  
  sensorinput.csv: contains testing data for Sensordata.

  * alert_system.py: this is alert system that takes in the sersor data from the input and does comparison for pulse, blood pressure and blood oxygen between each's upper and lower range, then print alert message to the output. 

  * Output.py: this outputs the the alert messages from the alert system and current patient's sensor data.

  * storage_mysqldb: MySQL database is implemented in this file. It creates a table, then extracts values obtained from json and stores the values corresponding to each columns into the table. 


# Run
to run the program, simply compile main.py 
