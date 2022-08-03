# SI 506 Lecture 06

## Marvel Super Heroes Exercise

## Topics

1. Variable assignment
2. Built-in functions
3. `str` methods
4. `list` methods
5. Method chaining
6. String formatting

## Reference

1. [`list` methods](https://www.w3schools.com/python/python_ref_list.asp)
2. [`str` methods](https://www.w3schools.com/python/python_ref_string.asp)

## Warmup 01

Replace the string "Black Widow" with "Black Panther" and assign the return value to `new_hero`.

```python
hero = 'Black Widow'

new_hero = None

print(f"\nnew hero = {new_hero}")
```

## Warmup 02

Restyle the Marvel Super Hero names contained in `marvel_heroes`, changing the all capitalized
letters to lowercase and each space with an underscore (`_`). Then split the string with the
appropriate delimiter and assign the return value to the variable `restyled_heroes`. The new list
must match `['captain_america', 'iron_man']`.

```python
marvel_heroes = 'Captain America, Iron Man'

restyled_heroes = None

print(f"\nRestyled heroes = {restyled_heroes}")
```

## Challenge 01

Convert the `marvel_heroes` string to a list and assign it to the variable `heroes`.

```python
marvel_heroes = "Black Panther, Black Widow, Captain America, Dr Strange, \
Hawkeye, Iron Man, Hulk, Scarlet Witch, Spider-Man, Thor"

# TODO convert string to a list.

print(f"\nheroes = {heroes}")
```

:bulb: You can join two or more physical lines into a single logical line by using a
backslash (`\`) character as a line continuation character at the end of each line. Do not confuse
this with the new line `\n` escape sequence.

## Challenge 02

Add the name T'Challa to the end of the multiline string `marvel_characters` on its own line.

```python
marvel_characters = """Bruce Banner
Clint Barton
Wanda Maximoff
Peter Parker
Steve Rogers
Natasha Romanoff
Tony Stark
Stephen Strange
Thor Odinson"""

# TODO add T'Challa.

print(f"\nAdded T'Challa = {marvel_characters}")
```

## Challenge 03

Convert the `marvel_characters` multiline string to a list and assign it to the variable `characters`.

```python
# TODO convert multiline string to a list.

print(f"\ncharacters = {characters}")
```

## Challenge 04

Convert the `hollywood_actors` string to a list and assign it to the variable `actors`.

```python
hollywood_actors = (
    "Chadwick Boseman | Benedict Cumberbatch | Robert Downey Jr | Chris Evans | "
    "Chris Hemsworth | Tom Holland | Scarlett Johansson | Elizabeth Olsen | "
    "Jeremy Renner | Mark Ruffalo"
    )

# TODO convert string to a list.

print(f"\nactors = {actors}")
```

:bulb: Long lines can also be written over multiple lines by _wrapping_ expressions in parentheses.

## Challenge 05

Assign the hero Thor to a variable named `thor` and then append `thor` to an empty list named `avengers`.

```python
# TODO create < thor > and append to < avengers >.

print(f"\navengers = {avengers}")
```

## Challenge 06

Append the hero Captain America directly to the `avengers` list.

```python

# TODO Add Captain America to the < avengers > list.

print(f"\navengers = {avengers}")
```

## Challenge 07

Insert the hero Iron Man in the second position (i.e., second element) in the `avengers` list.

```python
# TODO insert Iron Man as the second element in the < avengers > list.

print(f"\navengers = {avengers}")
```

## Challenge 08

Add the heroes Hulk and Black Widow (in that order) to an empty list named `other_avengers` list and
then add `other_avengers` to the `avengers` list.

```python

# TODO create < other_avengers >, add Hulk and Black Widow, and then add < other_avengers >.
# to < avengers >

print(f"\navengers = {avengers}")
```

## Challenge 09

Append the hero Hawkeye to the `avengers` list using `list.append()`. When calling `list.append()`
pass in the hero element using `list.index()` to "lookup" Hawkeye's index value instead of hard-
coding the value.

```python
# TODO append Hawkeye to < avengers > using list.index() to lookup Hawkeye's index value.

print(f"\navengers = {avengers}")
```

## Challenge 10

Return a count of the `avengers` and assign to `avengers_count`.

```python
# TODO return the length of the < avengers >.

print(f"\navengers count = {avengers_count}")
```

## Challenge 11

Match each hero in the `avengers` list to their character name and then update each element's string
value in the `avengers` list. Use an f-string to format each string as follows:

`< Hero > (< character >)`, e.g., 'Captain America (Steve Rogers)'

```python
# TODO update each < avenger > string value with the character name.

print(f"\navengers = {avengers}")
```

## Challenge 12

Replace Hawkeye with Black Panther (include character name). Use `str.join()` and an iterable (list)
to build the `< hero > ( < character  > )` string. Assign the return value of `str.join()` to a
variable named `hero`. Then assign `hero` to the appropriate `avengers` element.

```python
# TODO Replace Hawkeye with Black Panther

print(f"\navengers = {avengers}")
```

## Challenge 13

Replace the parentheses "()" surrounding Thor Odinson's name with '<' and '>'.

```python
# TODO replace () surrounding Thor Odinson with <>.

print(f"\navengers = {avengers}")
```

## Challenge 14

Black Widow and Iron Man sacrificed their lives in the struggle against Thanos. Sadly, we need to
remove them from the active `avengers` list. But we will also restore Hawkeye to the team.

1. Remove Black Widow from < avengers > using list.remove().
2. Remove Iron Man from < avengers > using list.pop(). But instead of passing a hard-coded position value
   to list.pop() call list.index() to obtain the index position, passing the expression to list.pop()
   of Iron Man and pass it to list.pop().
3. Add Hawkeye.

```python

# TODO remove Black Widow and Iron Man; restore Hawkeye.

print(f"\navengers = {avengers}")
```

## Sources

Wikipedia, ["Characters_of_the_Marvel_Cinematic_Universe"](https://en.wikipedia.org/wiki/Characters_of_the_Marvel_Cinematic_Universe)\
Wikipedia, ["Avengers (comics)"](https://en.wikipedia.org/wiki/Avengers_(comics))\
Fandom. Marvel Movies, ["Avengers (team)"](https://marvel-movies.fandom.com/wiki/Avengers_(team))