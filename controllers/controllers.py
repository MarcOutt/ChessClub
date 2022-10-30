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

        self.number_round = 0

    def run_app(self):
        while True:
            answer = self.view.main_menu()
            try:
                int(answer)
                if answer == 1:
                    self.run_manager_menu()

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
            elif answer_int == 5:
                print(self.round.matchs)
                for i in self.round.matchs:
                    print(i)

        except TypeError:
            print("Veuillez répondre par des chiffres")
            self.view.manager_menu()

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
                self.tournament.number_rounds = int(self.sub_menu_tournament(name, answer))
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
                print(self.tournament)
            elif answer_tournament_int == 8:
                self.run_manager_menu()

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
            var = True
            while var:
                print("\nAjouter joueur\n")
                answer_menu_player = self.view_player.menu_player()
                answer_menu_player_int = int(answer_menu_player)
                if answer_menu_player_int == 1:
                    name, answer = self.view_player.get_lastname()
                    self.player.lastname = self.sub_menu_tournament(name, answer)
                elif answer_menu_player_int == 2:
                    name, answer = self.view_player.get_firstname()
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
                elif answer_menu_player_int == 5:
                    name, answer = self.view_player.get_ranking()
                    self.player.ranking = self.sub_menu_tournament(name, answer)
                elif answer_menu_player_int == 6:
                    print(self.player)
                elif answer_menu_player_int == 7:
                    var = False
            self.tournament.players.append(self.player)
        self.run_manager_menu()

    def run_first_round(self):
        answer = self.view.first_round_view()
        if answer == 1:
            self.launch_first_round()
        elif answer == 2:
            now = datetime.now()
            self.round.name = "Round 1"
            self.view_tournament.ending_date = now.strftime("%d %b %Y")
            self.view_tournament.ending_date = now.strftime("%Hh%Mm%Ss")
        elif answer == 3:
            print(self.round)
        elif answer == 4:
            self.view.manager_menu()
        self.run_first_round()

    def sort_list_ranking_and_score(self):
        self.tournament.players = sorted(self.tournament.players, key=lambda players: players['Classement'], reverse=False)
        self.tournament.players = sorted(self.tournament.players, key=lambda players: players['Score'], reverse=True)

    def launch_first_round(self):  # sourcery skip: extract-method
        self.number_round += 1
        if self.number_round == 1:
            # création des listes niveaux haut et bas
            self.sort_list_ranking_and_score()
            half = len(self.tournament.players) // 2
            lower_list = self.tournament.players[:half]
            upper_list = self.tournament.players[half:]
            for i in range(len(lower_list)):
                match = [upper_list[i - 1], lower_list[i - 1]]
                self.round.matchs.append(match)
            print("Les matchs pour ce tour sont : ")  # Est-ce que je dois le mettre dans la vue
            for match in self.round.matchs:
                print(f"Mme/M {match[0]['Nom de famille']} vs Mme/M {match[1]['Nom de famille']}", end="\n")
        else:
            print("Le premier tour a déjà été effectué! \n"
                  "Veuillez lancer le tour suivant.")
            self.number_round += 1
        self.run_first_round()

    def matchs_next_round(self):
        matchs_sort = []
        next_matchs = []
        self.sort_list_ranking_and_score()
        print(f"classé par score{self.tournament.players}\n", end="")
        for i in range(0, len(self.tournament.players), 2):
            new_match = [self.tournament.players[i], self.tournament.players[i + 1]]
            new_match = sorted(new_match, key=lambda player_list: player_list['Nom de famille'])
            print(f"new match 1 : {new_match}")
            # print(self.matchs_list)
            for player in new_match:
                player = player.pop('Score')
            for match in self.round.matchs:
                old_match = sorted(match, key=lambda player_list: player_list['Nom de famille'])
                print(f"old_match = {old_match}")
                matchs_sort.append(old_match)
            print(new_match)
            print(f"view match{matchs_sort}")
            if str(new_match) in matchs_sort:
                print("match existe déjà")
                new_match = [self.tournament.players[i], self.tournament.players[i + 2]]
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

    def enter_result(self):
        answer_int = 1
        if answer_int == 1:
            self.result(1, 0)
        elif answer_int == 2:
            self.result(0, 1)
        elif answer_int == 3:
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



    def possible_player_pairs(self, array):
        results = []
        for i in range(0, len(array) - 1):
            for j in range(i + 1, len(array)):
                results.append(array[i] + array[j])
        return results
