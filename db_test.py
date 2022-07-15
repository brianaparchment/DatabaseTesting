import sys
import time
import unittest
from sqlite3 import connect

import mariadb
import selenium

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

class Access_db(unittest.TestCase):
    def setUp(self):
        #instructions and description of each table in the database
        self.instructions = ("This program allows users to access records from the database StudentRecords.\n")
        self.descriptions = ("Table Names and Descriptions \n Transcript: contains each student's transcript information\n Student: contains each students ID and email\n Personal Info: contains demographic information about each student\n")
        
    def test_input(self):
        print(self.instructions)
        print(self.descriptions)

        student_list = [] 
        point.execute("SELECT * FROM student")
        for row in point:
            #add table info into list 
            student_list.append(row)
        

        transcript_list = []
        point.execute("SELECT * FROM transcript")
        for row in point:
            transcript_list.append(row)
        

        personalInfo_list = []
        point.execute("SELECT * FROM personalInfo")
        for row in point:
            personalInfo_list.append(row)


        #user input to select specific records from database
        self.user_input = input("Enter a table name to view all records from a specific table:\n ")
        if self.user_input == "student":
            print(student_list) #print list based on user input
        elif self.user_input == "transcript":
            print(transcript_list)
        elif self.user_input == "personalInfo":
            print(personalInfo_list)
        else:
            print("Invalid Table Name") #prints if user enters table that does not exist

  
      

    def tearDown(self):
        point.close()
        connect_db.close()

if __name__ == "__main__":
    unittest.main()
