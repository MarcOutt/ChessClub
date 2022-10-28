
class Player:
    def __init__(self, lastname=None, firstname=None, birthday=None, gender=None, ranking=None):
        self.lastname = lastname
        self.firstname = firstname
        self.birthday = birthday
        self.gender = gender
        self.ranking = ranking

    def __repr__(self):
        return str(self.__dict__)
