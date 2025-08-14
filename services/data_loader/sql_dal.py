import mysql.connector

class SQLDAL:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
    
    def dal_get(self, table, query):
        with self.connection.cursor(dictionary=True) as cursor:
            cursor.execute(f"SELECT {query} FROM {table}")
            data = cursor.fetchall()
