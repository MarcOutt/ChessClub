"""Entry point."""

from controllers.controllers import Controller
from models.match import Match
from models.player import Player
from models.round import Round
from models.tournament import Tournament
from views.view_admin import ViewAdmin
from views.view_player import ViewPlayer
from views.views import View
from views.view_tournament import ViewTournament


def main():
    match = Match()
    view_tournament = ViewTournament()
    view_admin = ViewAdmin
    view_player = ViewPlayer
    player = Player()
    round = Round()
    view = View()
    tournament = Tournament()
    app = Controller(match=match, player=player, round=round,
                     tournament=tournament, view_tournament=view_tournament,
                     view=view, view_admin=view_admin, view_player=view_player)
    app.run_app()


if __name__ == "__main__":
    main()
