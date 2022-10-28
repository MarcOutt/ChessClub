class ViewPlayer:

    def menu_player(self):
        print("menu ajouter joueurs\n")
        while True:
            print(
                "1 - Ajouter nom de famille \n"
                "2 - Ajouter prénom\n"
                "3 - Ajouter date de naissance\n"
                "4 - Ajouter le sexe\n"
                "5 - Ajouter le classement\n"
                "6 - Revenir au menu principal")

            user = input("\nVeuillez entrez votre choix : \n")
            try:
                return int(user)
            except ValueError:
                print("Veuillez répondre par des chiffres\n")
                self.menu_player()

    def get_lastname(self):
        name = input("Quelle est le nom du joueur? ")
        answer = input(f"Le nom du joueur est {name}? \n"
                       "1 - Oui \n"
                       "2 - Non \n")
        return name, answer

    def get_firstname(self):
        name = input("Quelle est le prénom du joueur? ")
        answer = input(f"Le prénom du joueur est {name}? \n"
                       "1 - Oui \n"
                       "2 - Non \n")
        return name, answer

    def get_birthday(self):
        date = input("Quelle est la date de naissance? (DD/MM/YYYY) ")
        answer = input(f"La date de naissance du joueur est {date}? \n"
                       "1 - Oui \n"
                       "2 - Non \n")
        return date, answer

    def get_gender(self):
        return input("Quelle est le sexe?\n" "1 - Feminin \n" "2 - Masculin \n")

    def get_ranking(self):
        ranking = input("Quelle est la date de naissance? (XX) ")
        answer = input(f"Le nom du joueur est {ranking}? \n"
                       "1 - Oui \n"
                       "2 - Non \n")
        return ranking, answer
