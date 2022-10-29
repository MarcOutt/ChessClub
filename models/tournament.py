from datetime import date


class Tournament:
    def __init__(self, name: str = None, location: str = None, players: list = None,
                 number_players: int = None, description: str = None, number_rounds: int = 4, time_control: str = None):
        if players is None:
            players = []
        self.name = name
        self.location = location
        self.date = date.today()
        self.number_rounds = number_rounds
        self.tournee = ""
        self.number_players = number_players
        self.players = players
        # self.player_list = player_list
        self.time_control = time_control
        self.description = description
        self.round_instance = []

    def __repr__(self):
        return str(self.__dict__)

    def round_instance_list(self, round):
        self.round_instance.append(round)
        return self.round_instance