import requests, json

# LAB EXERCISE 10

# SETUP CODE
ENDPOINT = 'https://swapi.py4e.com/api/'

# END SETUP

# PROBLEM 01 (2.5 Points)

def get_resource(url, params=None):
    """
    This function initiates an HTTP GET request to a url to return a
    list of dictionaries. The function defines two parameters,
    the resource url (str) and an optional params (dict) query string of
    key:value pairs that may be provided as search terms (e.g., {'search': 'yoda'}).

    Parameters:
        url (str): the base url to look for response
        params (dict): the parameters to specify the query.

    Returns:
        people (list): a list of dictionaries, each of which describes a person
    """
    response = requests.get(url, params)
    people = response.json()
    return people

# END PROBLEM 01

# PROBLEM 02 (10 Points)

class Person:
    """
    This class contains selected information from the results of the API call.

    Instance Variables:
        name (str): Name of the person.
        hair_color (str): Hair color of the person.
        eye_color (str): Eye color of the person.
        species_name (str): Name of the species of the person.
    """

    def __init__(self, name, hair_color, eye_color, species_name):
        self.name = name
        self.hair_color = hair_color
        self.eye_color = eye_color
        self.species_name = species_name


    def jsonable(self):
        """Return a JSON-friendly representation of the object.
        Use a dictionary literal rather than built-in dict() to avoid
        built-in lookup costs.

        Parameters:
            None

        Returns:
            dict: dictionary of the object's instance variable values
        """

        dictionary_of_iv = {
            'name' : self.name,
            'hair color' : self.hair_color,
            'eye color' : self.eye_color,
            'species' : self.species_name
        }

        return dictionary_of_iv


    def __str__(self):
        return self.name

# END PROBLEM 02

# PROBLEM 3 (2.5 Points)

def write_json(filepath, data):
    '''
    Given a valid filepath writes data to a JSON file.

    Parameters:
        filepath (str): the path to the file.
        data (dict): the data to be encoded as JSON and written to the file.

    Returns:
        None
    '''
    with open(filepath, 'w', encoding='utf-8') as file_obj:
        json.dump(data, file_obj, ensure_ascii=False, indent=2)

# END PROBLEM 3

# PROBLEM 4 (10 Points)

def main():
    '''
    This function calls <get_resource> function to retrieve SWAPI character data. Creates an instance of < Person >. 
    Then it calls <write_json> function to store data to a json file.

    Parameters:
        None
    Return:
        None
    '''
    # Call < get_resource() > with the correct parameters and save results to < leia_data >
    base_url = ENDPOINT+'people'
    param = {'search':'leia'}
    data = get_resource(base_url, param)
    leia_data = data['results'][0]
    
    # Retrieve Leia's species and assign to < leia_species >
    species_url = leia_data['species'][0]
    species_data = get_resource(species_url)
    leia_species = species_data['name']

    leia_data['species_name'] = leia_species
    
    # Create an instance of < Person > using the data you have stored in < leia_data >
    name = leia_data['name']
    hair_color = leia_data['hair_color']
    eye_color = leia_data['eye_color']
    species_name = leia_data['species_name']

    leia = Person(name, hair_color, eye_color, species_name)
    print(leia)


    # Write out the information produced from the instance of < Person >
    leia_info = leia.jsonable()
    write_json('leia.json', leia_info)

# END PROBLEM 4

if __name__ == '__main__':
    main()

# END OF LAB EXERCISE