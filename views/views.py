class View:

    def main_menu(self):
        print("Bienvenue dans le logiciel pour les tournois Suisses\n")
        while True:
            print(
                "1 - Gestionnaire des tournois \n"
                "2 - Administrateur\n")

            user = input("\nVeuillez entrez votre choix : ")
            try:
                return int(user)
            except ValueError:
                print("Veuillez répondre par des chiffres\n")
                self.main_menu()

    def manager_menu(self):
        print("Bienvenue dans le gestionnaire de tournoi\n")
        menu = True
        while menu:
            print(
                "1 - Créer un tournoi \n"
                "2 - Ajouter les joueurs\n"
                "3 - Lancer le 1er round\n"
                "4 - Lancer le round suivant\n"
                "5 - Rentrer les résultats des rencontres\n"  # faire la selection de quel match pour mettre le résultat
                "6 - Voir le classement du tournoi\n"
                "7 - Afficher les joueurs\n"
                "8 - Sortir du programme")
            return input("\nVeuillez entrez votre choix : \n")

    def first_round_view(self):
        print("\n\nPREMIER TOUR\n\n"
              "Menu\n"
              "1 - Lancer le tour\n"
              "2 - Finir le tour\n"
              "3 - Afficher les informations du tour\n"
              "4 - Retour")
        return input("\nVeuillez entrez votre choix : ")

    def menu_result(self, matchs):  # sourcery skip: hoist-statement-from-loop
        print(" Veuillez choisir le match afin de rentrer ses résultats")
        for match in matchs:
            print(f"{matchs.index(match) + 1} - Mme/M {match[0]['Nom de famille']} VS Mme/M {match[1]['Nom de famille']}\n")
        print("0 - Précédent")
        return input("\nVeuillez entrez votre choix : \n")

    def enter_result(self, first_player, second_player):
        print("Quelle est le résultat de la partie ? \n"
              f"Si M/Mme {first_player} a gagné(e), tapé 1\n"
              f"Si M/Mme {second_player} a gagné(e), tapé 2\n"
              f"Si match nul, tapé 3")
        return input("Match result : Veuillez indiquer votre choix : ")
