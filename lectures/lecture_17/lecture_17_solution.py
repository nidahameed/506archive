# SI 506 Lecture 17

# < films > list located outside main() to minimize scrolling between functions.
films = [
    {
        'title': 'Psycho',
        'year_released': 1960,
        'budget': 806947,
        'box_office_receipts': 50000000,
        'scary_character': {
            'name': 'Norman Bates',
            'weapon': "chef's knife"
            }
        },
    {
        'title': 'Halloween',
        'year_released': 1978,
        'budget': 325000,
        'box_office_receipts': 70000000,
        'scary_character': {
            'name': 'Michael Myers',
            'weapon': "chef's knife"
            }
        },
    {
        'title': 'Friday the 13th',
        'year_released': 1980,
        'budget': 5500000,
        'box_office_receipts': 59800000,
        'scary_character': {
            'name': 'Jason Vorhees',
            'weapon': 'machete'
            }
        },
    {
        'title': 'The Shining',
        'year_released': 1980,
        'budget': 19000000,
        'box_office_receipts': 46200000,
        'scary_character': {
            'name': 'Jack Torrance',
            'weapon': 'ax'
            }
        },
    {
        'title': 'A Nightmare on Elm Street',
        'year_released': 1984,
        'budget': 1800000,
        'box_office_receipts': 25500000,
        'scary_character': {
            'name': 'Freddy Krueger',
            'weapon': 'clawed glove'
            }
        },
    {
        'title': "Child's Play",
        'year_released': 1988,
        'budget': 9000000,
        'box_office_receipts': 44200000,
        'scary_character': {
            'name': 'Chucky',
            'weapon': 'kitchen knife'
            }
        },
    {
        'title': 'The Ring',
        'year_released': 2002,
        'budget': 48000000,
        'box_office_receipts': 249400000,
        'scary_character': {
            'name': 'Samara',
            'weapon': 'nensha telepathy'
            }
        },
    {
        'title': 'The Babadook',
        'year_released': 2014,
        'budget': 2000000,
        'box_office_receipts': 10300000,
        'scary_character': {
            'name': 'Babadook',
            'weapon': 'possession'
            }
        },
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
        'box_office_receipts': 255400000,
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

# < ratings > list located outside main() to minimize scrolling between functions.
ratings = [
    {
        'title': 'Psycho',
        'year_released': 1960,
        'tomatometer': {
            'percent_score': .96,
            'avg_rating': 9.22,
            'raters': 101
            },
        'audience': {
            'percent_score': .95,
            'avg_rating': 4.46,
            'raters': 240145
            }
        },
    {
        'title': 'Halloween',
        'year_released': 1978,
        'tomatometer': {
            'percent_score': .96,
            'avg_rating': 8.63,
            'raters': 72
            },
        'audience': {
            'percent_score': .89,
            'avg_rating': 4.33,
            'raters': 303217
            }
        },
    {
        'title': 'Friday the 13th',
        'year_released': 1980,
        'tomatometer': {
            'percent_score': .64,
            'avg_rating': 5.92,
            'raters': 56
            },
        'audience': {
            'percent_score': .61,
            'avg_rating': 3.51,
            'raters': 229168
            }
        },
    {
        'title': 'The Shining',
        'year_released': 1980,
        'tomatometer': {
            'percent_score': .84,
            'avg_rating': 8.39,
            'raters': 93
            },
        'audience': {
            'percent_score': .93,
            'avg_rating': 4.37,
            'raters': 481925
            }
        },
    {
        'title': 'A Nightmare on Elm Street',
        'year_released': 1984,
        'tomatometer': {
            'percent_score': .94,
            'avg_rating': 7.77,
            'raters': 53
            },
        'audience': {
            'percent_score': .83,
            'avg_rating': 4.08,
            'raters': 415558
            }
        },
    {
        'title': "A Nightmare on Elm Street 2: Freddy's Revenge",
        'year_released': 1985,
        'tomatometer': {
            'percent_score': .41,
            'avg_rating': 5.10,
            'raters': 29
            },
        'audience': {
            'percent_score': .33,
            'avg_rating': 2.83,
            'raters': 321383
            }
        },
    {
        'title': "Child's Play",
        'year_released': 1988,
        'tomatometer': {
            'percent_score': .71,
            'avg_rating': 6.53,
            'raters': 49
            },
        'audience': {
            'percent_score': .63,
            'avg_rating': 3.55,
            'raters': 267564
            }
        },
    {
        'title': 'Scream',
        'year_released': 1996,
        'tomatometer': {
            'percent_score': .78,
            'avg_rating': 7.18,
            'raters': 74
            },
        'audience': {
            'percent_score': .79,
            'avg_rating': 3.92,
            'raters': 478586
            }
        },
    {
        'title': 'The Ring',
        'year_released': 2002,
        'tomatometer': {
            'percent_score': .71,
            'avg_rating': 6.61,
            'raters': 207
            },
        'audience': {
            'percent_score': .48,
            'avg_rating': 2.97,
            'raters': 32459
            }
        },
    {
        'title': 'The Babadook',
        'year_released': 2014,
        'tomatometer': {
            'percent_score': .98,
            'avg_rating': 8.20,
            'raters': 238
            },
        'audience': {
            'percent_score': .72,
            'avg_rating': 3.69,
            'raters': 39119
            }
        },
    {
        'title': 'Train to Busan',
        'year_released': 2016,
        'tomatometer': {
            'percent_score': .94,
            'avg_rating': 7.61,
            'raters': 116
            },
        'audience': {
            'percent_score': .88,
            'avg_rating': 4.17,
            'raters': 12758
            }
        },
    {
        'title': 'Get Out',
        'year_released': 2017,
        'tomatometer': {
            'percent_score': .98,
            'avg_rating': 8.35,
            'raters': 386
            },
        'audience': {
            'percent_score': .86,
            'avg_rating': 4.18,
            'raters': 75450
            }
        },
    {
        'title': 'It: Chapter One',
        'year_released': 2017,
        'tomatometer': {
            'percent_score': .85,
            'avg_rating': 7.27,
            'raters': 377
            },
        'audience': {
            'percent_score': .84,
            'avg_rating': 4.08,
            'raters': 67297
            }
        }
]


def calculate_audience_vs_critics_rating_diff(rating):
    """Returns rating differential between a film's  audience and the critics. Multiply by 100
    in order to work with integers (whole numbers). Positive score indicates that the general
    audience preferred the film despite the critics; negative score indicates that the general
    audience disliked the film more than did the critics (who may have actually praised the
    film).

    Parameters:
        rating: Film rating

    Returns:
        int: difference in points between critics and audience film rating.
    """

    audience_score = rating['audience']['percent_score'] * 100
    critics_score = rating['tomatometer']['percent_score'] * 100

    return audience_score - critics_score


def calculate_gross(film):
    """Calculates gross profits (box office receipts minus budget costs).

    Parameters:
        film (dict): film to be evaluated

    Returns:
        int: gross profits

    """

    return film['box_office_receipts'] - film['budget']


def get_top_grossing_film(films):
    """Returns top grossing film(s). Handles ties.

    Parameters:
        films (list): list of films to be evaluated

    Returns:
        list: top grossing film(s)
    """

    top_gross = []
    prev_gross = 0
    for film in films:
        gross = film['gross']
        if gross > prev_gross:
            top_gross.clear() # remove all films
            top_gross.append(film) # replace
            prev_gross = gross # reset
        elif gross == prev_gross:
            top_gross.append(film) # tied

    return top_gross


def get_critics_choice(ratings):
    """Returns top rated film(s) per Rotten Tomatoes approved critics. Handles ties.

    Parameters:
        films (list): list of film ratings to be evaluated

    Returns:
        list: top rated film(s)
    """

    critics_choice = []
    prev_score = 0.0
    for rating in ratings:
        score = rating['tomatometer']['percent_score']
        if score > prev_score:
            critics_choice.clear() # remove all film ratings
            critics_choice.append(rating) # replace
            prev_score = score # reset
        elif score == prev_score:
            critics_choice.append(rating) # tied

    return critics_choice


def reorder_film_dict(film, keys):
    """Returns a new dictionary base on the passed in < film > dictionary with the
    key-value pair order determined by the order of the items in the passed in
    < keys > tuple.

    Parameters:
        films (dict): film dict
        keys (tuple): item order determines key-value pair order of new dict

    Returns:
        dict: film dictionary with reordered key-value pairs
    """

    reordered = {}
    for key in keys:
        if key in film.keys():
            reordered[key] = film[key]

    return reordered

    # Alternative: dictionary comprehension
    # return {key: film[key] for key in keys if key in film.keys()}


def main():
    """Program entry point.

    Parameters:
        None

    Returns:
        None
    """

    # CHALLENGE 01

    film = f"{films[-1]['title']} ({films[-1]['year_released']})"

    print(f"\nChallenge 01: {film}")


    # CHALLENGE 02

    scary_character_name = f"{films[0]['scary_character']['name']}"

    print(f"\nChallenge 02: {scary_character_name}")


    # CHALLENGE 03

    scream = {}
    scream['title'] = 'Scream'
    scream['year_released'] = 1996
    scream['budget'] = 15000000
    scream['box_office_receipts'] = 173000000
    scream['scary_character'] = {} # empty nested dictionary
    scream['scary_character']['name'] = 'Ghostface'
    scream['scary_character']['weapon'] = 'knife'

    films.insert(-5, scream)

    print(f"\nChallenge 03. Scream added = {films[-6]}")


    # CHALLENGE 04

    elm_street_2 = {
        'title': "A Nightmare on Elm Street 2: Freddy's Revenge",
        'year_released': 1985,
        'budget': 3000000,
        'box_office_receipts': 30000000,
        'scary_character': {
            'name': 'Freddy Krueger',
            'weapon': 'clawed glove'
        }
    }

    films.insert(5, elm_street_2)

    print(f"\nChallenge 04. Nightmare on Elm Street 2 added = {films[5]}")


    # CHALLENGE 05

    scary_characters = []
    for film in films:
        if film['scary_character']['name'] not in scary_characters:
            scary_characters.append(film['scary_character']['name']) # filters out duplicates

    print(f"\nChallenge 05: Scary characters (no duplicates): {scary_characters}")


    # CHALLENGE 06

    for film in films:
        film['gross'] = calculate_gross(film)

    print(
        f"\nChallenge 06 Get Out {films[-2]['box_office_receipts']} "
        f"- {films[-2]['budget']} = {films[-2]['gross']} (gross)"
        )

    # CHALLENGE 06 (BONUS)
    # Format currency
    # https://www.python.org/dev/peps/pep-0498/#format-specifiers
    # :,  <-- adds a comma as a thousands separator
    # .2f <-- limits the string to two (2) decimal places

    gross = f"${films[-2]['gross']:,.2f}" # add format specifier
    # gross = "${:,.2f}".format(films[-1]['gross']) # str.format()

    print(f"\nChallenge 06 (bonus). Get Out gross (formatted): {gross}")


    # CHALLENGE 07

    top_grossing_films = get_top_grossing_film(films)

    print('\nChallenge 07: top grossing film(s)')

    for film in top_grossing_films:
        print(f"{film['title']} gross = ${film['gross']:,.2f}")


    # CHALLENGE 08
    # Implement < get_critics_choice > function. Return top rated film(s) in < ratings > list.

    top_rated_films = get_critics_choice(ratings)

    print('\nChallenge 08: top rated film(s) by the critics')

    for film in top_rated_films:
        print(f"{film['title']} = {film['tomatometer']['percent_score']} rating")


    # CHALLENGE 09

    ratings_diff = []
    for rating in ratings:
        diff = rating['title'], calculate_audience_vs_critics_rating_diff(rating) # tuple packing
        ratings_diff.append(diff) # tuple literal

    ratings_diff.sort(key=lambda x: x[1], reverse=True) # in-place sort using a lambda expression

    print(f"\nChallenge 09: Ratings diff: {ratings_diff}")


    # CHALLENGE 10

    for film in films:
        for rating in ratings:
            if (rating['title'].lower() == film['title'].lower()
                and rating['year_released'] == film['year_released']):

                film['rotten_tomatoes'] = {
                    'tomatometer': rating['tomatometer'],
                    'audience': rating['audience']
                }

                break

    print(f"\nChallenge 10: Films/ratings combined (example): {films[0]}")


    # CHALLENGE 11

    character_counts = {}
    for film in films:
        for key, val in film.items():
            if key == 'scary_character':
                name = val['name'] # get name
                if name in character_counts:
                    character_counts[name] += 1
                else:
                    character_counts[name] = 1

    print(f"\nChallenge 11: Character count: {character_counts}")


    # CHALLENGE 12

    key_order = (
        'title',
        'year_released',
        'budget',
        'box_office_receipts',
        'gross',
        'scary_character',
        'rotten_tomatoes'
        )

    movies = []
    for film in films:
        movie = reorder_film_dict(film, key_order)
        movies.append(movie)

    print(f"\nChallenge 12: Scary movies (reordered key-value pairs example): {movies[0]}")


if __name__ == '__main__':
    main()
