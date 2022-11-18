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

    def __str__(self):
        matchs = "".join(f"\nNom: {match[0]['lastname']}, prénom: {match[0]['firstname']},"
                         f" classement: {match[0]['ranking']} VS Nom: {match[1]['lastname']}, "
                         f"prénom: {match[1]['firstname']}, classement: {match[1]['ranking']}"
                         for match in self.matchs)
        return f"{self.name}\n" \
               f"Début du tour: {self.starting_date} à {self.starting_time}\n" \
               f"Fin du tour: {self.ending_date} à {self.ending_time}\n\n" \
               f"Rencontres: {matchs}"

    def serialized(self):
        """Serialise le modèle Round pour la sauvegarde"""
        return {"name": self.name,
                "starting_date": str(self.starting_date),
                "starting_time": str(self.starting_time),
                "ending_date": str(self.ending_date),
                "ending_time": str(self.ending_time),
                "matchs": self.matchs
                }

    def deserialized(self, serialized):
        """Deserialise le modèle round pour le chargement"""
        self.name = serialized['name']
        self.starting_date = serialized['starting_date']
        self.starting_time = serialized['starting_time']
        self.ending_date = serialized['ending_date']
        self.ending_time = serialized['ending_time']
        self.matchs = serialized['matchs']

    def endgame_date_time(self):
        """Donne la date et l'heure de fin du tour"""
        self.end_date = date.today()
        now = datetime.now()
        self.end_time = now.strftime("%H:%M:%S")
