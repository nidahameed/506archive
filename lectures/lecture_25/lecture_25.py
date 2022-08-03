import csv
import json
import os
import requests


ENDPOINT = "https://swapi.py4e.com/api"

class Film:
    """Represents a Star Wars Film.

      Attributes:
        url (str): identifier/locator
        title (str): film title
        episode (int): Star Wars episode number
        episode_roman_num (str): Star Wars Roman numeral episode number
        release_date (str): Release date
        planets (list): list of Planet instances referenced in the film

      Methods:
        jsonable: return JSON-friendly dict representation of the object
    """

    def __init__(self, url, title, episode_id, release_date, planets):
        """Instantiate Film instance."""

        self.url = url
        self.title = title
        self.episode_id = episode_id
        self.episode_roman_num = None
        self.release_date = release_date
        self.planets = planets

    def __str__(self):
        """String representation of the Film instance."""

        if self.episode_roman_num:
            return f"Episode {self.episode_roman_num}: {self.title}"
        else:
            return self.title


    def jsonable(self):
        """JSON-friendly representation of the Film instance."""

        planets_jsonable = []
        for planets in self.planets:
            planets_jsonable.append(planets.jsonable())

        return {
            'url' : self.url,
            'title' : self.title,
            'episode_id' : self.episode_id,
            'episode_rom_num' : self.episode_roman_num,
            'release_date' : self.release_date,
            'planets' : planets_jsonable
        }


class Planet:
    """Represents a Planet.

      Attributes:
        url (str): identifier/locator
        name (str): planet name
        diameter_km (int): diameter of planet measured in kilometers
        population (int): population size

    Methods:
        jsonable: return JSON-friendly dict representation of the object
    """

    def __init__(self, url, name, diameter, population):
        """Instantiate Planet instance."""

        self.url = url
        self.name = name
        self.diameter = diameter
        self.population = population

    def __str__(self):
        """String representation of the Film instance."""

        return self.name

    def jsonable(self):
        """JSON-friendly representation of the Film instance"""

        return {
            "url": self.url,
            "name": self.name,
            "diameter": self.diameter,
            "population": self.population
        }


def convert_str_to_int(data):
    """TODO"""

    pass # TODO Implement


def create_roman_numeral(value):
    """Return Equivalent Roman numeral equivalent of passed in Arabic numeral.

    Parameters:
        value (int): Arabic value to convert

    Returns:
        str: Roman numeral
    """

    # Tuples to the rescue
    roman = ((1, 'I'), (2, 'II'), (3, 'III'), (4, 'IV'), (5, 'V'), (6, 'VI'), (7, 'VII'))

    if 1 <= value <= 7:
        return roman[value - 1][1]
    else:
        # return None
        raise ValueError('Argument value must be between 1 and 7')


def get_swapi_resource(url, params=None, timeout=10):
    """Description removed. You will soon write it.

    Parameters:
        url (str): a url that specifies the resource.
        params (dict): optional dictionary of querystring arguments.
        timeout (int): timeout value in seconds

    Returns:
        dict: dictionary representation of the decoded JSON.
    """

    if params:
        return requests.get(url, params, timeout=timeout).json()
    else:
        return requests.get(url, timeout=timeout).json()


def write_json(filepath, data):
    """Serializes object as JSON. Writes content to the provided filepath.

    Parameters:
        filepath (str): the path to the file.
        data (dict)/(list): the data to be encoded as JSON and written to the file.

    Returns:
        None
    """

    with open(filepath, 'w', encoding='utf-8') as file_obj:
        json.dump(data, file_obj, ensure_ascii=False, indent=2)


def main():
    """Entry point for the program."""

    # ABSOLUTE PATH (VS CODE DEBUGGER-FRIENDLY)
    # WARN: autograder does not require absolute paths
    abs_path = os.path.dirname(os.path.abspath(__file__))

    # print(f"\n0.0: Absolute directory path = {abs_path}")


    # CHALLENGE 02 GET SWAPI Films (n = 7)
    response = get_swapi_resource(f"{ENDPOINT}/films/")
    swapi_films = response['results']


    # CHALLENGE 03 FILM INSTANCES
    films = []
    for film in swapi_films:
        films.append(Film(
            film['url'],
            film['title'],
            film['episode_id'],
            film['release_date'],
            film['planets']
            )
        )


    # TODO Implement LOOP

    # TODO UNCOMMENT
    print(f"\nChalllenge 03: Film count = {len(films)}\n")

    print(f"\nChalllenge 03: Films")
    for film in films:
        print(film) # leverage def __str__(self))

    print("\n") # padding


    # CHALLENGE 04 ADD ROMAN NUMERALS

    # TODO UNCOMMENT

    for film in films:
        film.episode_roman_num = create_roman_numeral(film.episode_id)

        # TODO UNCOMMENT
        print(f"Episode {film.episode_roman_num}: {film.title}")

    print("\n") # padding


    # CHALLENGE 05/06 CACHE CALLS TO SWAPI / CLEAN DATA
    planet_cache = {}

    for film in films[:2]: # TEST FIRST TWO FILMS
        for i, url in enumerate(film.planets):

            if url not in planet_cache.keys():
                response = get_swapi_resource(url)

                planet = Planet(
                    response['url'],
                    response['name'],
                    response['diameter'],
                    response['population']
                )

                planet_cache[url] = planet
            else:
                planet = planet_cache[url]
            
        film.planets[i] = planet #update instance

    # TODO IMPLEMENT CACHING WORKFLOW

    # TODO UNCOMMENT
    # Print cache size
    # print(f"\nChallenge 05: cache size (calls made) = {len(planet_cache)}")


    # BONUS: SORT BY EPISODE ID

    # Use built-in sorted() and a lambda (anonymous) function
    # Tutorial: https://www.afternerd.com/blog/python-sort-list/
    # Format: sorted(<list>, key = lambda <object>: <expression>)

    # episodes = sorted(films, key = lambda film: film.episode_id)

    # print(f"\nBONUS: sorted by episode_id\n")
    # for episode in episodes:
    #     print(episode) # film


    # WRITE TO FILE

    # TODO IMPLEMENT THIS TASK AFTER FIRST THROWING TYPEERROR

    # REQUIRED: convert films to a list of dictionaries

    films_jsonable = []

    # TODO UNCOMMENT
    # JSON-FRIENDLY LIST OF FILM DICTIONARIES
    for film in films:
        films_jsonable.append(film.jsonable())

    # TODO UNCOMMENT
    filepath = os.path.join(abs_path, 'stu_films.json')
    # filepath = 'stu_films.json'
    write_json(filepath, films_jsonable)


if __name__ == '__main__':
    main()
