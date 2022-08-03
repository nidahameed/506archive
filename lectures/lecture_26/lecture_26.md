
# SI 506: Next Steps

## 1.0 Coursera U-M Python offerings (self-study)

Don't let the semester break go by without writing code. Consider signing up for a Python course on
the Coursera program. As a University of Michigan student there is no charge for enrolling in U-M
authored courses. Below is a select list of available offerings.

**Coursera. Brenda Gunderson et al, [Understanding and Visualizing Data with Python](https://www.coursera.org/learn/understanding-visualization-data)**.

Beginner. Taught by LSA Statistics Dept faculty. Apply statistical concepts in Python using Numpy, Pandas, Statsmodels, Matplotlib, and Seaborn libraries. Course uses Coursera's Jupyter Notebook online environment.

**Coursera. Paul Resnick et al, [Python 3 Programming Specialization](https://www.coursera.org/specializations/python-3-programming).**

Beginner. Taught by UMSI faculty. Largely overlaps with SI 506 but includes several
topics not covered in this course: list comprehensions, lambda expressions, and class inheritance.

**Coursera. Chris Brooks, [Introduction to Data Science in Python](https://www.coursera.org/learn/python-data-analysis).**

Intermediate. Taught by UMSI faculty. Learn how to work with the Pandas
library in order clean, manipulate, analyze tabular data. This is course one in the five course
[Applied Data Science with Python Specialization](https://www.coursera.org/specializations/data-science-python#courses).

**Coursera. Charles Severance, [Django for Everybody](https://www.coursera.org/specializations/django).**

Intermediate. Taught by UMSI faculty. Learn how to build and deploy websites using the Django
web framework, written in Python.

## 2.0 Where to next?

### 2.1 Python Styling (PEP 8)

Writing Python code to be read as well as run is a key aspect of Python programming. Jasmine summarizes ably the Python Community's [Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/) (PEP 8).

**Jasmine Finer, ["How to Write Beautiful Python Code With PEP 8"](https://realpython.com/python-pep8/) (RealPython, Dec 2018).**

### 2.2 List and Dictionary comprehensions

Learn how to create lists and dictionaries using *comprehensions*, compact
expressions that return a `list` or a `dict` and can often be written in a single line of code.

#### `for` loop

```python
films_jsonable = []
for film in films:
    films_jsonable.append(film.jsonable())

```

#### list comprehension

```python
films_jsonable = [film.jsonable() for film in films]
```

**Lisa Tagliaferri, ["Understanding List Comprehensions in Python 3"](https://www.digitalocean.com/community/tutorials/understanding-list-comprehensions-in-python-3) (DigitalOcean, Jan 2017).**

**Trey Hunner, ["Python List Comprehensions: Explained Visually"](https://treyhunner.com/2015/12/python-list-comprehensions-now-in-color/) (Trey Hunner, 15 Dec 2015).**

**Josh Robin, ["Dictionary Comprehension in Python 3 for Beginners"](https://medium.com/@joshuapaulrobin/dictionary-comprehension-in-python3-for-beginners-54fb4ddd3982) (Medium, May 2019).**

### 2.3 Lambdas (anonymous functions)

A Lambda is an anonymous function, written as a single line of execution. You will often encounter
lambdas when working with classes or functions that accept a function as an argument (e.g., `list.sort(key=lambda x:x[0])` or `sorted(some_list, key=lambda x:x[0])`)

```python
films.sort(key=lambda film: film.episode_id) # sort in-place (faster)
```

```python
films = sorted(films, key=lambda film: film.episode_id) # built-in, returns new list (slower)
```

**Andre Burgaud, ["How to Use Python Lambda Functions"](https://realpython.com/python-lambda/) (Real Python, June 2019).**

**Karim Elghamrawy, [Python: How to Sort a List? (The Right Way)](https://www.afternerd.com/blog/python-sort-list/) (afternerd.com, n.d.).**

**Trey Hunner, ["Overusing lambda expressions in Python"](https://treyhunner.com/2018/09/stop-writing-lambda-expressions/) (Trey Hunner, September 2018).**

### 2.4 Multiple arguments: *args, **kwargs

A function can be designed to accept a variable number of positional arguments (`*args`) or a
variable number of keyword arguments (`*kwargs`).

**Lisa Tagliaferri, ["How To Use *args and **kwargs in Python 3"](https://www.digitalocean.com/community/tutorials/how-to-use-args-and-kwargs-in-python-3) (DigitalOcean, November 2017).**

**Davide Mastromatteo, [Python args and kwargs: Demystified](https://realpython.com/python-kwargs-and-args/) (Real Python, September 2019)**

### 2.5 Class inheritance

SI 506 introduced you to the Python class and touched on object-oriented programming (OOP) and class
design by exploring the concept of _composition_ in which a class instance (_composite_) is
composed of one or more class instances (_component_). The relationship between a composite and its
component is considered a "has-a" relationship (e.g., a `Starship` has a `Crew`).

A class can also _inherit_ attributes and methods from a base or parent class. Leveraging class
inheritance allows one to write specialized versions of a class in which an "is-a" relationship is
defined between the parent class (the _supertype_) and the child class (the _subtype_) (e.g., a
`Starship` is a `Vehicle`).

Subtypes inherit supertype attributes and behavior. But a subtype is also free to both add additional
attributes and methods as well as *override* supertype methods and attributes of the same name.

**Isaac Rodriguez, ["Inheritance and Composition: A Python OOP Guide"](https://realpython.com/inheritance-composition-python/).** (Real Python, n.d.).

**Lisa Tagliaferri, ["Understanding Class Inheritance in Python 3"](https://www.digitalocean.com/community/tutorials/understanding-class-inheritance-in-python-3).** (Digital Ocean, March 2018).

### 2.6 Modules

Besides importing Python standard library modules such as `csv` or `json` and third-party modules
such as `requests` you can leverage the modules concept to modularize your own code by dividing it
into modules and import each into your script or program in order to access the needed
functionality.

**Lisa Tagliaferri, ["How To Import Modules in Python 3"](https://www.digitalocean.com/community/tutorials/how-to-import-modules-in-python-3) (Digital Ocean, February 2017).**


## 3.0 More advanced stuff

### 3.1 Type hints

Python 3.5 introduced support for [type hints](https://docs.python.org/3/library/typing.html), a form of annotation useful during development and debugging. Python remains a dynamically-typed language but type hints help specify parameter types (e.g., `str`, `list`) for a function, method and/or variable are recoginized by linters such as `pylint` and other third party tools (e.g. [Mypy](http://www.mypy-lang.org/)) that use type hints to perform static analysis on your code and locate errors _before_ they are encountered during runtime.

#### Basic syntax

`variable: < type > = value`

```python
swapi_films: list = response['results']
```

`def func(param: < type >, optional_param: < type > = default_value) -> return_type:`

```python
def get_swapi_resource(url: str, timeout: int = 10) -> dict:
    """. . ."""

    return requests.get(url, timeout=timeout).json()
```

**Debanga Raj Neog, ["Python Type Hinting: Beginner's Cheat Sheet"](https://medium.com/depurr/python-type-hinting-a7afe4a5637e) (Medium, May 2017).**

**Geir Arne Hjelle, ["Python Type Checking (Guide)"](https://realpython.com/python-type-checking/) (Real Python, n.d.).**

**Mypy, ["Documentation"](https://mypy.readthedocs.io/en/stable/index.html).**

### 3.2 Unit tests

The Python standard library includes a `unittest` module for writing unit tests (other test
frameworks are also available). Learning how to write unit tests will improve not just the code you
write but your development skills.

**Python 3.x Official Documentation, ["unittest — Unit testing framework"](https://docs.python.org/3/library/unittest.html) (python.org, nd).**

**Anthony Shaw, ["Getting Started With Testing in Python"](https://realpython.com/python-testing/) (Real Python, nd).**

### 3.3 Decorators

Python functions are first class objects and can be passed an argument to another function. A
function can also be nested inside another function. A _decorator_ wraps a function and modifies its
behaviour without changing the function or its signature (e.g., parameters list). Decorated
functions can be annotated using the "pie" `@some_decorator` syntax to indicate the function is
"wrapped" by another function.

In the example below the function `get_swapi_resource()` is wrapped by the `functools.lru_cache`
function. This results in the memoization of the function in which return values are cached based
on the passed in arguments; calls to function that pass arguments that match previous calls use
the cached value rather than the function's computed value.

```python
@lru_cache(maxsize=64)
def get_swapi_resource(url: str, timeout: int = 10) -> dict:
    """..."""

    return requests.get(url, timeout=timeout).json()
```

You can also decorate class methods using built-in decorators like `@classmethod`, `@staticmethod`,
and `@property` as well as the class itself, such as `@dataclass` which provides a less verbose
form of a class definition.

**Geir Arne Hjelle, ["Primer on Python Decorators"](https://realpython.com/primer-on-python-decorators/) (Real Python, n.d.).**

**Geir Arne Hjelle, ["Data Classes in Python 3.7+ (Guide)"](https://realpython.com/python-data-classes/#adding-methods) (Real Python, n.d.).**

### 3.4 LRU caching (memoization)

Cache the output of a Python function based on the arguments passed to it. This
optimization technique is known as [memoization](https://en.wikipedia.org/wiki/Memoization)
and leverages the Python standard library's `functools.lru_cache`. A "memoized" function performs
a computation and returns a value _only_ once for each set of arguments passed to it. If the function
is called with arguments passed to it previously, the return value is retrieved from the cache.

The example below illustrates the switch from dictionary cache implementation to the use of
`functools.lru_cache()` which decorates `get_swapi_resource()` (see above).

### Simple in-memory cache using a dictionary

```python
planet_cache = {}

# for film in films[:2]: # TEST FIRST TWO FILMS
for film in films:
    for i, url in enumerate(film.planets):

        # Check cache
        if url not in planet_cache.keys():
            response = get_swapi_resource(url) # Get planet
            response = convert_str_to_int(response) # REFACTOR STEP

            planet = Planet(
                response['url'],
                response['name'],
                response['diameter'],
                response['population']
                )

            planet_cache[url] = planet # cache (store) the planet instance
        else:
            planet = planet_cache[url]

        film.planets[i] = planet # replace URL str with film object
```

### functools.lru_cache()

See `lru_cache()` decorated `get_swapi_resource()` above.

```python
for film in films:
    for i, url in enumerate(film.planets):
        planet_data: dict = utl.get_swapi_resource(url) # response cached
        planet_data = utl.convert_str_to_int(response)

        planet = Planet(
            planet_data['url'],
            planet_data['name'],
            planet_data['diameter'],
            planet_data['population']
            )

        film.planets[i] = planet # replace URL str with film object
```

**Dan Bader, "Memoization in Python: How to Cache Function Results"[https://dbader.org/blog/python-memoization] (danbader.org, n.d.).**

**Santiago Valdarrama, ["Caching in Python Using the LRU Cache Strategy"](https://realpython.com/lru-cache-python/) (Real Python, November 2020).**

### 3.5 Logging events

The Python standard library includes a
[logging module](https://docs.python.org/3/library/logging.html) for recording runtime events and
streaming them to the screen and/or writing them out to a file. Logging is useful both for debugging
and tracking program actions.

**Abhinav Ajitsaria, ["Logging in Python"](https://realpython.com/python-logging/) (Real Python, n.d.).**

**Akshar Raaj, ["Understanding the Python Logging Library"](https://blog.urbanpiper.com/understanding-python-logging-library/) (Medium, November 2020).**

## 3.6 Regular Expressions

Defining search patterns that can match complex character sequences requires the use of
_regular expressions_ (a.k.a regex or regexp) and the Python `re` module.

**Thomas Nield, ["An Introduction to Regular Expressions"](https://learning.oreilly.com/library/view/an-introduction-to/9781492082569/) (O'Reilly Media, Inc., June 2019).**

:bulb: For RegEx testing/debugging I recommend the online tool [regular expressions 101](https://regex101.com/).

## 3.7 Pandas, Numpy, and Matplotlib

If you are interested in data, data manipulation, and data science, then start learning
[Pandas](https://pandas.pydata.org/) now. Pandas is built on top of [Numpy](https://numpy.org/),
the base package for scientific computing. You will learn how to work with series, data frames
stored as numpy n-dimensional arrays and matrices. Then learn how to visualize your data starting
with the [Matplotlib](https://matplotlib.org/) package. You can also do your work and publish your
results using a web-based [Jupyter notebook](https://jupyter.org/).

**George McIntire, Brendan Martin, and Lauren Washington, ["Python Pandas Tutorial": A Complete Introduction for Beginners"](https://www.learndatasci.com/tutorials/python-pandas-tutorial-complete-introduction-for-beginners/).**

## 3.8 Generators

A Generator is a high-performance function that simplifies the building of iterators. It returns
what is known as a "lazy iterator" object, using a `yield` statement to suspend execution of the
loop temporarily in order to pass a value back to the caller "on demand" without actually exiting
the function. When the function is next called loop iteration continues yielding back the next value
in the sequence. Generators come in handy when working with very large data sets (e.g., large CSV
file).

**Dan Bader, ["What Are Python Generators?"](https://dbader.org/blog/python-generators) (dbader.org, nd).**

**Dan Bader, ["Generator Expressions in Python: An Introduction"](https://dbader.org/blog/python-generator-expressions) (dbader.org, nd).**

 **Kyle Stratis, ["How to Use Generators and yield in Python"](https://realpython.com/introduction-to-python-generators/) (Real Python, September, 2019).**

## 4.0 Enhancing your dev environment

## 4.1 Python virtual environments

When working on unrelated Python projects, I create a "virtual environment" for each. Doing so
creates an isolated development environment that allows each project to define its own dependencies
independent of other projects. This includes not only package dependencies and their versions but
also the Python version required for the project.

**Real Python, ["Python Virtual Environments: A Primer"](https://realpython.com/python-virtual-environments-a-primer/) (Real Python, nd).**

## 4.2 Git and Github

[Git](https://git-scm.com/) is a distributed version control system for tracking changes in source
code and other files. [Github](https://github.com/) is a hosting platform for developers (and others)
who version their work using git. Both the system and the platform are designed to support
collaborative work among programmers, but versioning your solo work and maintaining copies in the
cloud is smart practice.

**Roger Dudler, [git - the simple guide](http://rogerdudler.github.io/git-guide/).**

I love this guide.

**Ross Conyers, ["Learn Git in 3 Hours"](https://learning.oreilly.com/videos/learn-git-in/9781789348231).**

Video format. Videos grouped into four chapters. Chapter 4 focuses on Github.

* Chapter 1: Version Control and the Terminal
* Chapter 2: Learning the Basics of Git
* Chapter 3: Branches and Workflow
* Chapter 4: Advanced Git Workflow

## 4.3 Homebrew and Choco

Both macOS and Windows users can benefit from `pip`-like package managers that handle software
installs.

For my Mac I use [Homebrew](https://brew.sh/), a macOS package manager, to acquire and
maintain many of the software packages that I use on a daily basis, including Python. The Homebrew
approach is but one way to manage software installs. In the case of Python on a Mac it is often
described as the
[recommended way](https://python-docs.readthedocs.io/en/latest/starting/install3/osx.html) to
install and maintain it.

For Windows I turn to [Chocolatey](https://chocolatey.org/) to manage many of my installs.

## 5.0 Web development

If you are interested in web development consider exploring [Django](https://www.djangoproject.com/)
and/or [Flask](https://flask.palletsprojects.com/en/1.1.x/). Both are Python web frameworks designed
for rapid application development of database-driven web applications.

### 5.1 Learning Django

**Charles Severance, [Django for Everybody (DJ4E)](https://www.dj4e.com/lessons).**

**Django Girls, [Django Girls Tutorial](https://tutorial.djangogirls.org/en/).**

**Mozilla, MDN web docs. [Django Web Framework (Python)](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django).**

**Vitor Freitas, ["A Complete Beginner's Guide to Django"](https://simpleisbetterthancomplex.com/series/beginners-guide/1.11/).**

### 5.2 Learning Flask

**Miguel Grinberg, [Flask Web Development](https://learning.oreilly.com/library/view/flask-web-development/9781491991725/), 2nd Edition (O'Reilly Media, Inc., 2018).**

**Miguel Grinberg, ["The Flask Mega-Tutorial"](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world).**

An impressive series of blog posts that get you up an running with Flask.

**Miquel Grinberg, ["The New and Improved Flask Mega-Tutorial"](https://courses.miguelgrinberg.com/p/flask-mega-tutorial).**

What started as a series of blog posts is now a formal, fee-based, course offering on Flask web
development.

## 6.0 Database design and development

If you are new to database design and development consider starting with
[SQLite](https://www.sqlite.org/index.html), an in-memory database that is easy to install and
maintain. Additionally, you need to learn the Structured Query Language (SQL). You start learning
both by taking Dr Chuck's "Using Databases with Python" Coursera course.

**Coursera, Charles Severance,["Using Databases with Python"](https://www.coursera.org/learn/python-databases).**

Intermediate. Taught by UMSI faculty. Learn how to build and deploy websites using the Django
web framework, written in Python. This is course four in the five course
["Python for Everybody Specialization"](https://www.coursera.org/specializations/python).
