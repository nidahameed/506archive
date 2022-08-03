# START PROBLEM SET O5
print('Problem Set 05')

# Problem 01
print('\nProblem 1')

# SETUP
def count_vowels(word):
    lower_word = word.lower()
    num_a = lower_word.count("a")
    num_e = lower_word.count("e")
    num_i = lower_word.count("i")
    num_o = lower_word.count("o")
    num_u = lower_word.count("u")
    total_vowels = num_a + num_e + num_i + num_o + num_u
    return total_vowels

example_words = ["Scrabble",
"puppies",
"kittens",
"mellifluous",
"Supercalifragilisticexpialidocious"
]
# END SETUP

#1.2
callously_score = count_vowels('callously')
#print(callously_score)

#1.3
example_words_score = 0
for words in example_words:
    score = count_vowels(words)
    example_words_score += score
print(example_words_score)


## PROBLEM 2
print('\nProblem 2')

def score_list(word_list):
    counter = 0
    for word in word_list:
        score = count_vowels(word)
        counter += score
    return counter

val1 = score_list(['hello', 'there', '!'])
print(val1)

val2 = score_list(["this", "was", "a", "triumph"])
print(val2)


## PROBLEM 3
print('\nProblem 3')

def who_wins(player1_score, player2_score):
    a = 'Player 1 wins! Yay!'
    b = 'Player 2 wins! Boo.'
    c = "It was a tie! Well that's boring."
    if player1_score > player2_score:
        return a
    elif player1_score < player2_score:
        return b
    else:
        return c

val = who_wins(32, 0)
print(val)

val2 = who_wins(0, 32)
print(val2)

a_draw = who_wins(0, 0)
print(a_draw)


## PROBLEM 4
print('\nProblem 4')

def play_blinkbot_scrabble(player1_input, player2_input):
    counter_p1 = 0
    counter_p2 = 0
    for words in player1_input:
        player1_score = count_vowels(words)
        counter_p1 += player1_score
    for words in player2_input:
        player2_score = count_vowels(words)
        counter_p2 += player2_score
    return who_wins(counter_p1, counter_p2)

game1 = play_blinkbot_scrabble(["many", "vowels", "many", "words"], ["fewer"])
print(game1)

game2 = play_blinkbot_scrabble(["not", "fair"], ["Hahahahahahaha", "Loser"])
print(game2)

game3 = play_blinkbot_scrabble(["we're", "tied"], ["of", "course"])
print(game3)


## PROBLEM 5

# SETUP
def how_much_sleep(hours_slept):
    hours_left = 8 - hours_slept
    if hours_left >= 0:
        return hours_left
    else:
        return 0
# END SETUP

# COMPLETE THE FOLLOWING DOCUMENTATION
'''
Function name: how_much_sleep

Explanation:
    This function calculates how much sleep the chatbot has left to sleep.
    The chatbot is supposed to sleep 8 hours a day; if the chatbot has slept fewer hours,
    the function will state how many hours the chatbot has left to sleep.

Parameters:
    hours_slept, an integer

Returns:
    An integer that shows how many more hours Blinkbot needs to sleep.

'''