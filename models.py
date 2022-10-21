from collections import OrderedDict
from datetime import date, datetime
from operator import attrgetter

NB_PLAYER = 2


class Tournament:
    def __init__(self, player_list=None):
        if player_list is None:
            player_list = []
        self.name = "Val Tournament"
        self.location = "Paris"
        self.date = date.today()
        self.number_rounds = 4
        self.tournee = ""
        self.player_list = {'Nom de famille': 'aaaa', 'Classement': '5', 'Score': 5}, \
                           {'Nom de famille': 'bbbb', 'Classement': '2', 'Score': 4}, \
                           {'Nom de famille': 'cccc', 'Classement': '8', 'Score': 0}, \
                           {'Nom de famille': 'dddd', 'Classement': '3', 'Score': 3}, \
                           {'Nom de famille': 'eeee', 'Classement': '4', 'Score': 0}, \
                           {'Nom de famille': 'ffff', 'Classement': '6', 'Score': 1}, \
                           {'Nom de famille': 'gggg', 'Classement': '1', 'Score': 1}, \
                           {'Nom de famille': 'hhhh', 'Classement': '7', 'Score': 1}
        # self.player_list = player_list
        self.time_control = "Bullet, un blitz ou un coup rapide"
        self.description = "Mots du directeur"
        self.round_instance = []

    def __repr__(self):
        return str(self.__dict__)

    def tournament_presentation(self):
        return (
            f"\n\n      Bienvenue au {self.name.upper()} \n\n"
            f"Lieu du tournoi : {self.location}\n"
            f"Date de l'évènement : {self.date}\n"
            f"Nombre de tour du tournoi : {self.number_rounds}\n"
            f"Contrôle du temps : {self.time_control}\n"
            f"Description du tournoi : {self.description}\n"
        )

    def add_player(self):
        player_number = input("Combien de joueur souhaiter-vous ajouter? ")
        player_number_int = int(player_number)
        for _ in range(player_number_int):
            print("\nAjouter joueur\n")
            lastname = input("Nom de famille ")
            # self.firstname = input("Prénom")
            # self.birthday = input("Date de naissance ")
            # self.gender = input("Sexe ")
            ranking = input("Classement ")
            self.player_list.append(Player(lastname, ranking))
        return self.player_list

    def round_instance_list(self, round):
        self.round_instance.append(round)
        return self.round_instance


class Player:
    def __init__(self, lastname=None, ranking=None, score=0):
        self.lastname = lastname
        # self.firstname = input("Prénom")
        # self.birthday = input("Date de naissance ")
        # self.gender = input("Sexe ")
        self.ranking = ranking
        self.score = score

    def __repr__(self):
        return str(self.__dict__)


class Round:
    def __init__(self, player_list=None, name="", end_date=None, end_time=None, match_list=None):
        if player_list is None:
            player_list = []
        if match_list is None:
            match_list = []
        self.name = name
        self.star_date = date.today()
        now = datetime.now()
        self.start_time = now.strftime("%H:%M:%S")
        self.end_date = end_date
        self.end_time = end_time
        self.player_list = player_list
        self.matchs_list = match_list

    def __repr__(self):
        return f" Nom :{self.name} \n" \
               f" Date de commencement:  {self.star_date}\n" \
               f" Heure de début:{self.start_time}\n" \
               f" Date de fin: {self.end_date}\n" \
               f" Heure de fin: {self.end_time}\n" \
               f" Liste des joueurs: {self.player_list}\n" \
               f" Liste des matchs: {self.matchs_list}"

    def endgame_date_time(self):
        self.end_date = date.today()
        now = datetime.now()
        self.end_time = now.strftime("%H:%M:%S")

    def sort_list_ranking(self):
        d1 = sorted(self.player_list, key=lambda player_list: player_list['Score'], reverse=True)
        self.player_list = OrderedDict(sorted(d1[1], key=lambda player_list: player_list[1], reverse=False))
        return self.player_list

    def sort_list_score_and_ranking(self):
        # trier en nombre total de point
        s = sorted(self.player_list, key=attrgetter(str(self.fctSortDict)))  # sort on secondary key
        sorted(s, key=attrgetter('Score'), reverse=True)

    def first_round(self):
        # création des listes niveaux haut et bas
        self.sort_list_ranking()
        half = len(self.player_list) // 2
        lower_list = self.player_list[:half]
        upper_list = self.player_list[half:]
        for i in range(len(lower_list)):
            match_list = [upper_list[i - 1], lower_list[i - 1]]
            self.matchs_list.append(match_list)
        return self.matchs_list

    def next_round(self):
        # Lancer le trie par score et par rang
        self.sort_list_score_and_ranking()
        # Créer une liste de tous les matchs déjà effectués
        for player in sort_list:
            print(player)
        # Comparé les nouveaux matchs avec ceux qui existe
        # Si le match existe faire un i + 1 sur le second de la liste
        # Revérifier si le match n'a pas déjà eu lieu


class Match:

    def __init__(self, name="Match", first_player="", second_player="", match_result=None):
        if match_result is None:
            self.match_result = []
        self.name = name
        self.first_player = first_player
        self.second_player = second_player
        self.match_result = match_result

    def __repr__(self):
        return f"nom de la rencontre {self.name}\n" \
               f"rencontre entre M/Mme {self.first_player} et M/Mme {self.second_player}\n" \
               f"resultat du match : {self.match_result}"

    def match_result_(self):
        print("Quelle est le résultat de la partie ? \n"
              f"Si M/Mme {self.first_player} a gagné(e), tapé 1\n"
              f"Si M/Mme {self.second_player} a gagné(e), tapé 2\n"
              f"Si match nul, tapé 3")
        answer = input("Veuillez indiquer votre choix ")
        answer_int = int(answer)
        if answer_int == 1:
            player_win = [self.first_player, 1]
            player_loose = [self.second_player, 0]
            self.match_result = (player_win, player_loose)
        elif answer_int == 2:
            player_win = [self.second_player, 0]
            player_loose = [self.first_player, 1]
            self.match_result = (player_win, player_loose)
        elif answer_int == 3:
            player_win = [self.first_player, 0]
            player_loose = [self.second_player, 0]
            self.match_result = (player_win, player_loose)
        self.match_result = tuple(self.match_result)
        return self.match_result


# Controller
tournament = Tournament()
player = Player()
"""player_list = {'Nom de famille': 'aaaa', 'Classement': '5'}, {'Nom de famille': 'bbbb', 'Classement': '2'}, \
              {'Nom de famille': 'cccc', 'Classement': '8'}, {'Nom de famille': 'dddd', 'Classement': '3'}, \
              {'Nom de famille': 'eeee', 'Classement': '4'}, {'Nom de famille': 'ffff', 'Classement': '6'}, \
              {'Nom de famille': 'gggg', 'Classement': '1'}, {'Nom de famille': 'hhhh', 'Classement': '7'}"""
# player_list = tournament.add_player()
round = Round(tournament.player_list, "Round 1")
first_round = round.first_round()
for m in first_round:
    first_player = m[0]['Nom de famille']
    second_player = m[1]['Nom de famille']
    match = Match(m, first_player, second_player)
    match_result = match.match_result_()
    round.endgame_date_time()
tournament.round_instance_list(round)
print(round.player_list)
round.sort_list_ranking()


for p in tournament.player_list:
    print(p)
