import pymysql

class Connection:
    def __init__(self):
        self.conn = pymysql.connect(
      host='localhost',
      user='sammy',
      password = "password",
      db='test',
      )
    
    def getConnection(self):
        return self.conn

    def closeConnection(self):
        self.conn.close()


#   def mysqlconnect():
#     # To connect MySQL database
#     conn = pymysql.connect(
#       host='localhost',
#       user='sammy',
#       password = "password",
#       db='test',
#       )
    
#     cur = conn.cursor()
#     cur.execute("select @@version")
#     output = cur.fetchall()
#     print(output)
    
#     # To close the connection
#     conn.close()

#   # Driver Code
#   if __name__ == "__main__" :
#     mysqlconnect()
