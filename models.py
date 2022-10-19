from datetime import date, time, datetime
from operator import itemgetter, attrgetter

class Tournaments:
    def __init__(self):
        self.name = "Val Tournament"
        self.location = "Paris"
        self.date = date.today()
        self.number_rounds = 4
        self.tournee = ""
        self.player = ""
        self.time_control = "Bullet, un blitz ou un coup rapide"
        self.description = "Mots du directeur"

    def tournament_presentation(self):
        print(
            f"\n\n      Bienvenue au {self.name.upper()} \n\n"
            f"Lieu du tournoi : {self.location}\n"
            f"date de l'évènement : {self.date}\n"
            f"Nombre de tour du tournoi : {self.number_rounds}\n"
            f"Contrôle du temps : {self.time_control}\n"
            f"Description du tournoi : {self.description}\n"
        )

    def player_list(self, player):
        player_list = []


class Players:
    def __init__(self):
        self.lastname = ""
        # self.firstname = input("Prénom")
        # self.birthday = input("Date de naissance ")
        # self.gender = input("Sexe ")
        self.ranking = ""
        # self.score = ""

    def add_player(self):
        print("\nAjouter joueur\n")
        self.lastname = input("Nom de famille ")
        # self.firstname = input("Prénom")
        # self.birthday = input("Date de naissance ")
        # self.gender = input("Sexe ")
        self.ranking = input("Classement ")

    def infos_player(self):
        infos_player = {
            "Nom de famille": str(self.lastname),
            # "Prénom": str(self.firstname),
            # "Date de naissance": str(self.birthday),
            # "Sexe": self.gender,
            "Classement": str(self.ranking)
            # "Score": str(self.score)
        }
        return infos_player


class Rounds:
    nbr = 0

    def __init__(self):
        self.name = f"round "
        self.date = ""
        self.time = ""
        self.player_list = ""

    def sort_list_ranking(self):
        player = Players()  # Est-ce que cela est correct pour de la POO ???
        self.player_list = []
        for i in range(4):
            player.add_player()
            self.player_list.append(player.infos_player())
            # trié par classement
            sorted(self.player_list, key=lambda classement: classement["Classement"])
        return self.player_list

    def sort_list_score_and_ranking(self):
        # trier en nombre total de point
        s = sorted(self.player_list, key=attrgetter('Classement'))  # sort on secondary key
        sorted(s, key=attrgetter('Score'), reverse=True)

    def first_round(self):
        # création des listes niveaux haut et bas
        half = len(self.player_list) // 2
        lower_list = self.player_list[:half]
        upper_list = self.player_list[half:]
        match_list = []
        for i in range(len(lower_list)):
            list = []
            list.append(upper_list[i - 1])
            list.append(lower_list[i - 1])
            match_list.append(list)
        return match_list

    def next_round(self):
        # Créer une liste de tous les matchs déjà effectués
        # Comparé les nouveaux matchs avec ceux qui existe
        # Si le match existe faire un i + 1 sur le second de la liste
        pass


class Matchs:

    def __init__(self):
        pass

    def score(self):
        pass


"""Générer les paires (liste)
entrer les résultats"""

tournament = Tournaments()
tournament.tournament_presentation()
