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
                "7 - Sortir du programme")
            user = input("\nVeuillez entrez votre choix : \n")
            try:
                return int(user)
            except ValueError:
                print("Veuillez répondre par des chiffres\n")
                self.manager_menu()

    def first_round_view(self):
        print("\n\nPREMIER TOUR\n\n"
              "Menu\n"
              "1 - Lancer le tour\n"
              "2 - Finir le tour\n"
              "3 - Afficher les informations du tour\n"
              "4 - Retour")
        answer = input("\nVeuillez entrez votre choix : ")
        try:
            return int(answer)
        except ValueError:
            print("pas bon")
            print("Veuillez répondre par des chiffres\n")
            self.manager_menu()

    def enter_result(self, match):
        menu = True
        while menu:
            print(" Veuillez choisir le match afin de rentrer ses résultats")
            i = 1
            print(f"{i} - {match}\n")

            user = input("\nVeuillez entrez votre choix : \n")