from datetime import date


class Tournament:
    def __init__(self, name: str = None, location: str = None, number_players: int = 1, number_rounds: int = 1,
                 players: list = None, time_control: str = None, description: str = None, rounds_instance=None,
                 matchs: list = None, counter_round: int = 0, round_in_progress: bool = False,
                 check_result: bool = False):
        if rounds_instance is None:
            rounds_instance = []
        if matchs is None:
            matchs = []
        if players is None:
            players = []

        self.name = name
        self.location = location
        self.date = date.today()
        self.number_players = number_players
        self.number_rounds = number_rounds
        self.time_control = time_control
        self.description = description
        # self.players = players
        self.players = [{'lastname': 'Toto', 'firstname': 'Toto', 'birthday': '11-11-1111', 'gender': 'Feminin',
                         'ranking': 22, 'score': 0}, {'lastname': 'Tutu', 'firstname': 'Tutu', 'birthday': '11-11-1111',
                                                      'gender': 'Masculin', 'ranking': 33, 'score': 0},
                        {'lastname': 'Tata', 'firstname': 'Tata', 'birthday':
                            '11-11-1111', 'gender': 'Masculin', 'ranking': 44, 'score': 0},
                        {'lastname': 'Fefe', 'firstname': 'Fefe',
                         'birthday': '11-11-1111', 'gender': 'Masculin', 'ranking': 77, 'score': 0},
                        {'lastname': 'Fafa',
                         'firstname': 'Fafa', 'birthday': '22-11-1111', 'gender': 'Feminin', 'ranking': 99, 'score': 0},
                        {'lastname': 'Rere', 'firstname': 'Rere', 'birthday': '11-11-1111', 'gender': 'Masculin',
                         'ranking': 99,
                         'score': 0},
                        {'lastname': 'Baba', 'firstname': 'Baba', 'birthday': '11-11-1111', 'gender': 'Masculin',
                         'ranking': 1, 'score': 0}, {'lastname': 'Bobo', 'firstname': 'Bobo', 'birthday': '11-11-1111',
                                                     'gender': 'Masculin', 'ranking': 3, 'score': 0}]
        self.rounds_instance = rounds_instance
        self.matchs = matchs

        self.counter_round = counter_round
        self.round_in_progress = round_in_progress
        self.check_result = check_result

    def __str__(self):
        return f"\nNom : {self.name} \n" \
               f"Lieu: {self.location} \n" \
               f"Nombre de tours: {self.number_rounds} \n" \
               f"Nombre de joueurs: {self.number_players} \n" \
               f"Type de contrôle de temps: {self.time_control} \n" \
               f"Description : {self.description} \n" \
               f"Liste des joueurs: {self.players}"

    def __repr__(self):
        return str(self.__dict__)

    def serialized(self):
        return {"name": self.name, "location": self.location, "date": str(self.date),
                "number_players": self.number_players,
                "number_rounds": self.number_rounds,
                "time_control": self.time_control,
                "description": self.description,
                "players": str(self.players),
                "rounds_instance": self.rounds_instance,
                "matchs": str(self.matchs),
                "counter_round": self.counter_round,
                "round_in_progress": self.round_in_progress,
                "check_result": self.check_result}

    def unserialized(self, serialized):
        self.name = serialized['name']
        self.location = serialized['location']
        self.date = serialized['date']
        self.number_rounds = serialized['number_rounds']
        self.matchs = serialized['matchs']
        self.number_players = serialized['number_players']
        self.players = serialized['players']
        self.time_control = serialized['time_control']
        self.description = serialized['description']
        self.rounds_instance = serialized['round_instance']
        self.counter_round = serialized['counter_round']
        self.round_in_progress = serialized['round_in_progress']
        self.check_result = serialized['check_result']

    def round_instance_list(self, round):
        self.rounds_instance.append(round)
        return self.rounds_instance
