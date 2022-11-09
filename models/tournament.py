from datetime import date


class Tournament:
    def __init__(self, name: str = None, location: str = None, players: list = None,
                 number_players: int = 2, description: str = None, number_rounds: int = 2, time_control: str = None):
        if players is None:
            players = []
        self.name = name
        self.location = location
        self.date = date.today()
        self.number_rounds = number_rounds
        self.tournee = ""
        self.number_players = number_players
        self.players = [{'lastname': 'toto', 'firstname': 'toto', 'birthday': '11-11-1111', 'gender': 'Féminin', 'ranking': '4', 'score': 0},
           {'lastname': 'tutu', 'firstname': 'tutu', 'birthday': '11-11-1111', 'gender': 'Masculin', 'ranking': '3', 'score': 0},
           {'lastname': 'titi', 'firstname': 'toto', 'birthday': '11-11-1111', 'gender': 'Féminin', 'ranking': '2', 'score': 0},
           {'lastname': 'tata', 'firstname': 'tutu', 'birthday': '11-11-1111', 'gender': 'Masculin', 'ranking': '1', 'score': 0}]
        self.time_control = time_control
        self.description = description
        self.round_instance = []

    def __str__(self):
        return f"\nNom : {self.name} \n" \
               f"Lieu: {self.location} \n" \
               f"Date: {self.date} \n" \
               f"Nombre de tours: {self.number_rounds} \n" \
               f"Nombre de joueurs: {self.number_players} \n" \
               f"Type de contrôle de temps: {self.time_control} \n" \
               f"Description : {self.description} \n" \
               f"Liste des joueurs: {self.players}"

    def __repr__(self):
        return str(self.round_instance)

    def round_instance_list(self, round):
        self.round_instance.append(round)
        return self.round_instance