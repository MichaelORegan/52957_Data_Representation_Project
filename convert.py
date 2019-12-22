colnames=['id', 'League', 'Club', 'Known_As', 'Manager', 'Home_ground', 'Capacity']
result=(1,"Premier League", "Arsenal", "The Gunners", "Freddie Ljungberg", "Emirates Stadium", 60704)
item = {}

for i, colName in enumerate(colnames):
    value = result[i]
    item[colName] = value

print(item)