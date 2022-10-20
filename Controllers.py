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
    # Lancer le trie par score et par rang
    sort_list = self.sort_list_score_and_ranking()
    # Créer une liste de tous les matchs déjà effectués
    for player in sort_list:
        print(player)
    # Comparé les nouveaux matchs avec ceux qui existe
    # Si le match existe faire un i + 1 sur le second de la liste
    # Revérifier si le match n'a pas déjà eu lieu
    pass