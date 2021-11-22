import mysql.connector

username = None
password = None
host = None
database = None

def init(un, pw, ht, db):
    global username, password, host, database
    username = un
    password = pw
    host = ht
    database = db
    test = openConnection()
    if test != None:
        closeConnection(test)
        return True
    return False

def openConnection():
    print("opening connection with username={}, password={}, host={}, db={}".format(username, password, host, database))
    return mysql.connector.connect(user=username, password=password, host=host, database=database)

def closeConnection(conn):
    if conn != None:
        conn.close()

def closeConnectionAndCursor(conn, cursor):
    if(conn != None and conn.is_connected()):
        if(cursor != None):
            cursor.close()
        conn.close()

def findUserByUsernamePassword(username, password):
    conn = None
    cursor = None
    try: 
        print('finding user with username={}, password={}'.format(username, password))
        conn = openConnection()
        if(conn != None):
            cursor = conn.cursor(prepared=True)
            query = '''SELECT * FROM users WHERE username=%s AND password=%s'''
            cursor.execute(query, (username, password))
            data = cursor.fetchone()
            print("obtained user information: {}".format(data))
            if data == None:
                return None
            user = data[1].decode()
            password = data[2].decode()
            return {username: user, password: password}
        else:
            print('error opening connection when querying for user information')
            return None

    except mysql.connector.Error as error:
        print("error when querying for user information: {}".format(error))
    finally:
        closeConnectionAndCursor(conn, cursor)
