import mysql.connector 
class FootballDAO:     
    db=""     
    def __init__(self):          
        self.db = mysql.connector.connect(         
        host="localhost",         
        user="root",         
        password="",         
        database="leagues"
        )


    def create(self, values):         
        cursor = self.db.cursor()         
        sql="insert into football (league, club, known_as, manager, home_ground, capacity) values (%s,%s, %s, %s, %s, %s)"         
        cursor.execute(sql, values)

        self.db.commit()         
        return cursor.lastrowid 
    
    def getAll(self):         
        cursor = self.db.cursor()         
        sql="select * from football"         
        cursor.execute(sql)         
        results = cursor.fetchall()  
        returnArray = []
        for result in results:
            returnArray.append(self.convertToDictionary(result))
        return returnArray 
    
    def findByID(self, id):         
        cursor = self.db.cursor()         
        sql="select * from football where id = %s"         
        values = (id,) 
        
        cursor.execute(sql, values)         
        result = cursor.fetchone()         
        return self.convertToDictionary(result)

    def update(self, values):         
        cursor = self.db.cursor()         
        sql="update football set league= %s, club=%s,  known_as=%s, manager=%s, home_ground=%s, capacity=%s where id = %s"        
        cursor.execute(sql, values)         
        self.db.commit()     
    def delete(self, id):         
        cursor = self.db.cursor()         
        sql="delete from football where id = %s"         
        values = (id,) 
        
        cursor.execute(sql, values) 
        
        self.db.commit()         
        print("delete done")
    
    def convertToDictionary(self, result):
        colnames=['id', 'League', 'Club', 'Known_As', 'Manager', 'Home_ground', 'Capacity']

        item = {}

        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                item[colName] = value
        
        return item

footballDAO = FootballDAO()