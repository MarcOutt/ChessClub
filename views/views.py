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
                "3 - Lancer le round 1er round\n"
                "4 - Lancer le round suivant\n"
                "5 - Rentrer les résultats\n"
                "6 - Voir classement\n"
                "7 - Sortir du programme")
            user = input("\nVeuillez entrez votre choix : \n")
            try:
                return int(user)
            except ValueError:
                print("Veuillez répondre par des chiffres\n")
                self.manager_menu()



