import datetime


class MainView:

    def __init__(self, controller):
        self.controller = controller
        self.main_menu()

    def main_menu(self):
        """Affiche le menu principal"""

        print("\nBIENVENUE DANS LE GESTIONNAIRE DE TOURNOIS\n")

        while True:
            choice = input(" \n 1. Créer un tournoi \n"
                           " 2. Menu tournoi \n"
                           " 3. Charger un tournoi\n"
                           " 4. Editer un rapport\n"
                           " 5. Mettre à jour le classement\n"
                           " 6. Exit \n"
                           "--> ")
            try:
                choice_int = int(choice)
                if choice_int == 1:
                    self.create_tournament()
                    self.add_player()
                    break
                elif choice_int == 0:
                    self.add_player()
                    break
                elif choice_int == 2:
                    if self.controller.tournament.name is None:
                        print("Veuillez créer ou charger un tournoi pour accéder au menu tournoi.")
                    else:
                        break
                elif choice_int == 3:
                    self.screen_load_tournament()
                elif choice_int == 4:
                    self.menu_get_report()
                elif choice_int == 6:
                    self.main_menu()
            except ValueError:
                print("Veuillez répondre par un chiffre correspondant à votre choix.")

    @staticmethod
    def screen_tournament():
        """Affiche les informations du tournoi qui vient d'être créé"""
        print("Félicitation, vous avez créer votre un Tournoi")

    def create_tournament(self):
        """ Vue pour la création du tournoi"""
        name = input("Nom du tournoi: ").capitalize()
        location = input("Lieu du tournoi: ").capitalize()
        number_rounds = self.get_number_rounds()
        number_players = self.get_number_players()
        time_control = self.get_time_control()
        description = input("Veuillez ajouter la description du tournoi: ")
        self.controller.add_tournament(name=name, location=location, number_rounds=number_rounds,
                                       number_players=number_players, time_control=time_control,
                                       description=description)

    @staticmethod
    def get_number_players():
        """Récupère le nombre de joueurs"""
        try:
            return int(input("Quelle est le nombre de joueurs: "))
        except ValueError:
            print("Veuillez répondre par un chiffre correspondant à votre choix.")

    @staticmethod
    def get_number_rounds():
        """Récupère le nombre de tours"""
        try:
            return int(input("Quelle est le nombre de tours: "))
        except ValueError:
            print("Veuillez répondre par un chiffre correspondant à votre choix.")

    @staticmethod
    def get_time_control():
        """Récupère le type de contrôle de temps du tournoi"""
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
        for i in range(int(self.controller.tournament.number_players)):
            print(f"\nAjout du joueur {i + 1} sur {int(self.controller.tournament.number_players)}")
            lastname = input("Ajouter le nom de famille: ").capitalize()
            firstname = input("Ajouter le prénom: ").capitalize()
            birthday = self.get_birthday()
            gender = self.get_gender()
            ranking = self.get_ranking()
            self.controller.add_player(lastname=lastname, firstname=firstname, birthday=birthday, gender=gender,
                                       ranking=ranking)

    def get_birthday(self):
        """Demande la date de naissance du joueur et vérifie son format"""
        date_format = "%d-%m-%Y"
        birthday = input("Ajouter la date de naissance: (jj-mm-aaaa) ")
        try:
            valid_date = datetime.datetime.strptime(birthday, date_format)
            return birthday
        except ValueError:
            print("Date non valide! ", birthday)
            self.get_birthday()

    def get_gender(self):
        """Demande le sexe du joueur"""
        get_gender = input("Quelle est le sexe?\n" "1. Féminin / 2. Masculin \n")
        try:
            get_gender_int = int(get_gender)
            if get_gender_int == 1:
                return "Feminin"
            elif get_gender_int == 2:
                return "Masculin"
        except ValueError:
            print("Veuillez répondre par un chiffre correspondant à votre choix.")
            self.get_gender()

    def get_ranking(self):
        """Récupère le classement du joueur"""
        ranking = input("Ajouter le classement : (00) ")
        if len(ranking) == 2 and ranking.isdigit():
            return int(ranking)
        print("Veuillez répondre par 2 chiffres, exemple: 02")
        self.get_ranking()

    def menu_tournament(self):
        """Menu du tournoi"""
        while True:

            choice = input("\n\n    Menu tournoi\n"
                           " 1. Lancer le tour \n"
                           " 2. Finir le tour\n"
                           " 3. Entrer les résultats des matchs\n"
                           " 4. Afficher le classement\n"
                           " 5. Sauvegarder le tournoi\n"
                           " 6. Retour \n"
                           "--> ")
            try:
                choice_int = int(choice)
                if choice_int == 1:
                    self.controller.run_round()
                elif choice_int == 2:
                    self.controller.end_round()
                elif choice_int == 3:
                    self.controller.run_menu_result()
                elif choice_int == 4:
                    self.screen_ranking()
                elif choice_int == 5:
                    self.controller.save_tournament()
                    print("Le tournoi a été sauvegardé")
            except ValueError:
                print("Veuillez répondre par un chiffre correspondant à votre choix.")

    def screen_matchs(self, matchs):
        """Affiche les matchs"""
        print(f"\nTour {self.controller.counter_round}\n"
              "\nLes matchs pour ce tour sont : ")
        for match in matchs:
            print(f"Mme/M {match[0]['lastname']} vs Mme/M {match[1]['lastname']}", end="\n")

    @staticmethod
    def enter_result(player_1, player_2):
        """Vue pour dire quelle est le résultat"""
        print("\n   Entrer les résultats:\n"
              "Quelle est le résultat de la partie ? \n"
              f"Si M/Mme {player_1} a gagné(e), tapé 1\n"
              f"Si M/Mme {player_2} a gagné(e), tapé 2\n"
              f"Si match nul, tapé 3")
        return input("Match result : Veuillez indiquer votre choix : ")

    def screen_ranking(self):
        """Affiche le classement"""
        players = self.controller.sort_list_ranking_and_score()
        for player in players:
            print(f"Nom de famille : {player['lastname']}, classé: {player['ranking']} "
                  f"avec un score de : {player['score']} ")

    def menu_get_report(self):
        """Affiche le menu des rapports"""
        print("Affichage des rapports\n")
        while True:
            print(
                "1 - Afficher tous les joueurs de tous les tournois \n"
                "2 - Choisir le tournoi concerné\n")
            choice = input("\nVeuillez entrez votre choix : \n")
            try:
                choice_int = int(choice)
                if choice_int == 1:
                    self.get_actor_report()
                elif choice_int == 2:
                    self.screen_all_tournament()

            except ValueError:
                print("Veuillez répondre par un chiffre correspondant à votre choix.")
                self.main_menu()

    def get_actor_report(self):
        """Récupère tous les joueurs des tournois"""
        for player in self.controller.players_table:
            print(f"nom : {player['lastname']}\n"
                  f"Prénom: {player['firstname']}\n"
                  f"Date de naissance: {player['birthday']}\n"
                  f"Sexe : {player['gender']}\n"
                  f"Classement: {player['ranking']}\n")

    def screen_all_tournament(self):
        """Affiche la liste des tournois dans la database"""
        print("Faites votre choix:")
        for tournament_number, tournament in enumerate(self.controller.save_tournament_table, start=1):
            print(f"{tournament_number} - Nom du tournoi {tournament['name']}, lieu : {tournament['location']}, "
                  f"numéro d'identification : {tournament.doc_id}")
        choice = input("--> ")
        try:
            choice_int = int(choice)
            self.screen_edit_report_tournament(self.controller.save_tournament_table.get(doc_id=choice_int))
        except ValueError:
            print("Veuillez répondre par un chiffre correspondant à votre choix.")

    @staticmethod
    def screen_edit_report_tournament(tournament_database):
        """Affiche le menu des rapports pour le tournoi sélectionné"""
        print("\n1 - Liste de tous les joueurs du tournoi\n"
              "2 - Liste de tous les tours d'un tournoi\n"
              "3 - Liste de tous les matchs d'un tournoi")
        choice = input("\nVeuillez entrez votre choix : \n")
        try:
            choice_int = int(choice)
            if choice_int == 1:
                players = tournament_database['players']
                for player in players:
                    print(f"nom : {player['lastname']}\n"
                          f"Prénom: {player['firstname']}\n"
                          f"Date de naissance: {player['birthday']}\n"
                          f"Sexe : {player['gender']}\n"
                          f"Classement: {player['ranking']}\n")
            elif choice_int == 2:
                rounds_instance = tournament_database['round_instance']
                for round_instance in rounds_instance:
                    print(round_instance)
            elif choice_int == 3:
                matchs = tournament_database['matchs']
                for match in matchs:
                    print(match)
        except ValueError:
            print("Veuillez répondre par un chiffre correspondant à votre choix.")

    def screen_load_tournament(self):
        """Affiche le menu pour charger un tournoi non fini"""
        print("Veuillez choisir le tournoi à charger:")
        for tournament_number, tournament in enumerate(self.controller.save_tournament_table, start=1):
            print(f"{tournament_number} - Nom du tournoi {tournament['name']}, lieu : {tournament['location']}, "
                  f"numéro d'identification : {tournament.doc_id}")
        choice = input("--> ")
        try:
            choice_int = int(choice)
            tournament_database = self.controller.save_tournament_table.get(doc_id=choice_int)

        except ValueError:
            print("Veuillez répondre par un chiffre correspondant à votre choix.")
