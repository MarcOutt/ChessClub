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
                "6 - Vérifier les informations du joueurs\n"
                "7 - Suivant")

            user = input("\nVeuillez entrez votre choix : "
                         "\n")
            try:
                return int(user)
            except ValueError:
                print("Veuillez répondre par des chiffres\n")
                self.menu_player()

    def get_lastname(self):
        lastname = input("Quelle est le nom du joueur? ")
        print(f"Le nom du joueur est {lastname}? \n"
              "1 - Oui \n"
              "2 - Non \n")
        answer = input("--> ")
        return lastname, answer

    def get_firstname(self):
        firstname = input("Quelle est le prénom du joueur? ")
        print(f"Le prénom du joueur est {firstname}? \n"
              "1 - Oui \n"
              "2 - Non \n")
        answer = input("--> ")
        return firstname, answer

    def get_birthday(self):
        date = input("Quelle est la date de naissance? (DD/MM/YYYY) ")
        print(f"La date de naissance du joueur est {date}? \n"
              "1 - Oui \n"
              "2 - Non \n")
        answer = input("--> ")
        return date, answer

    def get_gender(self):
        return input("Quelle est le sexe?\n" "1 - Féminin \n" "2 - Masculin \n")

    def get_ranking(self):
        ranking = input("Quelle est le classement? (XX) ")
        print(f"Le classement du joueur est {ranking}? \n"
              "1 - Oui \n"
              "2 - Non \n")
        answer = input("--> ")
        return ranking, answer
