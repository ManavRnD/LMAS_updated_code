import mysql.connector
class MySQLDatabase:
    def __init__(self,host,user,password,database):
        self.host= host
        self.user=user
        self.password=password
        self.database=database
        self.connection= None
        self.cursor=None

    def connect(self):
        try:
            self.connection= mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            self.cursor = self.connection.cursor(dictionary=True)
        except mysql.connector.Error as err:
            print(f"Error:{err}")
            self.connection= None
            self.cursor = None

    def disconnect(self):
        if self.cursor:
            self.cursor.close()
        if self.connection and self.connection.is_connected():
            self.connection.close()

    def execute_query(self,query,params=None):
        try:
            if not self.connection or not self.cursor:
                self.connect()
            if not self.connection or not self.cursor:
                return None
            self.cursor.execute(query,params)
            result= self.cursor.fetchall()
            return result
        except mysql.connector.Error as err:
            print(f"Error:{err}")
            return None
        finally:
            self.disconnect()

    def count_as_trigger(self,macid,interval):

        query="""
            SELECT COUNT(*) as count
            FROM lmas_data
            WHERE macid= %s AND
                  date_time >=NOW()- INTERVAL %s MINUTE AND
                  `AS` IN (1,2)
        """
        params=(macid,interval)
        return self.execute_query(query,params)