import requests
from player import Player

class PlayerReader:

    def __init__(self, url):
        self.url = url

    def get_players(self):
        data = requests.get(self.url)
        players_data = data.json()

        players = [Player(player_dict) for player_dict in players_data]

        return players