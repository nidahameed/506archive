# SI 506 Lecture 17

## Challenge 01

Return formatted string comprising the title and release year of the _last_ film in the `films`
list. Assign to the variable `film`.

Format: `"< title > (< year_released >)"`

## Challenge 02

Return the scary character name from the first film in `films` list. Assign to the variable `scary_character_name`.

Format: `"< character >"`

## Challenge 03

Add _Scream_ (1996) to the `films` list. Assign new dictionary to the variable named `scream` and
then insert new element __between__ _Child's Play_ (1988) and _The Ring_ (2002).

* Title: Scream
* Released: 1996
* Budget: $15 million
* Box office: $173 million
* Scary character name: Ghostface
* Scary character weapon: knife

Start with an empty dictionary and add key-value pairs using bracket notation.

## Challenge 04

Add _A Nightmare on Elm Street 2: Freddy's Revenge_ (1985). Assign new dictionary to the variable
named `elm_street_2` and then insert new element after _A Nightmare on Elm Street_ (1984).

* Title: A Nightmare on Elm Street 2: Freddy's Revenge
* Released: 1982
* Budget: $3 million
* Box office: $30 million
* Scary character name: Freddy Krueger
* Scary character weapon: clawed glove

Create dictionary by defining a dictionary literal.

## Challenge 05

Return a list of scary character dictionaries filtering out any duplicate scary characters. Assign
scary character dictionaries to the variable named `scary_characters`.

## Challenge 06

Implement `calculate_gross` function. Call function for each film in the `films` list and assign
return value to new film 'gross` key.

## Challenge 07

Implement `get_top_grossing_film` function. Call function and assign return value to the variable
`top_grossing_films`.

## Challenge 08

Implement `get_critics_choice` function in order to determine which film(s) are considered the best
in the genre by Rotten Tomato critics. Call function and assign return value to the variable
`top_rated_films`.

## Challenge 09

Implement `calculate_audience_vs_critics_rating_diff` function in order to calculate the difference
between the critics ratings and audience ratings for a given film. Return a list of tuples
`[(< title >, < rating diff >), . . .]` and assign to the variable `ratings_diff`.

## Challenge 10

Add the `tomatometer` and `audience` key-value pairs from each rating dictionary in the `ratings`
list to the appropriate film dictionary in the `films` list. Store both dictionaries in a new film
key labeled `rotten_tomatoes` (i.e., film[`rotten_tomatoes`]).

## Challenge 11

Create a new dictionary comprising counts of the scary characters that appear in the `films` list.
Each key-value pair must represent a scary character, with the key labeled with the name of the
scary character and the corresponding integer value equal to the number of film apppearances.

:bulb: Employ `dict.items()` to solve this challenge.

## Challenge 12

Each film dictionary in the `films` list has been augmented with two new key-value pairs: `gross` and `rotten_tomatoes`. Management requests that we reorder each dictionary's key-value pairs according
to the following order:

```python
key_order = (
    'title',
    'year_released',
    'budget',
    'box_office_receipts',
    'gross',
    'scary_character',
    'rotten_tomatoes'
    )
```

Implement the function `reorder_film_dict` in order to mint new film dictionaries from the existing
ones per the order prescribed by the tuple `key_order`. Call the function inside a loop and assign
the new "movie" dictionaries to the variable `movies`.
