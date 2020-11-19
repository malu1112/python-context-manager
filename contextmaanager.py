import cx_Oracle
from os import environ


class ConnectDB:

    def __init__(self):
        # Can be loaded from properties or environment
        self.host = environ.get('ORACLE_HOST')
        self.port = environ.get('PORT')
        self.instance = environ.get('ORACLE_DB')
        self.username = environ.get('USERNAME')
        self.password = environ.get('PASSWORD')

    def __enter__(self):
        self.connection = cx_Oracle.connect(
            self.username,
            self.password,
            f'{self.host}:{self.port}/{self.instance}',
            encoding="UTF-8"
        )
        print('Connection made....')
        cursor = self.connection.cursor()
        return cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()
        print('Connection closed...')


# Make use of it
with ConnectDB as cur:
    cur.execute('select current_date from dual')
    print(cur.fetchall())
