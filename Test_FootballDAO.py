from Test_FootballDAO import FootballDAO

#create 
latestid = FootballDAO.create(('Premier League', 'Wolverhampton Wanderers', 'Wolves', 'Nuno Espirito Santo', 'Molineux', 31600)) 
# find by id 
result = FootballDAO.findByID(latestid); 
print (result) 
#update 
FootballDAO.update(('Championship', 'Leeds United', '‎The Whites The Peacocks', 'Marcelo Bielsa', 'Elland Road', 37980)) 
result = FootballDAO.findByID(latestid); 
print (result)
# get all  
allFootball_Leagues = FootballDAO.getAll() 
for Football_League in allFootball_Leagues:   
    print(Football_League) 
# delete 
FootballDAO.delete(latestid)