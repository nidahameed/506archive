# SI 506 Lecture 11

## Topics

1. Defining functions
2. Calling functions inside nested loops
3. Functions calling other functions

## Vocabulary

* __Argument__. A value or expression passed to a function.
* __Caller__. The initiator of a function call.
* __Function__. a named series of statements (a code block) that performs a computation whenever
  the function is invoked by a caller. Parameters can be declared in a function definition in order
  to permit the processing of input values (i.e., arguments). Functions typically, though not
  always, compute a result to be returned to the caller.
* __Parameter__. A named entity or object in a function definition that specifies an argument or
  arguments that the function can accept from a caller.

## 1.0 Function basics

### 1.1 Defining and calling a function

A function is defined using the keyword `def` and given a name that ends with an
open/close parentheses `()`.

Writing a function in order to perform a particular task is a form of code modularization designed
to simplify otherwise complex processes. Functions also encourage code re-use and adherance to the
_Don’t Repeat Yourself_ (DRY) principle of software development.

In the example below the function is called by name and responds by calling the built-in `print()`
function and passing to it a hard-coded string.

```python
def create_slogan():
    print('\n1.1 Snap. Crackle. Pop.') # Kellogg's Rice Crispies

create_slogan() # call function
```

### 1.2 Defining and calling a function with a parameter and return value

Functions are typically defined with one or more _parameters_ for accepting input and return
statement that signals the end of the computation and the "return" of a value to the caller.

:bulb: functions that do not include a `return` statement return `None` to the caller.

In the example below the function named `create_slogan` is provisioned with a single parameter named
`text`. The function accepts input and returns it without operating on the passed in `text` value
in any way.

```python
def create_slogan(text):
    return text

tagline = 'Snap. Crackle. Pop.'
rice_crispies = create_slogan(tagline)

print(f"\n1.2 {rice_crispies}")
```

### 1.3 Defining a function with multiple parameters

A function can be specified with multiple parameters. The caller _must_ pass to the function the
required number of _arguments_ or a runtime error will occur.

In the example below, the function `create_slogan` is called three times, with the required arguments
passed _by position_. The function's return value is then assigned to a variable.

```python
def create_slogan(text, emphasis):
    text = text.replace('.', emphasis)
    return text

# Postional arguments
tagline = 'Snap. Crackle. Pop.'
rice_crispies = create_slogan(tagline, '!')

tagline = "They’rrrre GR-R-REAT." # Kellog's Frosted Flakes
frosted_flakes = create_slogan(tagline, '!')

tagline = 'Silly Rabbit. Trix are for Kids.' # General Mills Trix
trix = create_slogan(tagline, '!')

print(f"\n1.3 {rice_crispies} {frosted_flakes} {trix}")
```

### 1.4 Positional arguments (order matters)

If positional arguments are passed to a function, the caller must pass them in the correct order in
order to ensure that the function can process the values as expected.

In the example below, the function `create_slogan` is called but the arguments are passed to it in
the wrong order. The resulting computation returns an unexpected and incorrect value.

```python
tagline = 'They’re always after me lucky charms.' # General Mills Lucky Charms leprechaun
lucky_charms = create_slogan('!', tagline) # Oops!

print(f"\n1.4 {lucky_charms}")
```

### 1.5 Keyword arguments

The caller can pass _keyword arguments_, specifying both a key and value in the form `key=value`. By
doing so, ordering the arguments per the order of the function's parameter list is no longer
required.

:exclamation: note that by convention keyword arguments do not include spaces on either side of the
assignment operator

```python
lucky_charms = create_slogan(emphasis='!', text=tagline) # pass args by name

print(f"\n1.5 {lucky_charms}")
```

### 1.6 Parameter default value

A function definition can specify one or more parameter values. If a a default value is specified
the caller is not required to pass in a corresponding argument unless there is a need to override
the default value.

In the example below, the `create_slogan` parameter named `emphasis` is provisioned with a default
value (`'!'`). The caller need only pass a single `text` argument to the function if the `emphasis`
parameter's default value meets their computational requirements.

```python
def create_slogan(text, emphasis='!'):
    text = text.replace('.', emphasis)
    return text

tagline = 'He likes it. Hey Mikey.' # Quaker Oats. 1970s TV ad campaign
life_cereal = create_slogan(tagline)

print(f"\n1.6 {life_cereal}")
```

## 2.0 Calling functions inside loops

A `for` loop code block can include statements that call functions. Below is a list of thirteen
breakfast cereals. Each nested list contains the following information:

* Manufacturer
* Cereal name
* Marketing slogan
* Year introduced
* Ingredients

```python
cereals = [
    [
        "Kellogg's",
        'Corn Flakes',
        "Taste them again, for the first time.",
        1894,
        ('Milled Corn, Sugar, Malt Flavoring, High Fructose Corn Syrup, Salt. Vitamins and Iron: '
        'Iron, Niacinamide, Sodium Ascorbate and Ascorbic Acid (Vitamin C), Pyridoxine Hydrochloride '
        '(Vitamin B6), Riboflavin (Vitamin B2), Thiamin Hydrochloride (Vitamin B1), Vitamin A '
        'Palmitate, Folic Acid, Vitamin B12 and Vitamin D. To Maintain Quality, BHT Has Been Added '
        'to the Packaging.')
        ],
    [
        "Kellogg's",
        'Frosted Flakes',
        "They’rrrre GR-R-REAT!",
        1952,
        ('Milled Corn, Sugar, Malt Flavoring, High Fructose Corn Syrup, Salt, Sodium Ascorbate and '
        'Ascorbic Acid (Vitamin C), Niacinamide, Iron, Pyridoxine Hydrochloride (Vitamin B6), '
        'Riboflavin (Vitamin B2), Thiamin Hydrochloride (Vitamin B1), Vitamin A Palmitate, '
        'Folic Acid, BHT (Preservative), Vitamin B12 and Vitamin D.')
        ],
    [
        "Kellogg's",
        'Raisin Bran',
        'Two Scoops of Raisins.',
        1926,
        ('Whole Grain Wheat, Raisins, Wheat Bran, Sugar, High Fructose Corn Syrup, Contains Two '
        'Percent or Less of Salt, Malt Flavoring, Invert Sugar, Niacinamide, Reduced Iron, '
        'Pyridoxine Hydrochloride (Vitamin B6), Zinc Oxide, Riboflavin (Vitamin B2), Thiamin '
        'Hydrochloride (Vitamin B1), Vitamin A Palmitate, Folic Acid, Vitamin D, Vitamin B12.')
        ],
    [
        "Kellogg's",
        'Rice Crispies',
        'Snap! Crackle! Pop!',
        1928,
        ('Rice, Sugar, Contains 2% or Less of Salt, Malt Flavor. BHT Added to Packaging for '
        'Freshness. Vitamins and Minerals: Iron, Vitamin C (Ascorbic Acid), Vitamin E (Alpha '
        'Tocopherol Acetate), Niacinamide, Vitamin A Palmitate, Vitamin B6 (Pyridoxine '
        'Hydrochloride), Vitamin B2 (Riboflavin), Vitamin B1 (Thiamin Hydrochloride), Folic Acid, '
        'Vitamin B12, Vitamin D.')
        ],
    [
        'General Mills',
        'Cheerios',
        'Only what matters.',
        1941,
        ('Whole Grain Oats (Includes the Oat Bran), Modified Corn Starch, Sugar, Salt, Tripotassium '
        'Phosphate, Oat Fiber, Wheat Starch. Vitamin E (Mixed Tocopherols) Added to Preserve '
        'Freshness. Vitamins and Minerals: Calcium Carbonate, Iron and Zinc (Mineral Nutrients), '
        'Vitamin C (Sodium Ascorbate), a B Vitamin (Niacinamide), Vitamin B6 (Pyridoxine '
        'Hydrochloride), Vitamin B2 (Riboflavin), Vitamin B1 (Thiamin Mononitrate), Vitamin A '
        '(Palmitate), a B Vitamin (Folic Acid), Vitamin B12, Vitamin D3.')
        ],
    [
        'General Mills',
        'Honey-nut Cheerios',
        'Bee Happy, Bee Healthy.',
        1979,
        ('Wholegrain Oats, Sugar, Oat Bran, Modified Corn Starch, Honey, Brown Sugar Syrup, Salt, '
        'Calcium Carbonate, Tripotassium Phosphate, Canola and/or Rice Bran Oil, Zinc and Iron '
        '(Mineral Nutrients), Vitamin C (Sodium Ascorbate), a B Vitamin (Niacinamide), Natural '
        'Almond Flavor, Vitamin B6 (Pyridoxine Hydrochloride), Vitamin B2 (Riboflavin), Vitamin B1 '
        '(Thiamin Mononitrate), Vitamin A (Palmitate), a B Vitamin (Folic Acid), Vitamin B12, '
        'Vitamin D, Wheat Flour, Vitamin E (Mixed Tocopherols) Added to Preserve Freshness.')
        ],
    [
        'General Mills',
        'Lucky Charms',
        'They’re Magically Delicious.',
        1964,
        ('Oats (Whole Grain Oats, Flour), Marshmallows (Sugar, Modified Corn Starch, Corn Syrup, '
        'Dextrose, Gelatin, Calcium Carbonate, Yellows 5&6, Blue 1, Red 40, Artificial Flavor), '
        'Sugar, Corn Syrup, Corn Starch, Salt, Calcium Carbonate, Artificial Color, Trisodium '
        'Phosphate, Zinc and Iron (Mineral Nutrients), Vitamin C (Sodium Ascorbate), a B Vitamin '
        '(Niacinamide), Artificial Flavor, Vitamin B6 (Pyridoxine Hydrochloride), Vitamin B2 '
        '(Riboflavin), Vitamin B1 (Thiamin Mononitrate), Vitamin A (Palmitate), a B Vitamin '
        '(Folic Acid), Vitamin B12, Vitamin D, Vitamin E (Mixed Tocopherols) Added to Preserve '
        'Freshness.')
        ],
    [
        'General Mills',
        'Trix',
        'Silly Rabbit. Trix are for Kids!',
        1954,
        ('Whole Grain Corn, Sugar, Rice Flour, Corn Syrup, Canola Oil, Salt, Trisodium Phosphate, '
        'Natural and Artificial Flavor, Red 40, Yellow 6, Blue 1 and Other Color Added, Citric '
        'Acid, Malic Acid., Vitamins and Minerals: Calcium Carbonate, Vitamins and Minerals: '
        'Tricalcium Phosphate, Vitamins and Minerals: Zinc and Iron (mineral nutrients), Vitamins '
        'and Minerals: Vitamin C (sodium ascorbate), Vitamins and Minerals: A B Vitamin '
        '(niacinamide), Vitamins and Minerals: Vitamin B6 (pyridoxine hydrochloride), Vitamins and '
        'Minerals: Vitamin B2 (riboflavin), Vitamins and Minerals: Vitamin B1 (thiamin '
        'mononitrate), Vitamins and Minerals: Vitamin A (palmitate), Vitamins and Minerals: A B '
        'Vitamin (folic acid), Vitamins and Minerals: Vitamin B12, Vitamins and Minerals: '
        'Vitamin D3.')
        ],
    [
        'General Mills',
        'Wheaties',
        'The Breakfast of Champions.',
        1921,
        ('Whole Grain Wheat, Sugar, Salt, Corn Syrup. Vitamin E (mixed tocopherols) added to '
        'preserve freshness. Vitamins and minerals: Calcium Carbonate, Zinc and Iron (mineral '
        'nutrients), A B Vitamin (Niacinamide), Vitamin C (Sodium Ascorbate), Vitamin B6 '
        '(Pyridoxine Hydrochloride), Vitamin B2 (Riboflavin), Vitamin B1 (Thiamin Mononitrate), '
        'Vitamin A (Palmitate), A B Vitamin (Folic Acid), Vitamin B12, Vitamin D3.')
        ],
    [
        'Post',
        'Grape-Nuts',
        "Fills you up, not out.",
        1897,
        ('Whole Grain Wheat Flour, Malted Barley Flour, Salt, Dried Yeast. Vitamins and Minerals: '
        'Reduced Iron, Niacinamide, Zinc Oxide (Source of Zinc), Vitamin B6, Thiamin Mononitrate '
        '(Vitamin B1), Folic Acid.')
        ],
    [
        'Post',
        'Shredded Wheat',
        "Bet you can't eat three.",
        1890,
        ('Whole Grain Wheat. To Preserve The Natural Wheat Flavor, Bht Is Added To The Packaging '
        'Material.')
        ],
    [
        'Quaker Oats',
        "Cap'n Crunch",
        "It's got corn for crunch, oats for punch, and it stays crunchy, even in milk.",
        1963,
        ('Corn Flour, Sugar, Oat Flour, Brown Sugar, Palm and/or Coconut Oil, Salt, Reduced Iron, '
        'Yellow 5, Niacinamide*, Zinc Oxide, Yellow 6, Thiamin Mononitrate*, BHT (a preservative), '
        'Pyridoxine Hydrochloride*, Riboflavin*, Folic Acid.')
        ],
    [
        'Quaker Oats',
        "Life Cereal",
        "He likes it! Hey Mikey!",
        1961,
        ('Whole Grain Oat Flour, Sugar, Corn Flour, Whole Wheat Flour, Rice Flour, Salt, Calcium '
        'Carbonate, Disodium Phosphate, Reduced Iron, Niacinamide, Zinc Oxide, BHT (a '
        'Preservative), Yellow 5, Yellow 6, Thiamin Mononitrate, Riboflavin, Pyridoxine '
        'Hydrochloride, Folic Acid, Contains Wheat Ingredients.')
        ]
]
```

If we wanted to return a string for each cereal formatted as

`< manufacturer > < cereal name > (debuted as < year >)`

we could assign the string formatting task to a function and then call the function from inside a
`for` loop as we iterate over the `cereals` list. We pass a `cereal` list to it and the function
returns a formatted string literal for our use.

```python
print(f"\n2.0 Breakfast cereals\n")

def format_cereal_name(cereal):
    return f"{cereal[0]} {cereal[1]}"


for cereal in cereals:
    string = format_cereal_name(cereal) # call function
    print(string)
```

The advantage of delegating the task to a function is that we can call the function in other places
in our code. We no longer need to reimplement the f-string elsewhere in our code; we can simply
call the `format_cereal_name` and pass to it a `cereal` object whenever we need to format the name.
The function helps to reduce code duplication while promoting code modularization and reuse.

## 3.0 Functions calling other functions

Since we will be working with the `cereals` nested list and making frequent recourse to index
operaters in order to select individual `cereal` elements, let's simplify our data access tasks
by writing a series of "helper" functions that accept a `cereal` object as an argument and return
a target element.

```python
def get_cereal_company(cereal):
    return cereal[0]

def get_cereal_name(cereal):
    return cereal[1]

def get_cereal_slogan(cereal):
    return cereal[2]

def get_cereal_year(cereal):
    return cereal[3]

def get_cereal_ingredients(cereal):
    return cereal[-1]
```

We can refactor our `format_cereal_name` function so that it calls the `get_cereal_company` and
`get_cereal_name` helper functions:

```python
def format_cereal_name(cereal):
    company_name = get_cereal_company(cereal)
    cereal_name = get_cereal_name(cereal)

    return f"{company_name} {cereal_name}"
```

By doing so we eliminate the need to maintain hard-coded index operators in two places of our code.

### 3.1 Challenge: filtering cereals by company

__Task__: write a function named `get_cereals_by_company` that defines two parameters: `cereals`
(`list`) and `company` (`str`). Given a list of cereals and a manufacturer (e.g., General Mills),
the function will iterate over the sequence and return to the caller, if found, a list of formatted
cereal  names filtered on the manufacturer. Test the function by retrieving all cereal products
produced by Kellogg's. Use available helper functions whenever possible.

:bulb: the `pass` statement is used as a placeholder for the code block to be implemented. The
`pass` statement is a `null` operation. When executed `pass` statements return nothing.

```python
def get_cereals_by_company(cereals, company):

    pass # Implement


company = "Kellogg's"
company_cereals = get_cereals_by_company(cereals, company) # call function

print(f"\n3.2 {company} cereals (n={len(company_cereals)}) = {company_cereals}")
```

### 3.2 Challenge: oldest cereal

__Task__: write a function named `get_oldest_cereal` that defines a single parameter `cereals`
(`list`). Given a list of cereals, the function will iterate over the sequence and return the
"oldest" cereal (formatted name only) by introduction date. _Assume that no cereals were introduced
together in the same year (no ties)_. Use available helper functions whenever possible.

:bulb: create a variable named `prev_year` and assign the current year (now) as the default value
using the `datetime` module.

```python
import datetime as dt # located at top of module

def get_oldest_cereal(cereals):
    now = dt.datetime.now() # datetime module current year
    prev_year = now.year

    pass # Implement


oldest_cereal = get_oldest_cereal(cereals)

print(f"\n3.2 Oldest cereal = {oldest_cereal}")
```

### 3.3 Challenge: check if a cereal contains a particular ingredient

__Task__: Write a helper function named `has_ingredient` that defines two parameters: `cereal`
(list) and `ingredient` (`str`). This function will search an individual cereal's ingredients string
for the specified `ingredient`. If the ingredient is found the function will return `True`;
otherwise, the function will return `False`. Test the function by passing the arguments `cereals[2]`
(i.e., Raisin Bran) and the ingredient "wheat".

:bulb: a function can be provisioned with multiple return statements. For this function include a
`return True` and a `return False`.

```python
def has_ingredient(): # TODO add parameters

    pass # Implement


raisin_bran_has_wheat = has_ingredient(cereals[2], 'wheat')

print(f"\n3.3 Raisin Bran ingredient search (has wheat) = {raisin_bran_has_wheat}")
```

### 3.4 Challenge: check all cereals for a particular ingredient

__Task__: Write a function named `search_ingrediants` that defines two parameters: `cereals` (`list`)
and `ingredient` (`str`). This function will search all cereals in the list `cereals` for the
specified `ingredient` and return a list of cereals (formatted name only) that include the
ingredient. Use the `has_ingredient` function to check each individual cereal as well as other
helper functions as required.

```python
def search_ingredients(): # TODO add parameters

    pass # Implement

ingredient = 'sugar'
results = search_ingredients(cereals, ingredient)

print(f"\n3.4 Cereals containing {ingredient} (n={len(results)}) = {results}")
```

## Sources

### A. History

1. _Wikipedia_, ["Cap'n Crunch"](https://en.wikipedia.org/wiki/Cap%27n_Crunch)
2. _Wikipedia_, ["Cheerios"](https://en.wikipedia.org/wiki/Cheerios)
3. _Wikipedia_, ["Corn Flakes"](https://en.wikipedia.org/wiki/Corn_flakes)
4. _Wikipedia_, ["Frosted Flakes"](https://en.wikipedia.org/wiki/Frosted_Flakes)
4. _Wikipedia_, ["Grape-nuts"](https://en.wikipedia.org/wiki/Grape-Nuts)
5. _Wikipedia_, ["Honey-nut Cheerios"](https://en.wikipedia.org/wiki/Honey_Nut_Cheerios)
6. _Wikipedia_, ["Life Cereal"](https://en.wikipedia.org/wiki/Life_(cereal))
7. _mashed.com_, ["Life Cereal: Untold Truth"](https://www.mashed.com/218962/the-untold-truth-of-life-cereal/)
8. _Wikipedia_, ["Lucky Charms"](https://en.wikipedia.org/wiki/Lucky_Charms)
9. _Wikipedia_, ["Raisin Bran"](https://en.wikipedia.org/wiki/Raisin_Bran)
10. _Wikipedia_, ["Rice Krispies"](https://en.wikipedia.org/wiki/Rice_Krispies)
11. _Wikipedia_, ["Shredded Wheat"](https://en.wikipedia.org/wiki/Shredded_wheat)
12. _Wikipedia_, ["Trix"](https://en.wikipedia.org/wiki/Trix_(cereal))
13. _Wikipedia_, ["Wheaties"](https://en.wikipedia.org/wiki/Wheaties)

### B. Ingredients

1. _cvs.com_, ["Cap'n Crunch"](https://www.cvs.com/shop/quaker-cap-n-crunch-original-prodid-111316)
2. _cvs.com_, ["Cheerios"](https://www.cvs.com/shop/cheerios-cereal-prodid-169905)
3. _cvs.com_, ["Corn Flakes"](https://www.cvs.com/shop/kellogg-s-corn-flakes-cereal-prodid-273722)
4. _cvs.com_, ["Frosted Flakes"](https://www.cvs.com/shop/kellogg-s-frosted-flakes-cereal-prodid-103604)
5. _amazon.com_, ["Grape-nus"](https://www.amazon.com/Post-Grape-Nuts-Breakfast-Cereal-Ounce/dp/B01MUXIRCR/ref=sr_1_2?dchild=1&fpw=pantry&keywords=grape-nuts&qid=1601937146&s=pantry&sr=1-2)
5. _cvs.com_, ["Honey-nut Cheerios"](https://www.cvs.com/shop/cheerios-honey-nut-cereal-prodid-731695)
6. _cvs.com_, ["Life Cereal"](https://www.cvs.com/shop/quaker-life-original-multigrain-cereal-13-oz-prodid-767123)
7. _cvs.com_, ["Lucky Charms"](https://www.cvs.com/shop/lucky-charms-cereal-prodid-731232)
8. _cvs.com_, ["Raisin Bran"](https://www.cvs.com/shop/kellogg-s-raisin-bran-cereal-prodid-353920)
9. _cvs.com_, ["Rice Krispies"](https://www.cvs.com/shop/kellogg-s-rice-krispies-cereal-prodid-720037)
10. _amazon.com_, ["Shredded Wheat"](https://www.amazon.com/Shredded-Wheat-Original-Cereal-15-Ounce/dp/B0035DZNUQ/ref=asc_df_B0035DZNUQ/?tag=hyprod-20&linkCode=df0&hvadid=312196444054&hvpos=&hvnetw=g&hvrand=11521080224598170722&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9017371&hvtargid=pla-569008279560&psc=1)
11. _cvs.com_, ["Trix"](https://www.cvs.com/shop/trix-cereal-family-size-prodid-2330225)
12. _amazon.com_, ["Wheaties"](https://www.amazon.com/General-Mills-Wheaties-Cereal-15-6/dp/B004G7NE3S#:~:text=Protein%202g.-,Ingredients%3A,WHEAT%3A%20MAY%20CONTAIN%20ALMOND%20INGREDIENTS)
