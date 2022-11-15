class Player:
    def __init__(self, player_id: int = None, lastname: str = None, firstname: str = None, birthday=None, gender: str = None,
                 ranking: int = None, score: int = 0):
        self.lastname = lastname
        self.firstname = firstname
        self.birthday = birthday
        self.gender = gender
        self.ranking = ranking
        self.score = score
        self.player_id = player_id

    def __str__(self):
        return f"nom : {self.lastname}\n" \
               f"Prénom: {self.firstname}\n" \
               f"Date de naissance: {self.birthday}\n" \
               f"Sexe : {self.gender}\n" \
               f"Classement: {self.ranking}\n"

    def __repr__(self):
        return str(self.__dict__)

    def serialized(self):
        return {
                "lastname": self.lastname,
                "firstname": self.firstname,
                "birthday": str(self.birthday),
                "gender": self.gender,
                "ranking": self.ranking,
                "score": self.score,
                "id": self.player_id
                }

    def deserialized(self, serialized):
        self.lastname = serialized["lastname"]
        self.firstname = serialized["firstname"]
        self.birthday = serialized["birthday"]
        self.gender = serialized["gender"]
        self.ranking = serialized["ranking"]
        self.score = serialized["score"]
        self.player_id = serialized["id"]

