from datetime import date, datetime
from operator import attrgetter

NB_PLAYER = 4


class Tournament:
    def __init__(self):
        self.name = "Val Tournament"
        self.location = "Paris"
        self.date = date.today()
        self.number_rounds = 4
        self.tournee = ""
        self.player = {'Nom de famille': 'aaaa', 'Classement': '5'}, {'Nom de famille': 'bbbb', 'Classement': '2'}, \
                      {'Nom de famille': 'cccc', 'Classement': '8'}, {'Nom de famille': 'dddd', 'Classement': '3'}, \
                      {'Nom de famille': 'eeee', 'Classement': '4'}, {'Nom de famille': 'ffff', 'Classement': '6'}, \
                      {'Nom de famille': 'gggg', 'Classement': '1'}, {'Nom de famille': 'hhhh', 'Classement': '7'}
        self.time_control = "Bullet, un blitz ou un coup rapide"
        self.description = "Mots du directeur"

    def tournament_presentation(self):
        return (
            f"\n\n      Bienvenue au {self.name.upper()} \n\n"
            f"Lieu du tournoi : {self.location}\n"
            f"Date de l'évènement : {self.date}\n"
            f"Nombre de tour du tournoi : {self.number_rounds}\n"
            f"Contrôle du temps : {self.time_control}\n"
            f"Description du tournoi : {self.description}\n"
        )

    def create_player_list(self):
        player = Player()
        self.player_list = []
        for _ in range(NB_PLAYER):
            player.add_player()
            self.player_list.append(player.infos_player())
        return self.player_list


class Player:
    def __init__(self, lastname=None):
        self.lastname = lastname
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

    def __str__(self):
        return f"Nom de famille{self.lastname}\n" \
               f"Classement{self.ranking}"
        # "Prénom": str(self.firstname),
        # "Date de naissance": str(self.birthday),
        # "Sexe": self.gender,
        # "Score": str(self.score)

    def infos_player(self):  # je l'utilise pour créer ma liste
        infos_player = {
            "Nom de famille": str(self.lastname),
            # "Prénom": str(self.firstname),
            # "Date de naissance": str(self.birthday),
            # "Sexe": self.gender,
            "Classement": str(self.ranking)
            # "Score": str(self.score)
        }
        return infos_player


class Round:
    def __init__(self, player_list, name="", end_date=None, end_time=None, match_list=None):
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

    def __str__(self):
        return self.name,

    def endgame_date_time(self):
        self.end_date = date.today()
        now = datetime.now()
        self.end_time = now.strftime("%H:%M:%S")

    def fctSortDict(self, player_list):
        return player_list['Classement']

    def sort_list_ranking(self):
        self.player_list = sorted(self.player_list, key=self.fctSortDict, reverse=False)
        # sorted(self.player_list, key=lambda classement: classement["Classement"])
        return self.player_list

    def sort_list_score_and_ranking(self):
        # trier en nombre total de point
        s = sorted(self.player_list, key=attrgetter('Classement'))  # sort on secondary key
        sorted(s, key=attrgetter('Score'), reverse=True)

    def multiple_match(self):
        pass

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
        sort_list = self.sort_list_score_and_ranking()
        # Créer une liste de tous les matchs déjà effectués
        for player in sort_list:
            print(player)
        # Comparé les nouveaux matchs avec ceux qui existe
        # Si le match existe faire un i + 1 sur le second de la liste
        # Revérifier si le match n'a pas déjà eu lieu
        pass


class Match:

    def __init__(self, name="Match", first_player="", second_player=""):
        self.name = name
        self.first_player = first_player
        self.second_player = second_player

    def match_result(self):
        print("Quelle est le résultat de la partie ? \n"
            f"Si M/Mme {self.first_player} a gagné, tapé 1\n"
            f"Si M/Mme {self.second_player} a gagné, tapé 2\n"
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

tournament = Tournament()
player_list = {'Nom de famille': 'aaaa', 'Classement': '5'}, {'Nom de famille': 'bbbb', 'Classement': '2'}, \
              {'Nom de famille': 'cccc', 'Classement': '8'}, {'Nom de famille': 'dddd', 'Classement': '3'}, \
              {'Nom de famille': 'eeee', 'Classement': '4'}, {'Nom de famille': 'ffff', 'Classement': '6'}, \
              {'Nom de famille': 'gggg', 'Classement': '1'}, {'Nom de famille': 'hhhh', 'Classement': '7'}
#  player_list = tournament.create_player_list()
round = Round(player_list)
first_round = round.first_round()
for m in first_round:
    first_player = m[0]['Nom de famille']
    second_player = m[1]['Nom de famille']
    match = Match(m, first_player, second_player)
    match_result = match.match_result()
    print(match_result)

