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

    def usernameTaken(self, username):
        conn = None
        cursor = None
        try: 
            print('checking if {} in db as username'.format(username))
            conn = self.openConnection()
            if(conn != None):
                cursor = conn.cursor(prepared=True)
                query = '''SELECT username FROM users WHERE username=%s LIMIT 1'''
                cursor.execute(query, (username,))
                data = cursor.fetchone()
                return True if data else False
            else:
                print('error opening connection when checking if username exists in db')
                return True

        except mysql.connector.Error as error:
            print("error when checking if username exists in db: {}".format(error))
            return True
        finally:
            self.closeConnectionAndCursor(conn, cursor)

    def emailTaken(self, email):
        conn = None
        cursor = None
        try: 
            print('checking if {} in db as email'.format(email))
            conn = self.openConnection()
            if(conn != None):
                cursor = conn.cursor(prepared=True)
                query = '''SELECT email FROM users WHERE email=%s LIMIT 1'''
                cursor.execute(query, (email,))
                data = cursor.fetchone()
                return True if data else False
            else:
                print('error opening connection when checking if email exists in db')
                return True

        except mysql.connector.Error as error:
            print("error when checking if email exists in db: {}".format(error))
            return True
        finally:
            self.closeConnectionAndCursor(conn, cursor)

    def insertNewUser(self, username, password, email):
        conn = None
        cursor = None
        try: 
            print('creating new user in db with information username={}, password={}, email={}'.format(username, password, email))
            conn = self.openConnection()
            if(conn != None):
                cursor = conn.cursor(prepared=True)
                query = '''INSERT INTO users (username, password, email) VALUES (%s, %s, %s)'''
                cursor.execute(query, (username, password, email))
                conn.commit()
                return True
            else:
                print('error opening connection when inserting new user')
                return False

        except mysql.connector.Error as error:
            print("error when inserting new user: {}".format(error))
            return False
        finally:
            self.closeConnectionAndCursor(conn, cursor)