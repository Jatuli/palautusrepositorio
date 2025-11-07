from player_reader import PlayerReader
from player import Player


class PlayerStats:

    def __init__(self, reader:PlayerReader):
        self.reader = reader

    def top_scorers_by_nationality(self, nationality: str):
        players = self.reader.get_players()

        by_nationality = [x for x in players if x.nationality == nationality]

        players_sorted = sorted(by_nationality, key = lambda p: p.points(), reverse=True)

        return players_sorted