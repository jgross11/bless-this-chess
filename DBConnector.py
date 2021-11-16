import mysql.connector

conn = None

def openConnection(username, password, host, database):
    if conn != None:
        return mysql.connector.connect(user=username, password=password, host=host, database=database)

def closeConnection():
    if conn != None:
        conn.close()