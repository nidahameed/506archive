# SI 506 Lecture 21

## Topics

1. Install the requests module using pip (pre-req).
2. Understands the basics of the HTTP request/response communication cycle.
3. Learn how to use the requests package to send HTTP GET requests to an endpoint.
4. Learn how to retrieve data from the Star Wars API.
5. Write utility functions to retrieve SWAPI resources and write JSON to a file.

## Vocabulary

* __API__: Application Programming Interface that species a set of permitted interactions between
  systems.
* __HTTP__: An application layer protocol designed to facilitate the distributed transmission of
  hypermedia. Web data communications largely depends on HTTP.
* __JSON__: Javascript Object Notation, a lightweight data interchange format.
* __Resource__: A named object (e.g., document, image, service, collection of objects) that is both
  addressable and accessible via an API.
* __URI__: Uniform Resource Identifier that identifies unambiguously a particular resource.

## 1.0 The requests package

The authors of the [requests package](https://requests.readthedocs.io/en/master/) describes it as
"an elegant and simple HTTP library for Python, built for human beings." With a single line of code
you can initiate communication over HTTP with a system that provides an
application programming interface (API) for accessing resources (i.e., objects) remotely. You can
utilize the requests package&mdash;imported as a module&mdash;to create, retrieve, modify, and
delete resources stored on servers and accessible via the HTTP protocol.

### 1.1 Install requests

Read the relevant install guide and use `pip` from the command line to install the
[requests](https://pypi.org/project/requests/) package.

* [macOS](https://www.si506.org/resources/mac-install_requests_package/)
* [Windows](https://www.si506.org/resources/win-install_requests_package/)

### 1.2 Confirm installation

Open VS Code or your source code editor/IDE of choice and run the file `swapi_test.py` from either
the command line (preferred) or directly from inside VS Code or other source code editor/IDE:

```python
import requests

# 1.0 SWAPI resource URI (Uniform Resource Identifier)
resource = 'https://swapi.py4e.com/api/people/4/'

# 2.0 HTTP GET request / response
# Returns an instance of requests.models.Response
response = requests.get(resource)

# 2.1 response object type
print(f"\nresponse = {type(response)}")

# 3.0 Decode JSON response (to str)
json = response.text # returns a string

print(f"\njson ({type(json)}) = {json}")

# 4.0 Decode JSON response (to dict)
person = response.json() # you will call this regularly

print(f"\nPerson ({type(person)}) = {person}")

# 4.1 Print person name
print(f"\n{person['name']}\n")
```

:exclamation: if VS Code does not recognize the `import requests` statement in your Python file or
you encounter a `ModuleNotFoundError` when running the file after pressing the green run button,
then VS Code is likely using the wrong Python environment. You can check which Python environment VS Code is using by first checking the Python version listed in the Side Bar (bottom left) of the interface. If it is a version other than what you installed at the beginning of the course, you may
need to "repoint" VS Code to the right environment. To do so, type `Cmd-Shift-P` (macOS) or `Ctrl-Shift-P` (Windows) to activate the Command Palette. Then in the search box type: "Python:
Select Interpreter". From the list of options, click on the relevant Python interepreter (e.g.,
Python 3.8.5 64-bit). You may need to restart VS Code before re-running the file. If the runtime
error persists contact the teaching team via Piazza.

For more info see, VS Code's
["Using Python Environments in VS Code"](https://code.visualstudio.com/docs/python/environments)

## 2.0 The Star Wars API (SWAPI)

The [Star Wars API](https://swapi.py4e.com/) (SWAPI) provides an API for retrieving representations
of films, people, planets, species, starships, and vehicles associated with the series situated
_a long time ago in a galaxy far, far away. . . ._

:exclamation: The SWAPI API currently accepts `GET` requests only (no `PUT`, `POST`, `DELETE`
requests accepted).

SWAPI provides the following endpoint for requesting resources:

```python
endpoint = 'https://swapi.py4e.com/api'
```

:bulb: For more information on how to utilize SWAPI to retrieve resources, see the SWAPI
[documentation](https://swapi.py4e.com/documentation) page.

:exclamation: Do _not_ use any of the available SWAPI helper libraries to write your code. You will
interact with SWAPI using the [requests](https://pypi.org/project/requests/) module only.

### 2.1 Get SWAPI resource categories (`/api/`)

To return a dictionary of key-value pairs that represent the current SWAPI resource categories,
add a trailing slash (`/`) to the endpoint when passing the URI to the `requests.get()` method.

:bulb: call the response object's `json()` method to "decode" the message as a list or dictionary.

```python
response = requests.get(endpoint + '/') # note trailing slash
resources = response.json() # convert message payload to dict

print(f"\n2.1 SWAPI Resources (n={len(resources)})")
for key, val in resources.items():
    print(f"{key.capitalize()}: {val}")
```

### 2.2 SWAPI: request resources by category (`/api/:category/`)

You can retrieve a collection of resources by category (e.g., people) by employing the following URI pattern:

`/api/:category/`

as in

`https://swapi.py4e.com/api/people/`

:exclamation: Note that SWAPI will _not_ respond by returning a collection of all people resources.
Instead, SWAPI responses are "paged", with each paged response limited to a max of ten (10) records
per request.

```python
uri = f"{endpoint}/people/"
response = requests.get(uri)

payload = response.json() # decode
payload_count = payload['count']
people_returned = len(payload['results']) # SWAPI only returns max 10 records per request
people = payload['results']

print(f"\n2.2: Payload count = {payload_count}; People returned = {people_returned}\n")

print(f"\n2.2: People returned (names only)")
for person in people:
    print(person['name'])
```

SWAPI will respond with the following JSON document with a paged list of resources stored in a
"results" list along with a URI that can be used to retrieve the next set of paged resources.

```json
{
    "count": 87,
    "next": "https://swapi.py4e.com/api/people/?page=2",
    "previous": null,
    "results": [{
        "name": "Luke Skywalker",
        "height": "172",
        "mass": "77",
        "hair_color": "blond",
        "skin_color": "fair",
        "eye_color": "blue",
        "birth_year": "19BBY",
        "gender": "male",
        "homeworld": "https://swapi.py4e.com/api/planets/1/",
        "films": [
          "https://swapi.py4e.com/api/films/2/",
          "https://swapi.py4e.com/api/films/6/",
          "https://swapi.py4e.com/api/films/3/",
          "https://swapi.py4e.com/api/films/1/",
          "https://swapi.py4e.com/api/films/7/"
        ],
        "species": [
          "https://swapi.py4e.com/api/species/1/"
        ],
        "vehicles": [
          "https://swapi.py4e.com/api/vehicles/14/",
          "https://swapi.py4e.com/api/vehicles/30/"
        ],
        "starships": [
          "https://swapi.py4e.com/api/starships/12/",
          "https://swapi.py4e.com/api/starships/22/"
        ],
        "created": "2014-12-09T13:50:51.644000Z",
        "edited": "2014-12-20T21:17:56.891000Z",
        "url": "https://swapi.py4e.com/api/people/1/"
      },
      { < Person object > },
      { < Person object > },
      { < Person object > },
      { < Person object > },
      { < Person object > },
      { < Person object > },
      { < Person object > },
      { < Person object > },
      { < Person object > }
    ]
  }
```

### 2.3 SWAPI: request single instance by id (/api/:category/:id/)

You can retrieve a single resource by specifying both its category and identifier (number only) of
by employing the following URI pattern:

`/api/:category/:id/`

as in

`https://swapi.py4e.com/api/people/1/`

```python
uri = f"{endpoint}/people/1/" # Luke Skywalker
response = requests.get(uri) # JSON representation of person returned
person = response.json() # decode to dict

print(f"\n2.3: Request person by id = {person}")
```

SWAPI will respond with a JSON document of the requested resource if it exists:

```json
{
  "name": "Luke Skywalker",
  "height": "172",
  "mass": "77",
  "hair_color": "blond",
  "skin_color": "fair",
  "eye_color": "blue",
  "birth_year": "19BBY",
  "gender": "male",
  "homeworld": "https://swapi.py4e.com/api/planets/1/",
  "films": [
    "https://swapi.py4e.com/api/films/1/",
    "https://swapi.py4e.com/api/films/2/",
    "https://swapi.py4e.com/api/films/3/",
    "https://swapi.py4e.com/api/films/6/",
    "https://swapi.py4e.com/api/films/7/"
  ],
  "species": [
    "https://swapi.py4e.com/api/species/1/"
  ],
  "vehicles": [
    "https://swapi.py4e.com/api/vehicles/14/",
    "https://swapi.py4e.com/api/vehicles/30/"
  ],
  "starships": [
    "https://swapi.py4e.com/api/starships/12/",
    "https://swapi.py4e.com/api/starships/22/"
  ],
  "created": "2014-12-09T13:50:51.644000Z",
  "edited": "2014-12-20T21:17:56.891000Z",
  "url": "https://swapi.py4e.com/api/people/1/"
}
```

### 2.4 SWAPI: search category by resources (`/api/:category/?search=<search term>`)

The SWAPI API also facilitates text-based searching of resources. This feature is limited currently
to name (all resources), title (Film) and model (Starship, Vehicle) searches. The search feature
employs _case-insensitive_ partial matches (i.e., contains) on searchable fields.

You can search a category by employing the following URI pattern, which appends a querystring to
the URI:

`/api/:category/?search=<search term>`

as in

`https://swapi.py4e.com/api/starships/?search=wing`

Convienently, the `requests.get()` function defines a second parameter named "params" for passing
querystring key-value pairs as dictionary key-value pairs as an optional argument.

```python
uri = f"{endpoint}/starships/"
params = {'search': 'wing'} # dict
response = requests.get(uri, params) # pass search parameters as 2nd argument

payload = response.json() # decode
starships = payload['results']

print(f"\n2.4: Search Starships ('wing') = {starships[0]}") # first element only
```

:bulb: one can solve the paging challenge by writing a [recursive function](https://realpython.com/python-thinking-recursively/) that calls itself repeatedly in order to return every paged set of
records. But learning how to write such a function is out of scope for SI 506.

### 2.5 SWAPI: method chaining

Note that you can chain the `response.json()` method call to `requests.get()` function call:

```python
# Get the Empire Strikes Back (1980)
uri = f"{endpoint}/films/"
params = {'search': 'empire strikes back'}
payload = requests.get(uri, params).json() # response.json() method chaining
film = payload['results'][0]

print(f"\n2.5: Film = {film['title']} ({film['release_date']})")
```

Note that you can also add bracket notation to retrieve an element from the returned "results" list:

```python
# Get Yoda
uri = f"{endpoint}/people/"
params = {'search': 'yoda'}
yoda = requests.get(uri, params).json()['results'][0] # whoa

print(f"\n2.5: Yoda = {yoda}")
```

### 2.6 Other Response object properties and methods

The return value of the `requests.get()` function is an instance of the `requests.Response` class.
The object is provisioned with a number of instance variables and methods. Although you will not be
required to make use of these variables or methods you should consider familiarizing yourself with the request module's [API](https://requests.readthedocs.io/en/latest/api/#) as you learn how to use it.

```python
# 2.6 Additional Response properties
    # Get Yoda
    uri = f"{endpoint}/people/"
    params = {'search': 'chewbacca'}
    response = requests.get(uri, params)

    # Status code
    print(f"\n2.6 Response status code = {response.status_code}")

    # Response headers
    print(f"\n2.6 Response headers = {response.headers}")

    # Encoding
    print(f"\n2.6 Response encoding = {response.encoding}")

    # Check for bad request
    if response.raise_for_status():
        print(f"\n2.6 Bad request")
    else:
        print(f"\n2.6 Valid request")

    # Decode response
    name = response.json()['results'][0]['name']
    print(f"\n2.6 Resource name = {name}")
```

## 3.0 Utility functions

Given that you will be making frequent requests to the SWAPI endpoint in order to retrieve resources
we should implement a function to handle the task. Since you will also be working with JSON documents
between now and the end of the semester implmenting a function that can read a JSON document as
well one that can write a JSON document to a file will prove useful.

## 3.1 get_swapi_resource()

This function "wraps" the request module's `requests.get()` function and permits sending requests
with and without querystring parameters. The function returns a decoded representation of a SWAPI
JSON resource.

:bulb: note that the function also sets a timeout value in seconds. This sets a limit on the wait time
allowed for a remote service to send back a response. If the wait time exceeds the timeout value
an exception is raised. You can test this feature by calling the function and passing to it a
timeout value of 0.001.

```python
def get_swapi_resource(uri, params=None, timeout=10):
    """Returns a decoded representation of a SWAPI JSON resource.

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
```

### 3.2 read_json()

This function reads a JSON document per the provided filepath, calls the json module's `json.load()` function in order to _decode_ the file data as a `dict` or a `list` (of dictionaries), and returns
the decoded data to the caller.

```python
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
```

### 3.3 write_json()

This function accepts a dictionary or a list of dictionaries, calls the json module's `json.dump()` function in order to _encode_ the passed in data as JSON, and writes the encoded data to the target
file.

```python
def write_json(filepath, data):
    """Encodes the object as JSON. Writes content to the provided filepath.

    Parameters:
        filepath (str): the path to the file.
        data (dict)/(list): the data to be encoded as JSON and written to the file.

    Returns:
        None
    """

    with open(filepath, 'w', encoding='utf-8') as file_obj:
        json.dump(data, file_obj, ensure_ascii=False, indent=2)
```
