 ###################################
#                                   #
#   Author: Zachary Feuerstein      #
#                                   #
#   File: fridgeTempSensor.py       #
#                                   #
#   Last-Date-Modified: 05-26-2013  #
#                                   #
 ###################################

from time import sleep
import time
import datetime
import sys
import os

while True:
    
    statusFile = open('status.txt', 'r')
    status = statusFile.read(1)

    if status == '1':
        print 'ok to go'
        tempfile = open('/sys/bus/w1/devices/28-000004950556/w1_slave', 'r')
        info = tempfile.read()
        tempfile.close()

        secondline = info.split("\n")[1]
        temperaturedata = secondline.split(" ")[9] 
        temperature = float(temperaturedata[2:]) 
        temperature = temperature / 1000
        temperature = ((9.0/5.0)*temperature) + 32

        fileName = datetime.date.today()
        time = datetime.datetime.now()

        if os.path.exists('%s.txt'  %fileName):
            
            infoFile = open('%s.txt'  % fileName, 'a')
            infoFile.write('temp: %s' %temperature )
            infoFile.write(' time: %s\n' %time )
            infoFile.close()
        else:
            
            infoFile = open('%s.txt' %fileName, 'w') 
            infoFile.write('temp: %s' %temperature)
            infoFile.write(' time: %s\n' %time )
            infoFile.close()

    else:
        print 'exit'
        exit()
        
    sleep(300)
        
