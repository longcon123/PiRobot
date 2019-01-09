import serial
import time
ard = serial.Serial('/dev/ttyACM0', 115200)
ard1 = serial.Serial('/dev/ttyUSB0', 9600)
while 1:
    da = str(input('nhap so :'))
    if da == '1':
        ard.write((da.encode()))
        time.sleep(1)
        da = '0'
        ard.write((da.encode()))
    if da == '6':
        while 1:
            ard1.write(('2'.encode()))
    if da == '3':
        ard.write((da.encode()))
        time.sleep(1)
        da = '0'
        ard.write((da.encode()))
    if da == '4':
        ard.write((da.encode()))
        time.sleep(1)
        da = '0'
        ard.write((da.encode()))
    if da == '5':
        while 1:
            ard.write(('5'.encode()))
    if da == '0':
        ard.write((da.encode()))
    if da == '2':
        ard.write((da.encode()))
        time.sleep(1)
        da = '0'
        ard.write((da.encode()))
    print('ok')

##		ard.write((str(data).encode()))

