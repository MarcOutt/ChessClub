from datetime import date, datetime

class Round:
    def __init__(self, name: str = "", ending_date: str = None, ending_time: str = None, matchs: list = None,
                 ):
        if matchs is None:
            matchs = []
        self.name = name
        now = datetime.now()
        self.starting_date = now.strftime("%d %b %Y")
        self.starting_time = now.strftime("%Hh%Mm%Ss")
        self.ending_date = ending_date
        self.ending_time = ending_time
        self.matchs = matchs

    def __repr__(self):
        return str(self.__dict__)

    def endgame_date_time(self):
        self.end_date = date.today()
        now = datetime.now()
        self.end_time = now.strftime("%H:%M:%S")
