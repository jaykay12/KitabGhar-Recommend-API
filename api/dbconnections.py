import MySQLdb
import os

LOCALHOST = os.environ.get('LOCALHOST')
USERNAME = os.environ.get('USERNAME')
PASSWORD = os.environ.get('PASSWORD')
DATABASE = os.environ.get('DATABASE')

class DBConnections:
    def getCursorObject(self):
        dbOBJ = MySQLdb.connect(host=LOCALHOST, user=USERNAME, passwd=PASSWORD, db=DATABASE)
        curOBJ = dbOBJ.cursor()
        return curOBJ