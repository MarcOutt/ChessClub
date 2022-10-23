
# Controller
from models import Tournament, Player, Round, Match

def create_tournament():
    tournament = Tournament()
    player = Player()
    return tournament


def add_player(tournament):
    #  player_list = tournament.add_player()
    pass


def launch_round_1(tournament):

    round = Round(player_list=tournament.player_list, name="Round 1")
    for m in round.first_round():
        first_player = m[0]['Nom de famille']
        second_player = m[1]['Nom de famille']
        match = Match(m, first_player, second_player, tournament.player_list)
        match_result = match.match_result_
        round.endgame_date_time()
    round.sort_list_ranking_and_score()
    tournament.round_instance_list(round)
    return round


# round 2
def launch_round_2(tournament, round):
    round_2 = Round(player_list=tournament.player_list, name="Round 2", match_list=round.matchs_list)
    for m in round_2.next_round():
        first_player = m[0]['Nom de famille']
        second_player = m[1]['Nom de famille']
        match = Match(m, first_player, second_player, tournament.player_list)
        match_result = match.match_result_
        round_2.endgame_date_time()
    tournament.round_instance_list(round_2)
    round_2.sort_list_ranking_and_score()
    print(round_2.sort_list_ranking_and_score())
    return round_2


def launch_round_3(round_2):
    tournament = Tournament()
    player = Player()
    round_3 = Round(player_list=tournament.player_list, name="Round 2", match_list=round_2.matchs_list)
    for m in round_3.next_round():
        first_player = m[0]['Nom de famille']
        second_player = m[1]['Nom de famille']
        match = Match(m, first_player, second_player, tournament.player_list)
        match_result = match.match_result_
        round_3.endgame_date_time()
    tournament.round_instance_list(round_2)
    round_3.sort_list_ranking_and_score()
    print(round_3.sort_list_ranking_and_score())


def save_result(match, round):
    match_result = match.match_result_
    round.endgame_date_time()