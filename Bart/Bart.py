import time
import serial
import csv
import sys

comPort = sys.argv[1]
print(comPort)

arduino = serial.Serial(comPort, baudrate = 57600, timeout = 0.1)

arduino.write('read'.encode())
time.sleep(1)
data = arduino.readline().decode()
if data:
    print(data)

if data == "START\r\n":
    with open('file.csv', 'w') as file:
        while data != "END\r\n":
            data = arduino.readline().decode()
            print(data)
            writer = csv.writer(file)
            writer.writerow([data])
    file.close()






