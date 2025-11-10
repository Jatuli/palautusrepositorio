class Season:
    def __init__(self, default_season="2024-25"):
        self.season = default_season

    def choose_season(self):
        print("Valitse kausi (esim. 2023-24)")
        user_selection = input("Anna kausi (Oletus = Enter): ").strip()

        if user_selection:
            self.season = user_selection

        else:
            print(f"Käytetään oletuskautta {self.season}")

        return self.season

    def get_url(self):
        return f"https://studies.cs.helsinki.fi/nhlstats/{self.season}/players"
