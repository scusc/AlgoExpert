def tournamentWinner(competitions, results):

#1-> home, 0-> away
#[home, away]
    winner = ""
    teams = {}
    max = 0
    for i in range(len(results)):
        if results[i] == 0:
            team = competitions[i][1]
            if team not in teams:
               teams[team] = 3
            else: teams[team] += 3
            if max< teams[team]:
                max = teams[team]
                winner = team
        else:
            team = competitions[i][0]
            if team not in teams:
               teams[team] = 3
            else: teams[team] += 3
            if max< teams[team]:
                max = teams[team]
                winner = team
    return winner