import csv
import json
import os
import requests


class Crew:
    """Representation of a Starship or Vehicle crew.

    Attributes:
        Instance variables are generated when an instance is instantiated based on
        the passed in key-value pairs.

    Methods:
        jsonable: return JSON-friendly dict representation of the object
    """

    def __init__(self, members):
        """Initialize Crew instance. Loops over the passed in dictionary and calls the built-in
        function < setattr() > to generate each instance variable and assign the value. The
        dictionary key (e.g., "pilot") will serve as the instance variable name to which the
        accompanying < Person > or < Droid > instance value will be assigned.

        Parameters:
            members (dict): crew members dictionary (< position >: < Person >)

        Returns:
            None
        """

        for key, val in members.items():
            setattr(self, key, val) # call built-in function

    def __str__(self):
        """Loops over the instance variables and return a string representation of each crew
        member < Person > object per the following format:

        < position >: < crew member name > e.g., "pilot: Han Solo, copilot: Chewbacca"
        """

        crew = None
        for key, val in self.__dict__.items():
            if crew:
                crew += f", {key}: {val}" # additional member
            else:
                crew = f"{key}: {val}" # 1st member

        return crew

    def jsonable(self):
        """Returns a JSON-friendly representation of the object. Loops over instance variables
        and converts person objects to dictionaries. Do not simply return self.__dict__. It can
        be intercepted and mutated, adding, modifying or removing instance attributes as a result.

        Parameters:
            None

        Returns:
            dict: dictionary of the object's instance variables
        """

        crew = {}
        for key, val in self.__dict__.items():
            crew[key] = val.jsonable() # person object

        return crew


class Droid:
    """Representation of a mechanical beings that possessed artificial intelligence.

    Attributes:
        url (str): identifier/locator
        name (str): droid name
        model (str): droid model
        manufacturer (str): creator
        create_year (str): droid's year of manufacture (akin to birth_year)
        height (float): droid's height in meters
        mass (float): droid's mass in kilograms
        equipment (list): droid's equipment, if any
        instructions (list): language modules, flight plans, etc.

    Methods:
        jsonable: return JSON-friendly dict representation of the object
        store_instructions: provides Droid instance with data to store
    """

    def __init__(self, url, name, model, manufacturer, create_year, height, mass, equipment):
        """Initialize a Droid instance."""

        self.url = url
        self.name = name
        self.model = model
        self.manufacturer = manufacturer
        self.create_year = create_year
        self.height = height
        self.mass = mass
        self.equipment = equipment
        self.instructions = []

    def __str__(self):
        """Return a string representation of the object."""

        return f"{self.name}"

    def store_instructions(self, instructions):
        """Provide droid with special instructions such as language modules, flight
        plans, etc.

        Parameters:
            instructions (dict): nested dictionary of key-value pairs of instructions

        Returns:
            None
        """

        #instructions = instructions.append(self.instructions)
        #instructions.append(self.instructions)
        self.instructions.append(instructions)

    def jsonable(self):
        """Returns a JSON-friendly representation of the object. Use a dictionary literal
        rather than a built-in dict() to avoid built-in lookup costs. Do not simply return
        self.__dict__. It can be intercepted and mutated, adding, modifying or removing
        instance attributes as a result.

        Parameters:
            None

        Returns:
            dict: dictionary of the object's instance variables
        """

        return {
            'url': self.url,
            'name' : self.name,
            'model' : self.model,
            'manufacturer' : self.manufacturer,
            'create_year' : self.create_year,
            'height' : self.height,
            'mass' : self.mass,
            'equipment' : self.equipment,
            'instructions' : self.instructions
        }


class Passengers:
    """Representation of a passengers carried on a Starship or Vehicle.

    Attributes:
        Instance variables are generated when an instance is instantiated based on
        the passed in list of < Person > and/or < Droid > objects. The instance name format
        is described in the < __init__() > method Docstring.

    Methods:
        jsonable: return JSON-friendly dict representation of the object
    """

    def __init__(self, passengers):
        """Initialize Passengers instance. Loops over the passed in list of < Person > and/or
        < Droid >objects and calls the built-in function < setattr() > to generate the instance
        variable and assign the value. The name of each < Droid > or < Person > will serve as
        the instance variable name (format: lowercase with spaces replaced by underscores, e.g.,
        "Luke Skywalker" to "luke_skywalker") to which the accompanying < Person > or < Droid >
        instance value will be assigned.

        Parameters:
            passengers (list): list of < Person > objects

        Returns:
            None
        """

        for passenger in passengers:
            setattr(self, passenger.name.lower().replace(' ', '_'), passenger)

    def __str__(self):
        """Loops over instance variable values and returns a string representation of each
        passenger < Person > object (passenger name only)."""

        passengers = None
        for val in self.__dict__.values():
            if passengers:
                passengers = f"{passengers}, {val.name}" # additional member
            else:
                passengers = val.name # 1st passenger

        return passengers

    def jsonable(self):
        """Returns a JSON-friendly representation of the object. Loops over instance variable
        values and converts passenger < Person > objects to dictionaries. Do not simply return
        self.__dict__. It can be intercepted and mutated, adding, modifying or removing instance
        attributes as a result.

        Parameters:
            None

        Returns:
            list: dictionary of the object's instance variables
        """

        passenger_list = []
        for val in self.__dict__.values():
            passenger_list.append(val.jsonable())

        return passenger_list


class Person:
    """Representation of a person.

    Attributes:
        url (str): identifer/locator
        name (str): person name
        birth_year (str): person's birth_year
        height (float): person's height in centimeters
        mass (float): person's weight in kilograms
        homeworld (Planet): person's home planet
        species (Species): species of person

    Methods:
        get_homeworld: retrieve home planet
        jsonable: return JSON-friendly dict representation of the object
    """

    def __init__(self, url, name, birth_year, height, mass):
        """Initialize a Person instance."""

        self.url = url
        self.name = name
        self.birth_year = birth_year
        self.height = height
        self.mass = mass
        self.homeworld = None
        self.species = None

    def __str__(self):
        """Return a string representation of the object."""

        return f"{self.name}"

    def jsonable(self):
        """Return a JSON-friendly representation of the object. Use a dictionary literal rather
        than a built-in dict() to avoid built-in lookup costs. Do not simply return self.__dict__.
        It can be intercepted and mutated, adding, modifying or removing instance attributes as a
        result.

        Parameters:
            None

        Returns:
            dict: dictionary of the object's instance variables
        """

        if self.homeworld:
            homeworld2 = self.homeworld.jsonable()
        else:
            homeworld2 = None

        if self.species:
            species2 = self.species.jsonable()
        else:
            species2 = None


        return {
            'url': self.url,
            'name': self.name,
            'birth_year': self.birth_year,
            'height': self.height,
            'mass': self.mass,
            'homeworld': homeworld2,
            'species': species2
        }


class Planet:
    """Representation of a planet.

    Attributes:
        url (str): identifier/locator
        name (str): planet name
        region (str): region name
        sector (str): sector name
        suns (int): number of suns
        moons (int): number of moons
        orbital_period_days (float): orbital period around sun(s) measured in days
        diameter_km (int): diameter of planet measured in kilometers
        gravity (dict): gravity level
        climate (list): climate type(s) found on planet
        terrain (list): terrain type(s) found on planet
        population (int): population size

    Methods:
        jsonable: return JSON-friendly dict representation of the object
    """

    def __init__(self, url, name, region, sector, suns, moons, orbital_period_days,
                diameter_km, gravity, climate, terrain, population):
        """Initialize a Planet instance."""

        self.url = url
        self.name = name
        self.region = region
        self.sector = sector
        self.suns = suns
        self.moons = moons
        self.orbital_period_days = orbital_period_days
        self.diameter_km = diameter_km
        self.gravity = gravity
        self.climate = climate
        self.terrain = terrain
        self.population = population


    def __str__(self):
        """Return a string representation of the object."""

        return f"{self.name}"

    def jsonable(self):
        """Return a JSON-friendly representation of the object. Use a dictionary literal rather
        than built-in dict() to avoid built-in lookup costs. Do not simply return self.__dict__.
        It can be intercepted and mutated, adding, modifying or removing instance attributes as
        a result.

        Parameters:
            None

        Returns:
            dict: dictionary of the object's instance variables
        """

        return {
            'url': self.url,
            'name': self.name,
            'region': self.region,
            'sector': self.sector,
            'suns': self.suns,
            'moons': self.moons,
            'orbital_period_days': self.orbital_period_days,
            'diameter_km': self.diameter_km,
            'gravity': self.gravity,
            'climate': self.climate,
            'terrain': self.terrain,
            'population': self.population,
        }


class Species:
    """A unit of biodiversity.

    Attributes:
        url (str): identifier/locator
        name (str): common name
        classification (str): classifier (e.g., 'mammal', 'reptile')
        designation (str): designation (e.g., 'sentient')
        language (str): language commonly spoken by species

    Methods:
        jsonable: return JSON-friendly dict representation of the object.
    """

    def __init__(self, url, name, classification, designation, language):
        """Initialize a Species instance."""
        self.url = url
        self.name = name
        self.classification = classification
        self.designation = designation
        self.language = language

    def __str__(self):
        """Human-readable string representation of the object."""

        return f"{self.name}"

    def jsonable(self):
        """Return a JSON-friendly representation of the object. Use a dictionary literal rather
        than a built-in dict() to avoid built-in lookup costs. Do not simply return self.__dict__.
        It can be intercepted and mutated, adding, modifying or removing instance attributes as
        a result.

        Parameters:
            None

        Returns:
            dict: dictionary of the object's instance variable values
        """

        return {
            'url': self.url,
            'name': self.name,
            'classification': self.classification,
            'designation': self.designation,
            'language': self.language
        }


class Starship:
    """A crewed vehicle used for traveling in realspace or hyperspace.

    Attributes:
        url (str): identifier/locator
        name (str): starship name or nickname
        model (str): manufacturer's model name
        starship_class (str): class of starship
        manufacturer (str): starship builder
        length (float): starship length
        max_atmosphering_speed (int): max sub-orbital speed
        hyperdrive_rating (float): lightspeed propulsion system rating
        MGLT (int): megalight per hour traveled
        armament [list]: offensive and defensive weaponry
        crew (int): crew size
        crew_members (Crew): Crew instance assigned to starship
        passengers (int): number of passengers starship rated to carry
        passengers_on_board (Passengers): passengers on board starship
        cargo_capacity (float): cargo metric tonnage starship rated to carry
        consumables (str): max period in months before on-board provisions must be replenished


    Methods:
        assign_crew: assign crew members to starship
        assign_passengers: assign passengers to starship
        jsonable: return JSON-friendly dict representation of the object
    """

    def __init__(self, url, name, model, starship_class, manufacturer, length,
                max_atmosphering_speed, hyperdrive_rating, MGLT, armament, crew,
                passengers, cargo_capacity, consumables, crew_members=None, passengers_on_board=None):
        """Initalize instance of a Starship."""

        self.url = url
        self.name = name
        self.model = model
        self.starship_class = starship_class
        self.manufacturer = manufacturer
        self.length = length
        self.max_atmosphering_speed = max_atmosphering_speed
        self.hyperdrive_rating = hyperdrive_rating
        self.MGLT = MGLT
        self.armament = armament
        self.crew = crew
        self.crew_members = crew_members
        self.passengers = passengers
        self.passengers_on_board = passengers_on_board
        self.cargo_capacity = cargo_capacity
        self.consumables = consumables

    def __str__(self):
        """String representation of the object."""

        return f"{self.model}"

    def add_passengers(self, passengers):
        """Add passengers to starship if passenger accommodations are available.

        Parameters:
            passengers (Passengers): Passengers object containing Person instances

        Returns:
            None
        """

        if self.passengers > 0:
            self.passengers_on_board = passengers

    def assign_crew_members(self, crew):
        """Assign crew_members.

        Parameters:
            crew (Crew): Object comprising crew members (role, person)

        Returns:
            None
        """

        self.crew_members = crew

    def jsonable(self):
        """Return a JSON-friendly representation of the object. Use a dictionary literal rather
        than a built-in dict() to avoid built-in lookup costs. Do not simply return self.__dict__.
        It can be intercepted and mutated, adding, modifying or removing instance attributes as a
        result.

        Parameters:
            None

        Returns:
            dict: dictionary of the object's instance variables
        """

        if self.crew_members:
            crew_mates = self.crew_members.jsonable()
        else:
            crew_mates = None

        if self.passengers_on_board:
            pobs = self.passengers_on_board.jsonable()
        else:
            pobs = None

        return {
            'url': self.url,
            'name': self.name,
            'model': self.model,
            'starship_class': self.starship_class,
            'manufacturer': self.manufacturer,
            'length': self.length,
            'max_atmosphering_speed': self.max_atmosphering_speed,
            'hyperdrive_rating': self.hyperdrive_rating,
            'MGLT': self.MGLT,
            'armament': self.armament,
            'crew': self.crew,
            'crew_members': crew_mates,
            'passengers': self.passengers,
            'passengers_on_board': pobs,
            'cargo_capacity': self.cargo_capacity,
            'consumables': self.consumables
        }


def clean_data(data):
    """Convert < data > string values to provided types. < var_types > provides a mapping
    of an object's instance variables that can be converted from a string to a more
    appropriate type (e.g., 'float', 'int', 'list'). Each < var_type > key name
    corresponds to a type while each value is a tuple of instance variable names whose
    values can be converted.

    For each < data > key-value pair with a value that is not None, the function performs
    the following operations:
        1. Checks if value is a string (use isinstance(val, str))
        2. if the string value is "n/a", "none", or "unknown" the value is converted to None.
        3. Checks if < var_types > has key (e.g., if 'float' in var_types.keys()) and if
           < data > key can be found in the < var_type > key's tuple values. If the membership
           check returns True the corresponding value is converted to the type specified by the
           < var_type > key name (e.g. 'float').
        3. When splitting strings into lists the delimiter is assumed to be ', '.

    Parameters:
        data (dict): string values to convert

    Returns
        dict: updated key-value pairs
    """

    # key-value pairs that map a tuple of instance variable names to a given type (the key name)
    var_types = {
        'float': ('height', 'hyperdrive_rating', 'length', 'mass', 'orbital_period_days'),
        'int': ('cargo_capacity', 'crew', 'diameter_km', 'max_atmosphering_speed', 'moons', 'MGLT', 'passengers', 'population', 'suns'),
        'list': ('armament', 'climate', 'equipment', 'terrain')
        }

    cleaned = {}
    none_val = ['n/a', 'none', 'unknown', 'None', 'null', '']
    for key, val in data.items():
        if isinstance(val, str):
            if val in none_val:
                val = None
                cleaned[key] = val
            elif key in var_types['float']:
                cleaned[key] = float(val)
            elif key in var_types['int']:
                cleaned[key] = int(val)
            elif key in var_types['list']:
                cleaned[key] = val.split(', ')
            else:
                cleaned[key] = val # PLACEHOLDER REMOVE WHEN IMPLEMENT IF-ELIF...-ELSE STATEMENTS
        else:
            cleaned[key] = val # non str key-value pairs

    return cleaned


def create_droid(data):
    """Creates a Droid instance from dictionary data, converting string values to the appropriate
    type whenever possible. Adding special instructions constitutes a seperate operation.

    Parameters:
        data (dict): source data

    Returns:
        Person: new Person instance
    """

    droid = Droid(
        data.get('url'),
        data.get('name'),
        data.get('model'),
        data.get('manufacturer'),
        data.get('create_year'),
        data.get('height'),
        data.get('mass'),
        data.get('equipment')
        #data.get('instructions')
    )
    return droid


def create_person(data, planets=None):
    """Creates a Person instance from dictionary data, converting string values to the appropriate
    type whenever possible. Calls < get_swapi_resource() > to retrieve homeworld and species data.
    Calls < create_planet() > and < create_species() > to add homeworld and species objects to the
    person instance.

    Parameters:
        data (dict): source data
        planets (list): supplemental planetary data

    Returns:
        Person: new Person instance
    """

    person = Person(data.get('url'), data.get('name'), data.get('birth_year'), data.get('height'), data.get('mass'))

    if data.get('homeworld'):
        homeworld_data = get_swapi_resource(data['homeworld'])
        if planets:
            planet_data = get_wookieepedia_planet(planets, homeworld_data['name'])
            if planet_data:
                homeworld_data.update(planet_data)
        homeworld_data = clean_data(homeworld_data)
        person.homeworld = create_planet(homeworld_data)

    if data.get('species'):
        species_data = get_swapi_resource(data['species'][0])
        species_data = clean_data(species_data)
        person.species = create_species(species_data)

    return person


def create_planet(data):
    """Creates a Planet instance from dictionary data, converting string values to the
    appropriate type whenever possible.

    Parameters:
        data (dict): source data

    Returns:
        Planet: new Planet instance
    """

    planet = Planet(
        data.get('url'),
        data.get('name'),
        data.get('region'),
        data.get('sector'),
        data.get('suns'),
        data.get('moons'),
        data.get('orbital_period_days'),
        data.get('diameter_km'),
        data.get('gravity'),
        data.get('climate'),
        data.get('terrain'),
        data.get('population'),
    )
    return planet


def create_species(data):
    """Returns a Species instance from provided dictionary data.

    Parameters:
        data (dict): source data

    Returns:
        Species: new Species instance
    """
    species = Species(
        data.get('url'),
        data.get('name'),
        data.get('classification'),
        data.get('designation'),
        data.get('language')
    )
    return species


def create_starship(data):
    """Creates a Starship instance from dictionary data, converting string values to the
    appropriate type whenever possible. Assigning crews and passengers consitute separate
    operations.

    Parameters:
        data (dict): source data

    Returns:
        starship: a new Starship instance
    """

    starship = Starship(
        data.get('url'),
        data.get('name'),
        data.get('model'),
        data.get('starship_class'),
        data.get('manufacturer'),
        data.get('length'),
        data.get('max_atmosphering_speed'),
        data.get('hyperdrive_rating'),
        data.get('MGLT'),
        data.get('armament'),
        data.get('crew'),
        data.get('passengers'),
        data.get('cargo_capacity'),
        data.get('consumables')
        #data.get('crew_members'),
        #data.get('passengers_on_board')
    )

    return starship


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


def get_wookieepedia_planet(planets, name):
    """Returns planet data sourced from Wookieepedia, if any, per provided planet
    name.

    Parameters:
        planets (list): list of planet dictionarys
        name (str): name of planet to locate

    Returns:
        dict: planet dictionary
    """

    for planet in planets:
        if planet['name'] == name:
            return planet

    #return planet


def read_csv_into_dicts(filepath, delimiter=','):
    """Accepts a file path, creates a file object, and returns a list of
    dictionaries that represent the row values using the cvs.DictReader().

    Parameters:
        filepath (str): path to file
        delimiter (str): delimiter that overrides the default delimiter

    Returns:
        list: nested dictionaries representing the file contents
     """

    with open(filepath, mode='r', newline='', encoding='utf-8-sig') as file_obj:
        data = list(csv.DictReader(file_obj))
    return data


def read_json(filepath):
    """Reads a JSON document, decodes the file content, and returns a list or dictionary if
    provided with a valid filepath.

    Parameters:
        filepath (str): path to file.

    Returns:
        dict/list: dictionary or list representations of the decoded JSON document.
    """

    with open(filepath, 'r', encoding='utf-8') as file_obj:
        return json.load(file_obj)


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
    """Entry point for program."""

    endpoint = 'https://swapi.py4e.com/api'

    # ABSOLUTE PATH (VS CODE DEBUGGER-FRIENDLY)
    # WARN: autograder does not require absolute paths
    # abs_path = os.path.dirname(os.path.abspath(__file__))
    # print(f"\n0.0: Absolute directory path = {abs_path}")

    # Example: absolute filepath (create)
    # filepath = os.path.join(abs_path, 'stu_swapi_species_wookiee.json')

    # Example: relative filepath
    # filepath = 'stu_swapi_species_wookiee.json'


    # CHALLENGE 02 SPECIES

    response = get_swapi_resource(url="https://swapi.py4e.com/api/species/", params={'search': 'wookiee'})
    wookiee_data = response['results'][0]
    #print(wookiee_data)
    wookiee = create_species(wookiee_data)
    #print(wookiee)

    write_json(filepath='stu_swapi_species_wookie.json', data=wookiee.jsonable())


    # CHALLENGE 03 PLANET

    response = get_swapi_resource(url="https://swapi.py4e.com/api/planets/", params={'search': 'hoth'})
    hoth_data = response['results'][0]
    #print(hoth_data)
    wookiee_planets = read_csv_into_dicts(filepath='wookieepedia_planets.csv')
    #print(wookiee_planets)
    hoth_data.update(wookiee_planets[5])
    #print(hoth_data)
    hoth = create_planet(hoth_data)
    #print(hoth)
    write_json(filepath='stu_swapi_planet_hoth.json', data=hoth.jsonable())


    # CHALLENGE 04 DROID

    response = get_swapi_resource(url="https://swapi.py4e.com/api/people/", params={'search': 'r2-d2'})
    r2_d2_data = response['results'][0]
    #print(r2_d2_data)
    wookiee_droids = read_json('wookieepedia_droids.json')
    #print(wookiee_droids)
    r2_d2_data.update(wookiee_droids[2])
    #print(r2_d2_data)
    r2_d2 = create_droid(r2_d2_data)
    #print(r2_d2)
    write_json(filepath='stu_swapi_droid_r2_d2.json', data=r2_d2.jsonable())


    # CHALLENGE 05 PERSON

    response = get_swapi_resource(url="https://swapi.py4e.com/api/people/", params={'search': 'Leia'})
    leia_data = response['results'][0]
    #print(leia_data)
    wookiee_people = read_json('wookieepedia_people.json')
    #print(wookiee_people[4])
    leia_data.update(wookiee_people[4])
    #print(leia_data)
    leia = create_person(leia_data, wookiee_planets)
    #print(leia)
    write_json(filepath='stu_swapi_person_leia.json', data=leia.jsonable())



    # CHALLENGE 07 STARSHIP

    response = get_swapi_resource(url="https://swapi.py4e.com/api/starships/", params={'search': 'T-70 X-wing'})
    x_wing_data = response['results'][0]
    #print(x_wing_data)
    wookiee_starships = read_csv_into_dicts(filepath='wookieepedia_starships.csv')
    #print(wookiee_starships[1])
    x_wing_data.update(wookiee_starships[1])
    #print(x_wing_data)
    x_wing = create_starship(x_wing_data)
    #print(x_wing)
    write_json(filepath = 'stu_swapi_starship_x_wing.json', data=x_wing.jsonable())



    # CHALLENGE 08 CLEAN_DATA()

    x_wing_data_cleaned = clean_data(x_wing_data)
    x_wing = create_starship(x_wing_data_cleaned)
    write_json(filepath = 'stu_swapi_starship_x_wing_cleaned.json', data=x_wing.jsonable())

    # CHALLENGE 09. MISSION TO JAKKU
    # 9.1
    response = get_swapi_resource(url="https://swapi.py4e.com/api/people/", params={'search': 'Poe'})
    poe_data = response['results'][0]
    #print(poe_data)
    poe_data.update(wookiee_people[6])
    #print(poe_data)
    poe_data = clean_data(poe_data)
    #print(poe_data)
    poe = create_person(poe_data, wookiee_planets)
    #print(poe)

    #9.2
    response = get_swapi_resource(url="https://swapi.py4e.com/api/people/", params={'search': 'BB8'})
    bb8_data = response['results'][0]
    bb8_data.update(wookiee_droids[0])
    bb8_data = clean_data(bb8_data)
    #print(bb8_data)
    bb8 = create_droid(bb8_data)
    #print(bb8)

    #9.3
    response = get_swapi_resource(url="https://swapi.py4e.com/api/planets/", params={'search': 'jakku'})
    jakku_data = response['results'][0]
    jakku_data.update(wookiee_planets[-4])
    jakku_data = clean_data(jakku_data)
    #print(jakku_data)
    jakku = create_planet(jakku_data)
    #print(jakku)

    #9.4
    flight_plan = {
        'flight_plan': {
            'destination': jakku.jsonable(),
            'hyperspace_route': "Burke's Trailing",
            'year': "34 ABY"
        }
    }
    bb8.store_instructions(flight_plan)

    #9.5
    lor_data = wookiee_people[5]
    lor_data = clean_data(lor_data)
    lor = create_person(lor_data, wookiee_planets)

    lor_dict = {
        'locate_person': lor.jsonable()
    }
    bb8.store_instructions(lor_dict)

    #9.6
    pass_to_crew_dict = {'pilot': poe, 'astro_mech_droid': bb8}
    x_wing_crew = Crew(pass_to_crew_dict)
    x_wing.assign_crew_members(x_wing_crew)

    #9.7
    write_json(filepath = 'stu_episode_vii_mission_jakku.json', data=x_wing.jsonable())


    # CHALLENGE 10 STAR MAP (ATTACK ON TUANUL)
    #10.1
    wookiee_star_map = read_json('wookieepedia_star_map.json')
    wookiee_star_map = clean_data(wookiee_star_map)

    star_map = {
        'star_map': wookiee_star_map
    }
    bb8.store_instructions(star_map)

    #10.2
    write_json(filepath = 'stu_episode_vii_star_map.json', data=bb8.jsonable())


    # CHALLENGE 11 ESCAPE FROM JAKKU
    # 11.1
    response = get_swapi_resource(url="https://swapi.py4e.com/api/people/", params={'search': 'rey'})
    rey_data = response['results'][0]
    rey_data.update(wookiee_people[7])
    rey_data = clean_data(rey_data)
    rey = create_person(rey_data, wookiee_planets)
    #print(rey)

    #11.2
    response = get_swapi_resource(url="https://swapi.py4e.com/api/people/", params={'search': 'finn'})
    finn_data = response['results'][0]
    finn_data.update(wookiee_people[1])
    finn_data = clean_data(finn_data)
    finn = create_person(finn_data, wookiee_planets)
    #print(finn)

    #11.3
    response = get_swapi_resource(url="https://swapi.py4e.com/api/starships/", params={'search': 'Millennium Falcon'})
    m_falcon_data = response['results'][0]
    m_falcon_data.update(wookiee_starships[4])
    m_falcon_data = clean_data(m_falcon_data)
    m_falcon = create_starship(m_falcon_data)
    #print(m_falcon)

    #11.4
    crew_dict_to_pass = {'pilot': rey, 'gunner': finn}
    m_falcon_crew = Crew(crew_dict_to_pass)
    m_falcon.assign_crew_members(m_falcon_crew)

    #11.5
    list_2_pass = [bb8]
    m_falcon_passengers = Passengers(list_2_pass)
    #print(m_falcon_passengers)
    m_falcon.add_passengers(m_falcon_passengers)

    #11.6
    write_json(filepath = 'stu_episode_vii_escape_jakku.json', data=m_falcon.jsonable())


    # CHALLENGE 12 JOURNEY TO TAKODANA
    # 12.1
    response = get_swapi_resource(url="https://swapi.py4e.com/api/people/", params={'search': 'Han Solo'})
    han_solo_data = response['results'][0]
    han_solo_data.update(wookiee_people[2])
    han_solo_data = clean_data(han_solo_data)
    han_solo = create_person(han_solo_data, wookiee_planets)
    #print(han_solo)

    #12.2
    response = get_swapi_resource(url="https://swapi.py4e.com/api/people/", params={'search': 'Chewbacca'})
    chewie_data = response['results'][0]
    chewie_data.update(wookiee_people[0])
    chewie_data = clean_data(chewie_data)
    chewie = create_person(chewie_data, wookiee_planets)
    #print(chewie)

    #12.3
    crew_list_yet_again = {'pilot': han_solo, 'co-pilot': chewie}
    m_falcon_crew = Crew(crew_list_yet_again)
    m_falcon.assign_crew_members(m_falcon_crew)

    #12.4
    even_more_passengers = [rey, finn, bb8]
    m_falcon_passengers = Passengers(even_more_passengers)
    m_falcon.add_passengers(m_falcon_passengers)
    #print(m_falcon)

    #12.5
    write_json(filepath='stu_episode_vii_journey_takodana.json', data=m_falcon.jsonable())




if __name__ == '__main__':
    main()
