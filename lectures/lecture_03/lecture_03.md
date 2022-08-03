# SI 506 Lecture 03

## Topics

1. Comments (single line, multiline)
2. Values (objects) and types
3. Variables (labels) and variable assignment
4. Built-in functions print(), type(), len()
5. Basic arithmetic operations (add, subtract, multiply, divide)

## 1.0 COMMENTS

```python
# A single line comment <-- commences with hash (#) character

"""
This is a block comment comprising a multi-line string. This is actually a string
constant that is denoted by the use of triple quotation marks.
"""
```

## 2.0 VALUES (OBJECTS) AND TYPES

### 2.1 NUMBERS: integer, float (decimal)

```python

506 # integer

.25 # float
```

### 2.2 SEQUENCES (ORDERED SET)

* string (immutable)
* list (mutable)
* tuple (immutable)

#### Definitions

* Immutable: object state cannot be modified following creation.
* Mutable: object state can be modified folliwng creation.

```python
'Welcome to SI 506' # string

['arwhyte', 'deahanyu', 'dsewhite', 'maxzhang', 'mhaidli', 'shrijesh'] # list with six elements

(506, 507, 618) # tuple with three items
```

### 2.3 ASSOCIATIVE ARRAY (MAP): dictionary (key-value pairs)

```python
{'course': "SI 506", 'instructor_count': 1, "gsi_count": 5, "ia_count": 2} # four key-value pairs
```

### 2.4 BOOLEAN

```python
True
False
```

### 2.5 NONE

`None` is an object of type `<class 'NoneType'>` and represents `null`.
Note that `None` does not equal 0.

```python
None
```

## 3.0 VARIABLES

A variable is a name or label that refers to an object in memory. Or as Jake VanderPlus describes the concept in _A Whirlwind Tour of Python_:

> “. . . variables are simply pointers [to objects], and the variable names themselves have no attached type information.”

You will use the assignment (=) operator to assign a value to a variable.

```python
num = 506

welcome_message = 'Welcome to SI 506'

teaching_team = ['arwhyte', 'deahanyu', 'dsewhite', 'maxzhang', 'mhaidli', 'shrijesh']

chorus = """
Hail! to the victors valiant
Hail! to the conquering heroes
Hail! Hail! to Michigan
the leaders and best!
"""
```

## 4.0 VARIABLE NAMING RULES AND CONVENTIONS

Default convention: lowercase word(s) or recognizable abbreviation (e.g., num, val, var);
separate words with an underscore.

:exclamation: Readability matters.

### 4.1 Good

```python
# Choose lowercase
uniqname = 'arwhyte'

# Separate words with underscore (_)
course_code = 'SI 506'

# Use plural form to indicate a set or sequence
course_codes = ['SI 506', 'SI 507', 'SI 618']

# Ok to use recognizable abbreviations like num[ber], val[ue] or var[iable].
num = 27

# "is_", "has_" Boolean true/false
is_enrolled = True
has_mask = True

# All caps designates a module level constant (special case)
BASE_URL = 'https://si506.org/'

# Function definition specifying two parameters x and y (a foreshadowing of the weeks ahead)
def multiply(x, y):
    return x * y # arithmetic

# Call the function and pass two numeric arguments
product = multiply(14, 27)

print(f"product = {product}") # formatted string literal (f-string)

# Built-in enumerate() function adds a counter < i > when looping over < course_codes >
for i, code in enumerate(course_codes, 1):
    print(f"{i}. {code}")
```

### 4.2 Bad (but legal)

```python

# Opaque
c = 'SI 506'
cc = 'SI 506'

# Reserve CamelCase for class names.
CourseCode = 'SI 506'

# Unnecessarily verbose; difficult to read.
c_o_u_r_s_e_c_o_d_e = 'SI 506'

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

### 4.3 Ugly (illegal)

The Python Interpreter will raise a `SyntaxError` at runtime whenever it encounters the
following illegal names:

:exclamation: Python [keywords](https://docs.python.org/3/reference/lexical_analysis.html#keywords) are
reserved and cannot be used as variable names. Also avoid use of
[built-in function](https://docs.python.org/3/library/functions.html) names. Name clashes will
result.

```python
# Illegal: keyword used as a variable name (language-specific identifiers reserved by Python)

class = 'SI 506'

# Illegal: variable name commences with a numeric value.

506_umsi = 'SI 506'

# Illegal: variable name commences with a special character (e.g., `@`, `%`, `$`, `&`, `!`)

$number = 506

# Illegal: variable name includes a dash (`-`).

course-list = ['SI 506', 'SI 507', 'SI 618']

# Illegal: variable name includes whitespace.

course name = 'SI 506' # illegal; uncomment to test

# Avoid: built-in function names (a few examples)

str = 'Go Blue'
min = 0
max = 100
len = 101
```

## 5.0 BUILT-IN FUNCTIONS (print(), type(), len())

### 5.1 `print()`: print passed in object to the screen

```python
# Passing a hard-coded string.
print('SI 506 rocks!')

# Passing a variable name which points to a string.
print(welcome_message)

# Passing a variable name which points to a multiline string.
print(chorus)
```

### 5.2 `type()`: determine object's data type

```python
data_type = type(num)
print(data_type) # returns <class 'int'>

data_type = type(welcome_message)
print(data_type) # returns <class 'str'>

data_type = type(teaching_team)
print(data_type) # returns <class 'list'>
```

### 5.3 `len()`: check length of sequence (i.e., number of elements)

```python
# Count characters in string (including whitespace).

chars_count = len(welcome_message)
print(chars_count)

# Count number of elements in list.

team_count = len(teaching_team)
print(team_count)
```

## 6.0 BASIC ARITHMETIC (addition, subtraction, multiplication, division)

### 6.1 Variable assignment

```python
# Counts
lecturer_count = 1
gsi_count = 5
ia_count = 2
lab_section_count = 10
student_count = 200
```

### 6.2 Addition (`+` operator)

```python
team_count = lecturer_count + gsi_count + ia_count
print(f"team_count = {team_count}")
```

### 6.3 Subtraction (`-` operator)

```python
instructor_count = team_count - ia_count
print(f"instructor_count = {instructor_count}")
```

### 6.3 Multiplication (`*` operator)

```python
max_enrollment = lab_section_count * 25
print(f"max_enrollment = str({max_enrollment})")
```

### 6.4 Floating point division (`/` operator)

Return a decimal value (a float).

```python
avg_lab_size = student_count / lab_section_count
print(f"average lab size = {avg_lab_size}")
```

### 6.5 Floor division a.k.a integer division (`//` operator)

Return an integer value (ignore fractional values).

```python
avg_lab_size = student_count // lab_section_count
print(f"average lab size = {avg_lab_size}")
```
