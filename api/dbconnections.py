import MySQLdb

class DBConnections:
    def getCursorObject(self):
        dbOBJ = MySQLdb.connect(host="localhost", user="root", passwd="jalaz", db="kitabghar")
        curOBJ = dbOBJ.cursor()
        return curOBJ