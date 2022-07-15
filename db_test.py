import sys
import time
import unittest
from sqlite3 import connect

import mariadb
from selenium import webdriver

class Access_db(unittest.TestCase):
    input_pass = input("Enter db password:")

    #connect to mariaDB
    try:
        connect_db = mariadb.connect(
            user = "user1",
            password= input_pass,
            host="localhost",
            port=3306,
            database="studentRecords" #name of db that will be accessed
        )
    except mariadb.Error as e:
        print(f"Could not connect to MariaDB: {e}")
        sys.exit(1) #exit due to error 

    point = connect_db.cursor() #get cursor

    point.execute(
        "SELECT transcriptID FROM transcript"
    )
    for (transcriptID) in point:
        print(f"TranscriptID: {transcriptID}")
