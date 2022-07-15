import sys
import time
import unittest
from sqlite3 import connect
from db_test import Check_db

import mariadb
import selenium



class Access_db():
    b = Check_db()
    
   
    
    #connect to mariaDB
    try:
        connect_db = mariadb.connect(
            user = "user1",
            password= b.input_pass,
            host="localhost",
            port=3306,
            database="studentRecords" #name of db that will be accessed
            )
    except mariadb.Error as e:
        print(f"Could not connect to MariaDB: {e}")
        sys.exit(1) #exit due to error 

    point = connect_db.cursor() #get cursor
      