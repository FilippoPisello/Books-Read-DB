"""Use credentials in db_credentials to access the database"""
import mysql.connector
from db_credentials import CD


db = mysql.connector.connect(host=CD.host, user=CD.username, passwd=CD.password)
GENERAL_CURSOR = db.cursor()


DB: mysql.connector.CMySQLConnection = mysql.connector.connect(
    host=CD.host,
    user=CD.username,
    passwd=CD.password,
    database="books_database",
)
CURSOR: mysql.connector.cursor_cext.CMySQLCursor = db.cursor()
