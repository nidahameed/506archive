import json
import requests

# SI 506 Lecture 22

def get_swapi_resource(uri, params=None, timeout=10):
    """Description removed. You will soon write it.

    Parameters:
        uri (str): a url that specifies the resource.
        params (dict): optional dictionary of querystring arguments.
        timeout (int): timeout value in seconds

    Returns:
        dict: dictionary representation of the decoded JSON.
    """

    if params:
        return requests.get(uri, params, timeout=timeout).json()
    else:
        return requests.get(uri, timeout=timeout).json()


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
    """Program entry point."""

    # 1.0 TEST PIP INSTALL OF REQUESTS PACKAGE
    # Run swapi_request_solution.py

    # 2.0 SWAPI ENDPOINT (REMOTE SERVICE)
    # Only accepts GET requests (no PUT, POST, DELETE requests accepted)

    endpoint = 'https://swapi.py4e.com/api'


    # 2.1 SWAPI: RETURN DICT OF AVAILABLE RESOURCES (n=6)
    # /api/
    response = requests.get(endpoint + '/') # note trailing slash
    resources = response.json() # convert message payload to dict

    # TODO UNCOMMENT
    print(f"\n2.1 SWAPI Resources (n={len(resources)})")
    for key, val in resources.items():
        print(f"{key.capitalize()}: {val}")

    # TODO UNCOMMENT
    # Write to file
    # output_path = 'swapi_resources.json'
    # write_json(output_path, resources)


    # 2.2 SWAPI: REQUEST RESOURCES BY CATEGORY (PAGED RESPONSE n=10 records)
    # /api/:category/

    uri = f"{endpoint}/people/"
    response = requests.get(uri)

    payload = response.json() # decode
    payload_count = payload['count']
    people_returned = len(payload['results']) # SWAPI only returns max 10 records per request
    people = payload['results']

    # TODO UNCOMMENT
    print(f"\n2.2: Payload count = {payload_count}; People returned = {people_returned}\n")

    # print(f"\n2.2: People returned (names only)")
    for person in people:
        print(person['name'])

    # TODO UNCOMMENT
    # Write to file
    output_path = 'swapi_people_page_01.json'
    write_json(output_path, people)


    # 2.3 SWAPI: REQUEST SINGLE RESOURCE BY ID
    # /api/:category/:id/

    uri = f"{endpoint}/people/1/" # Luke Skywalker
    response = requests.get(uri) # JSON representation of person returned
    person = response.json() # decode to dict

    # TODO UNCOMMENT
    # print(f"\n2.3: Request person by id = {person}")

    # TODO UNCOMMENT
    # Write to file
    output_path = 'swapi_luke_skywalker.json'
    write_json(output_path, person)


    # 2.4 SWAPI: SEARCH CATEGORY FOR RESOURCE(S)
    # /api/:category/?search=<search term>

    uri = f"{endpoint}/starships/"
    params = {'search': 'wing'} # dict
    response = requests.get(uri, params)

    payload = response.json() # decode
    starships = payload['results']

    # TODO UNCOMMENT
    print(f"\n2.4: Search Starships ('wing') = {starships[0]}") # first element only

    # TODO UNCOMMENT
    # Write to file
    output_path = 'swapi_starships_wing.json'
    write_json(output_path, starships)


    # 2.5 SWAPI: REQUEST FUNCTION/METHOD CHAINING

    # Get the Empire Strikes Back (1980)
    uri = f"{endpoint}/films/"
    params = {'search': 'empire strikes back'}
    payload = requests.get(uri, params).json() # .get() function, response.json() method chaining
    film = payload['results'][0]

    # TODO UNCOMMENT
    print(f"\n2.5: Film = {film['title']} ({film['release_date']})")

    # TODO UNCOMMENT
    # Write to file
    output_path = 'swapi_film_empire.json'
    write_json(output_path, film)

    # Get Yoda
    uri = f"{endpoint}/people/"
    params = {'search': 'yoda'}

    # TODO IMPLEMENT
    yoda = requests.get(uri, params).json()['results'][0]

    # TODO UNCOMMENT
    print(f"\n2.5: Yoda = {yoda}")

    # TODO UNCOMMENT
    # Write to file
    # output_path = 'swapi_yoda.json'
    # write_json(output_path, yoda)

    # 2.6 Additional Response properties
    # Get Yoda
    uri = f"{endpoint}/people/"
    params = {'search': 'chewbacca'}
    #response = requests.get(uri, params)

    # TODO UNCOMMENT

    # Status code
    # print(f"\n2.6 Response status code = {response.status_code}")

    # Response headers
    # print(f"\n2.6 Response headers = {response.headers}")

    # Encoding
    # print(f"\n2.6 Response encoding = {response.encoding}")

    # Check for bad request
    # if response.raise_for_status():
    #     print(f"\n2.6 Bad request")
    # else:
    #     print(f"\n2.6 Valid request")

    # TODO UNCOMMENT
    # Decode response
    # name = response.json()['results'][0]['name']
    # print(f"\n2.6 Resource name = {name}")


    # 3.0 UTILITY FUNCTIONS

    # Search and retrieve the astromech droid R2-D2
    uri = f"{endpoint}/people"
    params = {'search': 'r2'}

    # TODO IMPLEMENT
    # Call function, pass args
    r2_d2 = get_swapi_resource(uri, params)['results'][0]
    #r2_d2 = response['results'][0]

    # TODO UNCOMMENT
    print(f"\n3.0 R2-D2 = {r2_d2}\n")

    # TODO UNCOMMENT
    # Write to file
    output_path = 'swapi_r2d_d2.json'
    write_json(output_path, r2_d2)


if __name__ == '__main__':
    main()
