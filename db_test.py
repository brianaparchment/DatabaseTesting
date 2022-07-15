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
        print(self.instructions)
        print(self.descriptions)

        self.student_list = [] #empty list
        point.execute("SELECT * FROM student")
        for row in point:
            #add table info into list 
            self.student_list.append(row)

        self.transcript_list = []
        point.execute("SELECT * FROM transcript")
        for row in point:
            self.transcript_list.append(row) #add table info into list 

        self.personalInfo_list = []
        point.execute("SELECT * FROM personalInfo")
        for row in point:
            self.personalInfo_list.append(row) #add table info into list 


    def test_input(self):
        self.user_input = input("Enter a table name to view all records from a specific table:\n ")
                
        if self.user_input == "student":
            self.assertTrue(self.user_input == "student") #check user input
            print(self.student_list) #print specified list/ table info
       
        elif self.user_input == "transcript":
            self.assertTrue(self.user_input == "transcript") #check user input
            print(self.transcript_list) #print specified list/ table info

        elif self.user_input == "personalInfo":
            self.assertTrue(self.user_input == "personalInfo") #check user input
            print(self.personalInfo_list) #print specified list/ table info
        else:
            print("Invalid table name")

    def tearDown(self):
        point.close()
        connect_db.close() #end connection

if __name__ == "__main__":
    unittest.main()
