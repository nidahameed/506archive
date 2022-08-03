# SI 506 Lecture 12

## Topics

1. Docstrings
2. Optional function parameters
3. Truth value testing
4. Looping with range()
5. Tuple unpacking
6. Controlling execution flow with a main() function

## Vocabulary

1. __Flow of execution__. The order in which statements in a program are executed. Also referred to
   as _control flow_.
2. __Truth Value__. Each Python can be evaluated for its _truth value_ in a boolean context.
3. __Tuple Packing__. Assign items to a tuple.
4. __Tuple Unpacking__. Assign tuple items to an equal number of variables.

## Setup

### English Premier League club records, 2019-2020 season

Club attributes: `['Club', ('Win', 'Draw', 'Loss'), ('Goals For', 'Goals Against')]`

```python
premier_league = [
        ['Wolverhampton', (15, 14, 9), (51, 40)],
        ['Manchester United', (18, 12, 8), (66, 36)],
        ['Watford', (8, 10, 20), (36, 64)],
        ['Aston Villa', (9, 8, 21), (41, 67)],
        ['Tottenham', (16, 11, 11), (61, 47)],
        ['Newcastle United', (11, 11, 16), (38, 58)],
        ['Brighton & Hove Albion', (9, 14, 15), (39, 54)],
        ['Manchester City', (26, 3, 9), (102, 35)],
        ['Arsenal', (14, 14, 10), (56, 48)],
        ['Sheffield United', (14, 12, 12), (39, 39)],
        ['Bournemouth', (9, 7, 22), (40, 65)],
        ['Crystal Palace', (11, 10, 17), (31, 50)],
        ['Leicester City', (18, 8, 12), (67, 41)],
        ['Norwich City', (5, 6, 27), (26, 75)],
        ['Everton', (13, 10, 15), (44, 56)],
        ['Chelsea', (20, 6, 12), (69, 54)],
        ['Liverpool', (32, 3, 3), (85, 33)],
        ['Burnley', (15, 9, 14), (43, 50)],
        ['Southampton', (15, 7, 16), (51, 60)],
        ['West Ham', (10, 9, 19), (49, 62)]
        ]
```

## 1.0 Docstrings

The Python documentation string or [Docstring](https://www.python.org/dev/peps/pep-0257/) is a
string literal that is positioned as the first statement in a function. The Docstring provides a
short summary of the function's expected behavior, including details regarding defined parameters
(required and optional) and return value, if any. The Python interpreter assigns the string to the
special "dunder" `__doc__` object attribute. Docstrings can also be assigned to modules, classes,
and class methods, examples of which you will encounter later in the course.

There are two forms of Docstrings: single line and multi-line statements. Single line Docstrings are
reserved for describing obvious behaviors. For example, the built-in `len()` function is described
with a single line Docstring:

```commandline
>>> len.__doc__
'Return the number of items in a container.'
```

The built-in `print()` function is provisioned with a multiline Docstring:

```commandline
>>> print.__doc__
"print(value, ..., sep=' ', end='\\n', file=sys.stdout, flush=False)\n\nPrints the values to a stream, or to sys.stdout by default.\nOptional keyword arguments:\nfile:  a file-like object (stream); defaults to the current sys.stdout.\nsep:   string inserted between values, default a space.\nend:   string appended after the last value, default a newline.\nflush: whether to forcibly flush the stream."
```

The Docstrings in functions and other objects that you will encounter (and later write) in this
course will resemble a specially formatted multiline strings bounded by triple quotation marks
(`"""`).

The Docstring format we employ is as follows:

```python
"""Short description describing the purpose and expected behavior of the function. Between one
and five sentences should suffice to describe the function in all its glory.

Parameters:
    < name > (< type >): Terse description of the parameter.
    [Repeat for each parameter, required and optional]

Returns:
    < type >: Terse description of the return value. If no value is explicitly returned use `None`.
"""
```

Starting this week, we will make increasing use of Docstrings like the example below in both
lectures, labs, and problem sets and lab exercises to describe a function's purpose, defined
parameters and return value, if any.

```python
def get_club_name(club):
    """Return the club name. Function assumes that the first element in the club
    list represents the name of the club.

    Parameters:
        club (list): Representation of a football (i.e., soccer) club.

    Returns
        str: name of club.
    """

    return club[0]
```

## 2.0 Optional function parameters

A function can be defined with one or more optional parameters. Each optional parameter _must_ be
assigned a default value that the function will use if the caller chooses not to override the
default value when calling the function.

:bulb: if an optional parameter's default value satisfies the caller's requirements, the function
may be called without specifying the optional argument.

```python
def format_name(name, all_caps=False):
    """Trims name string and then converts the first character of each word to upper case
    unless optional all_caps argument is specified as True.
    """

    if all_caps: # truth value
        return name.strip().upper()
    else:
        return name.strip().title()

    return name


    # Returns club name trimmed with all words capitalized. Optional argument excluded.
    club_name = ' wolverhampton wanderers football club '
    formatted_club_name = format_name(club_name)

    print(f"\n1.0.1 Formatted name = {formatted_club_name}")

    # Returns club name trimmed with all characters converted to upper case.
    club_name = 'west ham united football club '
    formatted_club_name = format_name(club_name, True)

    print(f"\n1.0.2 Formatted name = {formatted_club_name}")

    # Employs keyword argument for passed in optional argument.
    # Hotspur - a rash, impetuous person (archaic).
    club_name = ' tottenham Hotspur football Club'
    formatted_club_name = format_name(club_name, all_caps=True)

    print(f"\n1.0.3 Formatted name = {formatted_club_name}")
```

## 3.0 Truth value testing

In Python every object can be tested for its
[_truth value_](https://docs.python.org/3/library/stdtypes.html#truth-value-testing). You can check
an object's truth value in an `if` or `while` statement or as an operand (i.e., the value the
operator operates on) in an `and`, `or` `not` Boolean operation. A value that evaluates to `True`
is considered _truthy_ while a value that evaluates to `False` is considered _falsy_.

For SI 506 the following values are considered "truthy" or "falsy":

### Truthy values

* Non-empty sequence or map (`list`, `tuple`, `str`, `dict`).
* Non-zero numeric values.
* Non-empty `range()`
* Boolean `True`

### Falsy values

* Empty sequence or map (list, tuple, string, dictionary)
* Numeric type with a value of zero (e.g., `int` (0), `float` (0.0))
* Boolean `False`
* Empty range `range(0)`
* Nonetype (e.g., `None`)

Below are a few examples of truth value testing:

```python
club_names = [] # falsy
if club_names: # evaluates to False
    print(f"\nclub_names list has {len(club_names)} elements.") # not called
else:
    print('\nclub_names list is empty.')

club_names = ['Arsenal', 'Aston Villa'] # truthy
if club_names: # evaluates to True
    print(f"\nclub_names list has {len(club_names)} elements.") # called
else:
    print('\nclub_names list is empty.')

# Boolean operation (not)
# Select favorite "Big Six" club (user-supplied input). Run while loop until condition evaluates to False.
big_six_clubs = ('arsenal', 'chelsea', 'liverpool', 'manchester city', 'manchester united', 'tottenham')
prompt = '\nWhich big six club is your favorite?: '

matched = False # falsy
while not matched:
    club = input(prompt)
    if club.lower() in big_six_clubs:
        print(f"\nThanks. I like {club.capitalize()} too.\n\nFinis.\n")
        matched = True
```

:bulb: You can also check if a value is either truthy or falsy using the built-in `bool()` function.

```python
club_names = [] # falsy
truth_value = bool(club_names) # returns False

club_names = ['Bournemouth', 'Southampton'] # truthy
truth_value = bool(club_names) # returns True
```

## 4.0 Looping with range()

In the official Python documentation `range()` is included among the list of
[built-in functions](https://docs.python.org/3/library/functions.html). While it bears the
appearance of a function, `range` is actually an immutable sequence type. An instance of the
`range()` type is initialized by passing it a required _stop_ integer value, and, optionally,
`start` and `step` values. `range()` is often used in conjunction with a `for` loop in order to
define a set number of iterations to be performed.

The following examples illustrate the use of `range()` in a `for` loop. Note the use of step values,
both positive and negative.

```python
for i in range(5):
    print(f"Iteration {i}")

print('\n') # padding

for i in range(0, 5, 2):
    print(f"Stepped iteration {i}")

print('\n') # padding

for i in range(5, -6, -1):
    print(f"Iteration {i}")
```

One common use case for `range()` is when you need to combine elements from two or more lists with
that share a common order. You construct a `for` loop using `range()` in which you specify the
number of loop iterations by passing the length of the "target" list to `range()` in the `for` loop.
Then use the loop variable `i` to select both "source" and "target" elements from the "source" and
"target lists and apply the values returned to the desired looping operation.

```python
clubs = [
    ['Wolverhampton', (15, 14, 9), (51, 40)],
    ['Arsenal', (14, 14, 10), (56, 48)],
    ['Sheffield United', (14, 12, 12), (39, 39)],
    ['Leicester City', (18, 8, 12), (67, 41)],
    ['Liverpool', (32, 3, 3), (85, 33)]
    ]

club_nicknames = [
    ['Wolverhampton', 'Wolves'],
    ['Arsenal', 'The Gunners'],
    ['Sheffield United', 'The Blades'],
    ['Leicester City', 'The Foxes'],
    ['Liverpool', 'The Reds']
    ]

# Insert the nicknames into the clubs list.
for i in range(len(clubs)):
    clubs[i].insert(1, club_nicknames[i][1])

print(f"\n clubs with nicknames added = {clubs}")
```

## 5.0 Tuple unpacking

Python functions can return multiple values. One common approach is to return a tuple of items. In
the following example the function `get_summary_statistics` accepts an individual club's season
record (e.g., wins, losses, draws, goals for, goals against). The function calls a set of
neighboring functions that either retrieve a value from the list or perform a calculation. The
return values are then "packed" as tuple using a comma as a value delimiter in the return statement.
The tuple return value can then be "unpacked" and its items assigned to an equal number of variables.

:bulb: you can also use parentheses `(name, points, goals_diff, goals_scored)` in the tuple packing
expression.

```python
def get_summary_stats(club):
    """Return a tuple representing clubs summary statistics (club name, points,
    goals differential, and goals scored for the season.

    Parameters:
        club (list): club record

    Returns
        tuple: name, points, goals_diff, goals_scored tuple items
    """

    name = get_name(club)
    points = calculate_points(club)
    goals_diff = calculate_goals_diff(club)
    goals_scored = get_goals_scored(club)

    return name, points, goals_diff, goals_scored

    # Call function and unpack the return value
    club_name, club_points, club_goals_diff, club_goals_scored = get_summary_stats(club)
```

## 6.0 Controlling execution flow with a main() function

Python features two file execution modes. Code in a file can be executed as a script from the
command line or the code can be imported into another Python file for use.

If a Python program is executed from the command line as a script the Python interpreter will
run the file under the special name of `__main__` rather than the program's actual file name (e.g.,
`lecture_13.py`). Given this naming behavior we can choose the program's entry point and control the
program's execution flow by directing the Python interpreter to call the `main()` function first in
order to execute the statements defined in its code block.

In the following example, the `main()` function's code block manages the program's control flow. The
flow of execution is as follows:

1. The Python interpreter reads the file, registering in memory the functions it encounters.
2. Since the program is run as a script from the command line, the conditional statement
   `if __name__ == '__main__'` evaluates to `True`, and the `main()` function, serving as the
   program's entry point, is called.
3. The `get_record` function is then called. When implemented the function will return a club's
   record (wins, losses, draws, and goals for and against) for a given season.
4. The `calculate function` function is then called.  When implemented the function will return the
5. total points earned by the club during season.
6. The built-in `print()` function is then called in order to print an f-string to the terminal
   screen.

Employing a `main()` function to manage your program's flow of execution keeps separate the
code you write to manage a program's work flow from the code you write to perform specific tasks
(e.g., functions). This encourages code modularization and, by relying on function calls to perform
specific tasks, helps to eliminate code duplication.

An important side benefit is that with the work flow code restricted to `main()` the other objects
comprising the file (e.g., functions, classes, constants) can be imported as a module into another
Python module without triggering the code located in `main()`. This can occur because module code
imported from one Python file into another Python file is known by the Python interpreter by the
module's actual file name and not by the name `__main__` as is the case with scripts run from the
command line.

:bulb: We will cover modules, and module imports, and execution modes in more detail _after_ the
midterm.

```python
def calculate_points(record):
    """Calculate league points per provided club record. Points are earned as follows:
    win 3 points, draw 1 point ,loss 0 points.

    Parameters:
        record (list): Club record (win, loss, draw, goals for and against).

    Returns
        int: total league points earned.
    """

    pass # TODO IMPLEMENT


def get_record(records, name):
    """Return club record filtered on club name.

    Parameters:
        records (list): Club records (win, loss, draw, goals for and against).
        name (str): Name of club.

    Returns:
        list: Club record if located otherwise None.
    """

    pass # TODO Implement


def main():
    """Program entry point. Orchestrates program control flow.

    Parameters:
        None

    Returns:
        None
    """

    # Retrieve Wolverhampton's 2019-20 Premier League record.
    wolves_record = get_record(premier_league, 'Wolverhampton')

    # Calculate points earned during the season.
    wolves_points = calculate_points(wolves_record)

    print(f"Wolverhampton earned {wolves_points} points (2019-2020)")


if __name__ == '__main__':
    main()
```

## Sources

### Premier League standings

[2019-2020 season](https://bit.ly/3nDkdvw)

### Club histories

1. _Wikipedia_, [Arsenal F.C.](https://en.wikipedia.org/wiki/Arsenal_F.C.)
2. _Wikipedia_, [Aston Villa F.C.](https://en.wikipedia.org/wiki/Aston_Villa_F.C.)
3. _Wikipedia_, [AFC Bournemouth](https://en.wikipedia.org/wiki/AFC_Bournemouth)
4. _Wikipedia_, [Brighton and Hove Albion F.C.](https://en.wikipedia.org/wiki/Brighton_%26_Hove_Albion_F.C.)
5. _Wikipedia_, [Burnley F.C.](https://en.wikipedia.org/wiki/Burnley_F.C.)
6. _Wikipedia_, [Chelsea F.C.](https://en.wikipedia.org/wiki/Chelsea_F.C.)
7. _Wikipedia_, [Crystal Palace F.C.](https://en.wikipedia.org/wiki/Crystal_Palace_F.C.)
8. _Wikipedia_, [Everton F.C.](https://en.wikipedia.org/wiki/Everton_F.C.)
9. _Wikipedia_, [Leicester City F.C.](https://en.wikipedia.org/wiki/Leicester_City_F.C.)
10. _Wikipedia_, [Liverpool F.C.](https://en.wikipedia.org/wiki/Liverpool_F.C.)
11. _Wikipedia_, [Manchester City F.C.](https://en.wikipedia.org/wiki/Manchester_City_F.C.)
12. _Wikipedia_, [Manchester United F.C.](https://en.wikipedia.org/wiki/Manchester_United_F.C.)
13. _Wikipedia_, [Newcastle United F.C.](https://en.wikipedia.org/wiki/Newcastle_United_F.C.)
14. _Wikipedia_, [Norwich City F.C.](https://en.wikipedia.org/wiki/Norwich_City_F.C.)
15. _Wikipedia_, [Sheffield United F.C.](https://en.wikipedia.org/wiki/Sheffield_United_F.C.)
16. _Wikipedia_, [Southampton F.C.](https://en.wikipedia.org/wiki/Southampton_F.C.)
17. _Wikipedia_, [Tottenham Hotspur F.C.](https://en.wikipedia.org/wiki/Tottenham_Hotspur_F.C.)
18. _Wikipedia_, [Watford F.C.](https://en.wikipedia.org/wiki/Watford_F.C.)
19. _Wikipedia_, [West Ham United F.C.](https://en.wikipedia.org/wiki/West_Ham_United_F.C.)
20. _Wikipedia_, [WolverhamptonWanderers F.C.](https://en.wikipedia.org/wiki/Wolverhampton_Wanderers_F.C.)
