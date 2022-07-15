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
        print(student_list)

        
        #user input to select specific records from database
        #self.user_input = input("Enter a table name to view all records from a specific table\n or Enter a studentID to view all records for a student: ")
  
       # point.execute(
        #    "SELECT transcriptID, credit_earned, credit_attempt, gpa, year, studentID FROM transcript"
       # )
       # for (transcriptID, credit_earned, credit_attempt, gpa, year, studentID) in point:
           # print(f"TranscriptID: {transcriptID}")
          #  print(f"Credits Earned: {credit_earned} ") 
           # print(f"Credits Attempted: {credit_attempt}") 
          #  print(f"GPA: {gpa}") 
          #  print(f"Year: {year}") 
          #  print(f"StudentID: {studentID}")

    def tearDown(self):
        point.close()
        connect_db.close()

if __name__ == "__main__":
    unittest.main()
