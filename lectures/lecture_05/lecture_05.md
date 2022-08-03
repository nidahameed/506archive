# SI 506 Lecture 05

## Topics

1. String methods
2. List methods
3. Index operator
4. Index operator: string and list methods
5. String formatting

## Background

It is quite natural to assume that the Python programming language is named after the family of
snakes known as _Pythonidae_ or pythons. But you would be wrong. Guido van Rossum, the creator of
the Python programming language named it after the absurdist English comedy sketch series
_Monty Python's Flying Circus_ (1969-1974) which starred the "Pythons" Graham Chapman, John Cleese,
Eric Idle, Terry Jones, Michael Palin and the animator Terry Gilliam.

Today's lecture will feature the cafe [menu](https://en.wikipedia.org/wiki/Spam_(Monty_Python)#/media/File:Monty_Python_Live_02-07-14_13_04_42_(14598710791).jpg) used in the Pythons' famous
["Spam" sketch](https://en.wikipedia.org/wiki/Spam_(Monty_Python)) (1970). During the Second World
War and after Britain imposed rationing restrictions and, starting in 1941, imported massive
quantities of canned spam from the United States as a protein substitute for imports of beef, pork,
and poultry. The public, including my parents, grew to loathe it--which the sketch plays upon in
surrealist fashion.

Let's use the Pythons' "Spam" menu to explore `str` and `list` methods. Today's discussion will also
demonstrate how use of index operators to access individual members of a sequence by their position.
Finally, we will look at three ways to format values as strings.

```python
menu = """Egg and bacon
Egg, sausage and bacon
Egg and Spam
Egg, bacon and Spam
Egg, bacon, sausage and Spam
Spam, bacon, sausage and Spam
Spam, egg, Spam, Spam, bacon and Spam
Spam, Spam, Spam, egg and Spam
Spam, Spam, Spam, Spam, Spam, Spam, baked beans, Spam, Spam, Spam and Spam
Lobster Thermidor aux crevettes with a Mornay sauce, garnished with truffle pâté, brandy and a fried egg on top, and Spam"""
```

:bulb: Have you ever wondered why unwanted email is referred to as "spam". Watch the
["Spam" sketch](https://vimeo.com/233994819) and you'll quickly understand why.

## Vocabulary

* __Built-in Function__. A [function](https://docs.python.org/3/library/functions.html) defined by the Standard Library that is always available for use.
* __Expression__. An accumulation of values, operators, and/or function calls that return a value. `len(< some_list >)` is considered an expression.
* __f-string__. Formatted string literal prefixed with `f` or `F`.
* __Function__. A defined block of code that performs (ideally) a single task. Functions only run when they are explicitly called. A function can be defined with one or more _parameters_ that allow it to accept _arguments_ from the caller in order to perform a computation. A function can also be designed to return a computed value. Functions are considered "first-class" objects in the Python eco-system.
* __Iterable__. An object capable of returning its members one at a time. Both strings and lists are examples of an iterable.
* __Keyword__. A [reserved word](https://www.w3schools.com/python/python_ref_keywords.asp) that cannot be use as an identifier.
* __Immutable__. Object state cannot be modified following creation. Strings are immutable.
* __Method__. A function that "belongs" to an object. For example the `str` type is provisioned with a number of methods including `str.strip()`.
* __Mutable__. Object state can be modified following creation. Lists are mutable.
* __Operator__. A [symbol](https://www.w3schools.com/python/python_operators.asp) for performing operations on values and variables. The assignment operator (`=`) and arithmetic operators (`+`, `-`, `*`, `/`, `**`, `%`, `//`).
* __Statement__. An instruction that the Python Interpreter can execute. For example, assigning a variable to a value such as `name = 'arwhyte'` is considered a statement.

## 1.0 String methods (select list)

:bulb: References to "str" refer to the `str` data type (i.e., string), an object defined as
an immutable  sequence of characters. In the examples below, `str` refers to a generic string
object that is provisioned with a particular method (e.g., `str.lower()`).

:exclamation: the examples below also illustrate different ways to format a string.

### 1.1 str.startswidth()

Return `True` if string commences with the specified value.

```python
is_first = menu.startswith('Spam')
print(f"\nis_first = {is_first}") # formatted string literal (f-string)
```

:bulb: you can call `str.endswith()` to check if a string _ends_ with the specified value.

:bulb: Recall that `\n` represents an escape sequence, specifically an ASCII linefeed (LF). Think of
`\n` as "new line". Passing `\n` in a string will insert a new line at the position of the escape sequence.

### 1.2 str.lower()

Switch menu text to lower case.

```python
lower_case = menu.lower()
print("\nlower_case = %s" % lower_case) # old school placeholder formatting (yuck)
```

:bulb: you can call `str.upper()` to switch text to upper case.

### 1.3 str.count()

Return the number of times a specified value occurs in a string.

```python
spam_count = menu.count('Spam')
print(f"spam_count = {spam_count}\n")
```

### 1.4 str.replace()

Replace "Spam" with "Gummies".

```python
gummies_menu = menu.replace('Spam', 'Gummies')
print("\ngummies_menu = {}".format(gummies_menu)) # str.format()
```

### 1.5 str.strip()

Remove spaces at the beginning _and_ end of a string.

```python
monty_python = " Monty Python's Flying Circus " # note leading and trailing spaces
monty_python = monty_python.strip() # note reassignment using same variable (economical)
print(f"\nMonty Python (stripped) = {monty_python}")
```

:bulb: To remove spaces from either the beginning or the end of the string only use `str.left()` or
`str.right()`.

### 1.6 str.join()

Takes all elements in an iterable and joins them to a string.

```python
items = ['Oatmeal', 'Fruit', 'Spam'] # a list
menu_item = ''.join(items) # join to blank or empty string (not so good in this case)
print(f"\nMenu item = {menu_item}")

menu_item = ', '.join(items) # better
print(f"\nMenu item = {menu_item}")
```

### 1.7 str.split()

Split string on the provided delimiter and return a list of character groups. Default behavior is
to split on a space.

```python
char_groups = menu.split() # returns list
print("\nchar_groups = {}".format(char_groups)) # str.format()
```

### 1.8 str.splitlines()

Split string at each line break and return a list of individual lines.

```python
menu_items = menu.splitlines() # returns list
print("\nmenu_items = {}".format(menu_items)) # str.format()
```

## 2.0 List methods

Earlier we used `str.splitlines()` to split the menu by item (i.e., by line) and return a list of
`menu_items`. Let's explore a number of `list` methods that we can use to operate on our _mutable_
list.

### 2.1 list.append()

Append element to the end of a list (in-place)

```python
menu_items.append('Red beans and rice, and Spam') # modify in-place (no variable assignment)
print(f"\nNew menu item = {menu_items}")
```

### 2.2 list.remove()

Remove element from list (in-place).

```python
menu_items.remove('Lobster Thermidor aux crevettes with a Mornay sauce, garnished with truffle pâté, brandy and a fried egg on top, and Spam')
print(f"\nNo Lobster Thermidor = {lines}")
```

### 2.3 list.extend()

Extend list with another list (in-place).

```python
healthy_items = ['Cereal and Yogurt, and Spam', 'Oatmeal, fruit plate, and Spam']
menu_items.extend(healthy_items)
print(f"\nNew menu extended = {menu_items}")
```

### 2.4 list.sort()

Sort the list. You can pass the optional arguments `reverse=True|False` (pipe = 'or') as well as
`key=some_function` in order to further specify the sorting criteria (out of scope for the moment).

```python
menu_items.sort() # default alpha sort
print(f"\nNew menu sorted = {menu_items}")
```

## 3.0 Index operator

You can access individual members of a sequence by their position or index value. Python's index
notation is __zero-based__. Individual characters in a string or individual elements in a list can be accessed using either a positive or negative index operator. Index operator notation utilizes two brackets `[]` together with the index value as in `var[0]`.

| &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; |
|:------ |:------ |:------ |:------ |:------ |:------ |:------ |:------ |:------ |:------ |:------ |:------ |
|   0    |   1    |   2    |   3    |   4    |   5    |   6    |   7    |   8    |   9    |   10   |   11   |
|   M    |   o    |   n    |   t    |   y    | &nbsp; |   P    |   y    |   t   |    h    |    o   |    n   |
|   -12  |   -11  |  -10   |   -9   |   -8   |   -7   |   -6   |   -5   |    -4  |   -3   |   -2   |   -1   |

### 3.1 Accessing a character in a string by position

```python
name = 'Monty Python'
letter = name[0] # first letter (zero-based index)
print(f"\nLetter = {letter}")

letter = name[4]
print(f"\nLetter = {letter}")

letter = name[-1]
print(f"\nLetter = {letter}")
```

:bulb: `name[0]` is considered an expression since it resolves to a value (e.g., "M").

### 3.2 Accessing a list element by position

```python
menu_item = menu_items[1] # second element (zero-based index)
print(f"\nMenu item = {menu_item}")

menu_item = menu_items[13]
print(f"\nMenu item = {menu_item}")

menu_item = menu_item[-2]
print(f"\nMenu item = {menu_item}")
```

### 3.3 IndexError

If an index operator references a non-existent position in a sequence an `IndexError` will be
raised.

```python
# UNCOMMENT
# menu_item = menu_items[13] # IndexError: list index out of range
```

## 4.0 Index operator: list and str methods

A number of useful `list` and `str` methods leverage indexing.

### 4.1 list.index()

Return index position by value.

```python
index = menu_items.index('Egg, bacon and Spam')
print(f"\nIndex postion = {index}\n")
```

### 4.2 list.insert()

Insert element at specified index position (in-place).

```python
menu_items.insert(1, 'Blueberry pancakes and Spam')
print(f"\nBlueberry pancakes added to the menu = {menu_items}")
```

### 4.3 list.pop()

Return an element "popped" or removed from a list.

```python
retired_item = menu_items.pop(-1) # pop the last item out of the list
print(f"\nRetired item = {retired_item}")
```

### 4.4 str.find()

Finds the _first_ occurence of the specified value and returns its index value. If the value is not
located -1 is returned.

```python
menu_item = 'Spam, Spam, Spam, egg and Spam'
position = menu_item.find('Spam')
print(f"\nIndex position = {position}")

menu_item = 'Spam, Spam, Spam, egg and Spam'
position = menu_item.find('ham')
print(f"\nIndex position = {position}")
```

:bulb: `str.rfind()` attempts to locate the _last_ occurence of the specified value. If the value
is not located -1 is returned.

### 4.5 str.index()

Finds the _first_ occurence of the specified value and returns its index value. If the value is not
located a `IndexError` is raised.

```python
menu_item = 'Spam, Spam, Spam, egg and Spam'
position = menu_item.index('Spam')
print(f"\nIndex position = {position}")

menu_item = 'Spam, Spam, Spam, egg and Spam'
# UNCOMMENT
# position = menu_item.index('ham')
print(f"\nIndex position = {position}")
```

:bulb: `str.rindex()` attempts to locate the _last_ occurence of the specified value. If the value
is not located a `IndexError` is raised.

## 5.0 String formatting

There are three ways to format one or more values as a string. We recommend that you utilize the
newest approach: the formatted string literal (f-string).

### 5.1 Formatted string literal (f-string)

The f-string syntax `f"some_string {some variable}"` is less verbose and easier to construct than
earlier string formatting approaches.

```python
special_item = 'egg, bacon, spam and sausage'
print(f"\nWhy can't she have {special_item}?") # embedded variable
```

### 5.2 str.format()

Formats the specified value(s) and inserts them inside the string's placeholder `{}`.

```python
question = "\nCould I have {}, {}, {} and {}, without the spam?".format('egg', 'bacon', 'spam', 'sausage')
print(question)
```

:bulb: The placeholders can be identified using empty placeholders `{}`, numbered indexes `{0}`, or  named indexes `{egg}`.

### 5.3 %-formatting

The oldest of the three string formatting approaches. Uses the `%` operator as a placeholde. Often difficult to read.  Avoid.

```python
question = "No, it wouldn't be %s, %s, %s and %s, would it?" % (egg, bacon, spam, sausage)
print(question)
```
