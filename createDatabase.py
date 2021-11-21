import CredentialLoader
import DBConnector

if __name__ == '__main__':
    credentials = CredentialLoader.load()
    DBConnector.init(
            credentials[CredentialLoader.MYSQL_USERNAME],
            credentials[CredentialLoader.MYSQL_ROOT_PASSWORD],
            credentials[CredentialLoader.MYSQL_HOST],
            credentials[CredentialLoader.MYSQL_DB],
        )
    conn = DBConnector.openConnection()

    # create users table
    query = '''
    CREATE TABLE `users` (
        `userId` int NOT NULL AUTO_INCREMENT,
        `username` varchar(64) NOT NULL,
        `password` varchar(64) NOT NULL,
        PRIMARY KEY (`userId`)
    ) '''
    cursor = conn.cursor()
    cursor.execute(query)

    # insert test user
    query = '''
        INSERT INTO users (username, password) VALUES ("testuser", "testpassword")
    '''
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()

    DBConnector.closeConnection(conn)