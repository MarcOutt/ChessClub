from datetime import datetime

from tinydb import TinyDB, where

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

        self.db = TinyDB('data.json', indent=4)
        self.save_tournament_table = self.db.table("tournament")
        self.players_table = self.db.table("players")

        self.counter_round = 0
        self.round_in_progress = False
        self.check_result = False
        self.matchs = []
        self.round = []

    def run(self):
        """Lance l'application"""

        self.view = views.MainView(self)
        self.view.screen_tournament()
        self.view.menu_tournament()

    def add_tournament(self, name: str, location: str, number_rounds: int, number_players: int, time_control: str,
                       description: str):
        """Crée un tournoi"""
        self.tournament.name = name
        self.tournament.location = location
        self.tournament.number_rounds = number_rounds
        self.tournament.number_players = number_players
        self.tournament.time_control = time_control
        self.tournament.description = description
        self.tournament.id = self.save_tournament_table.insert(self.tournament.serialized())
        self.save_tournament_table.update({'id': self.tournament.id}, doc_ids=[self.tournament.id])

    def add_player(self, lastname: str, firstname: str, birthday: str, gender: str, ranking: int):
        player = Player(lastname=lastname, firstname=firstname, birthday=birthday, gender=gender, ranking=ranking)
        """Ajoute le joueur dans le tournoi"""
        self.tournament.players.append(player.serialized())
        player.player_id = self.players_table.insert(player.serialized())
        print(player.player_id)
        self.players_table.update({'id': player.player_id}, doc_ids=[player.player_id])
        self.save_tournament_table.update(self.tournament.serialized(), doc_ids=[self.tournament.id])

    def sort_list_ranking_and_score(self):
        """Trie les joueurs en fonction de leur score et de leur classement"""
        self.tournament.players = sorted(self.tournament.players, key=lambda user: user['ranking'], reverse=False)
        self.tournament.players = sorted(self.tournament.players, key=lambda user: user['score'], reverse=True)
        return self.tournament.players

    def run_round(self):
        """Lance un tour"""
        if self.counter_round > self.tournament.number_rounds:
            print("\n\n      Le tournoi est fini")
        elif self.round_in_progress:
            print("Un tour est en cours")
            self.view.menu_tournament()
        elif not self.check_result:
            self.round_in_progress = True
            self.counter_round += 1
            if self.counter_round == 1:
                self.matchs = self.launch_first_matchs()
            else:
                players = self.tournament.players[:]
                self.matchs = self.launch_matchs(players)
            name = f"Round {self.counter_round}"
            self.round = Round(name=name, matchs=self.matchs)
            self.view.screen_matchs()
            self.tournament.round_instance_list(self.round.serialized())
        else:
            print("Veuillez rentrer les résultats avant de lancer le tour suivant")

    def launch_first_matchs(self):  # sourcery skip: extract-method
        """Lance les matchs du 1er tour"""
        if self.counter_round > self.tournament.number_rounds:
            print("\n\n      Le tournoi est fini")
        elif self.counter_round == 1:
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
        self.view.menu_tournament()

    def launch_matchs(self, players, matchs=None):
        """Lance les matchs"""
        # sourcery skip: extract-duplicate-method
        if matchs is None:
            matchs = []
        if self.counter_round <= 1:
            print("Veuillez lancer le 1er round")
            self.view.menu_tournament()
        else:
            while players:
                match = [players[0], players[1]]
                if match not in self.tournament.rounds_instance:
                    matchs.append(match)
                    players.remove(players[0])
                    players.remove(players[0])
                    self.launch_matchs(players, matchs)
                else:
                    match = [players[0], players[2]]
                    if match not in self.tournament.rounds_instance:
                        matchs.append(match)
                        players.remove(players[0])
                        players.remove(players[1])
                        self.launch_matchs(players, matchs)
            return matchs

    def end_round(self):
        """Fini le tour"""
        if self.round_in_progress:
            now = datetime.now()
            self.round.ending_date = now.strftime("%d %b %Y")
            self.round.ending_time = now.strftime("%Hh%Mm%Ss")
            self.tournament.round_instance_list(self.round.serialized())
            self.check_result = True
            self.round_in_progress = False
            print(self.round)
        else:
            print("Aucun tour n'est en cours")

    def run_menu_result(self):  # sourcery skip: extract-method
        """Lance le menu pour entrer les résultats"""
        if self.check_result:
            for match in self.matchs:
                player_1 = match[0]["lastname"]
                player_2 = match[1]["lastname"]
                choice = self.view.enter_result(player_1=player_1, player_2=player_2)
                score_player_1, score_player_2 = self.enter_result(choice=choice)
                player_1_with_score, player_2_with_score = self.result(player_1=player_1, player_2=player_2,
                                                                       score_player_1=score_player_1,
                                                                       score_player_2=score_player_2)
                match_result = self.get_match_result(player_1=player_1_with_score, player_2=player_2_with_score)
                winner = self.add_score(player_1=player_1_with_score, player_2=player_2_with_score)
                match = Match(player_1=player_1, player_2=player_2, match_result=match_result, winner=winner)
                self.tournament.matchs.append(match.serialized())
                self.check_result = False
            if self.counter_round == self.tournament.number_rounds:
                # À mettre dans les views???
                print("Félicitation le tournoi est fini\n Veuillez trouver ci-dessous le classement final:")
                self.sort_list_ranking_and_score()
        else:
            print("Le tour n'est pas encore fini ou commencé")

    def enter_result(self, choice: int):
        """Donne le résultat des joueurs de leur match"""
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

    @staticmethod
    def result(player_1: str, player_2: str, score_player_1: float, score_player_2: float):
        """Lie le score avec le joueur"""
        player_1 = [player_1, score_player_1]
        player_2 = [player_2, score_player_2]
        return player_1, player_2

    @staticmethod
    def get_match_result(player_1: list, player_2: list):
        """Donne le résultat du match"""
        match_result = (player_1, player_2)
        match_result = tuple(match_result)
        return match_result

    def add_score(self, player_1, player_2):
        """Ajoute le score du joueur dans la base de donnée du tournoi"""
        # sourcery skip: extract-duplicate-method, inline-immediately-returned-variable
        winner = ""
        for player in self.tournament.players:
            if player["lastname"] == player_1[0]:
                player["score"] += player_1[1]
                winner = player_1[0]
            if player["lastname"] == player_2[0]:
                player["score"] += player_2[1]
                winner = player_2[0]
        return winner

    def save_tournament(self):
        """Sauvegarde tournoi manuelle"""
        self.save_tournament_table.update({"matchs": self.tournament.matchs},
                                          where('name') == self.tournament.name)
        self.save_tournament_table.update({"rounds_instance": self.tournament.rounds_instance},
                                          where('name') == self.tournament.name)
        self.save_tournament_table.update({"counter_round": self.tournament.counter_round},
                                          where('name') == self.tournament.name)
        self.save_tournament_table.update({"round_in_progress": self.tournament.round_in_progress},
                                          where('name') == self.tournament.name)
        self.save_tournament_table.update({"check_result": self.tournament.check_result},
                                          where('name') == self.tournament.name)

    def load_tournament(self, tournament_database):
        self.tournament.unserialized(tournament_database)
        self.counter_round = self.tournament.counter_round
        self.check_result = self.tournament.check_result
        self.round_in_progress = self.tournament.round_in_progress
        print(self.tournament)