# EC500 exercise 1: I/O Operations
  * Modify project to take data coming on random time from an input process and can output data as they become available
  * Implement asynchronous input and output modules 


# Implementation
Extending from last exercise(Modularity), alert_system.py, storage_mysql.py and output.py are basically the same.  

* input_thread.py: this generates random data for PatientInfo and Sensordata, basically simulating practical situations and make the program more flexible    when we run threads in main. 



I created two types of implemtation using threads, one is main.py and one is main.queue.py. Both methods were discussed and approved by professor in the class.

* main.py: 

  This method runs whole program in one thread while creating more blocks of threads doing the same thing concurrently and continuously. 

* main.queue.py:

  This implemeentation is more practical usage, I seperate whole program into 3 different functions which are getAllInfo, manageDatabases and alert. I set 3 threads to handle each function's job concurrently and continuously. More importantly, I also implemented queues for the program to manage much better.

# Run
you can compile either main.py or main.queue.py to get the same result.

