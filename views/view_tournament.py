class ViewTournament:

    def tournament_display(self):
        print("\n\n     Menu Tournoi\n\n"
              "1 - Ajouter le nom du tournoi \n"
              "2 - Ajouter le lieu\n"
              "3 - Choisissez le nombre de tour (par défaut il est à 4)\n"
              "4 - Choisissez le nombre de joueurs\n"
              "5 - Choisissez le type de contrôle de temps\n"
              "6 - Ajouter la description du tournoi\n"
              "7 - Voir les informations du tournoi\n"
              "8 - Précédent\n")
        return input("\nVeuillez entrez votre choix: \n\n")

    def get_name_tournament(self):
        name = input("Quelle est le nom du tournoi? ")
        print(f"Le nom du tournoi est bien {name}? \n"
              "1 - Oui \n"
              "2 - Non \n")
        answer = input("--> ")
        return name, answer

    def get_location_tournament(self):
        location = input("Quelle est le lieu du tournoi? ")
        print(f"Le lieu du tournoi est bien {location}? \n"
              "1 - Oui \n"
              "2 - Non \n")
        answer = input("--> ")
        return location, answer

    def get_number_round(self):
        number_round = input("Quelle est le nombre de tour? ")
        print(f"Le nombre de tours souhaité {number_round}? \n"
              "1 - Oui \n"
              "2 - Non \n")
        answer = input("--> ")
        return number_round, answer

    def get_number_players(self):
        number_player = input("Quelle est le nombre de joueurs? ")
        print(f"Est ce que le nombre de joueurs est {number_player}? \n"
              "1 - Oui \n"
              "2 - Non \n")
        answer = input("--> ")
        return number_player, answer

    def get_time_control(self):
        print("Quelle est le contrôle du temps? \n" "1 - Un bullet\n" "2 - Un blitz\n" "3 - Un coup rapide")
        return input("--> ")

    def get_description(self):
        description = input("Quelle est la description du tournoi? ")
        print(f"Est ce que la description est {description}? \n"
              "1 - Oui \n"
              "2 - Non \n")
        answer = input("--> ")
        return description, answer
