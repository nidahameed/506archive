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

    def __init__(
        self,
        url: str,
        title: str,
        episode_id: int,
        release_date: str,
        planets: list
        ) -> None:
        """Instantiate Film instance."""

        self.url = url
        self.title = title
        self.episode_id = episode_id
        self.episode_roman_num = None
        self.release_date = release_date
        self.planets = planets

    def __str__(self) -> str:
        """String representation of the Film instance."""

        if self.episode_roman_num:
            return f"Episode {self.episode_roman_num}: {self.title}"
        else:
            return self.title


    def jsonable(self) -> dict:
        """JSON-friendly representation of the Film instance."""

        # Unnecessary: override json.dump() with CustomEncoder

        # planets_jsonable = []
        # for planet in self.planets:
        #     planets_jsonable.append(planet.jsonable())

        # planets_jsonable = [planet.jsonable() for planet in planets] # list comprehension

        return {
            'url': self.url,
            'title': self.title,
            'episode_id': self.episode_id,
            'episode_roman_num': self.episode_roman_num,
            'release_date': self.release_date,
            'planets': self.planets
            # 'planets': planets_jsonable
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

    def __init__(self, url: str, name: str, diameter: str, population: str):
        """Instantiate Planet instance."""

        self.url = url
        self.name = name
        self.diameter = diameter
        self.population = population

    def __str__(self) -> str:
        """String representation of the Film instance."""

        return self.name

    def jsonable(self) -> dict:
        """JSON-friendly representation of the Film instance"""

        return {
            'url': self.url,
            'name': self.name,
            'diameter': self.diameter,
            'population': self.population
        }
