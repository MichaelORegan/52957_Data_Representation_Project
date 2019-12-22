import mysql.connector 
mydb = mysql.connector.connect(   
    host="localhost",   
    user="root",   
    password="" ) 
mycursor = mydb.cursor() 
mycursor.execute("CREATE DATABASE leagues") 

import mysql.connector 

mydb = mysql.connector.connect(   
    host="localhost",   
    user="root",   
    password="",   
    database="leagues" ) 
mycursor = mydb.cursor() 
sql="CREATE TABLE football (id INT AUTO_INCREMENT PRIMARY KEY, league VARCHAR(255), club VARCHAR(255), known_as VARCHAR(255), manager VARCHAR(255), home_ground VARCHAR(255), capacity INT)" 
mycursor.execute(sql)