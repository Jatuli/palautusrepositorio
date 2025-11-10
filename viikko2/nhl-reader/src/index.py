from rich.table import Table
from rich.console import Console
from player_reader import PlayerReader
from player_stats import PlayerStats
from season import Season
from country import Country


def main():
    selected_country = choose_country()
    season = Season()
    selected_season = choose_season()
    url = season.get_url()
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality(selected_country)
    print_players_table(players, selected_country, selected_season)

def choose_country():
    country = Country()
    return country.choose_country()

def choose_season():
    season = Season()
    selected_season = season.choose_season()
    url = season.get_url()
    return selected_season, url

def print_players_table(players, country, season):
    console = Console()
    table = Table(title=f"{country} pelaajat kaudella {season}")

    table.add_column("Nimi", justify="left", style="cyan")
    table.add_column("Joukkue",justify="center", style="magenta")
    table.add_column("Maalit", justify="right", style="green" )
    table.add_column("Syötöt",justify="right", style="green")
    table.add_column("Pisteet", justify="right", style="green")

    for player in players:
        table.add_row(
            player.name,
            player.team,
            str(player.goals),
            str(player.assists),
            str(player.points())
       )

    console.print(table)

if __name__ == "__main__":
    main()
