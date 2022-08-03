# SI 506 Lecture 16

## Topics

1. The dictionary (`dict`) type
2. Dictionary methods

## Vocabulary

* __Dictionary__. An associative array or a map, wherein each specified value is associated with or
  mapped to a defined key that is used to access the value.

## 1.0 Sequence limitations

Lists and tuples are robust data structures but one downside that they both share is that neither
provides explicit hints as regards the meaning of each element or item.

```python
film = ['The Wizard of Oz', 1939, 2800000, 26100000]
```

While the first element in the above list is likely comprehensible (the film title), discerning the
meaning of the other three elements may require "insider" knowledge or an accompanying data
dictionary. Such a situation is rarely ideal when working with data.

## 2.0 The dictionary

The Python dictionary provides an alternative data structure for both _describing_ data and storing
values. Python dictionaries (the `dict` type) are considered associative arrays, wherein each
specified value is associated with or mapped to a defined key that is used to access the value.

You'll often hear people refer to dictionaries as unordered sets of key-value pairs or as _maps_.

However, since Python 3.7 dictionary order is guaranteed to be the key/value pair insertion order.
The beauty of the dictionary is the ability to identify data values by a label or key, usually
rendered as a readable string though not always (int, tuple also used as keys). In other words, you
can embed meaning into a data structure.

## 2.1 Syntax

Dictionaries are defined by enclosing within curly braces (`{}`) a comma-separated sequence of
key-value pairs. Each key-value pair is separated by a colon (`:`). Each value specified is
referenced by it's associated key rather than by its numercial position within the dictionary.

```python
# Format: {< key >: < value >}

# Single line
film = {'title': 'The Wizard of Oz', 'year_released': 1939}

# Multiple lines
film = {
    'title': 'The Wizard of Oz',
    'year_released': 1939,
    'budget': 2800000,
    'box_office_receipts': 26100000
    }

# Nested dictionary (< scary_character >)
film = {
    'title': 'The Wizard of Oz',
    'year_released': 1939,
    'budget': 2800000,
    'box_office_receipts': 26100000,
    'scary_character': {
        'name': 'The Wicked Witch of the West',
        'weapon': 'evil spells'
        }
    }

# Type
film_type = type(film) # <class 'dict'>

# Accessing a value
title = film['title']

# Accessing a nested dictionary's value
scary_character_name = film['scary_character']['name'] # chain keys
```

## 2.2 Defining a dictionary

There are several ways to define a dictionary.

### 2.2.1 Empty dictionary

```python
film = {}
film['title'] = 'Scream'
film['year_released'] = 1996
film['budget'] = 15000000
film['box_office_receipts'] = 173000000
film['scary_character'] = {} # Define nested dictionary
film['scary_character']['name'] = 'Ghostface' # chain keys
film['scary_character']['weapon'] = 'knife' # chain keys
```

### 2.2.2 Dictionary literal

```python
film = {
    'title': "A Nightmare on Elm Street 2: Freddy's Revenge",
    'year_released': 1985,
    'budget': 3000000,
    'box_office_receipts': 30000000,
    'scary_character': {
        'name': 'Freddy Krueger',
        'weapon': 'clawed glove'
        }
    }
```

### 2.2.3 Built-in `dict()` function

You can also use the built-in `dict()` function to define a dictionary. You can pass in a sequence
of keyword arguments separated by commas or pass in a sequence of tuples.

```python
# Keyword arguments (note used of nested dict())
film = dict(
    title='The Shining',
    year_released=1980,
    budget=19000000,
    box_office_receipts=46200000,
    scary_character=dict(name='Jack Torrance', weapon='Ax') #nested
    )

# Tuples (note used of nested dict())
film = dict(
    [
        ('title', 'The Shining'),
        ('year_released', 1980),
        ('budget', '19000000'),
        ('box_office_receipts', '46200000'),
        ('scary_character', dict([('name', 'Jack Torrance'), ('weapon', 'Ax')])) # nested
        ]
    )
```

## 2.3 Add, modify, delete a key-value pair

You can add a _new_ key-value pair to a dictionary by using bracket or "subscript" notation:

```python
film['director'] = 'Stanley Kubrick'
film['running_time_mins'] = 146 # premier
film['tomatometer'] = .84 # The Shining (audience score = 93%)
```

The new key-value pair is appended to the sequence of key-value pairs.

If you need to modify an existing value you can assign a new value by referencing the relevant key:

```python
film['running_time_mins'] = 144 # American release
```

If you need to delete a key-value pair you can use the built-in `del()` function.

```python
del(film['tomatometer'])
```

The above approaches holds true for nested dictionaries as well. Use bracket chaining to reference
the relevant key-value pair.

```python
film['scary_character']['actor'] = 'Jack Nicholson'
```

## 2.4 KeyError exception

If you attempt to access a dictionary value with a non-existing key you will trigger a `KeyError`.

```python
name = film['name'] # raises KeyError: 'name'
```

:hint: You can guard against this type of runtime exception by accessing dictionary methods using
the `dict.get()` method. See below for more details.

## 2.5 Dictionary methods

The Dictionary object is provisioned with several
[methods](https://www.w3schools.com/python/python_ref_dictionary.asp). For SI 506 we will focus on
the following methods:

* `dict.get()`
* `dict.keys()`
* `dict.values()`
* `dict.items()`

### 2.5.1 `dict.get()` method

```python
film = {
    'title': 'Get Out',
    'year_released': 2017,
    'budget': 4500000,
    'box_office_receipts': 255000000,
    'scary_character': {
        'name': 'Rose Armitage',
        'weapon': 'tricksterism'
        }
    }

film_name = film['name'] # raises KeyError: 'name'

film_name = film.get('name') # swallows the exception and returns None

film_name = film.get('title') # returns film title
```

### 2.5.2 `dict.keys()` method

You can retrieve all the keys in a dictionary by calling `dict.keys()`. The method returns a
`dict_keys` object, an object that provides a _view_ or a pointer to the dictionary's keys. While
you can loop over a `dict_keys` object you _cannot_ modify either the referenced keys or the
associated dictionary.

For the film dictionaries in this lecture, calling the `dict.keys()` method will return the
following object:

`dict_keys(['title', 'year_released', 'budget', 'box_office_receipts', 'scary_character'])`

:bulb: you can create a copy of the `dict_keys` object using the built-in `list()` function. Passing
the `dict_keys` object to `list()` will return a list of keys. Doing so simplifies working with the
keys.

```python
film = {
    'title': 'Halloween',
    'year_released': 1978,
    'budget': 325000,
    'box_office_receipts': 70000000,
    'scary_character': {
        'name': 'Michael Myers',
        'weapon': "chef's knife"
        }
    }

keys = film.keys() # returns dict_keys object

# Loop over dict_keys object
for key in film.keys():
    print(key)

keys = list(film.keys()) # convert to a list

# Loop over keys list, print each Film value by key reference
for key in keys:
    print(f"{film[key]}") # returns value
```

### 2.5.3 `dict.values()`

You can retrieve all the values in a dictionary by calling `dict.values()`. The method returns a
`dict_values` object, an object that provides a _view_ or a pointer to the dictionary's values. While
you can loop over a `dict_values` object you _cannot_ modify either the referenced values or the
associated dictionary.

For the film dictionaries in this lecture, calling the `dict.values()` method will return the
following object:

`dict_values([< title >, < year_released >, < budget >, < box_office_receipts >, < scary_character >])`

:bulb: you can create a copy of the `dict_values` object using the built-in `list()` function. Passing
the `dict_values` object to `list()` will return a list of values. Doing so simplifies working with the
values.

```python
film = {
    'title': 'Psycho',
    'year_released': 1960,
    'budget': 806947,
    'box_office_receipts': 50000000,
    'scary_character': {
        'name': 'Norman Bates',
        'weapon': "chef's knife"
        }
    }

values = film.values() # return dict_values object

# Loop over dict_values object
for value in film.values():
    print(value)

# Convert to a list
values = list(film.values()) # convert to a list
```

### 2.5.4 `dict.items()` method

You can loop over a dictionary's keys _and_ values by calling the `dict.items()` method. This
method is arguably the workhorse of the various dicitonary methods.

The following example illustrates use of a nested `for` loop to access the film title from each film
in the `films` list. The loop relies on accessing each films key-value pairs by calling the
`film.items()` method.

```python
films = [
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
        'box_office_receipts': 255000000,
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

# Task: extract film title and append to < film_titles > list.
# Nested loop iterates over each film's keys and values
film_titles = []
for film in films:
    for key, val in film.items():
        if key == 'title':
            film_titles.append(val)

print(f"\nFilm titles: {film_titles}")
```

Imagine a scenario in which you are asked to create a new dictionary comprising counts of the films
in the `films` list by year. Each key-value pair would represent a year, with the key labeled with
a year (e.g., 2016) with the corresponding value equal to the number of films released during the
year. The data for the new dictionary (including key labels) wouild be derived from the `films` list.

This problem can be solved by taking advantage of each film's `dict.items()` and `dict.keys()`
methods. The inner loop relies on `film.items()` to access each film's keys and values.
Conditional logic is then employed to both filter on the key (`year_released`) and check if the value
(e.g., `2017`) exists as a key in the "accumulator" dictionary's set of keys. If the second `if`
statement's membership check using the `in` operator evaluates to `True` the corresponding `release_year_counts` key-value pair is incremented by 1. If no key match is found a new key-value
pair is added to the dictionary and seeded with a value of 1.

```python
release_year_counts = {}
for film in films:
    for key, val in film.items():
        if key == 'year_released':
            if val in release_year_counts.keys():
                release_year_counts[val] += 1 # increment count
            else:
                release_year_counts[val] = 1 # new key-value

print(f"\nFilm releases by year: {release_year_counts}")
```

Below is an alternative solution employing the logical operator `and`.

```python
release_year_counts = {}
for film in films:
    for key, val in film.items():
        keys = release_year_counts.keys() # mutates
        if key == 'year_released' and val in keys:
            release_year_counts[val] += 1 # increment count
        elif key == 'year_released' and val not in keys:
            release_year_counts[val] = 1 # new key-value

print(f"\nFilm releases by year: {release_year_counts}")
```
