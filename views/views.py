import datetime


class MainView:

    def __init__(self, controller):
        self.controller = controller

    def main_menu(self):
        """Affiche le menu principal"""

        print("\nBIENVENUE DANS LE GESTIONNAIRE DE TOURNOIS\n")

        while True:
            choice = input(" 1. Créer un tournoi \n"
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
                    print("Félicitation, vous avez créer votre un Tournoi")
                    self.menu_tournament()
                    break
                elif choice_int == 0:
                    self.add_player()
                    self.menu_tournament()
                    break
                elif choice_int == 2:
                    if self.controller.tournament.name is None:
                        print("Veuillez créer ou charger un tournoi pour accéder au menu tournoi.")
                    else:
                        break
                elif choice_int == 3:
                    self.screen_load_tournament()
                    self.menu_tournament()
                elif choice_int == 4:
                    self.menu_get_report()
                elif choice_int == 5:
                    self.edit_ranking()
                elif choice_int == 6:
                    exit()
            except ValueError:
                print("Veuillez répondre par un chiffre correspondant à votre choix.")

    # Partie création de tournoi
    def create_tournament(self):
        """ Vue pour la création du tournoi"""
        name = input("Nom du tournoi: ")
        location = self.get_location()
        number_rounds = self.get_number_rounds()
        number_players = self.get_number_players()
        time_control = self.get_time_control()
        description = input("Veuillez ajouter la description du tournoi: ")
        self.controller.add_tournament(name=name, location=location, number_rounds=number_rounds,
                                       number_players=number_players, time_control=time_control,
                                       description=description)

    def get_location(self):
        """Récupère le lieu du tournoi"""
        location = input("Lieu du tournoi: ")
        answer = location.isalpha()
        if answer:
            return location.capitalize()
        print("Veuillez répondre avec des lettres")
        self.get_location()

    def get_number_rounds(self):
        """Récupère le nombre de tours"""
        number_rounds = input("Quelle est le nombre de tours: ")
        try:
            return int(number_rounds)
        except ValueError:
            print("Veuillez répondre par un chiffre correspondant à votre choix.")
            self.get_number_rounds()

    def get_number_players(self):
        """Récupère le nombre de joueurs"""
        number_players = input("Quelle est le nombre de joueurs: ")
        try:
            return int(number_players)
        except ValueError:
            print("Veuillez répondre par un chiffre correspondant à votre choix.")
            self.get_number_players()

    def get_time_control(self):
        """Récupère le type de contrôle de temps du tournoi"""
        time_control = input("\nQuelle est le type de contrôle de temps: \n"
                             "1. Bullet / 2. Blitz / 3. Coup rapide\n"
                             "--> ")
        try:
            time_control_int = int(time_control)
            if time_control_int == 1:
                return "Bullet"
            elif time_control_int == 2:
                return "Blitz"
            elif time_control_int == 3:
                return "Coup rapide"
            self.get_time_control()
        except ValueError:
            print("Veuillez répondre par un chiffre correspondant à votre choix.")
            self.get_time_control()

    # Partie ajout des joueurs
    def add_player(self):
        """Vue pour l'ajout d'un joueur'"""
        for i in range(int(self.controller.tournament.number_players)):
            print(f"\nAjout du joueur {i + 1} sur {int(self.controller.tournament.number_players)}")
            lastname = self.get_lastname()
            firstname = self.get_firstname()
            birthday = self.get_birthday()
            gender = self.get_gender()
            ranking = self.get_ranking()
            self.controller.add_player(lastname=lastname, firstname=firstname, birthday=birthday, gender=gender,
                                       ranking=ranking)

    def get_lastname(self):
        """Récupère le nom de famille du joueur"""
        lastname = input("Ajouter le nom de famille: ")
        answer = lastname.isalpha()
        if answer:
            return lastname.capitalize()
        print("Veuillez répondre avec des lettres")
        self.get_lastname()

    def get_firstname(self):
        """Récupère le prénom du joueur"""
        firstname = input("Ajouter le prénom: ")
        answer = firstname.isalpha()
        if answer:
            return firstname.capitalize()
        print("Veuillez répondre avec des lettres")
        self.get_firstname()

    def get_birthday(self):
        """Demande la date de naissance du joueur et vérifie son format"""
        date_format = "%d-%m-%Y"
        birthday = input("Ajouter la date de naissance: (jj-mm-aaaa) ")
        try:
            valide_date = str(datetime.datetime.strptime(birthday, date_format))
            return valide_date[:9]
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
            print("Veuillez répondre par un chiffre correspondant à votre choix.")
            self.get_gender()
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

    # Partie navigation tournoi
    def menu_tournament(self):
        """Affiche le menu du tournoi"""
        while True:

            choice = input("\n\n    MENU TOURNOI\n"
                           " 1. Lancer le tour \n"
                           " 2. Finir le tour\n"
                           " 3. Entrer les résultats des matchs\n"
                           " 4. Afficher le classement\n"
                           " 5. Sauvegarder le tournoi\n"
                           " 0. Retour \n"
                           "--> ")
            try:
                choice_int = int(choice)
                if choice_int == 0:
                    self.main_menu()
                    print("Le tournoi a été sauvegardé")
                elif choice_int == 1:
                    if self.controller.tournament.check_result:
                        print("\nVeuillez rentrer les résultats avant de lancer le tour suivant")
                    else:
                        print(f"\nRound {self.controller.tournament.counter_round + 1}\n")
                        self.controller.run_round()
                        self.display_matchs()
                elif choice_int == 2:
                    if self.controller.tournament.check_result:
                        print("\nVeuillez rentrer les résultats avant de lancer le tour suivant")
                    else:
                        self.controller.end_round()
                elif choice_int == 3:
                    self.controller.run_menu_result()
                elif choice_int == 4:
                    self.screen_ranking()
                elif choice_int == 5:
                    self.controller.save_tournament()
                self.menu_tournament()
            except ValueError:
                print("Veuillez répondre par un chiffre correspondant à votre choix.")

    def display_matchs(self):
        """Affiche les matchs du tour"""
        for match in self.controller.matchs:
            print(f"Nom : {match[0]['lastname']}, prénom: {match[0]['firstname']} "
                  f"vs Nom : {match[1]['lastname']}, prénom: {match[1]['firstname']}")

    def enter_result(self, player_1, player_2):
        """Donne le résultat du match"""
        print("\n   Entrer les résultats:\n"
              "Quelle est le résultat de la partie ? \n"
              f"Si M/Mme {player_1} a gagné(e), tapé 1\n"
              f"Si M/Mme {player_2} a gagné(e), tapé 2\n"
              f"Si match nul, tapé 3")
        choice = input("Match result : Veuillez indiquer votre choix : ")
        try:
            return int(choice)
        except ValueError:
            print("Veuillez répondre par un chiffre correspondant à votre choix.")
            self.enter_result(player_1, player_2)

    def screen_end_round(self):
        """Affiche la fin du tour"""
        print(f"\n      LE TOUR EST FINI: \n\n"
              f"{self.controller.round}")

    def screen_ranking(self):
        """Affiche le classement"""
        players = self.controller.sort_list_ranking_and_score()
        for player in players:
            print(f"Nom de famille : {player['lastname']}, classé: {player['ranking']} "
                  f"avec un score de : {player['score']} ")

    # Partie charger un tournoi
    def screen_load_tournament(self):
        """Affiche le menu pour charger un tournoi non fini"""
        print("\n MENU CHARGEMENT DES TOURNOIS\n"
              "\nVeuillez choisir le tournoi à charger:")
        for tournament_number, tournament in enumerate(self.controller.save_tournament_table, start=1):
            print(f"{tournament_number}. Nom du tournoi: {tournament['name']} - lieu : {tournament['location']} - "
                  f"numéro d'identification : {tournament.doc_id}")
        choice = input("--> ")
        try:
            choice_int = int(choice)
            tournament_database = self.controller.save_tournament_table.get(doc_id=choice_int)
            self.controller.load_tournament(tournament_database)

        except ValueError:
            print("Veuillez répondre par un chiffre correspondant à votre choix.")

    def ending_tournament(self):
        print("\nFélicitation le tournoi est fini\n\nVeuillez trouver ci-dessous le classement final:")
        self.screen_ranking()

    # Partie afficher des rapports
    def menu_get_report(self):
        """Affiche le menu des rapports"""
        while True:
            print("\n       MENU RAPPORT\n"
                  "\n1. Afficher tous les joueurs de tous les tournois \n"
                  "2. Choisir le tournoi concerné\n"
                  "0. Retour")
            choice = input("\nVeuillez entrez votre choix : \n")
            try:
                choice_int = int(choice)
                if choice_int == 1:
                    self.get_actor_report()
                elif choice_int == 2:
                    self.screen_all_tournament()
                elif choice_int == 0:
                    self.main_menu()
                self.menu_get_report()
            except ValueError:
                print("Veuillez répondre par un chiffre correspondant à votre choix.")
                self.main_menu()

    def get_actor_report(self):
        """Récupère tous les joueurs des tournois"""
        choice = input("1. Afficher les joueurs par ordre alphabétique\n"
                       "2. Afficher les joueurs par classement\n"
                       "0. Retour\n"
                       "Faites votre choix:")
        try:
            choice_int = int(choice)
            if choice_int == 0:
                self.menu_get_report()
            elif choice_int == 1:
                players = self.controller.actor_report_by_name()
                self.screen_player(players)
            elif choice_int == 2:
                players = self.controller.actor_report_by_ranking()
                self.screen_player(players)
        except ValueError:
            print("Veuillez répondre par un chiffre correspondant à votre choix.")
            self.main_menu()

    @staticmethod
    def screen_player(players):
        """Affiche les informations des joueurs"""
        for player in players:
            print(f"Nom : {player['lastname']}; "
                  f"Prénom: {player['firstname']}; "
                  f"Date de naissance: {player['birthday']}; "
                  f"Sexe : {player['gender']}; "
                  f"Classement: {player['ranking']}")

    def screen_all_tournament(self):
        """Affiche la liste des tournois dans la database"""
        print("Faites votre choix:")
        for tournament_number, tournament in enumerate(self.controller.save_tournament_table, start=1):
            print(f"{tournament_number}. Nom du tournoi {tournament['name']}, lieu : {tournament['location']}, "
                  f"numéro d'identification : {tournament.doc_id}")
        print("0. Retour\n")
        choice = input("--> ")
        try:
            choice_int = int(choice)
            if choice_int == 0:
                self.main_menu()
            self.screen_edit_report_tournament(self.controller.save_tournament_table.get(doc_id=choice_int))
        except ValueError:
            print("Veuillez répondre par un chiffre correspondant à votre choix.")

    def screen_edit_report_tournament(self, tournament_database):
        """Affiche le menu des rapports pour le tournoi sélectionné"""
        print("\n1. Liste de tous les joueurs du tournoi\n"
              "2. Liste de tous les tours d'un tournoi\n"
              "3. Liste de tous les matchs d'un tournoi\n"
              "0. Retour")
        choice = input("\nVeuillez entrez votre choix : \n")
        try:
            choice_int = int(choice)
            if choice_int == 0:
                self.screen_all_tournament()
            elif choice_int == 1:
                players = tournament_database['players']
                self.screen_player(players)
            elif choice_int == 2:
                rounds_instance = tournament_database['rounds_instance']
                for round_instance in rounds_instance:
                    matchs = "".join(f"\nNom: {match[0]['lastname']}, prénom: {match[0]['firstname']},"
                                     f" classement: {match[0]['ranking']} VS Nom: {match[1]['lastname']}, "
                                     f"prénom: {match[1]['firstname']}, classement: {match[1]['ranking']}"
                                     for match in round_instance['matchs'])
                    print(f"{round_instance['name']}, début: {round_instance['starting_date']} "
                          f"{round_instance['starting_time']},"f"fin :{round_instance['ending_date']} "
                          f"{round_instance['ending_time']}.\nRencontres : {matchs} \n")
            elif choice_int == 3:
                matchs = tournament_database['matchs']
                for match in matchs:
                    print(f"Nom : {match['player_1']} vs {match['player_2']}, le gagnant du match est nom : "
                          f"{match['winner']}")
            self.screen_edit_report_tournament(tournament_database)

        except ValueError:
            print("Veuillez répondre par un chiffre correspondant à votre choix.")

    def edit_ranking(self):  # sourcery skip: use-named-expression
        """"Affiche les joueurs de tous les tournois pour modifier leur classement"""
        print("\n       MENU MODIFICATION CLASSEMENT JOUEURS\n")
        for player in self.controller.players_table:
            print(f" - ID: {player['id']} - nom: {player['lastname']} - prénom: {player['lastname']} - classement: "
                  f"{player['ranking']}")
        try:
            choice = int(input("  <--  0 - retour"
                               "\n\nVeuillez indiquer le numéro d'id du joueur afin de modifier son classement: "))
            if choice == 0:
                return self.main_menu()
            try:
                ranking = int(input("Quelle est son nouveau classement? "))
                choice_exist = self.controller.edit_ranking(choice, ranking)
                if choice_exist:
                    players = self.controller.actor_report_by_ranking()
                    self.screen_player(players)
                else:
                    print("Veuillez indiquer le numéro d'id du joueur afin de modifier son classement")

            except ValueError:
                print("Veuillez répondre par un chiffre correspondant à votre choix.")
            self.edit_ranking()
        except ValueError:
            print("Veuillez répondre par un chiffre correspondant à votre choix.")
            self.edit_ranking()
        self.main_menu()
