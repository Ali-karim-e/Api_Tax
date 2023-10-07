import pyodbc
import json

class SQL_Database():

    def __init__(self):

        with open('config.json','r') as fh:
            config = json.load(fh)

        self.driver = config['driver']
        self.server = config['server']
        self.database = config['database']
        self.Username = config['Username']
        self.Password = config['Password']
        self.Trusted_Connection = config['Trusted_Connection']

    def create_server_connection(self):
        connection = None
        try:
            connection = pyodbc.connect(
            f'Driver={self.driver};'
            f'Server={self.server};'
            f'Database={self.database};'
            f'Username={self.Username};'
            f'Password={self.Password};'
            f'Trusted_Connection={self.Trusted_Connection};'
            )
            print("MySQL Database connection successful")
        except pyodbc.Error as err:
            print("Connection failed")
        return connection