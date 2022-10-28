from datetime import date, datetime

class Round:
    def __init__(self, name: str = "", end_date: str = None, end_time: str = None, matchs: list = None):
        if matchs is None:
            matchs = []
        self.name = name
        self.start_date = date.today()
        now = datetime.now()
        self.start_time = now.strftime("%H:%M:%S")
        self.end_date = end_date
        self.end_time = end_time

        self.matchs = matchs

    def __repr__(self):
        return str(self.__dict__)

    def endgame_date_time(self):
        self.end_date = date.today()
        now = datetime.now()
        self.end_time = now.strftime("%H:%M:%S")
