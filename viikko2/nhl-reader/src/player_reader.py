import requests
from player import Player

class PlayerReader:

    def __init__(self, url):
        self.url = url

    def get_players(self):
        data = requests.get(self.url, timeout=10)
        players_data = data.json()

        players = [Player(player_dict) for player_dict in players_data]
        return players

    def get_players_by_team(self, team: str):
        all_players = self.get_players()
        return [p for p in all_players if p.team == team]
