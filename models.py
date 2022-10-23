
from datetime import date, datetime


# je n'ai pas géré le trie par le score et le classement au niveau du round 2
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
        self.player_list = {'Nom de famille': 'aaaa', 'Classement': '1', 'Score': 0}, \
                           {'Nom de famille': 'bbbb', 'Classement': '2', 'Score': 0}, \
                           {'Nom de famille': 'cccc', 'Classement': '4', 'Score': 0}, \
                           {'Nom de famille': 'dddd', 'Classement': '5', 'Score': 0}, \
                           {'Nom de famille': 'eeee', 'Classement': '8', 'Score': 0}, \
                           {'Nom de famille': 'ffff', 'Classement': '6', 'Score': 0}, \
                           {'Nom de famille': 'gggg', 'Classement': '3', 'Score': 0}, \
                           {'Nom de famille': 'hhhh', 'Classement': '7', 'Score': 0}
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

    def sort_list_ranking_and_score(self):
        self.player_list = sorted(self.player_list, key=lambda player_list: player_list['Classement'], reverse=False)
        self.player_list = sorted(self.player_list, key=lambda player_list: player_list['Score'], reverse=True)
        return self.player_list

    def first_round(self):
        # création des listes niveaux haut et bas
        self.sort_list_ranking_and_score()
        # print(f"round 1 :{self.player_list}")
        half = len(self.player_list) // 2
        lower_list = self.player_list[:half]
        upper_list = self.player_list[half:]
        for i in range(len(lower_list)):
            match_list = [upper_list[i - 1], lower_list[i - 1]]
            self.matchs_list.append(match_list)
        return self.matchs_list

    def next_round(self):
        # Lancer le trie par score et par rang

        new_matchs_list = []
        # Créer une liste de tous les matchs déjà effectués
        self.player_list = self.sort_list_ranking_and_score()
        print(f"round 2 :{self.player_list}")
        for i in range(0, len(self.player_list), 2):
            new_match = [self.player_list[i], self.player_list[i + 1]]
            new_match = sorted(new_match, key=lambda player_list: player_list['Nom de famille'])
            # print(f"new match 1 : {new_match}")
            # print(self.matchs_list)
            match_list_sort = []
            for i in self.matchs_list:
                old_match = sorted(i, key=lambda player_list: player_list['Nom de famille'])
                match_list_sort.append(old_match)
            if str(new_match) in match_list_sort:
                    print("match existe déjà")
                    #  new_match = [self.player_list[i], self.player_list[i + 2]]
                    #  print(f"new match 1.2 : {new_match}")
            new_matchs_list.append(new_match)
        self.matchs_list = new_matchs_list
        return self.matchs_list
        # Comparé les nouveaux matchs avec ceux qui existe
        # Si le match existe faire un i + 1 sur le second de la liste
        # Revérifier si le match n'a pas déjà eu lieu

class Match:

    def __init__(self, name="Match", first_player="", second_player="",player_list=None, match_result=None):
        if player_list is None:
            player_list = []
        if match_result is None:
            self.match_result = []
        self.name = name
        self.first_player = first_player
        self.second_player = second_player
        self.match_result = match_result
        self.player_list = player_list

    def __repr__(self):
        return f"nom de la rencontre {self.name}\n" \
               f"rencontre entre M/Mme {self.first_player} et M/Mme {self.second_player}\n" \
               f"resultat du match : {self.match_result}"

    def add_score(self, player):
        tournament = Tournament()
        for p in self.player_list:
            if p["Nom de famille"] == player:
                p["Score"] += 1
            tournament.player_list = self.player_list

    @property
    def match_result_(self):  # sourcery skip: move-assign-in-block, switch
        print("Quelle est le résultat de la partie ? \n"
              f"Si M/Mme {self.first_player} a gagné(e), tapé 1\n"
              f"Si M/Mme {self.second_player} a gagné(e), tapé 2\n"
              f"Si match nul, tapé 3")
        answer = input("Veuillez indiquer votre choix : ")
        answer_int = int(answer)
        if answer_int == 1:
            player_win = [self.first_player, 1]
            player_loose = [self.second_player, 0]
            self.add_score(self.first_player)
            self.match_result = (player_win, player_loose)
        elif answer_int == 2:
            player_win = [self.second_player, 1]
            player_loose = [self.first_player, 0]
            self.add_score(self.second_player)
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
# player_list = tournament.add_player()
# round 1
round = Round(player_list=tournament.player_list, name="Round 1")
for m in round.first_round():
    first_player = m[0]['Nom de famille']
    second_player = m[1]['Nom de famille']
    match = Match(m, first_player, second_player, tournament.player_list)
    match_result = match.match_result_
    round.endgame_date_time()
round.sort_list_ranking_and_score()
tournament.round_instance_list(round)

# round 2
round_2 = Round(player_list=tournament.player_list, name="Round 2", match_list=round.matchs_list)
for m in round_2.next_round():
    first_player = m[0]['Nom de famille']
    second_player = m[1]['Nom de famille']
    match = Match(m, first_player, second_player, tournament.player_list)
    match_result = match.match_result_
    round.endgame_date_time()
tournament.round_instance_list(round_2)
round_2.sort_list_ranking_and_score()
print(round_2.sort_list_ranking_and_score())

# round 3
round_3 = Round(player_list=tournament.player_list, name="Round 2", match_list=round.matchs_list)
for m in round_3.next_round():
    first_player = m[0]['Nom de famille']
    second_player = m[1]['Nom de famille']
    match = Match(m, first_player, second_player, tournament.player_list)
    match_result = match.match_result_
    round.endgame_date_time()
tournament.round_instance_list(round_2)
round_3.sort_list_ranking_and_score()
print(round_3.sort_list_ranking_and_score())



