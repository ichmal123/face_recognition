import connection

def insertData (name, rfid):
    con = connection.Connection()
    cursor = con.getConnection().cursor()
    sql = "INSERT INTO user (name, rfid_card) VALUES (%s, %s)"
    value = (name, rfid)
    cursor.execute(sql, value)
    con.getConnection().commit()

    print("Data entered successfully.")