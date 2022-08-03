# SI 506 Lecture 12

## TOPICS

1. Functions (challenges)
2. Variable scope

## Vocabulary

* __Argument__. A value or expression passed to a function.
* __Caller__. The initiator of a function call.
* __Function__. a named series of statements (a code block) that performs a computation whenever
  the function is invoked by a caller. Parameters can be declared in a function definition in order
  to permit the processing of input values (i.e., arguments). Functions typically, though not
  always, compute a result to be returned to the caller.
* __Parameter__. A named entity or object in a function definition that specifies an argument or
  arguments that the function can accept from a caller.
* __Scope__. The part of a script or program in which a variable and the object to which it is
  assigned is visible and accessible.

```python
scale = [('5 stars', 5), ('4 stars', 4), ('3 stars', 3), ('2 stars', 2), ('1 star', 1)]

# Compiled 7 October 2020
cereals = [
    ["Cap'n Crunch", (5, 1), (4, 0), (3, 0), (2, 0), (1, 0)],
    ['Cheerios', (5, 40), (4, 6), (3, 0), (2, 0), (1, 0)],
    ["Cinnamon Toast Crunch", (5, 45), (4, 2), (3, 1), (2, 0), (1, 0)],
    ['Cocoa Puffs', (5, 18), (4, 1), (3, 1), (2, 0), (1, 0)],
    ['Corn Flakes', (5, 155), (4, 10), (3, 1), (2, 1), (1, 0)],
    ['Frosted Flakes', (5, 403), (4, 32), (3, 6), (2, 1), (1, 0)],
    ['Fruit Loops', (5, 187), (4, 32), (3, 3), (2, 2), (1, 0)],
    ['Honey-nut Cheerios', (5, 33), (4, 5), (3, 0), (2, 0), (1, 0)],
    ['Life Cereal', (5, 69), (4, 22), (3, 16), (2, 12), (1, 43)],
    ['Lucky Charms', (5, 12), (4, 0), (3, 0), (2, 0), (1, 0)],
    ['Raisin Bran', (5, 349), (4, 36), (3, 7), (2, 1), (1, 1)],
    ['Rice Krispies', (5, 145), (4, 17), (3, 2), (2, 1), (1, 1)],
]
```

## 1.0 Variable scope

Now that you have begun to write functions it's time to discuss Python's rules for resolving name
references (i.e., variables). Accessing a variable and the object to which it is assigned depends in
large part on _where_ the variable is defined in your program. An object's duration or lifetime also
depends in part on _where_ in your program it is assigned. A variable's _scope_ is limited to those
parts of a program in which the variable is visible and can be accessed.

A variable defined _inside_ a function is considered _local_ to that function. In other words, a
local variable can only be accessed from inside the function's code block. On the other hand, a
variable defined outside a function in the main part of a program file or module possesses top level
or _global_ scope. Such a variable is visible throughout the program from the point in which it was
first defined. Treat _global_ variables carefully. Referencing _global_ variables inside functions
can have unintended effects.

Python keywords and built-in functions possess a special _built-in_ scope and are also
available whenever you execute a script or run your program.

In the following example referencing the local variable `name` outside the function `format_name`
will trigger a `NameError` runtime exception.

```python
cereal = ('General Mills', 'Cocoa Puffs', 20, 4.9) # global scope

if cereal: # truth value
    cereal_exists = True # available globally

def format_name(cereal):
    name = f"{cereal[0]} {cereal[1]}" # local scope only
    return name

print(f"\n1.0: Cereal exists = {cereal_exists}")

cereal_name = format_name(cereal) # call function

print(f"\n1.0: Cereal name = {cereal_name}")

print(f"\n1.0: Local variable name = {name}") # Triggers NameError: name 'name' is not defined
```

## 2.0 Challenges

:bulb: for each of these challenges consider writing a `print()` statement and/or using VS Code's
debugger to confirm the function's return value.

### Challenge 01

Define a function named `get_cereal_name` with a single parameter: `cereal` (`list`). The function
will accept a single cereal argument (_not_ a nested list of cereals) and return the cereal's name
using an index operator.

Call the function by passing to it the following argument(s):

1. The _first element_ in the list `cereals`

:bulb: A single statement should suffice for the function block.

```python
# TODO: implement function

name = None # call function, assign return value
```

### Challenge 02

Define a function named `check_cereal_name` with two parameters: `cereal` (`list`) and `name`
(`str`). The function will accept a single cereal argument and check it for a matching cereal name;
if located return `True`, otherwise return `False`.

Call the function by passing to it the following argument(s):

1. the _last element_ in the cereal reviews list
2. the string "Rice Krispies".

Assign the return value to a variable named `has_element`.

:bulb: A single statement should suffice for the function block.

```python
# TODO: implement function

has_element = None # call function, assign return value
```

### Challenge 03

Define a function named `get_cereal` with two parameters: `cereals` (`list`) and `name` (`str`). The
function will loop over the nested `cereals` list and return the `cereal` element whose name matches
the passed in `name` argument. Write a conditional statement that calls the function `has_cereal` to
accomplish the filtering task.

Call the function by passing to it the following argument(s) _in the following order_ using
_keyword arguments_:

1. the string "Frosted Flakes".
2. the nested `cereals` list

Assign the return value to a variable named `cereal`.

```python
# TODO: implement function

cereal = None # call function, assign return value
```

### Challenge 04

Define a function named `count_cereal_reviews` with a single parameter: `cereal` (`list`). The
function will accept a single cereal argument and then loop over the rating elements in order to
sum all the ratings across each of the five tuples `( < star value >, < rating count >)`.

To obtain the desired cereal you _must_ first call the function `get_cereal` and pass to it the
following argument(s):

1. nested `cereals` list
2. the string "Frosted Flakes".

Assign the return value to a variable name `cereal`.

Then call `count_cereal_reviews` passing to it the following argument(s):

1. `cereal`

Assign the return value to a variable named `review_count`.

```python
# TODO: implement function

cereal = None # call function, assign return value
review_count = None # call function, assign return value
```

### Challenge 05

Define a function named `count_favorable_reviews` with a single parameter: `cereal` (`list`). The
function will return a count of reviews limited to 4 star and 5 star ratings _only_.

To obtain the desired cereal you _must_ first call the function `get_cereal` and pass to it the
following argument(s):

1. nested `cereals` list
2. the string "Raisin Bran".

Assign the return value to a variable name `cereal`.

Then call `count_favorable_reviews` passing to it the following argument(s):

1. `cereal`

Assign the return value to a variable named `favorable_count`.

```python
# TODO: implement function

cereal = None # call function, assign return value
favorable_count = None # call function, assign return value
```

### CHALLENGE 06

Define a function named `favorite_cereal` with a single parameter: `cereals` (`list`). The function
will loop over the nested `cereals` list and identify the cereal with the most favorable ratings.

In the function block create a local variable named `selection` (`list`). The list will hold the
"current" favorable cereal name (`str`) and the review rating count (`int`). Seed the list with
default values. These values will be updated whenever a new contender for "favorite cereal" is
identified when looping over the `cereals` list.

Call the function by passing to it the following argument(s):

1. the nested `cereals` list

Loop over each cereal in the `cereals` list. Call `count_favorable_reviews` and return a
count of the 4 star and 5 star review ratings. Assign it to a local variable. Then write a
conditional statement that checks if the current review ratings count is greater than the count
stored in the `selections` list.

If the conditional statement evaluates to `True` update the local `selection` list by first calling
`get_cereal_name` to retrieve the name of the current `cereal`. Assign the return value to the
first element. Then assign the current review ratings count to the second element.

exclamation: You _must_call `get_cereal_name` in order to retrieve the name of the current cereal
being evaluated before updating the `selection` list.

After the loop terminates return `selection` to the caller and assign the list to a variable named
`favorite`.

```python
# TODO: implement function

favorite = None # call function, assign return value
```

### CHALLENGE 07

Define a function named `count_unfavorable_reviews` with a single parameter: `cereal` (`list`). The
function will return a count of reviews limited to 1 star and 2 star ratings _only_.

To obtain the desired cereal you _must_ first call the function `get_cereal` and pass to it the
following argument(s):

1. nested `cereals` list
2. the string "Fruit Loops".

Assign the return value to a variable name `cereal`.

Then call `count_favorable_reviews` passing to it the following argument(s):

1. `cereal`

Assign the return value to a variable named `unfavorable_count`.

```python
# TODO: implement function

cereal = None # call function, assign return value
unfavorable_count = None # call function, assign return value
```

### CHALLENGE 08

Define a function named `least_favorite_cereal` with a single parameter: `cereals` (`list`). The function
will loop over the nested `cereals` list and identify the cereal with the least favorable ratings.

In the function block create a local variable named `selection` (`list`). The list will hold the
"current" least favorite cereal name (`str`) and the review rating count (`int`). Seed the list with
default values. These values will be updated whenever a new contender for "least favorite cereal" is
identified when looping over the `cereals` list.

Call the function by passing to it the following argument(s):

1. the nested `cereals` list

Loop over each cereal in the `cereals` list. Call `count_unfavorable_reviews` and return a
count of the 1 star and 2 star review ratings. Assign it to a local variable. Then write a
conditional statement that checks if the current review ratings count is greater than the count
stored in the `selections` list.

If the conditional statement evaluates to `True` update the local `selection` list by first calling
`get_cereal_name` to retrieve the name of the current `cereal`. Assign the return value to the
first element. Then assign the current review ratings count to the second element.

exclamation: You _must_call `get_cereal_name` in order to retrieve the name of the current cereal
being evaluated before updating the `selection` list.

After the loop terminates return `selection` to the caller and assign the list to a variable named
`least_favorite`.

```python
# TODO: implement function

least_favorite = None # call function, assign return value
```

### Challenge 09 (bonus)

:exclamation: for the midterm you will _not_ be asked to write a function that accepts another
function as an argument.

Recall that functions are first class objects. As such they can be passed to other functions as in
the example below, which represents a refactoring of the functions `favorite_cereal` and
`least_favorite_cereal` into a single function.

Note that the only difference between the two code blocks is in the choice of function employed to
return the review count (i.e., either `count_favorable_reviews` or `count_unfavorable_reviews`). In
the function `select_cereal_by_sentiment` the name assigned to either of these functions is passed
in by object reference as a second argument named `func_name`. The target function can then be
called by passing any required arguments to it.

```python
def select_cereal_by_sentiment(cereals, func_name):
    selection = [None, 0] # cereal name, count

    for cereal in cereals:
        review_count = func_name(cereal)
        if review_count > selection[1]:
            selection[0] = get_cereal_name(cereal)
            selection[1] = review_count

    return selection

favorite = select_cereal_by_sentiment(cereals, count_favorable_reviews)
print(f"\nChallenge 09 (refactored): favorite cereal: {get_cereal_name(favorite)} (n={favorite[1]})")

least_favorite = select_cereal_by_sentiment(cereals, count_unfavorable_reviews)
print(f"\nChallenge 09 (refactored): least favorite cereal: {get_cereal_name(favorite)} (n={least_favorite[1]})")
```

### Challenge 10

Define a function named `calculate_weighted_mean` with a single parameter: `cereal` (`list`). The
function will calculate a weighted mean for the ratings earned by a given cereal.

Inside the function create the local "accumulator" variables `dividend` and `divisor`. Assign each
the default value of zero.

Calculate the weighted mean by assigning a "weight" to each star based on the number of votes
it received. The following equation will suffice:

`(5 * < 5 star count > + 4 * < 4 star count > + 3 * < 3 star count > + 2 * < 2 start count > + 1 * < 1 start count >)` \
divided by (`/`) \
`(< 5 star count > + < 4 star count > + < 3 star count > + < 2 start count > + < 1 start count >)`

Example (Life Cereal): `(5 * 69 + 4 * 22 + 3 * 16 + 2 * 12 + 1 * 43) / (69 + 22 + 16 + 12 + 43)`

Loop over the cereal's five rating tuples. For each star rating tuple encountered, multiply the
star rating number (e.g., 5 for the 5 star rating) by the number of ratings the star received
(e.g., the rating count) and add the product to `dividend`. Then add the rating count to `divisor`.

Ater the loop terminates divide `dividend` by `divisor` and assign the return value (round to 2
decimal points) to a variable named `weighted_mean`. Return `weighted_mean` to the caller.

Test the function by first calling `get_cereal` and passing to it the nested `cereals` list and
a cereal name (e.g., "Corn Flakes"). Assign the return value to a variable named `cereal`
and then call `calculate_weighted_mean` passing in `cereal` as the argument. Assign the return value
to `weighted_mean`.

:bulb: For more info on weighted means see _Wikipedia_,
['Weighted Arithmetic Mean"](https://en.wikipedia.org/wiki/Weighted_arithmetic_mean).

```python
# TODO: implement function

cereal = None # call function, assign return value
weighted_mean = None # call function, assign return value
```

Then loop over the nested `cereals` list, calculate the rating weighted mean for each cereal, and
print the result using an f-string employing the format
`< cereal name >, < rating weighted mean > (n=< total ratings count >))`

```python
print(f"\nChallenge 10: {get_cereal_name(cereal)} rating {weighted_mean} (weighted mean)")

# Print all weighted means
print(f"\nCereal, Weighted mean, Total ratings\n")

for cereal in cereals:
    name = get_cereal_name(cereal)
    weighted_mean = calculate_weighted_mean(cereal)
    count = count_cereal_reviews(cereal)

    print(f"{name}, {weighted_mean} (n={count})")
```

:exclamation: _Out of scope_ for SI 506 but if you wanted to sort the cereals by weighted mean
(descending order) you can call the `list.sort()` method specifying a `lambda` function assigned to
that is assigned to the `key` parameter along with an option sort order. The anonymous `lambda`
function provides the sort algorithmn to be applied to the list.

```python
print(f"\nChallenge 10: Cereal, Weighted mean, Total ratings (sorted)\n")

# List comprehension returns a list of tuples.
ratings = [
    (get_cereal_name(cereal), calculate_weighted_mean(cereal), count_cereal_reviews(cereal))
    for cereal in cereals
    ]

# Sort list in-place using a lambda expression.
ratings.sort(key=lambda cereal: cereal[1], reverse=True) # sort by rating, reverse order

for cereal in ratings:
    print(f"{cereal[0]}, {cereal[1]} (n={cereal[2]})")
```

## Sources

1. _cvs.com_, ["Cap'n Crunch"](https://www.cvs.com/shop/quaker-cap-n-crunch-original-prodid-111316)
2. _cvs.com_, ["Cheerios"](https://www.cvs.com/shop/cheerios-cereal-prodid-169905)
3. _cvs.com_, ["Cinnamon Toast Crunch"](https://www.cvs.com/shop/general-mills-cinnamon-toast-crunch-cereal-prodid-813576)
4. _cvs.com_, ['Cocoa Puffs'](https://www.cvs.com/shop/general-mills-cocoa-puffs-whole-grain-cereal-prodid-558865)
5. _cvs.com_, ["Corn Flakes"](https://www.cvs.com/shop/kellogg-s-corn-flakes-cereal-prodid-273722)
6. _cvs.com_, ["Frosted Flakes"](https://www.cvs.com/shop/kellogg-s-frosted-flakes-cereal-prodid-103604)
7. _cvs.com_, ["Fruit Loops"](https://www.cvs.com/shop/kellogg-s-froot-loops-cereal-prodid-720656)
8. _cvs.com_, ["Honey-nut Cheerios"](https://www.cvs.com/shop/cheerios-honey-nut-cereal-prodid-731695)
9. _cvs.com_, ["Life Cereal"](https://www.cvs.com/shop/quaker-life-original-multigrain-cereal-13-oz-prodid-767123)
10. _cvs.com_, ["Lucky Charms"](https://www.cvs.com/shop/lucky-charms-cereal-prodid-731232)
11. _cvs.com_, ["Raisin Bran"](https://www.cvs.com/shop/kellogg-s-raisin-bran-cereal-prodid-353920)
12. _cvs.com_, ["Rice Krispies"](https://www.cvs.com/shop/kellogg-s-rice-krispies-cereal-prodid-720037)
