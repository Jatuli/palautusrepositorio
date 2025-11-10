class Country:
    def __init__(self, default_country="FIN"):
        self.country = default_country

    def choose_country(self):
        print("Valitse maa (esim. FIN)")
        user_selection = input("Anna maa (Oletus = Enter): ").strip()

        if user_selection:
            self.country = user_selection
        else:
            print(f"Käytetään oletuskautta {self.country}")

        return self.country

    def get_url(self):
        return f"https://studies.cs.helsinki.fi/nhlstats/{self.country}/players"
