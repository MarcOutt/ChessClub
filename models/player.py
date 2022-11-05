
class Player:
    def __init__(self, lastname: str = None, firstname: str = None, birthday=None, gender: str = None, ranking: int = None):
        self.lastname = lastname
        self.firstname = firstname
        self.birthday = birthday
        self.gender = gender
        self.ranking = ranking

    def __str__(self):
        return f"nom : {self.lastname}\n" \
               f"Prénom: {self.firstname}\n" \
               f"Date de naissance: {self.birthday}\n" \
               f"Sexe : {self.gender}\n" \
               f"Classement: {self.ranking}\n"

    def __repr__(self):
        return str(self.__dict__)