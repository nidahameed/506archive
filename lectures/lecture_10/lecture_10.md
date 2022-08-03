# SI 506 Lecture 10

## Topics

1. Nested loops
2. `while` loop (indefinite iteration)
3. `range()` type and `for` loops
4. Built-in `input()` function and `while` loops

## Vocabulary

* __Conditional Statement__. A statement that determines a computer program's _control flow_ or the
  order in which particular computations are to be executed.
* __Iteration__. Repetition of a computational procedure in order to generate a possible sequence of
  outcomes. Iterating over a `list` using a `for` loop is an example of iteration.

## Setup: Dinosaurs list

Below is a nested list of select dinosaurs. Each dinosaur list contains the following information:

* name
* clade
* geologic period
* max length (meters)
* max weight (kilograms)
* diet

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
```

## 1.0 Nested loops

A "nested loop" refers to a loop located within the code block of another loop. During each
iteration of the "outer" loop, the "inner" loop code block will be executed.

Three examples should suffice to get you thinking about how you can harness the power of
nested loops.

Consider the list `dinosaur_name_strings`. Each element provides a dinosaur's
scientific name (typically derived from two Greek words, as in _deinos_ (terrible) and _sauros_
(lizard) for dinosaur) along with a rough translation of the name's Greek meaning.

```python
dinosaur_name_strings = [
    'allosaurus, different lizard',
    'ankylosaurus, fused lizard',
    'apatosaurus, deceptive lizard',
    'brachiosaurus, arm lizard',
    'camptosaurus, flexible lizard',
    'ceratosaurus, horn lizard',
    'corythosaurus, helmet lizard',
    'deinocheirus, horrible hand',
    'diplodocus, double beam',
    'dreadnoughtus, fears nothing',
    'edmontosaurus, lizard from Edmonton',
    'gigantoraptor, giant seizer',
    'parasaurolophus, near crested lizard',
    'pachycephalosaurus, thick-headed lizard',
    'psittacosaurus, parrot lizard',
    'stegosaurus, roof lizard',
    'styracosaurus, spiked lizard',
    'triceratops, three-horned face',
    'tyrannosaurus, tyrant lizard',
    'velociraptor, swift seizer'
]
```

Let's see if we can use nested loops to combine data in `dinosaur_name_strings` with data in
`dinosaurs`.

### 1.1 Example: what's in a name?

Given that we can match on the scientific name in both lists, let's confirm that we can match every
dinosaur name in `dinosaurs` with a name in `dinosaur_name_strings`. We can employ a counter
`name_matched` to keep track of the name matches.

We can start by looping over `dinosaurs` and then employ a nested loop to traverse the elements in
`dinosaur_name_strings` seeking out name matches using a conditional statement.

:bulb: If the inner loop acts as a filter, utilize the `break` statement to terminate it whenever
the filter condition(s) evaluate to `True` and the inner loop's computation is performed. Doing so
will improve performance by eliminating unnecessary inner loop iterations.

```python
name_matched = 0
for dinosaur in dinosaurs:
    for name in dinosaur_name_strings:
        if name.lower().startswith(dinosaur[0].lower()):
            name_matched += 1 # increment
            break # terminate inner loop (avoid unnecessary iterations)

print(f"\n1.1 Dinosaurs (n = {len(dinosaurs)}); names matched = {name_matched}")
```

### 1.2 Challenge: insert name translations

Once we have confirmed that we can obtain a name match for every dinosaur represented in either
list, let's combine the data.

__Task__: utilize a nested loop to insert the rough translation of a dinosaur's scientific name
located in `dinosaur_name_strings` into the second (2nd) position of each `dinosaurs` nested list
after matching on the scientific name. Use a `break` statement to limit the number of inner loop
iterations after the data is inserted.

:bulb: consider splitting each `dinosaur_name_strings` element to simplify working with the data.

```python
# TODO insert rough name translations

print(f"\n1.2 Insert name translations = {dinosaurs}")
```

### 1.3 Example: rebuild string (add geologic period)

We can also combine data in the opposite direction, taking data from `dinosaurs` and adding it to
`dinosaur_name_strings`. But since we are working with strings we will need to reference the
`dinosaur_name_strings` element that we wish to "update" explicitly by its index position in order
to (re)point it at a new string value in memory. We cannot simply assign a new strin value to
`name`.

```python
for name in dinosaur_name_strings:
    names = name.split(', ')
    for dinosaur in dinosaurs:
        if dinosaur[0].lower() == names[0].lower():
            # name = f"{name}, {dinosaur[3].lower()}" # fail
            index = dinosaur_name_strings.index(name)
            dinosaur_name_strings[index] = f"{name}, {dinosaur[3].lower()}" # success
            break # terminate inner loop

print(f"\nName translations w/geologic period = {dinosaur_name_strings}")
```

## 2.0 `while` loop (indefinite iteration)

The `while` loop repeats a set of one or more statements _indefinitely_; that is until a condition
is imposed that evaluates to `False` and terminates the loop. If a `while` loop is implemented
incorrectly it could result in an _infinite loop_, a runaway process that is likely to demand over
time ever greater memory resources that will eventually force you to kill the process lest your
laptop overheats (you will hear the fans kick on as the laptop's internal temperature rises).

Choose a `while` loop only when you cannot determine in advance the number of iterations required to
perform a computation.

:exclamation: if you trigger an infinite loop while running your module in VS Code click the
terminal pane's trash can icon in order to kill the session and end the runaway process.

The following example is guaranteed to trigger a runaway process since the `while` condition remains
`True` indefinitely:

```python
while True:
    print("infinite loop triggered")
```

You can tame a `while` loop and avoid a triggering a runaway process with the use of a counter, a
conditional statement, and a `break` statement.

```python
i = 0
while True:
    print('infinite loop triggered')
    if i == 5:
        print('infinite loop terminated\n')
        break # exit the loop
    i += 1 # increment
```

### 2.1 `while` loops and comparison operators

You can also employ a comparison operator (e.g., `<`) together with a counter to limit the number of
iterations.

```python
i = 0
while i < 5:
    print('I love dinosaurs.')
    i += 1 # increment
```

The `while` loop includes a built-in `else` condition that you can use to execute one or more
statements after the loop terminates.

```python
i = 0
while i < 5:
    print('I love dinosaurs.')
    i += 1 # increment
else:
    print('Enough said. We believe you.')
```

You can employ `if-elif-else` logic inside a `while` loop in order to determine the control flow of
each iteration. In the following example the modulus (`%`) operator is used to identify even and odd
numbers between 0 and 10.

:bulb: use the modulus operator to return the remainder after one number is divided by another. If
the remainder equals zero the number evaluated is an even number.

```python
i = 0
while i < 10:
    if i % 2 == 0:
        print(f"{i} is an even number.")
    else:
        print(f"{i} is an odd number.")
    i += 1 # increment

i = 10
while i >= 0:
    if i % 2 == 0:
        print(f"{i} is an even number.")
    else:
        print(f"{i} is an odd number.")
    i -= 1 # decrement
```

### 2.2 `while` loops and sequence traversal

A `while` loop pattern encountered frequently involves use of a counter to traverse a sequence
so long as the counter value is less than the length of the target sequence.

In the example below, a `while` loop in combination with a conditional statement is employed to
locate the first instance of an omnivore in the `dinosaurs` list and then assign its name to the
variable `omnivore`.

```python
omnivore = None
i = 0
while i < len(dinosaurs):
    if dinosaurs[i][-1].lower() == 'omnivore':
        omnivore = dinosaurs[i][0]
        break # terminate the loop
    i += 1 # increment
else:
    print(f"\n Omnivore not found.")

print(f"\n2.2 First omnivore encountered = {omnivore}\n")
```

### 2.3 Challenge: identify dinosaurs < 4000 kg

__Task__: use a `while` loop together with a conditional statement to traverse the `dinosaurs` list and
identify dinosaurs that weigh less (`<`) than 4000 kilograms (4 metric tons). Once located append
the dinosaur name and weight to the `lightweights` list adhering to the following string format
`<name> (< weight > kg)`.

```python
lightweights = []
i = 0

# TODO implement while loop

print(f"\n2.3 Dinosaurs < 4000 kg (n = {len(lightweights)}) = {lightweights}\n")
```

### 2.4 Challenge: remove dinosaurs between 5 and 20 meters in length

Let's say a colleague requires a slimmed down version of our `dinosaurs` list that _excludes_ all
dinosaurs between five (5) and twenty (20) meters in length. In other words our colleague wants only
the lightest and heaviest dinosaurs from our list.

__Task__: make a copy of the `dinosaurs` list using `list.copy()`. Name it `dinos`. Then use a
`while True:` loop statement to traverse the list and write the code block using `list.pop()` to
extract the target dinosaurs as requested by our colleague.

:bulb: `list.pop(< index >)` returns the element removed from the list. Note that as elements are
removed list index values are decremented.

```python
dinos = dinosaurs.copy() # protect the original list
i = 0
while True:

    # TODO IMPLEMENT

print(f"\n2.4 Dinos <= 5 meters or >= 20 meters (n = {len(dinos)}) = {dinos}\n")
```

## 3.0 Looping and the range() type

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

### 3.1 Challenge: `range()` and sequence length

You can initialize `range()` in a `for` loop with the length of a sequence using the built-in
`len()` function. Given zero-based indexing, be sure to limit range to the length of the sequence
minus one (`- 1`).

__Task__: use `range()` together with the built-in `len()` function in a `for` loop to replace the
dinosaur name "Tyrannosaurus" with the more regal "Tyrannosaurus rex" in the `dinosaurs` list.

```python
# TODO implement for loop

print(f"\n3.1 Honor T. rex using range() = {dinosaurs[-1]}")
```

## 4.0 `while` loop and input()

The built-in `input()` function accepts user-supplied strings from the command prompt. It is often
positioned inside a `while` loop in order to process user input, especially incorrect input. The pattern is
illustrated in the following example drawn from the PBS children's series
[_Dinosaur Train_](https://pbskids.org/dinosaurtrain/).

```python
dinosaur_train = ('tiny', 'shiny', 'don', 'buddy')
prompt = '\nWho is your favorite Dinosaur Train character: '

while True:
    character = input(prompt)
    if character.lower() in dinosaur_train:
        print(f"\nThanks. I like {character.capitalize()} too.\n\nFinis.\n")
        break # terminate loop
```

## Sources

1. PBS, [_Dinosaur Train_](https://pbskids.org/dinosaurtrain/).
2. _Wikipedia_, ["Dinosaur"](https://en.wikipedia.org/wiki/Dinosaur).
3. _Wikipedia_, ["Allosaurus"](https://en.wikipedia.org/wiki/Allosaurus)
4. _Wikipedia_, ["Ankylosaurus"](https://en.wikipedia.org/wiki/Ankylosaurus)
5. _Wikipedia_, ["Apatosaurus"](https://en.wikipedia.org/wiki/Apatosaurus)
6. _Wikipedia_, ["Brachiosaurus"](https://en.wikipedia.org/wiki/Brachiosaurus)
7. _Wikipedia_, ["Camptosaurus"](https://en.wikipedia.org/wiki/Camptosaurus)
8. _Wikipedia_, ["Ceratosaurus"](https://en.wikipedia.org/wiki/Ceratosaurus)
9. _Wikipedia_, ["Corythosaurus"](https://en.wikipedia.org/wiki/Corythosaurus)
10. _Wikipedia_, ["Deinocheirus"](https://en.wikipedia.org/wiki/Deinocheirus)
11. _Wikipedia_, ["Diplodocus"](https://en.wikipedia.org/wiki/Diplodocus)
12. _Wikipedia_, ["Dreadnoughtus"](https://en.wikipedia.org/wiki/Dreadnoughtus)
13. _Wikipedia_, ["Edmontosaurus"](https://en.wikipedia.org/wiki/Edmontosaurus)
14. _Wikipedia_, ["Gigantoraptor"](https://en.wikipedia.org/wiki/Gigantoraptor)
15. _Wikipedia_, ["Parasaurolophus"](https://en.wikipedia.org/wiki/Parasaurolophus)
16. _Wikipedia_, ["Pachycephalosaurus"](https://en.wikipedia.org/wiki/Pachycephalosaurus)
17. _Wikipedia_, ["Psittacosaurus"](https://en.wikipedia.org/wiki/Psittacosaurus)
18. _Wikipedia_, ["Stegosaurus"](https://en.wikipedia.org/wiki/Stegosaurus)
19. _Wikipedia_, ["Styracosaurus"](https://en.wikipedia.org/wiki/Styracosaurus)
20. _Wikipedia_, ["Triceratops"](https://en.wikipedia.org/wiki/Triceratops)
21. _Wikipedia_, ["Tyrannosaurus"](https://en.wikipedia.org/wiki/Tyrannosaurus)
22. _Wikipedia_, ["Velociraptor"](https://en.wikipedia.org/wiki/Velociraptor)