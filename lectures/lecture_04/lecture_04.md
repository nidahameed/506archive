# SI 506 Lecture 04

## Topics

1. Variables (labels) and variable assignment
2. Variable naming rules and conventions
3. Built-in functions `print()`, `type()`, `len()`
4. Basic arithmetic operations (add, subtract, multiply, divide)
5. `str.split()` method
6. String formatting (f-string)

## 1.0 VARIABLES

A variable is a name or label that refers to an object in memory. Or as Jake VanderPlus describes
the concept in _A Whirlwind Tour of Python_:

> “. . . variables are simply pointers [to objects], and the variable names themselves have no
> attached type information.”

Use the assignment (`=`) operator to assign a value to a variable.

```python
name = "Graduate Employees' Union 3550" # warn: apostrophe must be surrounded by double ("...")
member_count = 2138  # Ann Arbor campus only
is_on_strike = True

chorus = """
Hail! to the victors valiant
Hail! to the conquering heroes
Hail! Hail! to Michigan
the leaders and best!
"""
```

## 2.0 VARIABLE NAMING RULES AND CONVENTIONS

Default convention: lowercase word(s) or recognizable abbreviation (e.g., num, val, var);
separate words with an underscore.

:exclamation: Readability and comprehensibility matters.

### 2.1 Good

```python
# Choose lowercase
acronym = 'GEO'

# Separate words with underscore (_)
twitter_handle = '@geo3550'
geo_start_year = 1974 # year certified by Michigan Employment Relations Commission (MERC)

# Use plural form to indicate a set or sequence
hash_tags = ['#GEOStrike', '#StrikeForSafeCampus', '#UMMakesUsSick', '#SolidarityForever']

strike_demands = [
    'transparent testing and contract tracing planning',
    'universal right to work remotely',
    'parent and caregiver subsidy',
    'repeal $500.00 international student fee and document shipping fee',
    'degree timeline extensions and funding, rent freezes, flexible on-campus leases',
    'disarmed and demilitarized workplace',
    'Defund DPSS by 50% and reallocate funds to community-based justice initiatives',
    'U-M cut all ties with Ann Arbor Police Dept and Immigration and Customs Enforcement (ICE)'
    ]

# Ok to use recognizable abbreviations like num[ber], val[ue] or var[iable].
num = 1250 # count of GEO members who attended on 9 Sept 2020 membership call
val = 'some_value'
var = 'some_value'

# "is_", "has_" Boolean true/false
is_member = True

# All caps designates a module level constant (special case)
BASE_URL = 'https://www.geo3550.org/'

# Mathematical expressions (function definition specifying two parameters x and y)
def multiply(x, y):
    return x * y # arithmetic

# Call the function and pass two numeric arguments
product = multiply(14, 27)

# Built-in enumerate() function adds a counter < i > when looping over < course_codes >
for i, demand in enumerate(strike_demands, 1):
    print(f"{i}. {demand}")
```

### 2.2 Bad (but legal)

```python
# Opaque
g = 'GEO'

# Reserve CamelCase for class names.
TwitterHandle = '@geo3550'

# Underscore overkill; difficult to read.
g_e_o = "Graduate Employee's Union 3550"

# Difficult to read; guaranteed to annoy.
cOUrsE_cOdE = 'SI 506'
```

:exclamation: Avoid prefixing or suffixing variable names with single (`_`) or double underscores (`__`)
&mdash; known in the Python community as a "dunder" &mdash; until you gain experience as a Python
programmer.

Variable names prefixed with a single underscore like `_course_code` are, by convention, considered
private member variables in a class. Variable names prefixed with a double underscore like
`__course_code__`, gets renamed at runtime by the Python interpreter in a process known as "name
mangling".

:bulb: These and other naming conventions that employ leading and/or trailing underscores are
_out of scope_ for SI 506. That said, if you want to learn more on the subject see D. Bader,
["The Meaning of Underscores in Python"](https://dbader.org/blog/meaning-of-underscores-in-python)
(dbader.org, nd).

### 2.3 Ugly (illegal)

The Python Interpreter will raise a `SyntaxError` at runtime whenever it encounters the
following illegal names:

:exclamation: Python [keywords](https://docs.python.org/3/reference/lexical_analysis.html#keywords) are
reserved and cannot be used as variable names. Also avoid use of
[built-in function](https://docs.python.org/3/library/functions.html) names. Name clashes will
result.

```python
# Illegal: keyword used as a variable name (language-specific identifiers reserved by Python)

class = 'SI 506'

class_ = 'SI 506' # legal: add trailing underscore (..._) to avoid reserved word clash (convention)

# Illegal: variable name commences with a numeric value.

3550_local = "Graduate Employee's Union 3550"

# Illegal: variable name commences with a special character (e.g., `@`, `%`, `$`, `&`, `!`)

@geo3550 = 'https://twitter.com/geo3550'

# Illegal: variable name includes a dash (`-`).

hash-tags = ['#GEOStrike', '#StrikeForSafeCampus', '#UMMakesUsSick', '#SolidarityForever']

# Illegal: variable name includes whitespace.

course name = 'SI 506'
```

Also avoid use of
[built-in function](https://docs.python.org/3/library/functions.html) names as variable names.
Name clashes may occur in your code. If you do opt to use or "shadow" such names add a trailing
underscore character to the name (`_`) per the
[PEP 08](https://www.python.org/dev/peps/pep-0008/#function-and-method-arguments) recommendation or
opt for a different name (`len_` or `length` for `len`).

```python
# Shadowing; risk name clash with built-in functions
id = 3550
str = 'GEO is on strike'
min = 0
max = 1250
len = 6

# Alternative names
id_ = 3550

str_ = 'GEO is on strike'
val = 'GEO is on strike'

min_ = 0
min_val = 0

max_ = 1250
max_val = 1250

len_ = 6
length = 6
```

## 3.0 BUILT-IN FUNCTIONS (print(), type(), len())

The Python Interpreter includes a number of
[built-in functions](https://docs.python.org/3/library/functions.html) that are always available for
you to call.

:bulb: A function is a defined block of code that performs (ideally) a single task. Functions only
run when they are explicitly called. A function can be defined with one or more _parameters_ that
allow it to accept _arguments_ from the caller in order to perform a computation. A function can
also be designed to return a computed value. Functions are considered "first-class" objects in the
Python eco-system. You will soon write your own functions; for now we introduce a select number of
built-in functions for you to use.

### 3.1 `print()`: print passed in object to the screen

```python
# Calling the built-in print() function and passing a hard-coded string.
print('GEO is on Strike')

# Passing a variable which points to a list.
print(hash_tags)

# Passing two variables separated by a comma.
print(name, acronym)
```

### 3.2 `type()`: determine an object's data type

```python
data_type = type(name)
print(data_type) # returns <class 'str'>

data_type = type(member_count)
print(data_type) # returns <class 'int'>

data_type = type(strike_demands)
print(data_type) # returns <class 'list'>
```

### 3.3 `len()`: check length of sequence (i.e., number of elements)

```python
# Count characters in string (including whitespace).
chars_count = len(name)
print(chars_count)

# Count number of elements in list.
demands = len(strike_demands)
print(demands)

# You can also pass a function to another function as an argument.
print(len(strike_demands))
```

## 4.0 BASIC ARITHMETIC (addition, subtraction, multiplication, division)

Python supports math operations. The order of operations is expressed conveniently by the acronym
__PEMDAS__: Parentheses, Exponentation, Muliplication \| Division (same precedence), Addition \|
Subtraction.

1. Parentheses have the highest precedence and can be used to force an expression to evaluate in the
   order you want. Since expressions in parentheses are evaluated first, `2 * (3-1)` is 4, and
   `(1+1)**(5-2)` is 8. You can also use parentheses to make an expression easier to read, as in
   `(minute * 100) / 60`, even though it doesn’t change the result.

2. Exponentiation has the next highest precedence, so `2**1+1` is 3 and not 4, and `3*1**3` is 3 and
   not 27.

3. Multiplication and both division operators have the same precedence, which is higher than
   addition and subtraction, which also have the same precedence. So `2*3-1` yields 5 rather than 4,
   and `5-2*2` is 1, not 6.

4. Operators with the same precedence (except for **) are evaluated from left-to-right. In algebra
   we say they are left-associative. So in the expression `6-3+2`, the subtraction happens first,
   yielding 3. We then add 2 to get the result 5. If the operations had been evaluated from right
   to left, the result would have been `6-(3+2)`, which is 1.

### 4.1 Addition (`+` operator)

```python
# Geo Strike demands count
covid_19_demands = 5
anti_policing_demands = 3

total_demands = covid_19_demands + anti_policing_demands

# equivalent to
total_demands = 5 + 3
```

### 4.2 Subtraction (`-` operator)

```python
# Ann Arbor campus (2019 numbers)
tenured_faculty = 3193
clinical_faculty = 2190
research_faculty = 898 # assume no researchers teach for this exercise
lecturer_faculty = 964

teaching_faculty = tenured_faculty + clinical_faculty + lecturer_faculty

unionized_faculty = teaching_faculty - lecturer_faculty

# equivalent to
unionized_faculty = 6347 - 964
```

### 4.3 Multiplication (`*` operator)

```python
# Ann Arbor campus
gsi_count = 2138 # includes Graduate Student Staff Assistants (GSSA)
work_hrs_per_week = 20 # individual GSI committment

work_hrs_withheld_per_week = gsi_count * work_hrs_per_week

# equivalent to
work_hrs_withheld_per_week = 2138 * 20
```

### 4.4 Floating point division (`/` operator)

Return a decimal value (a float).

```python
student_count = 225
lab_count = 10

avg_lab_size = student_count / lab_count

# equivalent to
avg_lab_size = 225 / 10

```

### 4.5 Floor division a.k.a integer division (`//` operator)

Return an integer value (ignore fractional values).

```python
student_count = 225
lab_count = 10

avg_lab_size = student_count / lab_count

# equivalent to
avg_lab_size = 225 // 10
```

## 5.0 Look-ahead: str.split() method

The string (`str`) type or object can be said to exhibit behaviors that are expressed in the form of
_methods_ that you can call. For example, we can call `str.upper()` to convert a string to all
upper case characters:

```python
declaration = 'GEO is on strike'

print(declaration.upper())
```

Another `str` method that you will use frequently is the `str.split()` method. This method allows
you to return a list of character "chunks" after splitting the string on a specified delimiter
(default is a space).

```python
val = '#GEOStrike #StrikeForSafeCampus #UMMakesUsSick #SolidarityForever'
hash_tags = val.split()

print(hash_tags)
```

When you split `val` on a space the return value is a list:

`['#GEOStrike', '#StrikeForSafeCampus', '#UMMakesUsSick', '#SolidarityForever']`

Note that you can pass a specified delimiter to the `str.split()` method, as in the following
example:

```python
val = '#GEOStrike,#StrikeForSafeCampus,#UMMakesUsSick,#SolidarityForever'
hash_tags = val.split(',')

print(hash_tags)
```

:warning: Consider carefully your choice of delimiter when splitting a string. In the following
example, specifing a comma as the sole delimiter upon which to split the string will lead to
unexpected results:

```python
val = '#GEOStrike, #StrikeForSafeCampus, #UMMakesUsSick, #SolidarityForever'
hash_tags = val.split(',')

print(hash_tags)
```

The list returned by the split operation will contain string elements with a leading space--usually
not the desired outcome.

`['#GEOStrike', ' #StrikeForSafeCampus', ' #UMMakesUsSick', ' #SolidarityForever']`

Instead specify a delimiter that also includes a space:

```python
val = '#GEOStrike, #StrikeForSafeCampus, #UMMakesUsSick, #SolidarityForever'
hash_tags = val.split(', ')

print(hash_tags)
```

Over the course of the semester you will learn to use a number of `str` methods. For a complete
listing see w3schools' ["Python String Methods"](https://www.w3schools.com/python/python_ref_string.asp)

Other types such as lists, tuples, and dictionaries also include methods you can call. We will
explore those types and their methods in the coming weeks.

## 6.0 String formatting (look ahead)

Problem Set 01 contains a number of pre-positioned `print()` statements in which a formatted string
literal (a.k.a f-string) is passed in as an argument.

The f-string syntax `f"some_string {some variable}"` is less verbose and easier to construct than
earlier string formatting approaches. You will learn how to write f-strings as well as format string
using the older approaches in the very near future.

```python
print(f"\nValid = {valid_variables}")
```

:bulb: `\n` represents an escape sequence, specifically an ASCII linefeed (LF). Think of `\n` as
"newline". Passing `\n` in a string will insert a new line at the position of the escape sequence.

## Sources

GEO, ["History"](https://www.geo3550.org/about/history/) \
GEO, ["GEO's Demands for a Safe and Just Pandemic Response for All"](https://www.geo3550.org/2020/09/04/geos-demands-for-a-safe-and-just-pandemic-response-for-all/) \
GEO, ["News"](https://www.geo3550.org/news/) \
GEO ["Twitter Feed"](https://twitter.com/geo3550) \
U-M HR, ["About GEO"](https://hr.umich.edu/working-u-m/my-employment/academic-human-resources/contracts/about-geo) \
U-M, ["Facts and Figures"](https://umich.edu/facts-figures/) \
U-M, ["Almanac"](https://obp.umich.edu/wp-content/uploads/pubdata/almanac/Almanac_Ch1_Jan2020.pdf#:~:text=Based%20on%20the%20Fall%202019,All%20other%20staff%20total%2016%2C243.) (Jan 2020)
