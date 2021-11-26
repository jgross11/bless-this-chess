import re

class CredentialLoader:
    MYSQL_ROOT_PASSWORD = "MYSQL_ROOT_PASSWORD"
    MYSQL_PORT = "MYSQL_PORT"
    MYSQL_HOST = "MYSQL_HOST"
    MYSQL_USERNAME = "MYSQL_USERNAME"
    MYSQL_DB = "MYSQL_DB"

    def loadCredentials(self, path = "./"):
        ENV_PATH = path
        ENV_NAME = ".env"
        result = {}
        with open(ENV_PATH + ENV_NAME) as file:
            for line in file:
                split = line.split("=")
                key = split[0]
                value = re.split('"(.*)"', split[1])[1]
                result[key] = value
        return result