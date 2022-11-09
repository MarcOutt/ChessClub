import datetime

class MainView():

    def __init__(self, controller):
        self.controller = controller
        self.main_menu()

    def main_menu(self):
        """Menu principal"""
        while True:
            choice = input(" 1. Créer un tournoi \n"
                           " 2. Ajouter les joueurs au tournoi \n"
                           " 3. Charger un tournoi\n"
                           " 4. Editer un rapport\n"
                           " 5. Mettre à jour le classement\n"
                           " 6. Exit \n"
                           "--> ")
            try:
                choice_int = int(choice)
                if choice_int == 1:
                    self.create_tournament()
                elif choice_int == 2:
                    self.add_player()
                    break
                elif choice_int == 3:
                    break
                elif choice_int == 4:
                    self.menu_get_report()
            except ValueError:
                print("Veuillez répondre par un chiffre correspondant à votre choix.")

    def screen_tournament(self):
        """Affiche les informations du tournoi qui vient d'être créé"""
        print("Félicitation, vous avez créer votre un Tournoi")

    def create_tournament(self):
        """ Vue pour la création du tournoi"""
        name = input("Nom du tournoi: ")
        location = input("Lieu du tournoi: ")
        number_rounds = self.get_number_rounds()
        # tournée = ??
        number_players = self.get_number_players()
        time_control = self.get_time_control()
        description = input("Veuillez ajouter la description du tournoi: ")
        self.controller.add_tournament(name=name, location=location, number_rounds=number_rounds,
                                       number_players=number_players, time_control=time_control,
                                       description=description)

    def get_number_players(self):
        try:
            return int(input("Quelle est le nombre de joueurs: "))
        except ValueError:
            print("Veuillez répondre par un chiffre correspondant à votre choix.")

    def get_number_rounds(self):
        try:
            return int(input("Quelle est le nombre de tours: "))
        except ValueError:
            print("Veuillez répondre par un chiffre correspondant à votre choix.")

    def get_time_control(self):
        """Permet de récupérer le type de contrôle de temps"""
        time_control = input("Quelle est le type de contrôle de temps: \n"
                             "1. Bullet / 2. Blitz / 3. Coup rapide\n"
                             "--> ")
        try:
            time_control_int = int(time_control)
            if time_control_int == 1:
                return "Bullet"
            elif time_control == 2:
                return "Blitz"
            elif time_control_int == 3:
                return "Coup rapide"
        except ValueError:
            print("Veuillez répondre par un chiffre correspondant à votre choix.")

    def add_player(self):
        """Vue pour l'ajout d'un joueur'"""
        for _ in range(int(self.controller.tournament.number_players)):
            lastname = input("Ajouter le nom de famille:")
            firstname = input("Ajouter le prénom: ")
            birthday = self.get_birthday()
            gender = self.get_gender()
            ranking = input("Ajouter le classement : 00")
            self.controller.add_player(lastname=lastname, firstname=firstname, birthday=birthday, gender=gender,
                                       ranking=ranking)

    def get_birthday(self):
        """Permet de demander la date de naissance et de vérifier son format"""
        date_format = "%d-%m-%Y"
        birthday = input("Ajouter la date de naissance: jj-mm-aaaa")
        try:
            valid_date = datetime.datetime.strptime(birthday, date_format)
            return birthday
        except ValueError:
            print("Date non valide! ", birthday)
            self.get_birthday()

    def get_gender(self):
        """Permet de demander le sexe"""
        get_gender = input("Quelle est le sexe?\n" "1. Féminin / 2. Masculin \n")
        try:
            get_gender_int = int(get_gender)
            if get_gender_int == 1:
                return "Féminin"
            elif get_gender_int == 2:
                return "Masculin"
        except ValueError:
            print("Veuillez répondre par un chiffre correspondant à votre choix.")
            self.get_gender()

    def menu_tournament(self):
        """Menu du tournoi"""
        while True:
            choice = input("\n\n 1. Lancer le 1er tour \n"
                           " 2. Lancer le tour suivant \n"
                           " 3. Entrer les résultats des matchs\n"
                           " 4. Finir le tour\n"
                           " 5. Afficher le classement\n"
                           " 6. Exit \n"
                           "--> ")
            try:
                choice_int = int(choice)
                if choice_int == 1:
                    self.controller.run_first_round()
                elif choice_int == 2:
                    self.controller.run_next_round()
                elif choice_int == 3:
                    self.controller.run_menu_result()
                elif choice_int == 4:
                    self.controller.end_round()
                elif choice_int == 5:
                    self.screen_ranking()
            except ValueError:
                print("Veuillez répondre par un chiffre correspondant à votre choix.")

    def screen_matchs(self, matchs):
        print("\nLes matchs pour ce tour sont : ")

        for match in matchs:
            print(f"Mme/M {match[0]['lastname']} vs Mme/M {match[1]['lastname']}", end="\n")

    def get_result(self, matchs):
        print(" Veuillez choisir le match afin de rentrer ses résultats")
        for match in matchs:
            print(
                f"{matchs.index(match) + 1}. Mme/M {match[0]['lastname']} VS Mme/M {match[1]['lastname']}")
        print("0. Précédent")
        return input("\nVeuillez entrez votre choix : \n")

    def enter_result(self, player_1, player_2):
        print("Quelle est le résultat de la partie ? \n"
              f"Si M/Mme {player_1} a gagné(e), tapé 1\n"
              f"Si M/Mme {player_2} a gagné(e), tapé 2\n"
              f"Si match nul, tapé 3")
        return input("Match result : Veuillez indiquer votre choix : ")

    def screen_ranking(self):
        players = self.controller.sort_list_ranking_and_score()  # est-ce que je dois créer une fonction ?
        for player in players:
            print(f"Nom de famille : {player['lastname']}, classé: {player['ranking']} "
                  f"avec un score de : {player['score']} ")

    def menu_get_report(self):
        print("Affichage des rapports\n")
        while True:
            print(
                "1 - Rapport de tous les acteurs \n"
                "2 - Liste de tous les joueurs du tournoi\n"
                "3 - Liste de tous les tournois\n"
                "4 - Liste de tous les tours d'un tournoi"
                "5 - Liste de tous les matchs d'un tournoi")

            choice = input("\nVeuillez entrez votre choix : \n")
            try:
                choice_int = int(choice)

            except ValueError:
                print("Veuillez répondre par un chiffre correspondant à votre choix.")
                self.main_menu()

    def screen_all_rounds(self):
        for round in self.controller.tournament.round_instance:
            print(round)
