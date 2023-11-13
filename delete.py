# installed library mysql-connector-python
import mysql.connector

#creating connection 

class delete:
    def __init__(self):
        self.conn = mysql.connector.connect(
                host = "localhost",
                user = "root",
                password = "Munnimunni@123",
                database = "bank"
                )
    
    def specific_del(self,table_name,cid):
        cur = self.conn.cursor()
        cur.execute(f"delete from {table_name} where customerid={cid}")
        self.conn.commit()
        print("Data has been deleted sucessfully")