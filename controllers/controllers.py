from datetime import datetime


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

        self.counter_round = 0

    def run_app(self):
        while True:
            answer = self.view.main_menu()
            try:
                int(answer)
                if int(answer) == 1:
                    self.run_manager_menu()
                elif int(answer) == 3:
                    exit()

            except ValueError:
                print("Veuillez mettre un chiffre")
                self.view.manager_menu()

    def run_manager_menu(self):
        answer = self.view.manager_menu()
        try:
            answer_int = int(answer)
            if answer_int == 1:
                self.create_tournament()
            elif answer_int == 2:
                self.add_player()
            elif answer_int == 3:
                self.run_first_round()
            elif answer_int == 4:
                self.run_next_round()
                players = self.tournament.players[:]
                self.launch_next_round(players)

            elif answer_int == 5:
                self.run_menu_result()
            elif answer_int == 6:
                self.sort_list_ranking_and_score()
                for players in self.tournament.players:
                    print(players)
            elif answer_int == 7:
                for player in self.tournament.players:
                    print(player)
            elif answer_int == 8:
                self.run_app()

        except ValueError:
            print("Veuillez répondre par des chiffres\n")
        self.run_manager_menu()

    def sub_menu(self, name, answer):
        try:
            answer_int = int(answer)
            if answer_int == 1:
                return name
            elif answer_int == 2:
                self.create_tournament()
        except ValueError:
            print("Veuillez répondre par des chiffres\n")
            self.sub_menu(name, answer)

    def create_tournament(self):
        while True:
            answer_tournament = self.view_tournament.tournament_display()
            try:
                answer_tournament_int = int(answer_tournament)
                if answer_tournament_int == 1:
                    name, answer = self.view_tournament.get_name_tournament()
                    self.tournament.name = self.sub_menu(name, answer)
                elif answer_tournament_int == 2:
                    name, answer = self.view_tournament.get_location_tournament()
                    self.tournament.location = self.sub_menu(name, answer)
                elif answer_tournament_int == 3:
                    self.get_number_round()
                elif answer_tournament_int == 4:
                    self.get_number_player()
                elif answer_tournament_int == 5:
                    self.get_time_control()
                elif answer_tournament_int == 6:
                    name, answer = self.view_tournament.get_description()
                    self.tournament.description = self.sub_menu(name, answer)
                elif answer_tournament_int == 7:
                    print(self.tournament)
                elif answer_tournament_int == 8:
                    self.run_manager_menu()
            except ValueError:
                print("Veuillez répondre par un chiffre")
                self.create_tournament()

    def get_number_round(self):
        name, answer = self.view_tournament.get_number_round()
        try:
            answer_int = int(answer)
            self.tournament.number_rounds = int(self.sub_menu(name, answer_int))
        except ValueError:
            print("Veuillez répondre par un chiffre")
            self.get_number_round()

    def get_number_player(self):
        name, answer = self.view_tournament.get_number_players()
        try:
            answer_int = int(answer)
            self.tournament.number_players = int(self.sub_menu(name, answer_int))
        except ValueError:
            print("Veuillez répondre par un chiffre")
            self.get_number_player()

    def get_time_control(self):
        answer = self.view_tournament.get_time_control()
        try:
            answer_int = int(answer)
            if answer_int == 1:
                self.tournament.time_control = "Bullet"
                print(f"Le type de contrôle est {self.tournament.time_control}")
            elif answer_int == 2:
                self.tournament.time_control = "Blitz"
                print(f"Le type de contrôle est {self.tournament.time_control}")
            elif answer_int == 3:
                self.tournament.time_control = "Coup rapide"
                print(f"Le type de contrôle est {self.tournament.time_control}")
        except ValueError:
            print("Veuillez répondre par un chiffre")
            self.get_time_control()

    def add_player(self):
        if len(self.tournament.players) < self.tournament.number_players:
            #  for _ in range(self.tournament.number_players):
            var = True
            while var:
                print("\nAjouter joueur\n")
                answer_menu_player = self.view_player.menu_player()
                try:
                    answer_menu_player_int = int(answer_menu_player)
                    if answer_menu_player_int == 1:
                        name, answer = self.view_player.get_lastname()
                        self.player.lastname = self.sub_menu(name, answer)
                    elif answer_menu_player_int == 2:
                        name, answer = self.view_player.get_firstname()
                        self.player.firstname = self.sub_menu(name, answer)
                    elif answer_menu_player_int == 3:
                        name, answer = self.view_player.get_birthday()
                        self.player.birthday = self.sub_menu(name, answer)
                    elif answer_menu_player_int == 4:
                        answer = self.view_player.get_gender()
                        try:
                            answer_int = int(answer)
                            if answer_int == 1:
                                self.player.gender = "Féminin"
                                print(f"Le sexe du joueur est {self.player.gender}")
                            elif answer_int == 2:
                                self.tournament.time_control = "Masculin"
                                print(f"Le sexe du joueur est {self.player.gender}")
                        except ValueError:
                            print("Veuillez répondre par un chiffre")
                    elif answer_menu_player_int == 5:
                        name, answer = self.view_player.get_ranking()
                        self.player.ranking = self.sub_menu(name, answer)
                    elif answer_menu_player_int == 6:
                        print(self.player)
                    elif answer_menu_player_int == 7:
                        self.tournament.players.append(self.player)
                        print(self.tournament.players)
                        self.add_player()
                    elif answer_menu_player_int == 8:
                        self.tournament.players.append(self.player)
                except ValueError:
                    print("Veuillez répondre par un chiffre")
                    self.add_player()

        else:
            print("Le tournoi est complet")
        self.run_manager_menu()

    def sort_list_ranking_and_score(self):
        self.tournament.players = sorted(self.tournament.players, key=lambda players: players['Classement'],
                                         reverse=False)
        self.tournament.players = sorted(self.tournament.players, key=lambda players: players['Score'], reverse=True)

    def run_first_round(self):
        answer = self.view.first_round_view()
        if answer == 1:
            self.launch_first_round()
        elif answer == 2:
            now = datetime.now()
            self.round.name = "Round 1"
            self.round.ending_date = now.strftime("%d %b %Y")
            self.round.ending_time = now.strftime("%Hh%Mm%Ss")
            self.tournament.round_instance_list(self.round)
        elif answer == 3:
            print(self.round)
        elif answer == 4:
            self.view.manager_menu()
        self.run_first_round()

    def launch_first_round(self):  # sourcery skip: extract-method
        self.counter_round += 1
        if self.counter_round == 1:
            # création des listes niveaux haut et bas
            self.sort_list_ranking_and_score()
            half = len(self.tournament.players) // 2
            lower_list = self.tournament.players[:half]
            upper_list = self.tournament.players[half:]
            for i in range(len(lower_list)):
                match = [upper_list[i], lower_list[i]]
                self.round.matchs.append(match)
            print("Les matchs pour ce tour sont : ")  # Est-ce que je dois le mettre dans la vue
            for match in self.round.matchs:
                print(f"Mme/M {match[0]['Nom de famille']} vs Mme/M {match[1]['Nom de famille']}", end="\n")
        else:
            print("Le premier tour a déjà été effectué! \n"
                  "Veuillez lancer le tour suivant.")
            self.counter_round -= 1
        self.run_first_round()

    def run_next_round(self):
        answer = self.view.next_round_view()
        if answer == 1:
            players = self.tournament.players[:]
            self.launch_next_round(players)
        elif answer == 2:
            now = datetime.now()
            self.round.name = f"Round {self.counter_round}"
            self.round.ending_date = now.strftime("%d %b %Y")
            self.round.ending_time = now.strftime("%Hh%Mm%Ss")
            self.tournament.round_instance_list(self.round)
        elif answer == 3:
            print(self.round)
        elif answer == 4:
            self.view.manager_menu()
        self.run_first_round()

    def launch_next_round(self, players):  # sourcery skip: extract-duplicate-method
        self.counter_round += 1
        if self.counter_round >= 2:
            try:
                match = [players[0], players[1]]
                print(self.round.matchs)
                if match not in self.round.matchs:
                    self.round.matchs.append(match)
                    players.remove(players[0])
                    players.remove(players[0])
                    self.launch_next_round(players)
                    print(f"match if {match}")
                else:
                    match = [players[0], players[2]]
                    if match not in self.round.matchs:
                        self.round.matchs.append(match)
                        players.remove(players[0])
                        players.remove(players[1])
                        self.launch_next_round(players)
                        print(f"match else{match}")
                if not players:
                    return
            except IndexError:
                print("Fini")
        else:
            print("Veuillez lancer le 1er round")

    def run_menu_result(self):
        answer = self.view.menu_result(self.round.matchs)
        if int(answer) in range(1, len(self.round.matchs)):
            first_player = self.round.matchs[int(answer) - 1][0]["Nom de famille"]
            second_player = self.round.matchs[int(answer) - 1][0]["Nom de famille"]
            answer = self.view.enter_result(first_player, second_player)
            self.enter_result(answer)
        elif int(answer) == 0:
            self.run_manager_menu()
        self.run_menu_result()

    def enter_result(self, answer):
        if int(answer) == 1:
            self.result(1, 0)
        elif int(answer) == 2:
            self.result(0, 1)
        elif int(answer) == 3:
            self.result(0.5, 0.5)

    def result(self, score_first_player, score_second_player):
        player_1 = [self.match.first_player, score_first_player]
        player_2 = [self.match.second_player, score_second_player]
        self.get_match_result(player_1=player_1, player_2=player_2)
        self.add_score()

    def get_match_result(self, player_1: list, player_2: list):
        self.match_result = (player_1, player_2)
        self.match_result = tuple(self.match_result)

    def add_score(self):
        for p in self.tournament.players:
            if p["Nom de famille"] == self.match.player_1[0]:
                p["Score"] += self.match.player_1[1]
            if p["Nom de famille"] == self.match.player_2[0]:
                p["Score"] += self.match.player_2[1]