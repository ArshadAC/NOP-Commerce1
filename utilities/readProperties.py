import configparser
config = configparser.RawConfigParser()

config.read("E:\\Automation Project\\New NOP commerece\\Configuration\\config.ini")

class Readconfig:

    @staticmethod
    def geturl():
        url = config.get('common info','URL')
        return url

    @staticmethod
    def getemail():
        email = config.get('common info','Email')
        return email

    @staticmethod
    def getpassword():
        password = config.get('common info', 'Password')
        return password
