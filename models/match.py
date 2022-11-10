class Match:
    def __init__(self, match_result=None, player_1=None, player_2=None, winner=None):
        if player_2 is None:
            player_2 = []
        if player_1 is None:
            player_1 = []
        if match_result is None:
            self.match_result = []
        self.player_1 = player_1
        self.player_2 = player_2
        self.match_result = match_result
        self.winner = winner

    def __str__(self):
        return f"Rencontre entre M/Mme {self.match_result[0]['Nom de famille']} et M/Mme " \
               f"{self.match_result[1]['Nom de famille']}\n" \
               f"Le gagnant du match est : {self.winner}"
