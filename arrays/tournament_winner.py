# O(n) time | O(k) space
# n is number of competition and k is number of teams
def tournamentWinner(competitions, results):
    teamPoints = {}
    max_points = 0
    winner_team = None
    for i, teams in enumerate(competitions):
        home_team, away_team = teams[0], teams[1]
        if home_team not in teamPoints:
            teamPoints[home_team] = 0
        if away_team not in teamPoints:
            teamPoints[away_team] = 0
        if results[i]:
            teamPoints[home_team] += 3
            if teamPoints[home_team] > max_points:
                max_points = teamPoints[home_team]
                winner_team = home_team
        else:
            teamPoints[away_team] += 3
            if teamPoints[away_team] > max_points:
                max_points = teamPoints[away_team]
                winner_team = away_team
    return winner_team
