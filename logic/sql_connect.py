import pyodbc
import getpass

from logic.config.app_config import (
    ERROR_COLOR,
    SQL_DRIVER,
)


def Connection(ServerName,Auth):
    
    Connected = False

    while Connected is not True:
        AuthType = Auth
        databaseName = 'Master'
        if AuthType:
            try:
                conn = pyodbc.connect('''Driver={%s};
                                            Server=%s;
                                            Database=%s;
                                            Trusted_Connection=yes;''' % (SQL_DRIVER, ServerName,databaseName))
                Connected = True
                return conn
            except Exception as e:
                print(f"{ERROR_COLOR}{str(e)}")
                print('')
        elif not AuthType:
            Username = input('Enter Username: ')
            Passwrd =  getpass.getpass()
            try:
                conn = pyodbc.connect('''Driver={%s};
                                            Server=%s;
                                            Database=%s;
                                            uid=%s;
                                            Pwd=%s;
                                            Trusted_connection=no''' % (SQL_DRIVER,ServerName,databaseName,Username,Passwrd))
                Connected = True
                return conn
            except Exception as e:
                print(f"{ERROR_COLOR}{str(e)}")
                print('')
        else:
            print('Please enter Y or N!')