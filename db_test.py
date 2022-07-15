#this program allows users to search the contents of the database
#the test will check the databse to see if the user input matches database records

from sqlite3 import connect
import mariadb
import sys

from selenium import webdriver

#connect to mariaDB
try:
    connect_db = mariadb.connect(
        user = "user1",
        password="Zoe456bp",
        host="localhost",
        port=3306,
        database="studentRecords" #name of db that will be accessed
    )
except mariadb.Error as e:
    print(f"Could not connect to MariaDB: {e}")
    sys.exit(1)

point = connect_db.cursor() #get cursor

point.execute(
    "SELECT transcriptID FROM transcript"
)
for (transcriptID) in point:
    print(f"TranscriptID: {transcriptID}")
