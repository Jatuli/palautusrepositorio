from player_reader import PlayerReader

class PlayerStats:

    def __init__(self, reader:PlayerReader):
        self.reader = reader

    def top_scorers_by_nationality(self, nationality: str):
        players = self.reader.get_players()

        by_nationality = [x for x in players if x.nationality == nationality]

        players_sorted = sorted(by_nationality, key = lambda p: p.points(), reverse=True)

        return players_sorted

    def average_points(self):
        players = self.reader.get_players()
        if not players:
            return 0
        total_points = sum(p.points() for p in players)
        return total_points / len(players)

    def _points(self, player):
        return player.points()
