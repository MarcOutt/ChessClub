class ViewAdmin:

    def menu_admin(self):
            print("Bienvenue dans le gestionnaire de tournoi\n")
            while True:
                print(
                    "1 - Afficher un rapport \n"
                    "2 - Mettre à jour le classement\n"
                    "3 - Retour au menu principal\n")

                user = input("\nVeuillez entrez votre choix : \n")
                try:
                    return int(user)
                except ValueError:
                    print("Veuillez répondre par des chiffres\n")
                    self.menu_admin()
