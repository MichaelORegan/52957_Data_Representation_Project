import mysql.connector 
db = mysql.connector.connect(   
    host="localhost",   
    user="root",   
    password="",   
    #user="datarep",  
    # # this is the user name on my mac   
    # #passwd="password" # for my mac   
    database="leagues" 
    ) 
 
cursor = db.cursor() 
sql="delete from football where id = %s" 
values = (1,) 
 
cursor.execute(sql, values) 
 
db.commit() 
print("delete done")