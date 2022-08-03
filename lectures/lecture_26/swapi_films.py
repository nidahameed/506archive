"""
This script leverages SWAPI's linked data to create composite SWAPI Film instances enriched
with SWAPI Planet data. Each enriched Film instance is then written to a JSON file.

This modest program illustrates the following Python features:
1. custom module imports (swapi_entities, swapi_utils)
2. type hinting
3. lru_cache
4. lambda function
5. list comprehension

Attributes
    ENDPOINT (str): SWAPI endpoint
"""

import os
import swapi_utils as utl

from swapi_entities import Film, Planet

ENDPOINT = "https://swapi.py4e.com/api"


def main():
    """Entry point for the program."""

    # ABSOLUTE PATH (VS CODE DEBUGGER-FRIENDLY)
    # WARN: autograder does not require absolute paths
    abs_path: str = os.path.dirname(os.path.abspath(__file__))

    # print(f"\n0.0: Absolute directory path = {abs_path}")


    # GET SWAPI Films (n = 7)
    response: dict = utl.get_swapi_resource(f"{ENDPOINT}/films/")
    swapi_films: list = response['results']


    # FILM INSTANCES

    # List comprehension (elegant)
    films: list = [
        Film(
            film['url'],
            film['title'],
            film['episode_id'],
            film['release_date'],
            film['planets']
        ) for film in swapi_films
    ]

    # films: list = []
    # for film in swapi_films:
    #     films.append(Film(
    #         film['url'],
    #         film['title'],
    #         film['episode_id'],
    #         film['release_date'],
    #         film['planets']
    #         )
    #     )

    print(f"\nFilm count = {len(films)}\n")

    print('\nFilms')
    for film in films:
        print(film) # leverage def __str__(self))

    print('\n') # padding

    # ADD ROMAN NUMERALS

    # Add Roman numerals
    for film in films:
        film.episode_roman_num = utl.create_roman_numeral(film.episode_id)
        # film.episode_roman_num = utl.create_roman_numeral("force_error") # test mypy
        print(f"Episode {film.episode_roman_num}: {film.title}")


    # CACHE CALLS TO SWAPI / CLEAN DATA
    # planet_cache = {}

    # for film in films[:2]: # TEST FIRST TWO FILMS
    url_count: int = 0
    for film in films:
        url_count += len(film.planets)
        for i, url in enumerate(film.planets):
            planet_data: dict = utl.get_swapi_resource(url) # response cached
            planet_data = utl.convert_str_to_int(planet_data)

            planet = Planet(
                planet_data['url'],
                planet_data['name'],
                planet_data['diameter'],
                planet_data['population']
                )

            film.planets[i] = planet # replace URL str with film object

    # URL count (potential HTTP GET requests)
    print(f"\nURL count = {url_count}")

    # Cache info
    print(f"\nCache info = {utl.get_swapi_resource.cache_info()}")

    # NEXT STEPS: LAMBDA SORT: SORT BY EPISODE ID
    # Format: list.sort(key=lambda <object>: <expression>)
    # Format: sorted(<list>, key=lambda <object>: <expression>)

    films.sort(key=lambda film: film.episode_id) # sort in-place
    # films = sorted(films, key=lambda film: film.episode_id) # built-in sorted() function

    print('\nLambda sort: by episode_id\n')
    for film in films:
        print(film) # film


    # NEXT STEPS: LIST COMPREHENSION

    # Convert films to a list of dictionaries
    films_jsonable: list = [film.jsonable() for film in films] # list comprehension

    # films_jsonable = []
    # for film in films:
    #     films_jsonable.append(film.jsonable())

    filepath: str = os.path.join(abs_path, 'stu_films.json')
    # filepath = 'stu_films.json'

    # BONUS: WRITE TO FILE REFERENCING CUSTOM ENCODER
    # utl.write_json(filepath, films_jsonable)
    utl.write_custom_json(filepath, films_jsonable) # overrides default json.dump() behavior


if __name__ == '__main__':
    main()
