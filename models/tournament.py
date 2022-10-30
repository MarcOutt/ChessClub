from datetime import date


class Tournament:
    def __init__(self, name: str = None, location: str = None, players: list = None,
                 number_players: int = 8, description: str = None, number_rounds: int = 4, time_control: str = None):
        if players is None:
            players = []
        self.name = name
        self.location = location
        self.date = date.today()
        self.number_rounds = number_rounds
        self.tournee = ""
        self.number_players = number_players
        self.players = {'Nom de famille': '1', 'Classement': '1', 'Score': 0}, \
                           {'Nom de famille': '2', 'Classement': '2', 'Score': 0}, \
                           {'Nom de famille': '4', 'Classement': '4', 'Score': 0}, \
                           {'Nom de famille': '5', 'Classement': '5', 'Score': 0}, \
                           {'Nom de famille': '8', 'Classement': '8', 'Score': 0}, \
                           {'Nom de famille': '6', 'Classement': '6', 'Score': 0}, \
                           {'Nom de famille': '3', 'Classement': '3', 'Score': 0}, \
                           {'Nom de famille': '7', 'Classement': '7', 'Score': 0}
        self.time_control = time_control
        self.description = description
        self.round_instance = []

    def __repr__(self):
        return str(self.__dict__)

    def round_instance_list(self, round):
        self.round_instance.append(round)
        return self.round_instance