import connection
import serial

try:
  port_arduino = serial.Serial("/dev/ttyUSB0", baudrate=9600, timeout=1)
except Exception as error:
  print(error)

while True:
  data = port_arduino.read(128)
  rawdata = str(data.hex())
  value = len(data)
  if value >= 1:
    con = connection.Connection()

    cursor = con.getConnection().cursor()

    sql = "SELECT rfid_card from user where rfid_card = (%s)"
    value = (rawdata)
    

    cursor.execute(sql, value)
    selectData = cursor.fetchone()

    print(selectData[0])
    
