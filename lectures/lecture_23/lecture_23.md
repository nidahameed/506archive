# SI 506: Lecture 23

## Topics

1. Work with the Star Wars API and local JSON files using the `requests` and `json` modules.
2. Implement class methods
3. Use a class' `__dict__` variable to create instance variables dynamically.
4. Use the built-in functions `setattr()`, `hasattr()`, and `delattr()`.
5. Render JSON-friendly representations of class instances with a `jsonable()` method.
6. Encode an object as JSON and write it to a file.

## Vocabulary

* __API__: Application Programming Interface that species a set of permitted interactions between
  systems.
* __HTTP__: An application layer protocol designed to facilitate the distributed transmission of
  hypermedia. Web data communications largely depends on HTTP.
* __JSON__: Javascript Object Notation, a lightweight data interchange format.
* __Resource__: A named object (e.g., document, image, service, collection of objects) that is both
  addressable and accessible via an API.
* __URI__: Uniform Resource Identifier that identifies unambiguously a particular resource.

## 1.0 json module

Like the `csv` module the Python standard libary's `json` module provides enhanced functionality for
working with JSON files. JSON is a lightweight data interchange format for exchanging information
between systems.

To use the `json` module you must import it in your Python file:

```python
import json
```

There are four `json` module functions; two of which are of particular interest to us:

1. __`json.load()`__ -- _deserializes_ (decodes) a text or binary file that contains a JSON document
   to a `dict` or `list`.
2. `json.loads()` -- _deserializes_ (decodes) a string, bytes, or bytearry containing a JSON
   document to a `dict` or `list`.
3. __`json.dump()`__ -- _serializes_ (encodes) an object as a JSON formatted stream to be stored in a file.
4. `json.dumps()` -- _serializes_ (encodes) an objecty to a JSON formatted string.

### 1.1 Reading JSON files (`json_load()`)

The function `read_json()` reads a JSON document per the provided filepath, calls the json module's
`json.load()` function in order to _decode_ the file data as a `dict` or a `list` (of dictionaries),
and returns the decoded data to the caller.

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

### 1.1 Reading JSON files (`json_dump()`)

The function `write_json()` accepts a dictionary or a list of dictionaries, calls the json module's
`json.dump()` function in order to _encode_ the passed in data as JSON, and writes the encoded data
to the target file.

```python
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
```

## Challenges

Today's challenge involves making crew assignments to the
[Millennium Falcon](https://starwars.fandom.com/wiki/Millennium_Falcon), a modified Corellian
YT-1300f light freighter employed by the smugglers during the Galactic Civil War.
### CHALLENGE 01

Retrieve a JSON representation of the Millennium Falcon data from SWAPI (a starship) and combine it
with the "local" Wookieepedia Millennium Falcon data stored in `wookieepedia_m_falcon.json`.  Assign
the combined data to the variable `swapi_m_falcon` (`dict`).

### CHALLENGE 02

Create a Millennium Falcon instance of `Starship` and assign it to the variable `m_falcon`. Assign
all `swapi_m_falcon` values to the matching `m_falcon` instance variables.

### CHALLENGE 03

Retrieve JSON representations of both Han Solo and Chewbacca (people) and create associated `Person`
instances for each, assigned to the variables `solo` and `chewie` respectively. Call the `Person`
`add_homeworld()` for each instance, passing the relevant homeworld URL to it as an argument.

### CHALLENGE 04

Implement the `Crew` class' `__init__()` and `jsonable()` methods.

:bulb:  `__init__()` method implementation: loop over the passed in `members` dictionary and call
the built-in `setattr()` (i.e., set attribute) function to both create instance variables
(using the key as the name) and assign values to each.

```python
for key, val in members.items():
    setattr(self, key, val) # call built-in function
```

:bulb: `jsonable()` method implementation: write a `for` loop that loops over the  `Crew` class'
dunder variable expression `__dict__.items()`, which exposes each instance variable as a key-value
pair. Each key represents the name of the instance value (e.g., "pilot") while each value
corresponds to a `Person` instance. Add each key-value pair to an accumulator dictionary, calling
each `Person` instance's `jsonable()` method in order to return a JSON-friendly dictionary of
nested person dictionaries.

#### JSON-friendly representation of a Crew instance

```python
{
    'pilot': {
        'url': 'https://swapi.py4e.com/api/people/14/',
        'name': 'Han Solo',
        'birth_year': '29BBY',
        'homeworld': {
            'url': 'https://swapi.py4e.com/api/planets/22/',
            'name': 'Corellia',
            'gravity': '1 standard',
            'climate': 'temperate',
            'terrain': 'plains, urban, hills, forests',
            'population': '3000000000'
        }
    },
    'co-pilot': {
        'url': 'https://swapi.py4e.com/api/people/13/',
        'name': 'Chewbacca',
        'birth_year': '200BBY',
        'homeworld': {
            'url': 'https://swapi.py4e.com/api/planets/14/',
            'name': 'Kashyyyk',
            'gravity': '1 standard',
            'climate': 'tropical',
            'terrain': 'jungle, forests, lakes, rivers',
            'population': '45000000'
        }
    }
}
```

### Challenge 05

Implement the `Starship.assign_crew_members()` method. Then assign Hano Solo as the pilot and
Chewbacca as the co-pilot of the Millennium Falcon to the `m_falcon` instance.

### Challenge 06

Implement the `Starship.update_crew_members()` method. Then retrieve a SWAPI representation of Rey
and combine the SWAPI data with Wookieepedia-sourced data stored locally in `wookieepedia_rey.json`.
Replace Han Sol as pilot with Rey.

### Challenge 07

Implement the `Starship.remove_crew_members_by_position()` method. Once implemented remove the
the Millennium Falcon's `m_falcon` co-pilot.

### Challenge 08

Restore Chewbacca as co-pilot of the Millennium Falcon (everybody loves Chewie) and then call
`write_json()` and encode `m_falcon` as JSON and write the serialized object to the file
`si506_m_falcon.json`.
