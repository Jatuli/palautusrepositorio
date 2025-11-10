import requests
from player_reader import PlayerReader
from player_stats import PlayerStats
from rich import print
from rich.table import Table
from rich.console import Console
from season import Season
from country import Country


def main():
    country = Country()
    selected_country = country.choose_country()
    season = Season()
    selected_season = season.choose_season()
    url = season.get_url()
    reader = PlayerReader(url)
    stats = PlayerStats(reader)

    
    
    finnish_players = stats.top_scorers_by_nationality(selected_country)

    console = Console()

    table = Table(title=f"{selected_country} pelaajat kaudella {selected_season}")

    table.add_column("Nimi", justify="left", style="cyan")
    table.add_column("Joukkue",justify="center", style="magenta")
    table.add_column("Maalit", justify="right", style="green" )
    table.add_column("Syötöt",justify="right", style="green")
    table.add_column("Pisteet", justify="right", style="green")

    for player in finnish_players:
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
