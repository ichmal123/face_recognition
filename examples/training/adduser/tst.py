import serial

try:
    port_arduino = serial.Serial("COM3", baudrate=9600, timeout=1)
    while True:
        data = port_arduino.read(128)
        rawdata = data.hex()
        value = len(data)
        if value >= 1:
            print(rawdata)
except Exception as error:
    print(error)

# while True:
#     print (len(port_arduino.readline()))

