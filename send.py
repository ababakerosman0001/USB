import serial
import time

ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)
time.sleep(2)

ser.write(b'uart\n')
print("Message sent!")

ser.close()
