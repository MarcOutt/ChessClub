class Player:
    def __init__(self, lastname: str = None, firstname: str = None, birthday=None, gender: str = None,
                 ranking: int = None, score: int = 0):
        self.lastname = lastname
        self.firstname = firstname
        self.birthday = birthday
        self.gender = gender
        self.ranking = ranking
        self.score = score

    def __str__(self):
        return f"nom : {self.lastname}\n" \
               f"Prénom: {self.firstname}\n" \
               f"Date de naissance: {self.birthday}\n" \
               f"Sexe : {self.gender}\n" \
               f"Classement: {self.ranking}\n"

    def __repr__(self):
        return str(self.__dict__)

    def serialized(self):
        return {"lastname": self.lastname,
                "firstname": self.firstname,
                "birthday": str(self.birthday),
                "gender": self.gender,
                "ranking": self.ranking,
                "score": self.score
                }

