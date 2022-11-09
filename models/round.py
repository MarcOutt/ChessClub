from datetime import date, datetime

class Round:
    def __init__(self, name: str = "", ending_date: list = None, ending_time: list = None, matchs: list = None):
        if ending_date is None:
            ending_date = []
        if ending_time is None:
            ending_date = []
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
        return f"Tour numéro {self.name}\n" \
               f"Début du tour: {self.starting_date} à {self.starting_time}\n" \
               f"Fin du tour: {self.ending_date} à {self.ending_time}\n" \
               f"Rencontres: {self.matchs}\n"

    def endgame_date_time(self):
        self.end_date = date.today()
        now = datetime.now()
        self.end_time = now.strftime("%H:%M:%S")

