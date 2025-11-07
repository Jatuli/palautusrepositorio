import requests
from player import Player

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players"
    response = requests.get(url).json()
    
    players = response

    finnish_players = [x for x in players if x.get("nationality") == "FIN"]

    finnish_players_list = [Player(x) for x in finnish_players]

    print("Suomalaiset pelaajat:")

    for player in finnish_players_list:
        print(player)


if __name__ == "__main__":
    main()
