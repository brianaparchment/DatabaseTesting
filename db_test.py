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
