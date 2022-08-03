# SI 506 Lecture 09

## Topics

1. `for` loop (definite iteration)
2. Conditional statements
3. `if` statement
4. `if-elif-else` blocks
5. `continue`, `break` statements

## Vocabulary

* __Conditional Statement__. A statement that determines a computer program's _control flow_ or the
  order in which particular computations are to be executed.
* __Iteration__. Repetition of a computational procedure in order to generate a possible sequence of
  outcomes. Iterating over a `list` using a `for` loop is an example of iteration.

## 1.0 Iteration

Suspend disbelief and imagine that you are a paleontologist working with data about a class of
extinct reptiles known as dinosaurs. Given a list of dinosaur names and a task to return a subset of
all names that commence with the letter 'T' we could accomplish the task by referencing each targeted
element's index position.

```python
dinosaur_names = [
    'Psittacosaurus',
    'Brachiosaurus',
    'Edmontosaurus',
    'Parasaurolophus',
    'Triceratops',
    'Apatosaurus',
    'Diplodocus',
    'Deinocheirus',
    'Ankylosaurus',
    'Ceratosaurus',
    'Stegosaurus',
    'Velociraptor',
    'Styracosaurus',
    'Allosaurus',
    'Dreadnoughtus',
    'Camptosaurus',
    'Corythosaurus',
    'Pachycephalosaurus',
    'Tyrannosaurus',
    'Gigantoraptor'
    ]

dinosaur_names_t = []
dinosaur_names_t.append(dinosaur_names[4])
dinosaur_names_t.append(dinosaur_names[-2])

print(f"\n1.0 T named dinosaurs = {dinosaur_names_t}")
```

The efficiency of referencing individual list elements by their index position begins to fall away
as the list of names grows in size. In the case of dinosaurs, it is reported that "paleontologists
have identified over 500 distinct genera and more than 1,000 different species of non-avian
dinosaurs" [<a name="endnote_01">1</a>]. Accessing dinosaur species with a name starting with the
letter "T" in the manner above would prove both time consuming and result in a series of repetitive
statements that would prove difficult to maintain as the list of dinosaur names mutated over time.

### 1.1 `for` loop and `if` statement

A more efficient approach is to utilize a `for` loop that includes an `if` statement. The `for`
loop employs the keywords `for` and `in` as in the expression `for < element > in < some_sequence >:`
along with a trailing colon (`:`) that indicates the start of the loop's code block. The statement(s)
that comprise the loop's code block _must_ be indented four spaces. The statements are local to the
the loop and are only executed when the loop is run.

Likewise, a block of one or more statements that are to be executed whenever an `if` statement
evaluates to `True` _must_ also be indented.

For the current task, a conditional statement can be designed to test for dinosaur names that
commence with the letter "T". In this scenario, the `if` statement acts as a filter, identifying "T"
named dinosaurs whenever the condition evaluates to `True`. When an element satisfies the condition
it can be appended to a target list that acts as an "accumulator".

:exclamation: Failure to employ Python's indentition rules can lead to unexpected computations and/or
trigger an `IndentionError`.

```python
dinosaur_names_t = [] # accumulator
for dinosaur in dinosaur_names:
    if dinosaur.lower().startswith('t'):
        dinosaur_names_t.append(dinosaur)

print(f"\n1.1 T named dinosaurs = {dinosaur_names_t}")
```

### 1.2 Working with "overloaded" string data

However, what if the list of strings contained more information about each individual dinosaur than
just a name? Let's assume that each string comprising the list also included information on clade
(i.e., group affiliation), the geologic period (e.g., Jurassic or Cretaceous) in which the dinosaur
lived, along with its max length (meters), max weight (kilograms), and diet.

```python
dinosaur_strings = [
    'Psittacosaurus, Marginocephalia, Cretaceous, 2, 20, herbivore',
    'Brachiosaurus, Sauropoda, Jurassic, 21, 58000, herbivore',
    'Edmontosaurus, Ornithopoda, Cretaceous, 12, 4000, herbivore',
    'Parasaurolophus, Ornithopoda, Cretaceous, 9.5, 2500, herbivore',
    'Triceratops, Marginocephalia, Cretaceous, 9, 12000, herbivore',
    'Apatosaurus, Sauropoda, Jurassic, 22, 22400, herbivore',
    'Diplodocus, Sauropoda, Jurassic, 24, 14800, herbivore',
    'Deinocheirus, Theropoda, Cretaceous, 11, 6400, omnivore',
    'Ankylosaurus, Eurypoda, Cretaceous, 8, 8000, herbivore',
    'Ceratosaurus, Theropoda, Jurassic, 7, 980, carnivore',
    'Stegosaurus, Eurypoda, Jurassic, 9, 7000, herbivore',
    'Velociraptor, Theropoda, Jurassic, 1.5, 33, carnivore',
    'Styracosaurus, Marginocephalia, Cretaceous, 5.5, 3000, herbivore',
    'Allosaurus, Theropoda, Jurassic, 12, 1500, carnivore',
    'Dreadnoughtus, Sauropoda, Cretaceous, 26, 38192, herbivore',
    'Camptosaurus, Ornithopoda, Cretaceous, 7.9, 874, herbivore',
    'Corythosaurus, Ornithopoda, Cretaceous, 8.1, 3078, herbivore',
    'Pachycephalosaurus, Marginocephalia, Cretaceous, 4.5, 450, herbivore',
    'Tyrannosaurus, Theropoda, Cretaceous, 12.3, 8400, carnivore',
    'Gigantoraptor, Theropoda, Cretaceous, 8.9, 3600, carnivore'
    ]

dinosaur_count = len(dinosaurs_strings)
print(f"\n1.2.1 Dinosaurs count = {dinosaur_count}")
```

If we wanted to identify all theropods in the list we could write an `if` statement that evaluates
to `True` if the substring 'theropoda' is found to exist in the string.

:bulb: Note the use of `str.lower()` together with `str.find()` in the conditional statement's
method chaining. `str.lower()` ensures that no variations in a substring's case will lead to an
otherwise targeted element being missed. This is an example of "defensive" programming. When
working with string data never assume that the data is "clean" (i.e., uniform and consistent).

```python
# str.find() returns -1 if the index position is not found.
therapods = []
for dinosaur in dinosaurs_strings:
    if dinosaur.lower().find('theropoda') >= 0:
        therapods.append(dinosaur)

print(f"\n1.2.2 Therapods using find() = {therapods}")
```

Working with string data gets trickier when you need to filter on multiple conditions.

Are there any saurpods in the `dinosaurs` list that roamed the earth during the Cretaceous Period?
We can employ the logical operator `and` in an attempt to filter on two conditional statements but
the Python interpreter will not perform the computation as written.

```python
# This fails
sauropods = []
for dinosaur in dinosaurs_strings:
    if dinosaur.lower().find('saurapoda') >= 0 and dinosaur.lower().find('cretaceous') >= 0:
        sauropods.append(dinosaur)

print(f"\n1.2.3 Cretaceous Saurapods find() x 2 fail = {sauropods}")
```

We need a different approach. We could either use the `re` module and a regular expression to
search for both substrings in the string or use the built-in `all()` function together with a list
comprehension to implement our intended filter. Both approaches, however, are _out of scope_ for
SI 506.

```python
# Regular expression (out of scope)
pattern = re.compile(r"^.*?\bSauropoda\b.*?\bCretaceous\b.*?$") # regular expression
sauropods = []
for dinosaur in dinosaurs_strings:
    if pattern.match(dinosaur):
        sauropods.append(dinosaur)

print(f"\n1.2.4 Cretaceous saurapods regex = {sauropods}")

# Built-in all() function with comprehension (out of scope)
words = ('Sauropoda', 'Cretaceous')
sauropods = []
for dinosaur in dinosaurs_strings:
    if all(word in dinosaur.split(', ') for word in words):
        sauropods.append(dinosaur)

print(f"\n1.2.5 Cretaceous saurapods all() = {sauropods}")
```

We need a different approach that better aligns with your current Python knowledge. The example
below demonstrates that you can leverage your string handling skills to accumulate the same values
returned by the more refined approaches illustrated above. When looping over `dinosaur_strings`
split each string element encountered and assign the returned list to a variable (e.g., `data`)
inside the loop. Then revise the conditional statement comparing the relevant `data` element against
the appropriate filter string value (e.g., "sauropoda", "cretaceous"). List elements that satisfy
the comparison checks can then be converted back to a string and appended to the `sauropods` list
or simply appended to `sauropods` creating a list of lists.

```python
sauropods = []
for dinosaur in dinosaur_strings:
    data = dinosaur.split(', ')
    if data[1].lower() == 'sauropoda' and data[2].lower() == 'cretaceous':
        sauropods.append(', '.join(data)) # recreate string
        # sauropods.append(data) # more likely scenario: append list to list

print(f"\n1.2.6 Cretaceous saurapods split() = {sauropods}")
```

### 1.3 Nested lists

Operating on a list of strings, each of which is masquerading as a set of comma-separated dinosaur
attributes is always tricky. Instead, consider splitting the string on the appropriate delimiter and
creating a nested list.

:bulb: Assume that the `dinosaur_strings` list has been sorted alphabetically by calling
`dinosaur_strings.sort()`, an in-place operation.

```python
dinosaur_strings = [
    'Allosaurus, Theropoda, Jurassic, 12, 1500, carnivore',
    'Ankylosaurus, Eurypoda, Cretaceous, 8, 8000, herbivore',
    'Apatosaurus, Sauropoda, Jurassic, 22, 22400, herbivore',
    'Brachiosaurus, Sauropoda, Jurassic, 21, 58000, herbivore',
    'Camptosaurus, Ornithopoda, Cretaceous, 7.9, 874, herbivore',
    'Ceratosaurus, Theropoda, Jurassic, 7, 980, carnivore',
    'Corythosaurus, Ornithopoda, Cretaceous, 8.1, 3078, herbivore',
    'Deinocheirus, Theropoda, Cretaceous, 11, 6400, omnivore',
    'Diplodocus, Sauropoda, Jurassic, 24, 14800, herbivore',
    'Dreadnoughtus, Sauropoda, Cretaceous, 26, 38192, herbivore',
    'Edmontosaurus, Ornithopoda, Cretaceous, 12, 4000, herbivore',
    'Gigantoraptor, Theropoda, Cretaceous, 8.9, 3600, carnivore',
    'Pachycephalosaurus, Marginocephalia, Cretaceous, 4.5, 450, herbivore',
    'Parasaurolophus, Ornithopoda, Cretaceous, 9.5, 2500, herbivore',
    'Psittacosaurus, Marginocephalia, Cretaceous, 2, 20, herbivore',
    'Stegosaurus, Eurypoda, Jurassic, 9, 7000, herbivore',
    'Styracosaurus, Marginocephalia, Cretaceous, 5.5, 3000, herbivore',
    'Triceratops, Marginocephalia, Cretaceous, 9, 12000, herbivore',
    'Tyrannosaurus, Theropoda, Cretaceous, 12.3, 8400, carnivore',
    'Velociraptor, Theropoda, Jurassic, 1.5, 33, carnivore'
    ]

dinosaurs = []
for dinosaur in dinosaur_strings:
    data = dinosaur.split(', ')
    dinosaurs.append(data)

print(f"\n1.3.1 Dinosaurs nested lists ({len(dinosaurs)}) = {dinosaurs}")
```

Working with each dinosaur attribute split out into an individual list
element is easier than parsing the same data lumped together in a single string.

```python
dinosaurs = [
    ['Allosaurus', 'Theropoda', 'Jurassic', '12', '1500', 'carnivore'],
    ['Ankylosaurus', 'Eurypoda', 'Cretaceous', '8', '8000', 'herbivore'],
    ['Apatosaurus', 'Sauropoda', 'Jurassic', '22', '22400', 'herbivore'],
    ['Brachiosaurus', 'Sauropoda', 'Jurassic', '21', '58000', 'herbivore'],
    ['Camptosaurus', 'Ornithopoda', 'Cretaceous', '7.9', '874', 'herbivore'],
    ['Ceratosaurus', 'Theropoda', 'Jurassic', '7', '980', 'carnivore'],
    ['Corythosaurus', 'Ornithopoda', 'Cretaceous', '8.1', '3078', 'herbivore'],
    ['Deinocheirus', 'Theropoda', 'Cretaceous', '11', '6400', 'omnivore'],
    ['Diplodocus', 'Sauropoda', 'Jurassic', '24', '14800', 'herbivore'],
    ['Dreadnoughtus', 'Sauropoda', 'Cretaceous', '26', '38192', 'herbivore'],
    ['Edmontosaurus', 'Ornithopoda', 'Cretaceous', '12', '4000', 'herbivore'],
    ['Gigantoraptor', 'Theropoda', 'Cretaceous', '8.9', '3600', 'carnivore'],
    ['Pachycephalosaurus', 'Marginocephalia', 'Cretaceous', '4.5', '450', 'herbivore'],
    ['Parasaurolophus', 'Ornithopoda', 'Cretaceous', '9.5', '2500', 'herbivore'],
    ['Psittacosaurus', 'Marginocephalia', 'Cretaceous', '2', '20', 'herbivore'],
    ['Stegosaurus', 'Eurypoda', 'Jurassic', '9', '7000', 'herbivore'],
    ['Styracosaurus', 'Marginocephalia', 'Cretaceous', '5.5', '3000', 'herbivore'],
    ['Triceratops', 'Marginocephalia', 'Cretaceous', '9', '12000', 'herbivore'],
    ['Tyrannosaurus', 'Theropoda', 'Cretaceous', '12.3', '8400', 'carnivore'],
    ['Velociraptor', 'Theropoda', 'Jurassic', '1.5', '33', 'carnivore']
    ]

dinosaur_name = dinosaurs[-1][0]
print(f"\n1.3.2 Dinosaur name = {dinosaur_name}")

dinosaur_names = []
for dinosaur in dinosaurs:
   dinosaur_names.append(dinosaur[0])

print(f"\n1.3.3 Dinosaur names = {dinosaur_names}")
```

### 1.4 Looping and slicing

If the `dinosaurs` list is sorted by geologic period (e.g., Jurassic, Cretaceous) and
questions were scoped by geologic period, an opportunity exists to loop over a _slice_ of the
list rather than the list in its entirety.

For example, loop over a 'Cretaceous' slice of `dinosaurs` and assign each Cretaceous dinosaur to
the list `cretaceous_dinosaurs`.

```python
dinosaurs = [
    ['Allosaurus', 'Theropoda', 'Jurassic', '12', '1500', 'carnivore'],
    ['Apatosaurus', 'Sauropoda', 'Jurassic', '22', '22400', 'herbivore'],
    ['Brachiosaurus', 'Sauropoda', 'Jurassic', '21', '58000', 'herbivore'],
    ['Ceratosaurus', 'Theropoda', 'Jurassic', '7', '980', 'carnivore'],
    ['Diplodocus', 'Sauropoda', 'Jurassic', '24', '14800', 'herbivore'],
    ['Stegosaurus', 'Eurypoda', 'Jurassic', '9', '7000', 'herbivore'],
    ['Velociraptor', 'Theropoda', 'Jurassic', '1.5', '33', 'carnivore'],
    ['Ankylosaurus', 'Eurypoda', 'Cretaceous', '8', '8000', 'herbivore'],
    ['Camptosaurus', 'Ornithopoda', 'Cretaceous', '7.9', '874', 'herbivore'],
    ['Corythosaurus', 'Ornithopoda', 'Cretaceous', '8.1', '3078', 'herbivore'],
    ['Deinocheirus', 'Theropoda', 'Cretaceous', '11', '6400', 'omnivore'],
    ['Dreadnoughtus', 'Sauropoda', 'Cretaceous', '26', '38192', 'herbivore'],
    ['Edmontosaurus', 'Ornithopoda', 'Cretaceous', '12', '4000', 'herbivore'],
    ['Gigantoraptor', 'Theropoda', 'Cretaceous', '8.9', '3600', 'carnivore'],
    ['Pachycephalosaurus', 'Marginocephalia', 'Cretaceous', '4.5', '450', 'herbivore'],
    ['Parasaurolophus', 'Ornithopoda', 'Cretaceous', '9.5', '2500', 'herbivore'],
    ['Psittacosaurus', 'Marginocephalia', 'Cretaceous', '2', '20', 'herbivore'],
    ['Styracosaurus', 'Marginocephalia', 'Cretaceous', '5.5', '3000', 'herbivore'],
    ['Triceratops', 'Marginocephalia', 'Cretaceous', '9', '12000', 'herbivore'],
    ['Tyrannosaurus', 'Theropoda', 'Cretaceous', '12.3', '8400', 'carnivore']
    ]

cretaceous_dinosaurs = []
for dinosaur in dinosaurs:
    if dinosaur[2].lower() == 'cretaceous':
        cretaceous_dinosaurs.append(dinosaur)

print(f"\n1.4.1 Cretaceous dinosaurs unsliced ({len(cretaceous_dinosaurs)}) = {cretaceous_dinosaurs}")

# More efficient (slice)
cretaceous_dinosaurs = []
for dinosaur in dinosaurs[7:]:
    cretaceous_dinosaurs.append(dinosaur)

print(f"\n1.4.2 Cretaceous dinosaurs sliced ({len(cretaceous_dinosaurs)}) = {cretaceous_dinosaurs}")
```

:bulb: Out of scope for SI 506 but Python provides an elegant alternative to the `for` loop that is
useful in a number of situations: the
[list comprehension](https://realpython.com/list-comprehension-python/). The above example can be
expressed in a single line of code.

```python
# elegant
cretaceous_dinosaurs = [dinosaur for dinosaur in dinosaurs[7:]]

print(f"\n1.4.3 Cretaceous dinosaurs list comprehension ({len(cretaceous_dinosaurs)}) = {cretaceous_dinosaurs}")
```

## 2.0 Conditional statements

The rationale for looping over a list using a `for` loop is often expressed in one or more
conditional statements located within the body of the loop. The conditional statement determines
which computations, if any, are to be performed during the current iteration depending on whether
the condition expressed evaluates to true or false. More generally, conditional statements help
determine a computer program's _control flow_ or the order in which individual statements are
executed.

In the examples below, the conditional statements embedded within the body of each loop operate
in the main as data filters. But conditional statements can also be employed to trigger other actions
including changes in an object's state.

### 2.1 Counting

The built-in `len()` function provides us with the overall length or size of a list. But if we
want to return a count of a subset of a sequence in which slicing cannot be used, then consider
using a counter variable to hold a rolling count of the elements that satisfy a given condition as
in the example below.

```python
sauropod_count = 0 # counter
for dinosaur in dinosaurs:
    if dinosaur[1].lower() == 'sauropoda':
        # sauropod_count = sauropod_count + 1
        sauropod_count += 1 # equivalent

print(f"\n2.1.1 Sauropod count = {sauropod_count}")
```

We can slice on the Jurassic period and obtain counts of herbivores, carnivores, and omnivores using
`if-elif-else` logic.

```python
herbivore_count = 0
carnivore_count = 0
omnivore_count = 0

for dinosaur in dinosaurs[:7]:
    if dinosaur[-1].lower() == 'herbivore':
        herbivore_count += 1
    elif dinosaur[-1].lower() == 'carnivore':
        carnivore_count += 1
    else:
        omnivore_count += 1

msg = (
    '\n2.1.2 Jurassic Period diet counts'
    f"\nherbivore count = {herbivore_count}"
    f"\ncarnivore count = {carnivore_count}"
    f"\nomnivore count = {omnivore_count}"
)

print(msg)
```

### 2.2 Comparison operators; continue and break

Conditional statements often compare two values using comparison operators
(`==`, `!=`, `>`, `<`, `>=`, `<=`). The return value of such expressions is either `True` or
`False`.

Let's assume that a "large" dinosaur is at least 15 meters in length. We can add a conditional
statement that tests for this condition using the greater than (`>`) comparison operator.

```python
large_dinosaurs = []
for dinosaur in dinosaurs:
    if float(dinosaur[3]) > 15:
        large_dinosaurs.append(dinosaur)

print(f"\n2.2.1 Large dinosaurs (> 15 meters) = {large_dinosaurs}")
```

A more complex example involves looping over the `dinosaurs` list in search of the largest dinosaur
in terms of length. The variable `prev_length` holds the length of the last dinosaur evaluated in
order to compare it to the next dinosaur's length. If the next dinosaur is larger than the previous
dinosaur, the dinosaur's name is assigned to the string variable `largest_dinosaur`. If a larger
dinosaur is later encountered `largest_dinosaur` is reassigned. If a dinosaur of the same length is
encountered, the dinosaur's name and weight are added to `largest_dinosaur` (ties accommodated).

```python
largest_dinosaur = None
prev_length = 0
for dinosaur in dinosaurs:
    if float(dinosaur[3]) > prev_length:
        largest_dinosaur = f"{dinosaur[0]} ({dinosaur[3]} meters)"
        prev_length = float(dinosaur[3]) # reset
    elif float(dinosaur[3]) == prev_length:
        largest_dinosaur = f"{largest_dinosaur}, {dinosaur[0]} ({dinosaur[3]} meters)" # tied
    else:
        continue

print(f"\n2.2.2 Largest dinosaur (length) = {largest_dinosaur}")
```

The next example returns the smallest dinosaur. The loop utilizes the built-in `enumerate()`
function to provide a counter (`i`) that is used to enumerate the each iteration of the loop. During
the first iteration of the loop (`i = 0`) the `prev_length` variable is seeded with the length of
the first dinosaur encountered. This sets up the less than (`<`) comparison check between the
"previous" dinosaur and the "current" dinosaur. Ties are handled by the `elif` condition.

```python
smallest_dinosaur = None
prev_length = 0
for i, dinosaur in enumerate(dinosaurs):
    if i == 0:
        prev_length = float(dinosaur[3]) # seed with first length

    if float(dinosaur[3]) < prev_length:
        smallest_dinosaur = f"{dinosaur[0]} ({dinosaur[3]} meters)"
        prev_length = float(dinosaur[3]) # reset
    elif float(dinosaur[3]) == prev_length:
        smallest_dinosaur = f"{smallest_dinosaur}, {dinosaur[0]} ({dinosaur[3]} meters)" # tied
    else:
        continue

print(f"\n2.2.3 Smallest dinosaur (length) = {smallest_dinosaur}")
```

The above examples made use of the `continue` statement, which explicitly directs the looping
operation to proceed to the next iteration (looping typically occurs implicitly). We can also
choose to terminate looping using the `break` statement.

In the following example we will search for the first dinosaur that is a member of the Ornithopoda
clade, assign it's name to the variable `duck_billed_dinosaur` and then exit the loop by invoking the
`break` statement.

```python
duck_billed_dinosaur = None
for dinosaur in dinosaurs:
    if dinosaur[1].lower() == 'ornithopoda':
        duck_billed_dinosaur = dinosaur[0] # name only
        break

print(f"\n2.2.4 Duck-billed dinosaur = {duck_billed_dinosaur}")
```

### 2.3 Comparison operators (between x and y)

Use comparison operators arranged as `x < y < z` or `x <= y <= z` to test if a number is _between_
two numbers. The expression returns either `True` or `False`.

In the following example, if a dinosaur weighs between 10000 and 6000 kg (10 and 60 metric tons) the
dinosaur is added to the `heavy_dinosaur` list.

```python
heavy_dinosaurs = []
for dinosaur in dinosaurs:
    if 10000 < float(dinosaur[-2]) < 60000:
        heavy_dinosaurs.append(f"{dinosaur[0]} ({dinosaur[-2]} kg)") # name and weight

print(f"\n2.3 Dinosaurs weighing between 10000 and 60000 kg ({len(heavy_dinosaurs)}) = {heavy_dinosaurs}")
```

### 2.4. Membership operators

Python provides the membership operators `in` and `not in` for testing the presence/non-presence of
a sequence in an object.

In the example below the `in` operator check if a Cretaceous dinosaur's _clade_ (e.g., group with a common
ancestor) is either Marginocephalia or Ornithopoda (both Cerapoda). If a dinosaur's clade matches
either of the tuple items, the dinosaur is appended to the `cerapods` list.

```python
cerapods = []
for dinosaur in dinosaurs[7:]:
    if dinosaur[1].lower() in ('marginocephalia', 'ornithopoda'):
        cerapods.append(f"{dinosaur[0]} ({dinosaur[1]})") # name and clade

print(f"\n2.4.1 Cretaceous Period Cerapods ({len(cerapods)}) = {cerapods}")

eurypoda = []
for dinosaur in dinosaurs[7:]:
    if dinosaur[1].lower() not in ('marginocephalia', 'ornithopoda', 'sauropoda', 'theropoda'):
        eurypoda.append(f"{dinosaur[0]} ({dinosaur[1]})") # name and clade

print(f"\n2.4.2 Cretaceous Period Eurypods ({len(eurypoda)}) = {eurypoda}")
```

### 2.5 Logical operators

The logical operators `and`, `or` and `not` are used to combine conditional statements.

The logical `and` operator used in a conditional statement evaluates to `True` if _both_ of the
expressions evaluates to `True`; otherwise `False` is returned.

In the following example, the `dinosaurs` list is sliced in favor of the Cretaceous Period, and
then the Cretaceous dinosaurs are filtered on clade and weight using the `and` logical operator.
Only Ornithopods are selected with the variable `weight` restricting still further the filtering
selection to that of the heaviest Ornithopod.

```python
heaviest_ornithopod = None
weight = 0
for dinosaur in dinosaurs[7:]:
    if dinosaur[1].lower() == 'ornithopoda' and float(dinosaur[-2]) > weight:
        heaviest_ornithopod = dinosaur
        weight = float(dinosaur[-2]) # reset

print(f"\n2.5.1 Heaviest Cretaceous Ornithopod = {heaviest_ornithopod[0]} ({heaviest_ornithopod[4]} kg)")
```

The logical `or` operator used in a conditional statement evaluates to `True` if _either_ of the
expression evaluates to `True`; otherwise `False` is returned.

Let's return a list of dinosaurs with names that begin with either the letter 'C' or 'D'.

```python
dinosaur_names_cd = []
for dinosaur in dinosaurs:
    if dinosaur[0].lower().startswith('c') or dinosaur[0].lower().startswith('d'):
        dinosaur_names_cd.append(dinosaur[0]) # name only

dinosaur_names_cd.sort() # in-place sort

print(f"\n2.5.2 Dinosaur names that begin with C or D = {dinosaur_names_cd}")
```

Utilize the logical `not` operator to reverse the return value of the conditional expression; if the
expression evaluates to `True`, `not` reverses it to `False` and vice-versa.

The following example employs the `not` logical operator to return a list of all non-herbivore
(i.e., meat-eating) dinosaurs.

```python
meat_eaters = []
for dinosaur in dinosaurs:
    if not dinosaur[-1].lower() == 'herbivore':
        meat_eaters.append(f"{dinosaur[0]} ({dinosaur[-1]})")

print(f"\n2.5.3 Meat-eating dinosaurs ({len(meat_eaters)}) = {meat_eaters}")
```

Retrieving dinosaur names lacking the classic dinosaurian suffix _-saurus_ is a straightforward
task when using the `not` logical operator.

```python
non_saurus_names = []
for dinosaur in dinosaurs:
    if not dinosaur[0].lower().endswith('saurus'):
        non_saurus_names.append(dinosaur[0]) # name only

print(f"\n2.5.4 Dinosaur names without the 'saurus' (lizard) suffix = {non_saurus_names}")
```

## Sources

1. <a href="#endnote_01"></a>Wikipedia, ["Dinosaur"](https://en.wikipedia.org/wiki/Dinosaur).
2. _Wikipedia_, ["Allosaurus"](https://en.wikipedia.org/wiki/Allosaurus)
3. _Wikipedia_, ["Ankylosaurus"](https://en.wikipedia.org/wiki/Ankylosaurus)
4. _Wikipedia_, ["Apatosaurus"](https://en.wikipedia.org/wiki/Apatosaurus)
5. _Wikipedia_, ["Brachiosaurus"](https://en.wikipedia.org/wiki/Brachiosaurus)
6. _Wikipedia_, ["Camptosaurus"](https://en.wikipedia.org/wiki/Camptosaurus)
7. _Wikipedia_, ["Ceratosaurus"](https://en.wikipedia.org/wiki/Ceratosaurus)
8. _Wikipedia_, ["Corythosaurus"](https://en.wikipedia.org/wiki/Corythosaurus)
9. _Wikipedia_, ["Deinocheirus"](https://en.wikipedia.org/wiki/Deinocheirus)
10. _Wikipedia_, ["Diplodocus"](https://en.wikipedia.org/wiki/Diplodocus)
11. _Wikipedia_, ["Dreadnoughtus"](https://en.wikipedia.org/wiki/Dreadnoughtus)
12. _Wikipedia_, ["Edmontosaurus"](https://en.wikipedia.org/wiki/Edmontosaurus)
13. _Wikipedia_, ["Gigantoraptor"](https://en.wikipedia.org/wiki/Gigantoraptor)
14. _Wikipedia_, ["Parasaurolophus"](https://en.wikipedia.org/wiki/Parasaurolophus)
15. _Wikipedia_, ["Pachycephalosaurus"](https://en.wikipedia.org/wiki/Pachycephalosaurus)
16. _Wikipedia_, ["Psittacosaurus"](https://en.wikipedia.org/wiki/Psittacosaurus)
17. _Wikipedia_, ["Stegosaurus"](https://en.wikipedia.org/wiki/Stegosaurus)
18. _Wikipedia_, ["Styracosaurus"](https://en.wikipedia.org/wiki/Styracosaurus)
19. _Wikipedia_, ["Triceratops"](https://en.wikipedia.org/wiki/Triceratops)
20. _Wikipedia_, ["Tyrannosaurus"](https://en.wikipedia.org/wiki/Tyrannosaurus)
21. _Wikipedia_, ["Velociraptor"](https://en.wikipedia.org/wiki/Velociraptor)
