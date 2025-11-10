class Player:
    def __init__(self, dicti):
        self.name = dicti['name']
        self.team = dicti['team']
        self.goals = dicti['goals']
        self.assists = dicti['assists']
        self.nationality = dicti['nationality']

    def points(self):
        return self.goals + self.assists

    def __str__(self):
        return f"{self.name}, ({self.team}), {self.goals}, + {self.assists} = {self.points()} pistettä"
