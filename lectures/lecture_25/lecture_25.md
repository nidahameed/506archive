# SI 506: Lecture 25

## In-class Challenge

Write code to match the JSON document `fxt_films.json`.

## Challenge 01 Implement `Film` and `Planet` classes

Implement the `Film` and `Planet` classes and the `jsonable()` method for each. See the Docstrings
for more details.

:bulb: Focus on implementing `Film.jsonable()` only.

## Challenge 02 Retrieve SWAPI films

Call `get_swapi_resource()` and retrieve all SWAPI film resources.

:bulb: See `fxt_swapi_films.json` for how SWAPI represents a film.

## Challenge 03 Instantiate Film instances

Create a list of `Film` instances utilizing the SWAPI data as values. Assign each film instance to a
variable named `films`.

Test your work by calling `write_json()` and passing to it a JSON-friendly list of film dictionaries.
Write the serialized (encoded) JSON to a file named `stu_films.json`. Compare output against
`fxt_films.json`.

## Challenge 04 Add episode Roman numeral to Film instances

Implement the function `create_roman_numeral()` and add the matching Roman Numeral to each `Film`
instance based on its `episode_id` (e.g., episode 7 = VII)

:bulb: there are seven (7) SWAPI films (`episode_id` values range from 1 to 7).

Test your work by calling `write_json()` and passing to it a JSON-friendly list of film dictionaries.
Write the serialized (encoded) JSON to a file named `stu_films.json`. Compare output against
`fxt_films.json`.

## Challenge 05 Add simple caching

Individual planets may be associated with more than one film. Issuing repeated HTTP GET requests
to retrieve data on the same planets increases the time required for the script to complete its
tasks -- in other words, it's a potential performance bottleneck.

### 05.1 SWAPI Film references to planets

 Episode I = 3 planets
 Episode II = 5 planets
 Episode III = 13 planets
 Episode IV = 3 planets
 Episode V = 4 planets
 Episode VI = 5 planets
 Episode VII = 1 planets

That's 34 HTTP GET requests that are required to retrieve all film-related planet data including
duplicate planet data (yikes!). See `fxt_swapi_films.json` for all the planet URLs that can be
used to retrieve more data from SWAPI.

We can improve performance by adding a simpling caching feature to the script. Normally, we would
add an "expiry" feature that clears the cache after a certain period of time in order (e.g.,
60 secs, 120 secs, 3600 secs (1 hour), etc.) to reduce the likelihood that that the data stored in
the cache has not grown stale (i.e., the SWAPI service might update its data in the interim) but
this script is short-lived so we will ignore implementing a cache expiration time in the interests
of simplicity.

The goal is to write code that reduces the number of HTTP GET requests that must be made to retrieve
planet data to the absolute minimum.

First, create an empty dictionary named `cache`. The cache's key-value pairs will utilize the planet
URL as the key with the corresponding `Planet` instance as the value.

```python
cache = {
    "https://swapi.py4e.com/api/planets/1/": < planet instance >
    . . .
}
```

### 05.2 Caching workflow

Loop over the `films` list and for each film encountered loop over its list of planet URLs. Before
calling `get_swapi_resource()` to retrieve a representation of the planet, check the cache to
see it has already been retrieved and stored.

:bulb: use the built-in enumerate function when looping over the list of planet URLs so that you
can use the counter value to assign the planet instance to the film's appropriate list element (e.g.,
film.planets[i] = planets).

If the planet _is not in_ the cache, call `get_swapi_resource()` and retrieve a SWAPI representation
of the planet. Then create a new `Planet` instance using the SWAPI data, add the instance to the
cache using the URL as the key and then assign the planet instance to the `film.planets` replacing
the string URL with the planet instance.

Otherwise, if the planet was previously saved to the cache, assign it to the `film.planets`
replacing the string URL with the planet instance.

With the cache implemented we can avoid issuing duplicate HTTP GET requests that return to us
duplicate data.

Test your work by calling `write_json()` and passing to it a JSON-friendly list of film dictionaries.
Write the serialized (encoded) JSON to a file named `stu_films.json`. Compare output against
`fxt_films.json`.

:bulb: the last assignment could be refactored to include a cache. This would reduce
the number of repetitive calls made to SWAPI to retrieve a representation of the Human species.

## Challenge 06 convert `Planet` diameter and population values to type int (refactoring)

Many SWAPI string values can be converted to more appropriate types (e.g., `float`, `int`, `list`).
Let's modify the behavior of our script by implementing the function `convert_str_to_int()`.

The goal is to be able to convert the SWAPI planet values `diameter` and `population` to type
`int` _before_ creating a `Planet` instance.

:exclamation: Howver, not all `population` values are numbers masquerading as strings. In such cases
convert the value to `None`.

### SWAPI JSON representation of the ice planet Hoth

```json
{
  "name": "Hoth",
  "rotation_period": "23",
  "orbital_period": "549",
  "diameter": "7200",
  "climate": "frozen",
  "gravity": "1.1 standard",
  "terrain": "tundra, ice caves, mountain ranges",
  "surface_water": "100",
  "population": "unknown",
  "residents": [],
  "films": [
    "https://swapi.py4e.com/api/films/2/"
  ],
  "created": "2014-12-10T11:39:13.934000Z",
  "edited": "2014-12-20T20:58:18.423000Z",
  "url": "https://swapi.py4e.com/api/planets/4/"
}
```

Implement `convert_str_to_int()` and insert it in the appropriate location in `main()`.

Test your work by calling `write_json()` and passing to it a JSON-friendly list of film dictionaries.
Write the serialized (encoded) JSON to a file named `stu_films.json`. Compare output against
`fxt_films.json`.

## Appendix. Anticipated runtime exceptions

1. AttributeError: `convert_str_to_int()` fails to account for non `str` value types when
   attempting to convert values:

   ```commandline
   File ".../lecture_25/lecture_25_solution_new.py", line 121, in convert_str_to_int
   if val.lower() == 'unknown':
   AttributeError: 'list' object has no attribute 'lower'
   ````

2. ValueError: `convert_str_to_int()` fails to account for value that cannot be converted
   to an `int`.

   ```commandline
   File ".../lecture_25/lecture_25_solution_new.py", line 122, in convert_str_to_int
   converted[key] = int(val)
   ValueError: invalid literal for int() with base 10: 'unknown'
   ````

3. TypeError: `json.dump()` in `write_json()` is unable to serialize a custom object
   (e.g., `Film`).

   ```commandline
   . . .
   raise TypeError(f'Object of type {o.__class__.__name__} '
   TypeError: Object of type Film is not JSON serializable
   ```
