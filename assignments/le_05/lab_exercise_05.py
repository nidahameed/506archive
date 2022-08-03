# START LAB EXERCISE 05
print('Lab Exercise 05 \n')

# SETUP

record = [
    ['school', 'year', 'won', 'lost', 'win_percent', 'bowl_appear', 'bowl_win'],
    ['Michigan', 2019, 9, 4, None, True, False],
    ['Michigan', 2018, 10, 3, None, True, False],
    ['Michigan', 2017, 8, 5, None, True, False],
    ['Michigan', 2016, 10, 3, None, True, False],
    ['Michigan', 2015, 10, 3, None, True, True],
    ['Michigan', 2014, 5, 7, None, False, False],
    ['Michigan', 2013, 7, 6, None, True, False],
    ['Michigan', 2012, 8, 5, None, True, False],
    ['Michigan', 2011, 11, 2, None, True, True],
    ['Michigan', 2010, 7, 6, None, True, False],
    ['Michigan', 2009, 5, 7, None, False, False],
    ['Michigan', 2008, 3, 9, None, False, False],
    ['Michigan', 2007, 9, 4, None, True, True],
    ['Michigan', 2006, 11, 2, None, True, False],
    ['Michigan', 2005, 7, 5, None, True, False],
    ['Michigan', 2004, 9, 3, None, True, False],
    ['Michigan', 2003, 10, 3, None, True, False],
    ['Michigan', 2002, 10, 3, None, True, True],
    ['Michigan', 2001, 8, 4, None, True, False],
    ['Michigan', 2000, 9, 3, None, True, True]
]

# END SETUP

# PROBLEM 1.0 (5 Points)
def calculate_win_percentage(wins, losses):
    total_games = wins + losses
    win_percentage = wins / total_games
    win_percentage = round(win_percentage, 3)
    return win_percentage

#print(calculate_win_percentage(5, 5))
#print(calculate_win_percentage(33, 65))


# PROBLEM 2.0 (5 Points)

for row in record[1:]:
    number_of_wins = row[2]
    number_of_losses = row[3]
    win_percentage = calculate_win_percentage(number_of_wins, number_of_losses)
    row[4] = win_percentage

#print(record)


# PROBLEM 3.0 (5 Points)

record_wins = 0
record_losses = 0
for row in record[1:]:
    number_of_wins = row[2]
    number_of_losses = row[3]
    record_wins += number_of_wins
    record_losses += number_of_losses

#print(record_losses, record_wins)
record_win_percent = calculate_win_percentage(record_wins, record_losses)
#print(record_win_percent)

# PROBLEM 4.0 (5 Points)
best_year = None
def calculate_best_year(record):
    best_wp = 0.0
    for row in record[1:]:
        win_percentage = row[4]
        year = row[1]
        bowl_win = row[-1]
        if win_percentage > best_wp:
                best_wp = win_percentage
                best_year = year
        elif bowl_win and win_percentage == best_wp:
            best_wp = win_percentage
            best_year = year
    return best_year

print(calculate_best_year(record))

worst_year = None
def calculate_worst_year(record):
    worst_wp = 1.0
    for row in record[1:]:
        win_percentage = row[4]
        year = row[1]
        bowl_lose = row[-1]
        if win_percentage < worst_wp:
            worst_wp = win_percentage
            worst_year = year
        elif bowl_lose and win_percentage == worst_wp:
            worst_wp = win_percentage
            worst_year = year
    return worst_year

print(calculate_worst_year(record))


# END LAB EXERCISE