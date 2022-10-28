from datetime import date, datetime


class Tournament:
    def __init__(self, name: str = "", location: str = "", players: list = None,
                 number_players: int = None, description: str = ""):
        if players is None:
            players = []
        self.name = name
        self.location = location
        self.date = date.today()
        self.number_rounds = 4
        self.tournee = ""
        self.number_players = number_players
        self.players = players
        # self.player_list = player_list
        self.time_control = "Bullet, un blitz ou un coup rapide"
        self.description = description
        self.round_instance = []

    def __repr__(self):
        return str(self.__dict__)

    def round_instance_list(self, round):
        self.round_instance.append(round)
        return self.round_instance