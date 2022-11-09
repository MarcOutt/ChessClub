from datetime import datetime

import views
from models.tournament import Tournament
from models.round import Round
from models.match import Match
from models.player import Player


class Controller:
    def __init__(self):
        # Models
        self.tournament = Tournament()
        # Views
        self.view = None

        self.counter_round = 0
        self.matchs = []
        self.round = []

    def run(self):
        """Lance l'application"""
        print("Start App")  # A supprimer lors de la finalisation de l'app
        self.view = views.MainView(self)
        self.view.screen_tournament()
        self.view.menu_tournament()

    def add_tournament(self, name: str, location: str, number_rounds: int, number_players: int, time_control: str,
                       description: str):
        """Permet de créer un tournoi"""
        self.tournament.name = name
        self.tournament.location = location
        self.tournament.number_rounds = number_rounds
        self.tournament.number_players = number_players
        self.tournament.time_control = time_control
        self.tournament.description = description

    def add_player(self, lastname: str, firstname: str, birthday: str, gender: str, ranking: int):
        player = Player(lastname=lastname, firstname=firstname, birthday=birthday, gender=gender, ranking=ranking)
        self.tournament.players.append(player)
        print(self.tournament.players)

    def sort_list_ranking_and_score(self):
        self.tournament.players = sorted(self.tournament.players, key=lambda player: player['ranking'], reverse=False)
        self.tournament.players = sorted(self.tournament.players, key=lambda player: player['score'], reverse=True)
        return self.tournament.players

    def run_first_round(self):
        self.counter_round += 1
        self.matchs = self.launch_first_round()
        name = f"{self.counter_round}"
        self.round = Round(name=name, matchs=self.matchs)
        self.tournament.round_instance_list(round)
        self.view.screen_matchs(self.matchs)

    def launch_first_round(self):  # sourcery skip: extract-method
        if self.counter_round == 1:
            # création des listes niveaux haut et bas
            self.sort_list_ranking_and_score()
            half = len(self.tournament.players) // 2
            lower_list = self.tournament.players[:half]
            upper_list = self.tournament.players[half:]
            matchs = []
            for i in range(len(lower_list)):
                match = [upper_list[i], lower_list[i]]
                matchs.append(match)
            return matchs
        else:
            print("Le premier tour a déjà été effectué! \n"
                  "Veuillez lancer le tour suivant.")
            self.counter_round -= 1
        self.run_first_round()

    def run_next_round(self):
        players = self.tournament.players[:]
        self.matchs = self.launch_matchs(players)
        name = f"Round {self.counter_round}"
        self.round = Round(name=name, matchs=self.matchs)
        self.tournament.round_instance_list(round)
        self.view.screen_matchs(self.matchs)

    def launch_matchs(self, players, matchs=None):
        # sourcery skip: extract-duplicate-method
        if matchs is None:
            matchs = []
        self.counter_round += 1
        if self.counter_round > self.tournament.number_rounds:
            print("Le tournoi est fini")
        elif self.counter_round <= 1:
            print("Veuillez lancer le 1er round")
            self.view.menu_tournament()
        else:
            while players:
                match = [players[0], players[1]]
                if match not in self.tournament.round_instance:
                    matchs.append(match)
                    players.remove(players[0])
                    players.remove(players[0])
                    self.launch_matchs(players, matchs)
                else:
                    match = [players[0], players[2]]
                    if match not in self.tournament.round_instance:
                        matchs.append(match)
                        players.remove(players[0])
                        players.remove(players[1])
                        self.launch_matchs(players, matchs)
                    if self.counter_round == self.tournament.number_rounds:
                        print("Le tournoi est fini")
            return matchs

    def end_round(self):
        # protégé le end-round avec une variable pour dire que le round est en cours ou pas
        now = datetime.now()
        self.round.ending_date = now.strftime("%d %b %Y")
        self.round.ending_time = now.strftime("%Hh%Mm%Ss")
        self.tournament.round_instance_list(self.round)
        print(self.round)

    def run_menu_result(self):  # sourcery skip: extract-method
        choice = self.view.get_result(self.matchs)
        try:
            choice_int = int(choice)
            if choice_int in range(1, len(self.matchs)+1):
                player_1 = self.matchs[choice_int - 1][0]["lastname"]
                player_2 = self.matchs[choice_int - 1][1]["lastname"]
                choice = self.view.enter_result(player_1=player_1, player_2=player_2)
                score_player_1, score_player_2 = self.enter_result(choice=choice)
                player_1_with_score, player_2_with_score = self.result(player_1=player_1, player_2=player_2,
                                                                       score_player_1=score_player_1,
                                                                       score_player_2=score_player_2)
                match_result = self.get_match_result(player_1=player_1_with_score, player_2=player_2_with_score)
                winner = self.add_score(player_1=player_1_with_score, player_2=player_2_with_score)
                match = Match(player_1=player_1, player_2=player_2, match_result=match_result, winner=winner)
            elif choice_int == 0:
                self.view.menu_tournament()
            self.run_menu_result()
        except ValueError:
            print("Veuillez répondre par un chiffre correspondant à votre choix.")
            self.run_menu_result()

    def enter_result(self, choice: int):
        # sourcery skip: remove-unnecessary-cast
        try:
            score_player_1 = 0
            score_player_2 = 0
            if int(choice) == 1:
                score_player_1 = 1
                score_player_2 = 0
            elif int(choice) == 2:
                score_player_1 = 0
                score_player_2 = 1
            elif int(choice) == 3:
                score_player_1 = 0.5
                score_player_2 = 0.5
            return score_player_1, score_player_2
        except ValueError:
            print("Veuillez répondre par un chiffre correspondant à votre choix.")
            self.run_menu_result()

    def result(self, player_1: str, player_2: str, score_player_1: float, score_player_2: float):
        player_1 = [player_1, score_player_1]
        player_2 = [player_2, score_player_2]
        return player_1, player_2

    def get_match_result(self, player_1: list, player_2: list):
        match_result = (player_1, player_2)
        match_result = tuple(match_result)
        return match_result

    def add_score(self, player_1, player_2):
        # sourcery skip: extract-duplicate-method, inline-immediately-returned-variable
        winner = ""
        print(self.tournament.players)
        for player in self.tournament.players:
            print(player)
            print(player["lastname"], player_1[0])
            if player["lastname"] == player_1[0]:
                player["score"] += player_1[1]
                print(player["score"], player_1[1])
                winner = player_1[0]
            if player["lastname"] == player_2[0]:
                player["score"] += player_2[1]
                winner = player_2[0]
        print("score ajouté:", self.tournament.players)
        return winner



    def get_report(self, choice):
        if choice == 1:
            pass
        elif choice == 2:
            self.view.screen_ranking()
        elif choice == 3:
            self.view.screen_all_rounds()
