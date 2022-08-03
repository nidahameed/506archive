# START LAB EXERCISE 06
print('Lab Exercise 06 \n')

#SETUP
mario_kart_game = [
('Peach', 49), ('Mario', 35), ('Yoshi', 23),
('Wario', 20), ('Daisy', 18), ('Luigi', 10)
]

# END SETUP

# PROBLEM 1 (5 points)
def scores(game):
    #split them into two teams
    team1 = game[:3] #0,1,2
    team2 = game[3:] #3,4,5
    #get the sum of their scores
    score1 = team1[0][1] + team1[1][1] + team1[2][1]
    score2 = team2[0][1] + team2[1][1] + team2[2][1]
    return score1, score2


# PROBLEM 2 (5 points)
def blue_shell(game):
    #place the player in first place to third
    first_player = game[0]
    game.pop(0)
    game.insert(2, first_player)
    return game


# PROBLEM 3 (5 points)
# SETUP
new_mario_kart_game =  [
('Donkey Kong', 45), ('Mario', 30), ('Yoshi', 22),
('Wario', 20), ('Toad', 18), ('Peach', 15)
]
# END SETUP

# PROBLEM 4 (5 points)
def top_three(game):
    top_three_players = game[:3]
    return [top_three_players[0][0], top_three_players[1][0], top_three_players[2][0]]


# main()
def main():
    pass
    # Call < scores() > and assign to < team_scores >
    team_scores = scores(mario_kart_game)
    print(f'First game team scores: {team_scores}') ## Uncomment when ready!

    blue_shell_players = blue_shell(mario_kart_game)
    print(f'Player positions after blue shell: {blue_shell_players}') ## Uncomment when ready!

    new_player = ('Bowser', 60)
    new_mario_kart_game.insert(0, new_player)
    print(f'Updated new game: {new_mario_kart_game}') ## Uncomment when ready!

    top_three_players = top_three(new_mario_kart_game)
    print(f'Top three players: {top_three_players}') ## Uncomment when ready!

    # END LAB EXERCISE

if __name__ == '__main__':
    main()