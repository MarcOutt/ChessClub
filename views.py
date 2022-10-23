
from Controllers import create_tournament, add_player, launch_round_1, launch_round_2, launch_round_3, save_result

print("Bienvenue dans le logiciel pour les tournois Suisses\n"
      "1 - Créer un tournoi \n"
      "2 - Ajouter les joueurs \n"
      "3 - Lancer le round 1\n"
      "4 - Lancer le round 2\n "
      "5 - Lancer le round 3\n"
      "6 - Rentrer les résultats\n")

user = input("Veuillez entrez votre choix : ")
user_int = int(user)
tournament = []
round = []
round_2 = []
round_3 = []
if user_int == 1:
      tournament = create_tournament()
elif user_int == 2:
      add_player(tournament)
elif user_int == 3:
      round = launch_round_1(tournament)
elif user_int == 4:
      round_2 = launch_round_2(round)
elif user_int == 5:
      round_3 = launch_round_3(round_2)
elif user_int == 6:
      save_result()



# Lancer tour
# Rentrer les résultats
