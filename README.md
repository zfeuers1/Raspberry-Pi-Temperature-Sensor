#Raspberry Pi Temperature Sensor

Takes the temperature every five minutes and records it to a txt file with the current date.
Checks a file called status.txt to see if you want to keep the sensor on. This is used so you can stop the program remotely. If you want the program to run type 1 into status.txt. To kill it enter 0.