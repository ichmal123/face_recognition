import serial

try:
  port_arduino = serial.Serial("/dev/ttyUSB0", baudrate=9600, timeout=1)
except Exception as error:
  print(error)

def get_rfid():
  rfid = 0
  while rfid == 0:
    data = port_arduino.read(128)
    rawdata = str(data.hex())
    value = len(data)
    if value >= 1:
      rfid = rawdata
      return rfid
      # con = connection.Connection()

      # username = input('Nama : ')
      # umur = input('Umur : ')
      # rfid_card = rawdata

      # cursor = con.getConnection().cursor()

      # sql = "INSERT INTO user (name, rfid_card, umur) VALUES (%s, %s, %s)"
      # value = (username, rfid_card, umur)

      # cursor.execute(sql, value)
      # con.getConnection().commit()

      # print("Data entered successfully.")
      # time.sleep(5)
      
