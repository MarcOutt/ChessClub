players = [{'lastname': 'toto', 'firstname': 'toto', 'birthday': '11-11-1111', 'gender': 'Féminin', 'ranking': '4', 'score': 0},
           {'lastname': 'tutu', 'firstname': 'tutu', 'birthday': '11-11-1111', 'gender': 'Masculin', 'ranking': '3', 'score': 1},
           {'lastname': 'toto', 'firstname': 'toto', 'birthday': '11-11-1111', 'gender': 'Féminin', 'ranking': '2', 'score': 2},
           {'lastname': 'tutu', 'firstname': 'tutu', 'birthday': '11-11-1111', 'gender': 'Masculin', 'ranking': '1', 'score': 1}]

players = sorted(players, key=lambda player: player['ranking'], reverse=False)
players = sorted(players, key=lambda player: player['score'], reverse=True)
print(players)
