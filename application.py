#!flask/bin/python 
from flask import Flask, jsonify, request, abort
from footballDAO import footballDAO
#from flask_cors import CORS


# pip install flask
# pip install flask_cors
# set FLASK_APP=application.py
# flask run
#
# cmd 1
# C:\Users\micha\GMIT\52957 DATA REPRESENTATION\52957_Data_Representation_Project (master -> origin)
# (Project_venv) λ flask run
#
# cmd 2
# C:\Users\micha\GMIT\52957 DATA REPRESENTATION\52957_Data_Representation_Project (master -> origin)
# 

app = Flask(__name__, static_url_path='', static_folder='.')
#CORS(app)

#football=[
#{"id":1, "League": "Premier League", "Club":"AFC Bournemounth", "Known_As": "The Cherries", "Manager":"Eddie Howe", "Home_ground": "Vitality Stadium", "Capacity":11360},
#{"id":2, "League": "Premier League", "Club":"Arsenal", "Known_As": "The Gunners", "Manager":"Freddie Ljungberg", "Home_ground": "Emirates Stadium", "Capacity":60260},
#{"id":3, "League": "Premier League", "Club":"Aston Villa", "Known_As": "The Villains", "Manager":"Dean Smith", "Home_ground": "Villa Park", "Capacity":42682},
#{"id":4, "League": "Premier League", "Club":"Brighton & Hove Albion", "Known_As": "The Seagulls", "Manager":"Graham Potter", "Home_ground": "Amex Stadium", "Capacity":30750},
#{"id":5, "League": "Premier League", "Club":"Burnley", "Known_As": "The Clarets", "Manager":"Sean Dyche", "Home_ground": "Turf Moor", "Capacity":22546},
#{"id":6, "League": "Premier League", "Club":"Chelsea", "Known_As": "The Blues Or The Pensioners", "Manager":"Frank Lampard", "Home_ground": "Stamford Bridge", "Capacity":41631},
#{"id":7, "League": "Premier League", "Club":"Crystal Palace", "Known_As": "The Eagles", "Manager":"Roy Hodgson", "Home_ground": "Selhurst Park", "Capacity":25456},
#{"id":8, "League": "Premier League", "Club":"Everton", "Known_As": "The Toffees", "Manager":"Duncan Ferguson", "Home_ground": "Goodison Park", "Capacity":39572},
#{"id":9, "League": "Premier League", "Club":"Leicester City", "Known_As": "The Foxes", "Manager":"Brendan Rodgers", "Home_ground": "King Power Stadium", "Capacity":32312},
#{"id":10, "League": "Premier League", "Club":"Liverpool", "Known_As": "The Reds", "Manager":"Jürgen Klopp", "Home_ground": "Anfield", "Capacity":54074},
#{"id":11, "League": "Premier League", "Club":"Manchester City", "Known_As": "The Citizens", "Manager":"Pep Guardiola", "Home_ground": "Etihad Stadium", "Capacity":55097},
#{"id":12, "League": "Premier League", "Club":"Manchester United", "Known_As": "The Red Devils", "Manager":"Ole Gunnar Solskjaer", "Home_ground": "Old Trafford", "Capacity":74994},
#{"id":13, "League": "Premier League", "Club":"Newcastle United", "Known_As": "The Magpies", "Manager":"Steve Bruce", "Home_ground": "St James’ Park", "Capacity":52405},
#{"id":14, "League": "Premier League", "Club":"Norwich City", "Known_As": "The Canaries", "Manager":"Daniel Farke", "Home_ground": "Carrow Road", "Capacity":27244},
#{"id":15, "League": "Premier League", "Club":"Sheffield United", "Known_As": "The Blades", "Manager":"Chris Wilder", "Home_ground": "Bramall Lane", "Capacity":32701},
#{"id":16, "League": "Premier League", "Club":"Southampton", "Known_As": "The Saints", "Manager":"Ralph Hasenhüttl", "Home_ground": "St Mary’s Stadium", "Capacity":32505},
#{"id":17, "League": "Premier League", "Club":"Tottenham Hotspur", "Known_As": "The Spurs", "Manager":"Jose Morinho", "Home_ground": "Tottenham Hotspur Stadium", "Capacity":62062},
#{"id":18, "League": "Premier League", "Club":"Watford", "Known_As": "The Hornets", "Manager":"Nigel Pearson", "Home_ground": "Vicarage Road", "Capacity":21577},
#{"id":19, "League": "Premier League", "Club":"West Ham United", "Known_As": "The Hammers", "Manager":"Manuel Pellegrini", "Home_ground": "London Stadium", "Capacity":60000},
#{"id":20, "League": "Premier League", "Club":"Wolverhampton Wanderers", "Known_As": "Wolves", "Manager":"Nuno Espirito Santo", "Home_ground": "Molineux", "Capacity":31700}
#]

# curl "http://127.0.0.1:5000/football"
@app.route('/football')
def getAll():
    results = footballDAO.getAll()
    return jsonify(results)

# curl "http://127.0.0.1:5000/football/1"
@app.route('/football/<int:id>')
def findByID(id):
    foundTeams = footballDAO.findByID(id)

    return jsonify(foundTeams)
    
    
    #foundTeams = list(filter(lambda t: t['id']==id, football))
    #if len(foundTeams) == 0:
    #    return jsonify({}), 204
    #return jsonify(foundTeams[0])

# curl -i -H "Content-Type:application/json" -X POST -d "{\"League\": \"Championship\",\"Club\":\"Shrew\",\"Home_ground\":\"Stadium\",\"Known_As\":\"Bugles\",\"Manager\":\"Me\",\"Capacity\":12000}" http://127.0.0.1:5000/football
# curl -i -H "Content-Type:application/json" -X POST -d "{\"League\": \"Premier League\",\"Club\":\"AFC Bournemounth\",\"Home_ground\":\"Vitality Stadium\",\"Known_As\":\"The Cherries\",\"Manager\":\"Eddie Howe\",\"Capacity\":11360}" http://127.0.0.1:5000/football
# curl -i -H "Content-Type:application/json" -X POST -d "{\"League\": \"Premier League\",\"Club\":\"Arsenal\",\"Home_ground\":\"Emirates Stadium\",\"Known_As\":\"The Gunners\",\"Manager\":\"Freddie Ljungberg\",\"Capacity\":42682}" http://127.0.0.1:5000/football
# curl -i -H "Content-Type:application/json" -X POST -d "{\"League\": \"Premier League\",\"Club\":\"Aston Villa\",\"Home_ground\":\"Villa Park\",\"Known_As\":\"The Villains\",\"Manager\":\"Dean Smith\",\"Capacity\":11360}" http://127.0.0.1:5000/football
# curl -i -H "Content-Type:application/json" -X POST -d "{\"League\": \"Premier League\",\"Club\":\"Brigthon and Hove Albion\",\"Home_ground\":\"Amex Stadium\",\"Known_As\":\"The Seagulls\",\"Manager\":\"Graham Potter\",\"Capacity\":30750}" http://127.0.0.1:5000/football
# curl -i -H "Content-Type:application/json" -X POST -d "{\"League\": \"Premier League\",\"Club\":\"Chelsea\",\"Home_ground\":\"Stamford Bridge\",\"Known_As\":\"The Blues\",\"Manager\":\"Frank Lampard\",\"Capacity\":41631}" http://127.0.0.1:5000/football

@app.route('/football', methods=['POST'])
def create():
    if not request.json:
        abort(400)
    # other checking
    team = {
        "League": request.json['League'],
        "Club": request.json['Club'],
        "Known_As": request.json['Known_As'],
        "Manager": request.json['Manager'], 
        "Home_ground": request.json['Home_ground'], 
        "Capacity":request.json['Capacity']
    }
    values = (team['League'], team['Club'],team['Known_As'],team['Manager'],team['Home_ground'],team['Capacity'])
    newId = footballDAO.create(values)
    team['id'] = newId
    return jsonify(team)

# curl -i -H "Content-Type:application/json" -X PUT -d "{\"League\": \"Championship\",\"Club\":\"Shrew\",\"Home_ground\":\"Stadium\",\"Known_As\":\"Bugles\",\"Manager\":\"Me\",\"Capacity\":12000}" http://127.0.0.1:5000/football/
# curl -i -H "Content-Type:application/json" -X PUT -d "{\"Capacity\":10000}" http://127.0.0.1:5000/football/1
# curl -i -H "Content-Type:application/json" -X PUT -d "{\"League\": \"Premier League\",\"Club\":\"AFC Bournemounth\",\"Home_ground\":\"Vitality Stadium\",\"Known_As\":\"The Cherries\",\"Manager\":\"Eddie Howe\",\"Capacity\":11360}" http://127.0.0.1:5000/football/1
@app.route('/football/<int:id>', methods=['PUT'])
def update(id):
    foundTeam = footballDAO.findByID(id)
    if not foundTeam:
        abort(404)

    if not request.json:
        abort(400)
    reqJson = request.json
    if 'Capacity' in reqJson and type(reqJson['Capacity']) is not int:
        abort(400)

    if 'League' in reqJson:
        foundTeam['League'] = reqJson['League']
    if 'Club' in reqJson:
        foundTeam['Club'] = reqJson['Club']
    if 'Known_As' in reqJson:
        foundTeam['Known_As'] = reqJson['Known_As']
    if 'Manager' in reqJson:
        foundTeam['Manager'] = reqJson['Manager']
    if 'Home ground' in reqJson:
        foundTeam['Home_ground'] = reqJson['Home_ground']
    if 'Capacity' in reqJson:
        foundTeam['Capacity'] = reqJson['Capacity']
    
    values = (foundTeam['League'], foundTeam['Club'],foundTeam['Known_As'],foundTeam['Manager'],foundTeam['Home_ground'],foundTeam['Capacity'],foundTeam['id'])
    footballDAO.update(values)
    return jsonify(foundTeam)
# error checking use code from b server if not int for capacity and if not string for others return error


# curl -X DELETE "http://127.0.0.1:5000/football/1"
@app.route('/football/<int:id>', methods=['DELETE'])
def delete(id):
    footballDAO.delete(id)
    return jsonify({"done":True})


if __name__ == '__main__':
    app.run(debug=True)