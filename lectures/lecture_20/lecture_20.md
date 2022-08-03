# SI 506: Lecture 20

## Topics

1. The Python class
2. Defining a class
3. Instantiating a class
4. The class constructor and the role of `self`
5. Accessing instance variables
6. Representing a class instance as a string
7. Defining instance methods
8. Calling instance methods

## Vocabulary

* __Class__: "A template for creating user-defined objects. Class definitions normally contain method definitions which operate on instances of the class." [Python Official Documentation](https://docs.python.org/3/glossary.html).
* __Instance__: An individual object whose type is defined by the class by which it was instantiated or created.
* __Instance variable__: An variable and value bound to a specific instance of a class.
* __Instance method__: A function defined by a class and bound to a specific instance of a class.
* __self__: A variable that represents an instance of a class.

## 1.0 The class

The Python class is a beautiful thing. When you define a class, say `Publication`, you provide a
blueprint, a template, or better yet, a model comprising attributes and methods that objects based
on the class are provisioned with when created or instantiated, e.g. =
`Publication('Recommender Systems', 'Resnick, P; Varian', 'COMMUNICATIONS OF THE ACM', 1997))`.
Designing custom classes allows you to instantiate (i.e., create) multiple objects of the same type.

### 1.1 Defining a `class`

Use the `class` keyword to define a class. The name of the class should employ "CamelCase" styling
using one or more nouns.

```python
class Publication:
    """Representation of a Publication."""

    pass # TODO Implement
```

### 1.2 Instantiating a class

Instantiating a class or creating an instance of a class is similar to calling a function and
assigning a return value to a variable.

```python
var = MyClass()
```

:exclamation: `class` is a reserved word and therefore is ineligble for use as a variable.

### 1.3 The class constructor and the role of `self`

In most cases instantiating a class instance requires passing in one or more required attributes.
A special "dunder" `__init__()` method is used to accomplish the task. Optional parameters with
default values can also be defined.

:exclamation: Unlike other languages, Python requires that the object instance of a class be referenced
_explicitly_ whenever accessing instance variables or calling instance methods that are bound to the
class definition. Python community practice is to refer to the class instance as `self`. When
defining a class, each variable assignment involving an instance variable _must_ be
prefixed by `self` using dot notation (`.`). Method calls _must_ also be prefixed by `self` using dot
notation (`.`). In addition, when defining a method, `self` _must_ always be listed as a parameter
and positioned first.

```python
def __init__(self, title, authors, source, year, total_citations):
    """Called after instance is created but before object is returned to the caller.
    Permits initialization of instance variables with passed in argument values.

    Parameters:
        title (str): title of publication
        authors (str): semi-colon delimited string of authors
        source (str): title of source volume
        year (int): year of publication
        total_citations (int): count of citations
        cited_publication (list): list of publications cited by this publication
        citing_publications (list): list of publications that cite this publication

    Returns
        None:
    """

    self.title = title
    self.authors = authors
    self.source = source
    self.year = int(year) # cast to int
    self.total_citations = int(total_citations) # cast to int
    self.cited_publications = [] # default value
    self.citing_publications = [] # default value
```

The example below illustrates instantiating an instance of `Publication` from data read in from a
CSV file. The `Publication` instance `publ_01` is instantiated with five (5) requried instance
attributes: title, authors, source title, publication year, total citations.

```python
# Retrieve data
data = read_csv(publ_path)
headers = data[0]

# Instantiate two Publication instances
publ_01 = Publication(
    data[1][headers.index('Title')],
    data[1][headers.index('Authors')],
    data[1][headers.index('Source Title')],
    data[1][headers.index('Publication Year')],
    data[1][headers.index('Total Citations')]
    )

publ_02 = Publication(
    data[2][headers.index('Title')],
    data[2][headers.index('Authors')],
    data[2][headers.index('Source Title')],
    data[2][headers.index('Publication Year')],
    data[2][headers.index('Total Citations')]
    )
```

Multiple `Publication` instances can be created by looping over the `data` and storing each
instance in a list.

```python
# Retrieve data
data = read_csv(publ_path)
headers = data[0]

# Create a list of Publication instances
publications = []
for publ in data[1:]:
    publications.append(
        Publication(
            publ[headers.index('Title')],
            publ[headers.index('Authors')],
            publ[headers.index('Source Title')],
            publ[headers.index('Publication Year')],
            publ[headers.index('Total Citations')]
            )
        )
```

### 1.4 Accessing instance variables

Instance variables (i.e., object attributes)) are accessed using dot notation (`.`).

```python
title = publ_01.title
```

### 1.5 Representing a class instance as a string

You can return a `str` representation of a class instance by adding a "dunder" or "magic `__str__()`
method to the the class definition. The method returns a human-friendly string representation of the
object of your own design. Implementing `__str__()` method is considered a best practice and avoids
returning the largely opaque string that provides only the object's internal identifier (e.g.,
`<__main__.Publication object at 0x106262790>`) when passing the object to the built-in
`print()` function (e.g., `print(pub_01)`).

```python
def __str__(self):
    """Human-readable representation of the object."""

    return f"{self.format_authors(self.authors)}, {self.title}, {self.source} ({self.year})"
```

## 1.6 Defining instance methods

You can define one or more instance methods that can be called once a class is instantiated. At a
minimum, `self` _must_ be defined as a parameter but other parameters can also be defined including
optional parameters.

The example method below provides the caller with the ability to converts a publication's authors
string (e.g., `"Li, Cheng; Resnick, Paul; Mei, Qiaozhu"`) to a list of author dictionaries.

```python
def split_authors_to_dicts(self):
    """Returns a list of author dictionaries derived from the original authors
    string.

    Parameters:
        None

    Returns:
        list: sequence of author dictionaries
    """

    names = []
    for author in self.authors.split('; '):
        name = author.split(', ')
        names.append({'first_name': name[1], 'last_name': name[0]}) # dict literal

    return names
```

The next example method provides a caller with the ability to confirm if the publication includes at
least one scholar in a list of passed in scholars.

```python
def has_coauthor(self, scholars):
    """Returns True if at least one member of a passed in list of scholars is found among
    the publication's authors. A match is obtained if the surname and first initial of given
    name can be matched.

    WARN: The matching rule is imperfect as it fails to distinguish between authors possessing the
    same surname and first name initial as well as authors whose surnames may have changed since a
    publication was released.

    Parameters:
        scholars (list): list of author strings < "last name, first name/initial(s)" >

    Returns:
        bool: True if match is obtained; False otherwise.

    """

    # Get authors
    authors = self.split_authors_to_dicts()

    # Match authors
    for author in authors:
        for scholar in scholars:
            name = scholar.split(', ')
            if (author['last_name'].lower() == name[0].lower() and
                author['first_name'][0].lower() == name[1][0].lower()):
                return True
    return False
```

### 1.7 Calling instance methods

Instance methods are called employing dot notation (`.`). Calling an instance method does not
require passing to it `self` as an argument.

```python
authors = publ_01.split_authors_to_dicts() # method call
```
