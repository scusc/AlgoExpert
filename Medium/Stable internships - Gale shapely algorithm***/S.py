def stableInternships(interns, teams):
    free_interns = list(range(len(interns)))
    engaged = {}
    intern_next_proposal = [0] * len(interns)
    team_preferences = [{intern: pref for  pref, intern in enumerate(currentTeamPref)} for currentTeamPref in teams]

    while free_interns:
        intern = free_interns.pop()
        team = interns[intern][intern_next_proposal[intern]]
        intern_next_proposal[intern] += 1
        if team not in engaged.keys():
            engaged[team] = intern
        else:
            if team_preferences[team][intern] < team_preferences[team][engaged[team]]:
                free_interns.append(engaged[team])
                engaged[team] = intern
            else:
                free_interns.append(intern)

    return [[intern, team] for team, intern in engaged.items()]

print(stableInternships([
    [0, 1, 2, 3],
    [0, 1, 3, 2],
    [0, 2, 3, 1],
    [0, 2, 3, 1]
  ],
  [
    [1, 3, 2, 0],
    [0, 1, 2, 3],
    [1, 3, 2, 0],
    [3, 0, 2, 1]
  ]
))

"""
output: 
[
  [0, 1],
  [1, 0],
  [2, 3],
  [3, 2]
]
"""