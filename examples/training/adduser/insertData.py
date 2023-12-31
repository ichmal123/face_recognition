import sys
sys.path.append("examples/training")
try:
    from training.adduser import connection
except:
    import connection

def insertData (nik, nama, tempatTgl, tgl, kelamin, alamat, agama, status, pekerjaan, kewarganegaraan, berlaku, rfid):
    con = connection.Connection()
    cursor = con.getConnection().cursor()
    sql = "INSERT INTO user (nik, nama, tempat_tanggal_lahir, tanggal_lahir, jenis_kelamin, alamat, agama, status, pekerjaan, kewarganegaraan, berlaku_hingga, rfid) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    value = (nik, nama, tempatTgl, tgl, kelamin, alamat, agama, status, pekerjaan, kewarganegaraan, berlaku, rfid)
    cursor.execute(sql, value)
    con.getConnection().commit()

    print("Data entered successfully.")

def selectData (rfid):
    x = []
    con = connection.Connection()
    cursor = con.getConnection().cursor()
    sql = "SELECT * FROM user WHERE rfid = %s"
    value = (rfid)
    cursor.execute(sql, value)
    result = cursor.fetchone()

    if result is not None:
        for item in result:
            x.append(item)

        dateStr = '{:%d-%B-%Y}'.format(result[4])
        x[4] = dateStr

    return x

    
