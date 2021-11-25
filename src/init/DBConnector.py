import mysql.connector

class DBConnector:

    username = None
    password = None
    host = None
    database = None

    def init(self, un, pw, ht, db):
        global username, password, host, database
        username = un
        password = pw
        host = ht
        database = db
        test = self.openConnection()
        if test != None:
            self.closeConnection(test)
            return True
        return False

    def openConnection(self):
        print("opening connection with username={}, password={}, host={}, db={}".format(username, password, host, database))
        return mysql.connector.connect(user=username, password=password, host=host, database=database)

    def closeConnection(self, conn):
        if conn != None:
            conn.close()

    def closeConnectionAndCursor(self, conn, cursor):
        if(conn != None and conn.is_connected()):
            if(cursor != None):
                cursor.close()
            conn.close()

    def findUserByUsernamePassword(self, username, password):
        conn = None
        cursor = None
        try: 
            print('finding user with username={}, password={}'.format(username, password))
            conn = self.openConnection()
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
            self.closeConnectionAndCursor(conn, cursor)