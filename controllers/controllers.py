class Controller:
    def __init__(self, match, player, round, tournament, view, view_tournament, view_admin, view_player):

        # models
        self.match = match
        self.player = player
        self.round = round
        self.tournament = tournament

        # view
        self.view = view
        self.view_tournament = view_tournament
        self.view_admin = view_admin
        self.view_player = view_player

    def run_app(self):
        answer = self.view.main_menu()
        try:
            int(answer)
            if answer == 1:
                answer = self.view.manager_menu()
                try:
                    answer_int = int(answer)
                    if answer_int == 1:
                        self.create_tournament()
                    elif answer_int == 2:
                        print("ok")
                        self.add_player()
                except ValueError:
                    print("Veuillez mettre un chiffre")
                    self.view.manager_menu()

            elif answer == 2:
                self.view_admin.menu_admin()

        except ValueError:
            print("Veuillez répondre par des chiffres\n")
            self.run_app()

    def create_tournament(self):

        while True:
            answer_tournament = self.view_tournament.tournament_display()
            answer_tournament_int = int(answer_tournament)
            if answer_tournament_int == 1:
                name, answer = self.view_tournament.get_name_tournament()
                self.tournament.name = self.sub_menu_tournament(name, answer)
            elif answer_tournament_int == 2:
                name, answer = self.view_tournament.get_location_tournament()
                self.tournament.location = self.sub_menu_tournament(name, answer)
            elif answer_tournament_int == 3:
                name, answer = self.view_tournament.get_number_round()
                self.tournament.number_rounds = self.sub_menu_tournament(name, answer)
            elif answer_tournament_int == 4:
                name, answer = self.view_tournament.get_number_players()
                self.tournament.number_players = int(self.sub_menu_tournament(name, answer))
            elif answer_tournament_int == 5:
                answer = self.view_tournament.get_time_control()
                try:
                    answer_int = int(answer)
                    if answer_int == 1:
                        self.tournament.time_control = "Bullet"
                        print(f"Le type de contrôle  est{self.tournament.time_control}")
                    elif answer_int == 2:
                        self.tournament.time_control = "Blitz"
                        print(f"Le type de contrôle  est{self.tournament.time_control}")
                    elif answer_int == 3:
                        self.tournament.time_control = "Coup rapide"
                        print(f"Le type de contrôle  est{self.tournament.time_control}")
                except ValueError:
                    print("Veuillez répondre par un chiffre")
            elif answer_tournament_int == 6:
                name, answer = self.view_tournament.get_description()
                self.tournament.description = self.sub_menu_tournament(name, answer)
            elif answer_tournament_int == 7:
                self.run_app()

    def sub_menu_tournament(self, name, answer):
        try:
            answer_int = int(answer)
            if answer_int == 1:
                return name
            elif answer_int == 2:
                self.create_tournament()
        except ValueError:
            print("Veuillez répondre par des chiffres\n")
            self.sub_menu_tournament(name, answer)

    def add_player(self):
        for _ in range(self.tournament.number_players):
            print("\nAjouter joueur\n")
            answer_menu_player = self.view_player.menu_player()
            answer_menu_player_int = int(answer_menu_player)
            if answer_menu_player_int == 1:
                name, answer = self.view_tournament.get_name_tournament()
                self.player.lastname = self.view_player.get_lastname(name, answer)
            elif answer_menu_player_int == 2:
                name, answer = self.view_player.get_first_name()
                self.player.firstname = self.sub_menu_tournament(name, answer)
            elif answer_menu_player_int == 3:
                name, answer = self.view_player.get_birthday()
                self.player.birthday = self.sub_menu_tournament(name, answer)
            elif answer_menu_player_int == 4:
                answer = self.view_player.get_gender()
                try:
                    answer_int = int(answer)
                    if answer_int == 1:
                        self.player.gender = "Féminin"
                        print(f"Le type de contrôle  est {self.player.gender}")
                    elif answer_int == 2:
                        self.tournament.time_control = "Masculin"
                        print(f"Le sexe du joueur  est {self.player.gender}")
                except ValueError:
                    print("Veuillez répondre par un chiffre")
            elif answer_menu_player_int == 6:
                self.run_app()

"""
    def sort_list_ranking_and_score(self):
        self.players = sorted(self.players, key=lambda players: players['Classement'], reverse=False)
        self.players = sorted(self.players, key=lambda players: players['Score'], reverse=True)
        return self.players

    def matchs_round_1(self):
        # création des listes niveaux haut et bas
        self.sort_list_ranking_and_score()
        half = len(self.players) // 2
        lower_list = self.players[:half]
        upper_list = self.players[half:]
        for i in range(len(lower_list)):
            match = [upper_list[i - 1], lower_list[i - 1]]
            self.matchs.append(match)
        print(f"matchs_list ={self.matchs}", end="\n")

    def matchs_next_round(self):
        matchs_sort = []
        next_matchs = []
        self.sort_list_ranking_and_score()
        print(f"classé par score{self.players}\n", end="")
        for i in range(0, len(self.players), 2):
            new_match = [self.players[i], self.players[i + 1]]
            new_match = sorted(new_match, key=lambda player_list: player_list['Nom de famille'])
            print(f"new match 1 : {new_match}")
            # print(self.matchs_list)
            for player in new_match:
                player = player.pop('Score')
            for match in self.matchs:
                old_match = sorted(match, key=lambda player_list: player_list['Nom de famille'])
                print("old_match = " + old_match)
                matchs_sort.append(old_match)
            print(new_match)
            print(f"view match{matchs_sort}")
            if str(new_match) in matchs_sort:
                print("match existe déjà")
                new_match = [self.players[i], self.players[i + 2]]
                #  print(f"new match 1.2 : {new_match}")
            next_matchs.append(new_match)
        self.matchs = []
        self.matchs = next_matchs
        # Créer une liste avec tous les matchs possibles
        # Créer les premières rencontres
        # Supprimer les rencontres de la liste
        # Prendre le meilleur de la liste et le second
        # vérifier si le match n'a pas déjà eu lieu
        # Supprimer les joueurs
        # Re

    def launch_round(self):
        self.first_player = None
        self.second_player = None
        self.round = Round(name="Round 1")
        for m in self.matchs:
            self.first_player = m[0]['Nom de famille']
            self.second_player = m[1]['Nom de famille']
            print(self.first_player, self.second_player, end="\n")

    def enter_result(self, answer_int: int = None, first_player: str = None, second_player: str = None):

        if answer_int == 1:
            player_1 = [first_player, 1]
            player_2 = [second_player, 0]
            self.get_match_result(player_1=player_1,player_2=player_2)
            self.add_score(player_1=player_1, player_2=player_2)
        elif answer_int == 2:
            player_1 = [first_player, 0]
            player_2 = [second_player, 1]
            self.get_match_result(player_1=player_1,player_2=player_2)
            self.add_score(player_1=player_1, player_2=player_2)
        elif answer_int == 3:
            player_1 = [first_player, 0.5]
            player_2 = [second_player, 0.5]
            self.get_match_result(player_1=player_1,player_2=player_2)
            self.add_score(player_1=player_1, player_2=player_2)

    def get_match_result(self, player_1: list, player_2: list):
        self.match_result = (player_1, player_2)
        self.match_result = tuple(self.match_result)
        self.match = Match(match_result=self.match_result,
                           player_1=player_1,
                           player_2=player_2,
                           winner="aucun")

    def add_score(self, player_1: list = None, player_2: list = None):  # sourcery skip: hoist-statement-from-loop
        for p in self.players:
            if p["Nom de famille"] == player_1[0]:
                p["Score"] += player_1[1]
            if p["Nom de famille"] == player_2[0]:
                p["Score"] += player_2[1]



    def possible_player_pairs(self, array):
        results = []
        for i in range(0, len(array) - 1):
            for j in range(i + 1, len(array)):
                results.append(array[i] + array[j])

        return results"""
