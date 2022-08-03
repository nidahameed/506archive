# SI 506 Lecture 16

# 2.1 SYNTAX

# Single line
film = {'title': 'The Wizard of Oz', 'year_released': 1939}

# Multiple lines
film = {
    'title': 'The Wizard of Oz',
    'year_released': 1939,
    'budget': 2800000,
    'box_office_receipts': 26100000
    }

# Nested dictionary (< scary_character >)
film = {
    'title': 'The Wizard of Oz',
    'year_released': 1939,
    'budget': 2800000,
    'box_office_receipts': 26100000,
    'scary_character': {
        'name': 'The Wicked Witch of the West',
        'weapon': 'evil spells'
        }
    }

print(f"\n2.1 film = {film}")

# Type
film_type = type(film) # <class 'dict'>

print(f"\n2.1 film type = {film_type}")

# Accessing a value
title = film['title']

print(f"\n2.1 Film title = {title}")

# Accessing a nested dictionary's value
scary_character_name = film['scary_character']['name'] # chain keys

print(f"\n2.1 Scary character name = {scary_character_name}")


# 2.2 DEFINING A DICTIONARY

# 2.2.1 EMPTY DICTIONARY
film = {}
film['title'] = 'Scream'
film['year_released'] = 1996
film['budget'] = 15000000
film['box_office_receipts'] = 173000000
film['scary_character'] = {} # Define nested dictionary
film['scary_character']['name'] = 'Ghostface' # chain keys
film['scary_character']['weapon'] = 'knife' # chain keys

print(f"\n2.2.1 Scream = {film}")


# 2.2.2 DICTIONARY LITERAL

film = {
    'title': "A Nightmare on Elm Street 2: Freddy's Revenge",
    'year_released': 1985,
    'budget': 3000000,
    'box_office_receipts': 30000000,
    'scary_character': {
        'name': 'Freddy Krueger',
        'weapon': 'clawed glove'
        }
    }

print(f"\n2.2.2 Nightmare on Elm Street 2 = {film}")


# 2.2.3 BUILT-IN DICT() FUNCTION

film = dict(
    title='The Shining',
    year_released=1980,
    budget=19000000,
    box_office_receipts=46200000,
    scary_character=dict(name='Jack Torrance', weapon='Ax') #nested
    )

print(f"\n2.2.3 The Shining = {film}")


# 2.3 ADD, MODIFY, DELETE KEY-VALUE PAIRS

film['director'] = 'Stanley Kubrick'
film['running_time_mins'] = 146 # premier
film['tomatometer'] = .84 # The Shining (audience score = 93%)

print(f"\n2.3 The Shining (additions) = {film}")

film['running_time_mins'] = 144 # American release

del(film['tomatometer'])

print(f"\n2.3 The Shining (modified) = {film}")


# 2.4 EXCEPTION: KEYERROR

# TODO UNCOMMENT (raise exception)
# name = film['name'] # raises KeyError: 'name'


# 2.5 DICTIONARY METHODS

# 2.5.1 DICT.GET()

film = {
    'title': 'Get Out',
    'year_released': 2017,
    'budget': 4500000,
    'box_office_receipts': 255000000,
    'scary_character': {
        'name': 'Rose Armitage',
        'weapon': 'tricksterism'
        }
    }

film_name = film.get('name') # swallows the exception and returns None

print(f"\n2.5.1 film.get('name') = {film_name}")

film_name = film.get('title') # returns film title

print(f"\n2.5.1 film.get('title') = {film_name}\n")


# 2.5.2 DICT.KEYS()

film = {
    'title': 'Halloween',
    'year_released': 1978,
    'budget': 325000,
    'box_office_receipts': 70000000,
    'scary_character': {
        'name': 'Michael Myers',
        'weapon': "chef's knife"
        }
    }

keys = film.keys() # returns dict_keys object

# Loop over dict_keys object
for key in keys:
    print(key)

print('\n') # padding

keys = list(film.keys()) # convert to a list

print(f"\n2.5.2 list(film.keys()) = {keys}")

# Loop over keys list, print each Film value by key reference
for key in keys:
    print(f"{film[key]}") # returns value

print('\n') # padding

# 2.5.3 DICT.VALUES()

film = {
    'title': 'Psycho',
    'year_released': 1960,
    'budget': 806947,
    'box_office_receipts': 50000000,
    'scary_character': {
        'name': 'Norman Bates',
        'weapon': "chef's knife"
        }
    }

values = film.values() # return dict_values object

# Loop over dict_values object
for value in values:
    print(value)

# Convert to a list
values = list(film.values()) # convert to a list

print(f"\n2.5.3 list(film.values()) = {values}")


# 2.5.4 DICT.ITEMS()

films = [
    {
        'title': 'Train to Busan',
        'year_released': 2016,
        'budget': 8500000,
        'box_office_receipts': 98500000,
        'scary_character': {
            'name': 'Zombie',
            'weapon': 'incisors'
            }
        },
    {
        'title': 'Get Out',
        'year_released': 2017,
        'budget': 4500000,
        'box_office_receipts': 255000000,
        'scary_character': {
            'name': 'Rose Armitage',
            'weapon': 'tricksterism'
            }
        },
    {
        'title': 'It: Chapter One',
        'year_released': 2017,
        'budget': 35000000,
        'box_office_receipts': 700000000,
        'scary_character': {
            'name': 'Pennywise the Dancing Clown',
            'weapon': 'superhuman strength'
            }
        }
    ]

# Task: extract film title and append to < film_titles > list.
# Nested loop iterates over each film's keys and values
film_titles = []
for film in films:
    for key, val in film.items():
        if key == 'title':
            film_titles.append(val)

print(f"\n2.5.4 Film titles: {film_titles}")


release_year_counts = {}
for film in films:
    for key, val in film.items():
        if key == 'year_released':
            if val in release_year_counts.keys():
                release_year_counts[val] += 1 # increment count
            else:
                release_year_counts[val] = 1 # new key-value

print(f"\n2.5.4 Film releases by year: {release_year_counts}")