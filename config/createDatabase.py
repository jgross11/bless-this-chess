import sys
sys.path.append("..")
from bless_this_chess import DBConnector, CredentialLoader

if __name__ == '__main__':
    cursor = None
    conn = None
    try:
        dbConnector = DBConnector()
        credentialLoader = CredentialLoader()
        credentials = credentialLoader.loadCredentials()
        dbConnector.init(
                credentials[credentialLoader.MYSQL_USERNAME],
                credentials[credentialLoader.MYSQL_ROOT_PASSWORD],
                credentials[credentialLoader.MYSQL_HOST],
                credentials[credentialLoader.MYSQL_DB],
            )
        conn = dbConnector.openConnection()

        # wipe db if it exists
        print("wiping old data")
        query = '''DROP DATABASE IF EXISTS ''' + credentials[credentialLoader.MYSQL_DB] # no quotes around db name?!?!
        cursor = conn.cursor(prepared=True)
        cursor.execute('set profiling = 1')
        cursor.execute(query)

        # create db
        print("recreating db")
        query = '''CREATE DATABASE IF NOT EXISTS ''' + credentials[credentialLoader.MYSQL_DB] # no quotes around db name?!?!
        cursor = conn.cursor(prepared=True)
        cursor.execute(query)

        print("selecting db")
        query = '''USE ''' + credentials[credentialLoader.MYSQL_DB] # no quotes around db name?!?!
        cursor = conn.cursor()
        cursor.execute(query)

        # create users table
        print("creating user table")
        query = '''
        CREATE TABLE `users` (
            `userId` int NOT NULL AUTO_INCREMENT,
            `username` varchar(64) NOT NULL,
            `password` varchar(64) NOT NULL,
            `email` varchar(64) NOT NULL,
            PRIMARY KEY (`userId`)
        ) 
        '''
        cursor = conn.cursor()
        cursor.execute(query)

        # insert test user
        print("inserting test user")
        query = '''
            INSERT INTO users (username, password, email) VALUES ("testuser", "testpassword", "test@test.com")
        '''
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
    finally:
        cursor.execute('set profiling = 0')
        dbConnector.closeConnection(conn)