import serial

try:
    port_arduino = serial.Serial("/dev/ttyUSB1", baudrate=9600, timeout=1)
except:
    print("Please Check The Port")

# while True:
#     print (len(port_arduino.readline()))

while True:
    data = port_arduino.read(128)
    rawdata = data.hex()
    value = len(data)
    if value >= 1:
        print(rawdata)