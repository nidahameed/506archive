# SI 506 Lecture 07

## Topics

1. Review: method chaining gotchas
2. Tuples
3. Slicing
4. Slicing assignment
5. Built-in `del()` function and slicing
6. Built-in `sliced()` function

## Vocabulary

* __Slice__. An object usually containing a portion of a sequence. A slice is created using the
  subscript notation `[]` with colons separating numbers when several are given, such as in
  `variable_name[1:3:5]`. The bracket notation uses slice objects internally.
* __Tuple__. An ordered sequence that cannot be modified once it is created.

## Background

Today's lecture will highlight the jazz artists of the
[Jazz at Lincoln Center Orchestra](https://www.jazz.org/JLCO/) (JLCO). The JLCO is led by Wynton
Marsalis, trumpeter, composer, educator and founding member of the JLCO. We will work with the JLCO
and its list of substitute jazz artists as in order to explore sequence slicing.

```python
orchestra = [
    'Wynton Marsalis, trumpet',
    'Marcus Printup, trumpet',
    'Kenny Rampton, trumpet',
    'Sherman Irby, alto saxophone',
    'Paul Nedzela, baritone saxophone',
    'Walter Blanding, saxophone',
    'Ted Nash, saxophone',
    'Victor Goines, saxophone',
    'Chris Crenshaw, trombone',
    'Vincent Gardner, trombone',
    'Elliot Mason, trombone',
    'Carlos Henriquez, bass',
    'Dan Nimmer, piano'
]

substitutes = [
    'Anthony Lustig, baritone saxophone',
    'Carl Maraghi, baritone saxophone',
    'Erika Von Kleist, alto saxophone | flute',
    'Kurt Bacher, alto saxophone',
    'Sharel Cassity, alto saxophone | clarinet | flute',
    'Anat Cohen, clarinet | tenor saxophone',
    'Dan Block, clarinet | tenor saxophone',
    'Julian Lee, clarinet | tenor saxophone',
    'James Burton, trombone',
    'Wayne Goodman, trombone',
    'Eric Miller, trombone',
    'Kalia Vandever, trombone',
    'Mike Rodriguez, trumpet',
    'Bruce Harris, trumpet',
    'Greg Gisbert, lead trumpet',
    'Tanya Darby, lead trumpet',
    'Frank Green, lead trumpet',
    'Liesl Whitaker, lead trumpet',
    'Adam Birnbaum, piano',
    'Helen Sung, piano',
    'Christian Sands, piano',
    'Russell Hall, bass',
    'Rodney Whitaker, bass',
    'Linda Oh, bass',
    'Ulysses Owens, drums',
    'Jerome Jennings, drums',
    'Allison Miller, drums',
    'Jason Marsalis, drums'
]
```

## 1.0 Review: method chaining gotchas

### 1.1 Challenge 01

Insert Tanya Darby as lead trumpet in the _first position_ of the `orchestra` list.

```python
# TODO Retrieve Tanya's index value from the < substitutes > list.

print("\n Tanya index = {}".format(index)) # str.format()

# Insert Tanya in the first position of the < orchestra > list.

print("\n JLCO w/lead trumpet = {}".format(orchestra)) # str.format()
```

### 1.2 Challenge 02

Replace the JLCO alto saxophonist Sherman Irby with Sharel Cassity. Use `list.index()` to lookup the
index values of Irby and Cassity before effecting the substitution.

```python
irby_index = None
cassity_index = None

# TODO swap out Irby for Cassity

print(f"\nChallenge 02: w/Cassity = {orchestra}")
```

### 1.3 Challenge 03

:bulb: inspired by a Piazza post.

Remove the JLCO trumpeter Kenny Rampton from the `orchestra` list. Then add (i.e., append) Kalia
Vandever as Kenny's replacement.

:exclamation: Be careful when opting for method chaining. Recall that each method call in the chain
is an expression that returns a value. Second, recall that each method is bound to a particular
data type (e.g., `str` or `list`). Successful chaining requires that the value type returned by the
preceding method call support the next method call in the chain; if a mismatch occurs between
object and method an `AttributeError` will be raised.

```python
sax = ' alto_saxophone,baritone_saxophone,saxophone '

# Triggers an AttributeError: 'list' object has no attribute 'replace'
saxophones = sax.strip().split(',').replace('_', ' ')

# Order matters
saxophones = sax.strip().replace('_', ' ').split(',')
```

Be careful when performing in-place operations.

```python
# DON'T DO THIS

# Triggers an AttributeError: 'str' object has no attribute 'append'
# orchestra.pop().append(substitutes[substitutes.index('Helen Sung, piano')])

# or this

# AttributeError: 'NoneType' object has no attribute 'append'
# orchestra.remove('Dan Nimmer, piano').append(substitutes[substitutes.index('Helen Sung, piano')])

# TODO remove Nimmer, add Sung


print(f"\n Challenge 03: w/Sung = {orchestra}")
```

## 2.0 Tuples (a brief intro)

A Python `tuple` is an ordered sequence of items. Like `list` elements, tuple items can be accessed
via indexing and slicings, but unlike lists, tuple values cannot be modified (immutable). This
feature provides optimization opportunities when working with sequences of values that either must
not change or form “natural” associations ('New Orleans', 'LA', ‘USA’).

Tuples are defined by enclosing the items in parentheses `()` instead of square brackets `[]` as
is the case with lists. A single item tuple must include a trailing comma (`,`) or the Python
interpreter will consider the expression a string.

```python
city = ('New Orleans',) # single item tuple

print(type(city)) # prints <class 'tuple'>
```

Once created a tuple cannot be modified. Attempts to modify or replace any tuple item will Trigger
a `TypeError` runtime exception.

```python
city = ('New Orleans', 'LO', 'USA') # error in state code
city[1] = 'LA' # triggers TypeError: 'tuple' object does not support item assignment
```

You can access individual tuple items using indexing.

```python
# Wynton Marsalis, Majesty of the Blues (1989)
majesty_blues = (
    'The Majesty Of The Blues (The Puheeman Strut)',
    'Hickory Dickory Dock',
    'The Death Of Jazz',
    'Premature Autopsies (Sermon)',
    'Oh, But On The Third Day (Happy Feet Blues)'
)

sermon = majesty_blues[3]

print(f"\n2.0 Majesty of the Blues sermon = {sermon}")
```

## 3.0 Slicing

You can access a `list` element, `tuple` item, or `str` character by position using an index
operator. You can also access a subset or _slice_ of elements, items, or characters using Python's
slicing notation.

To initate a slicing operation specify a range of index values by extending the index operator to
include an _optional_ integer `start` value, a _required_ integer `end` value that specifies the
position in which to end the slicing operation, and an _optional_ `stride` value that specifies the
slicing step (default = 1).

The slicing notation syntax simplifies referencing and/or extracting a subset of a given sequence.
List slicing can result in list traversal performance gains since slicing obviates the need to loop
over an entire list in order in order to operate on a targeted subset of elements. We will explore
this aspect of slicing when we explore list iteration in more detail starting next week.

```python
quintet = (
    'Wynton Marsalis, trumpet',
    'Walter Blanding, tenor sax | soprano sax | clarinet',
    'Carlos Henriquez, bass',
    'Jason Marsalis, drums',
    'Dan Nimmer, piano'
)

# Returns Carlos Henriquez and Jason Marsalis
bass_drums = quintet[2:4] # range of index values

print(f"\nbass_drums = {bass_drums}")

# Returns Walter Blanding and Carlos Henriquez
sax_bass = quintet[-4:-2]

print(f"\nsax_bass = {sax_bass}")
```

In the above slicing example the start value "2" is considered _inclusive_ while the end value
"4" is considered _exclusive_. Negative slicing can also be employed to return a subset of a
sequence.

Let's explore more examples.

### 3.1 slice from index 0 to index n (stride = 1)

Return first three JLCO musicians.

```python
musicians = orchestra[:3] # or orchestra[0:3]

print(f"\n3.1 First 3 musicians = {musicians}")
```

### 3.2 slice from index -1 to index -n (stride = 1)

Return last three musicians (negative slicing).

```python
musicians = orchestra[-3:] # warn: not the same as orchestra[-3:-1]

print(f"\n3.2 Last 3 musicians = {musicians}")
```

### 3.3 slice from index n to index n (stride = 1)

Return all JLCO saxophonists.

```python
# WARN: earlier we inserted a lead trumpeter into position 0, so select range wisely.
musicians = orchestra[4:9]

print(f"\n3.3 JLCO saxophonists = {musicians}")
```

### 3.4 slice from index -n to index -n (stride = 1)

Return trombonists (negative slicing)

```python
musicians = orchestra[-5:-2]

print(f"\n3.4 JLCO trombonists = {musicians}")
```

### 3.5 slice from index n to index n (stride = 2)

Return every other JLCO substitute musician, starting at index 0.

```python
musicians = substitutes[0::2]

print(f"\n3.5 Every other substitute musician = {musicians}")
```

### 3.6 slice from index -n to index -n (stride = 2)

Return every other substitute bassist, pianist, and drummer, using negative indexing.

```python
musicians = substitutes[-10::2]

print(f"\n3.6 Every other substitute bassist, pianist, and drummer = {musicians}")
```

### 3.7 slice from index 0 to end of list (stride = -1)

Return JLCO musicians in reverse order.

```python
musicians = orchestra[::-1]

print(f"\n3.7 JLCO musicians in reverse order = {musicians}")
```

### 3.8 slice from index n to index n (set stride = -1)

Return substitute clarinets in reverse order.

```python
musicians = substitutes[5:8:-1] # does not work
# musicians = substitutes[-23:-20:-1] # does not work

print(f"\n3.8 Substitute clarinetists in reverse order = {musicians}")

# This approach works
musicians = substitutes[5:8]
musicians = musicians[::-1]

print(f"\n3.8 Substitute clarinetists in reverse order = {musicians}")
```

## 4.0 Slice Assignment

You can replace a subset of a list with another list using slice assignment.

### 4.1 Replace part of a list (length remains unchanged)

Replace three JLCO trombonists with first three substitute trombonists.

```python
# Replace Crenshaw, Gardner, and Mason with Burton, Goodman, and Miller.
orchestra[-5:-2] = substitutes[8:11]

print(f"\n3.9 Replace JLCO trombonists with substitutes = {orchestra}")
```

### 4.2 Replace part of a list (length changes)

Replace JLCO trumpeters (n=3) with all substitute trumpeters including leads (n=6)

```python
orchestra[:4] = substitutes[12:18]

print(f"\n3.10 Replace JLCO trumpeters with substitute trumpeters = {orchestra}")
```

:bulb: you can also replace part of list with a smaller list. You can also replace every n-th
element by specifying a step value.

## 5.0 Built-in `del()` function and slicing

You can delete a subset of a list using slicing in combination with the built-in del() function.

### 5.1  Delete a slice with built-in del() function

Delete the lead trumpeters we just added.

```python
del(orchestra[2:6])

print(f"\n3.11 Delete lead trumpeters = {orchestra}")
```

## 6.0 Built-in `slice()` function

:exclamation: The built-in `slice()` function is out-of-scope for SI 506.

You can also slice a sequence using the built-in `slice()` function. The `slice()` function
returns a `slice` object accepts up to three arguments, an optional integer `start` value
(default = 0), a required integer `end` value that specifies the position in which to end the
slicing operation, and an optional `step` value that specifies the slicing step (default = 1).

```python
musicians = ['Ellis Marsalis', 'Wynton Marsalis', 'Branford Marsalis', 'Delfeayo Marsalis', 'Jason Marsalis']

# slice([start, ]end[, step]) object
s = slice(1, 4, 2)
wynton_delfeayo = musicians[s]

print(f"\nslice() example = {wynton_delfeayo}")
```
