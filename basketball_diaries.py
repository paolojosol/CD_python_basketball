#1 and #2
players = [
    {
    	"name": "Kevin Durant", 
    	"age":34, 
    	"position": "small forward", 
    	"team": "Brooklyn Nets"
    },
    {
    	"name": "Jason Tatum", 
    	"age":24, 
    	"position": "small forward", 
    	"team": "Boston Celtics"
    },
    {
    	"name": "Kyrie Irving", 
    	"age":32,
        "position": "Point Guard", 
    	"team": "Brooklyn Nets"
    },
    {
    	"name": "Damian Lillard", 
    	"age":33,
        "position": "Point Guard", 
    	"team": "Portland Trailblazers"
    },
    {
    	"name": "Joel Embiid", 
    	"age":32,
        "position": "Power Foward", 
    	"team": "Philidelphia 76ers"
    },
    {
        "name": "DeMar DeRozan",
        "age": 32,
        "position": "Shooting Guard",
        "team": "Chicago Bulls"
    }
]

class Player:
    def __init__(self, name, age, position, team):
        self.name = name
        self.age = age
        self.position = position
        self.team = team


kevin = {"name": "Kevin Durant", "age":34, "position": "small forward", "team": "Brooklyn Nets"}
player_kevin = Player(kevin["name"], kevin["age"], kevin["position"], kevin["team"])



jason = {
    	"name": "Jason Tatum", 
    	"age":24, 
    	"position": "small forward", 
    	"team": "Boston Celtics"
    }
player_jason = Player(jason["name"], jason["age"], jason["position"], jason["team"])



kyrie = {
    	"name": "Kyrie Irving", 
    	"age":32,
        "position": "Point Guard", 
    	"team": "Brooklyn Nets"
    }
player_kyrie = Player(kyrie["name"], kyrie["age"], kyrie["position"], kyrie["team"])



damian = {
    	"name": "Damian Lillard", 
    	"age":33,
        "position": "Point Guard", 
    	"team": "Portland Trailblazers"
    }

player_damian = Player(damian["name"], damian["age"], damian["position"], damian["team"])



joel = {
    	"name": "Joel Embiid", 
    	"age":32,
        "position": "Power Foward", 
    	"team": "Philidelphia 76ers"
    }

player_joel = Player(joel["name"], joel["age"], joel["position"], joel["team"])


demar = {
        "name": "DeMar DeRozan",
        "age": 32,
        "position": "Shooting Guard",
        "team": "Chicago Bulls"
    }

player_demar = Player(demar["name"], demar["age"], demar["position"], demar["team"])

#3
new_team = []
new_team.append(Player("Kevin Durant", 34, "small forward","Brooklyn Nets"))
new_team.append(Player("DeMar DeRozan", 32, "Shooting Guard","Chicago Bulls"))
new_team.append(Player("Damian Lillard", 33, "Power Forward","Philidelphia 76ers"))
for baller in new_team:
    print(baller.name, baller.age, baller.position, baller.team )
