import connection

def insertData (nik, nama, tempatTgl, tgl, kelamin, alamat, agama, status, pekerjaan, kewarganegaraan, berlaku, rfid):
    con = connection.Connection()
    cursor = con.getConnection().cursor()
    sql = "INSERT INTO user (nik, nama, tempatTgl, tgl, kelamin, alamat, agama, status, pekerjaan, kewarganegaraan, berlaku, rfid) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    value = (nik, nama, tempatTgl, tgl, kelamin, alamat, agama, status, pekerjaan, kewarganegaraan, berlaku, rfid)
    cursor.execute(sql, value)
    con.getConnection().commit()

    print("Data entered successfully.")
