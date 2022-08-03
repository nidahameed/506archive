# SI 506 Midterm 03

## 1.0 Overview

The midterm exam is open network, open readings, open notes, open slide decks. You may refer to
code in previous lecture exercises, lab exercises, and problem sets for inspiration.

We recommend that at a minimum you bookmark the following
[w3schools](https://www.w3schools.com/python/default.asp) Python pages and/or have them open in a
set of browser tabs as you work on the midterm exam:

* [Python keywords](https://www.w3schools.com/python/python_ref_keywords.asp)
* [Python operators](https://www.w3schools.com/python/python_operators.asp)
* [Python built-in functions](https://www.w3schools.com/python/python_ref_functions.asp)
* [Python `list` methods](https://www.w3schools.com/python/python_ref_list.asp)
* [Python `str` methods](https://www.w3schools.com/python/python_ref_string.asp)

## 2.0 Points

The midterm is worth 1000 points and you accumulate points by passing a series of autograder tests.

## 3.0 A few rules

:exclamation: Please download the midterm files from Canvas Files as soon as they are
released. This is a timed event and delays in acquiring the assignment files will shorten the time
available to engage with the assignment. The clock is not your friend.

:exclamation: You are prohibited from soliciting assistance or accepting assistance from any person
while taking the exam. The midterm code that you submit _must_ be your own work. Likewise, you are
prohibited from assisting any other student required to take this exam. This includes those taking
the exam during the regular exam period, as well as those who may take the exam at another time
and/or place due to scheduling conflicts or other issues.

## 4.0 README and template files

:exclamation: _DO NOT_ modify, remove, or change the order of the scaffolded code that we provide in
the Python template file unless instructed to do so.

In line with the weekly lab exercises and problem sets the midterm comprises a `README.md`
(this document) that contains assignment instructions together with a numbered `midterm_XX.py`
template file for you to write your code.

The template file contains a number of function definitions that you will implement along with a
`main()` function from which you will call the other functions, make variable assignments, and
perform other tasks in response to a series of challenges described below.

Implementing functions involves replacing the placeholder `pass` statement with working code. You
will call each function from `main()` passing arguments to the function and assigning the return
value to a specified variable per the instructions.

The template `*.py` file resembles the following skeletal implementation (verbose multi-line
Docstring instructions are shortened to a single line in the example):

```python
def some_function(some_parameter, another_parameter):
    """A description of expected behavior.

       Parameters:
            ...

        Returns:
            ...
    """

    pass # TODO Implement


def main():
    """Entry point for the program.

       Parameters:
            ...

        Returns:
            ...
    """

    # CHALLENGE 01

    # Manage execution flow per instructions.

    var_01 = None # TODO Call function; assign return value

    # . . .

    # CHALLENGE 08

    var_02 = None # TODO Call function; assign return value

    # Manage execution flow per instructions.


# Check if the Python interepreter knows this file as "__main__" (i.e., a script
# intended to be run from the command line). If True, call the main() function
# which serves as the entry point to the program.
if __name__ == '__main__':
    main()
```

## 5.0 A note on styling

The autograder includes tests that will check whether or not you are adhering to Python styling
guidelines relative to the [use of whitespace](https://www.python.org/dev/peps/pep-0008/#id26) in
certain expressions and statements. The goal is to encourage you to write code that adheres to
the Python community's code styling practices. Doing so enhances code readability and aligns you
with other Python programmers.

In particular, always surround the following operators on either side with a single space:

* assignment (`=`)
* augmented assignment (`+=`, `-=`, etc.)
* comparisons (`==`, `<`, `>`, `!=`, `<>`, `<=`, `>=`, `in`, `not in`, `is`, `is not`)
* Booleans (`and`, `or`, `not`).

```python
# Correct
clubs = search_club_names(clubs, search_term)

# Incorrect
clubs=search_club_names(clubs, search_term)

# Correct
count += 1

# Incorrect
count+=1
```

Note however that an exception exists with respect to function parameters and arguments. Do _not_
surround optional parameter default value assignments or keyword argument assignments with spaces.

```python
# Correct
def create_email_address(uniqname, domain='umich.edu'):
   """TODO"""
   return f"{uniqname}@{domain}"

# Incorrect
def create_email_address(uniqname, domain = 'umich.edu'):
   """TODO"""
   return f"{uniqname}@{domain}"

# Correct
email_address = create_email_address(uniqname='anthwhyte', domain='gmail.com')

# Incorrect
email_address = create_email_address(uniqname = 'anthwhyte', domain = 'gmail.com')
```

## 6.0 Challenges

The midterm comprises a number of challenges. Some challenges are "standalone" and can be completed
in any order. Other challenges have dependencies on previous challenges and require that the previous
challenge(s) be completed first before attempting the new challenge. A table describing challenge
dependencies is included below:

| Challenge | Dependency |
| :-------- | :--------- |
| Challenge 01 | None |
| Challenge 02 | None |
| Challenge 03 | None |
| Challenge 04 | Challenge 03 |
| Challenge 05 | Challenge 04 |
| Challenge 06 | Challenge 05 |
| Challenge 07 | None |

:bulb: The teaching team recommends that you engage with the challenges as currently ordered.
However, some students may prefer to implement the "standalone" challenges first in order to earn
"standalone" challenge points via the autograder before tackling the linked challenges.

The midterm is based in part on data drawn from the
[Chinese Women's Super League](https://en.wikipedia.org/wiki/Chinese_Women%27s_Super_League) (CWSL).
Inaugurated in 1997, the CWSL is China's top level women's football league.

You will work with two lists. The first list named `regions` comprises a select list of Chinese
[provinces](https://en.wikipedia.org/wiki/Provinces_of_China) along with an element listing four
cities administered directly by the central government. Each element is represented by a list that
includes the province/direct administration name and a tuple of select Chinese cities. This list
will be used to perform province/city lookups.

The second list named `clubs` provides string representations of the eight teams that comprised the
CWSL for the [2019-2020](https://en.wikipedia.org/wiki/2019_Chinese_Women%27s_Super_League) season.
Each "club" list includes the following data:

* Team name
* Home town (city)
* Matches Played (MP)
* Won (W)
* Draw/Tie (D)
* Loss (L)
* Goals For (GF)
* Goals Against (GA)

During the midterm you will calculate the following additional statistics:

* Goal Difference (GD)
* Points earned (Pts)
* Points per game (PPG)

The final challenge involves parsing a
[Megan Rapinoe](https://hbr.org/2020/07/lifes-work-an-interview-with-megan-rapinoe) quote.

```python
# Data: ['Province', ('City',)],
regions = [
   ['Liaoning Province', ('Anshan', 'Dalian', 'Fushun', 'Shenyang')],
   ['Jiangsu Province', ('Changzhou', 'Nanjing', 'Suzhou', 'Wuxi')],
   ['Jilan Province', ('Changchun', 'Jilin', 'Siping', 'Yanji')],
   ['Hubei Province', ('Wuhan', 'Xiangyang', 'Yichang', 'Jingzhou')],
   ['Henan Province', ('Anyang', 'Kaifeng', 'Luoyang', 'Zhengzhou')],
   ['Guangdong Province', ('Foshan', 'Guangzhou', 'Meizhou', 'Shenzhen')],
   ['Direct Administration', ('Beijing', 'Shanghai', 'Tianjin', 'Chongqing')]
   ]

# Chinese Women's Super League, 2019-2020 season
# Data: 'Club, City, MP, W, D, L, GF, GA' (will add GD and Pts later)
clubs = [
   ['Beijing BG Phoenix', 'Beijing', 14, 4, 4, 6, 19, 20],
   ['Changchun Zhuoyue', 'Changchun', 14, 7, 3, 4, 26, 27],
   ['Dalian', 'Dalian', 14, 1, 3, 10, 6, 29],
   ['Henan Huishang', 'Luoyang', 14, 3, 3, 8, 20, 27],
   ['Wuhan Jianghan University', 'Wuhan', 14, 6, 1, 7, 16, 21],
   ['Jiangsu Suning', 'Nanjing', 14, 12, 1, 1, 43, 9],
   ['Shanghai Shengli', 'Shanghai', 14, 8, 5, 1, 35, 11],
   ['Meizhou Huijun', 'Meizhou', 14, 4, 2, 8, 15, 36]
   ]

megan_quote = ("If you miss a shot, you missed it. You can't go back. You can "
   "only try to not make the same mistake twice. I've won a lot in my career, and "
   "I've lost a lot. You take the good with the bad. Also, it's not only about "
   "winning. It's about the process and the journey, the people you're with, "
   "continuing to grow and learn, and getting better every day.")
```

### Challenge 01

covers: list indexing and slicing, variable assignment, `main()`.

1. Use indexing _and_ slicing with __positive__ values to return a `list` of the Won, Draw, Loss
   integer values (`[W, D, L]`) for the __fifth (5th) team__ in the `clubs` list.

2. Assign the return value to the variable named `club_wdl` in `main()`.

### Challenge 02

covers: functions (implementing and calling), accumulator pattern, `for` loop, `if` statement,
list indexing, `str` methods, `list` methods, variable assignment, `main()`.

1. Implement the function named `search_club_names`. The function defines two required parameters
   `clubs` (`list`) and `search_term` (`str`), and returns a list of club record lists.

   The function will search the passed in `clubs` list for club names that contain the passed
   in `search_term`. The search performed _must_ be case _insensitive_. In other words, the case of
   the passed in `search_term` is to be ignored and all matches, irrespective of case (i.e., upper
   or lower) are to be returned.

   Read the function Docstring for more information regarding the function's expected behavior.

   :bulb: Write a conditional statement that checks if the passed in `search_term` string can be
   found in any of the club names found in the `clubs` list, irrespective of case. Use a local
   "accumulator" list to store the club record lists with names that include the `search_term`.

2. Once the function is implemented, assign the string __'university'__ to the variable `search_term`
   in `main()`.

3. Call the function from `main()` passing to it as arguments the `clubs` list and the `search_term`.

4. Assign the return value to the variable named `clubs_by_name`.

   :bulb: the return value _must_ be a list comprising one or more club lists in which each club
   name contains the passed in `search_term` argument.

   ```python
   [
      ['Club name', 'Home location', 22, 16, 1, 5, 67, 24],
      # . . . additional list elements, if any
      ]
   ```

### Challenge 03

covers: functions (implementing and calling), arithmetic operations (multiplication, division,
addition, subtraction), built-in functions, `main()`, `for` loop, list methods, variable assignment.

1. Implement the function named `calculate_goals_diff`. The function defines a single required
   parameter `club` (list) and returns an integer value. Read the function Docstring for more
   information regarding the function's expected behavior.

   :bulb: this function requires an equation that can be implemented with a single line of code.

2. Implement the function named `calculate_points`. The function defines a single required
   parameter `club` (list) and returns an integer value. Read the function Docstring for more
   information regarding the function's expected behavior.

   :bulb: this function requires an equation that can be implemented with a single line of code.

3. Implement the function named `calculate_points_per_game`. The function defines a single required
   parameter `club` (list) and returns a float value __rounded to the second decimal place__. Read the
   function Docstring for more information regarding the function's expected behavior.

   :bulb: this function requires an equation that can be implemented with a single line of code along
   with use of a built-in function to perform the rounding operation.

4. After implementing the three functions, write a `for` loop in `main()` that iterates over the
   `clubs` list. During each iteration of the loop do the following in the order specified:

   1. Call the function `calculate_goals_diff` and pass to it as an argument the current club list.

   2. Append the return value to the current club list.

   3. Call the function `calculate_points` and pass to it as an argument the current club list.

   4. Append the return value to the current club list.

   5. Call the function `calculate_points_per_game` and pass to it as an argument the current club
      list.

   6. Append the return value to the current club list.

      Each club record list in the `clubs` list should now include the three summary statistics as
      elements.

   Alternatively, implement step 4 above by using the `list.extend()` method to update the
   current club list with the GD, Pts, and PPG values. You can accomplish the task with a single
   line of code but recall that `list.extend()` takes an _iterable_ (i.e., an object like a `list`
   or a `tuple` with member objects that can be accessed) as an argument so construct the argument
   to be passed to the built-in function carefully.

   :bulb: Each club in the `clubs` should resemble the following list which now includes three
   new elements: goal difference, points, and average points per game (values are placeholders):

   ```python
   ['Club name', 'Home location', 22, 20, 2, 0, 93, 8, 85, 62, 2.82]
   ```

### Challenge 04

covers: functions (implementing and calling), accumulator pattern, nested `for` loop,
`if` statement, list indexing, membership operators, `list` methods, variable assignment, `main()`.

1. Implement the function named `get_clubs_by_regions`. The function defines two required
   parameters `clubs` (`list`) and `regions` (`list`), and returns a list of club record lists
   filtered on the cities, counties, and/or states included in the list of passed in `regions`.

   The function will use the `regions` list to filter the clubs in the `clubs` list. If a club's
   home location matches a location in one of the passed in region's tuple of city, county,
   and/or state locations, the club will be stored in a local "accumulator" list; the list of
   matched clubs will be returned to the caller after the loop terminates.

   Read the function Docstring for more information regarding the function's expected behavior.

   :bulb: This challenge will require implementation of an outer loop (iterate over `clubs`) and an
   inner loop (iterate over `regions`). Write a conditional statement inside the `regions` loop that
   checks whether or not the current club's home location is __in__ the current region's tuple of city,
   county, and/or state locations. If the conditonal statement evaluates to `True`, add the matched
   club to a local "accumulator" list.

2. Once the function is implemented return to `main()` and __slice__ the
   __Henan and Hubei province elements__ of the `regions` list into a new list and assign it to the
   variable `henan_hubei`.

3. Next, call the function `get_clubs_by_regions` and pass to it as arguments
   the `clubs` list and the `henan_hubei` list.

4. Assign the return value to the variable `henan_hubei_clubs`.

   :bulb: the return value _must_ be a list comprising one or more club lists in which each club
   home location can be found in any of the passed in `regions` list of region tuples of city,
   county, and/or state locations. Example below (values are placeholders):

   ```python
   [
      ['Club name', 'Home location', 28, 13, 10, 5, 52, 42, 10, 49, 1.75],
      # . . . additional list elements, if any
      ]
   ```

### Challenge 05

covers: list indexing, functions (calling, keyword arguments), variable assignment, `main()`.

1. From `main()` use indexing to access the __Direct Administration__ element from the `regions` list
   and assign it to a an empty list named `envelope` using a  `list` literal (e.g., `x = [y]`).

2. Then call the function `get_clubs_by_regions` using _keyword arguments_ in order to pass in the
   `clubs` list and the `envelope` list in __reverse__ order.

   :exclamation: You _must_ use keyword arguments to satisfy this challenge.

3. Assign the return value to the variable `direct_admin_clubs`.

   :bulb: the return value _must_ be a list comprising one or more club lists in which each club
   home location can be found in the `envelope` list of region tuples of city, county, and/or state
   locations. Example below (values are placeholders):

   ```python
   [
      ['Club name A', 'Home location', 16, 13, 2, 1, 60, 7, 53, 41, 2.56],
      ['Club name B', 'Home location', 16, 7, 3, 6, 21, 26, -5, 24, 1.5],
      # . . . additional list elements, if any
      ]
   ```

### Challenge 06

covers: functions (implementing and calling), accumulator pattern, `for` loop, `if-elif`
blocks, index operators, comparison operators, f-strings, variable assignment, `main()`.

After completing Challenge 03 each club in the `clubs` list now includes the average points per
game (PPG) value (last element). You will now retrieve the top club(s) possessing highest PPG.

1. Implement the function named `get_top_club_by_ppg`. The function defines a single required
   parameter `clubs` (`list`) and returns a formatted string literal (f-string) of the top team(s)
   as measured by points earned.

   The function will loop over the `clubs` list, employing `if-elif` conditional logic inside the
   loop in order to identify the club(s) with the highest PPG for the season. A formatted string
   literal (f-string) will be used to represent the top club(s). Built it according to the following
   criteria:

   A. If the current club's PPG is greater than the previous club's PPG then assign the
   following f-string to a local variable named `top_club` per the following format:

   `"< current club name > (< current club average points per game > PPG)"`

   B. If the current club's PPG is equal to the previous club's PPG then assign the
   following f-string to the local variable `top_club` per the following format:

   `"< previous top_club > and < current club name > (< current club average points per game > PPG)"`

   :bulb: Work with two local variables. The first is `top_club` which is used to store the current
   top club string. Use a second local variable named `points_per_game` to store the current club's
   PPG value so that it can be compared to the next club's PPG value. Assign `points_per_game` an
   initial value of `0.0`.

   Read the function Docstring for more information regarding the function's expected behavior.

2. Once the function is implemented call the function from `main()` passing to it as an argument the
   `henan_hubei_clubs` list.

3. Assign the return value to the variable `top_henan_hubei_club`.

   :bulb: The return value should resemble either the first string (one top club) or the second
   string (two or more clubs tied for top PPG). All values are placeholders:

   ```python
   'Club name A (2.2 PPG)'
   ```

   or

   ```python
   'Club name A (2.4 PPG) and Club name B (2.4 PPG) and Club name C (2.4 PPG)'
   ```

### Challenge 07

covers: functions (implementing and calling), accumulator pattern, counter, `for` loop,
`str` methods, `if` statement, membership operator, `list` methods, variable assignment, `main()`.

US veteran winger Megan Rapinoe was interviewed recently by the
[Harvard Business Review](https://hbr.org/2020/07/lifes-work-an-interview-with-megan-rapinoe).
During the interview Megan was asked whether taking World Cup penalty shots made her nervous. She
replied:

> If you miss a shot, you missed it. You can't go back. You can only try to not make the same
mistake twice. I've won a lot in my career, and I've lost a lot. You take the good with the bad.
Also, it's not only about winning. It's about the process and the journey, the people you're
with, continuing to grow and learn, and getting better every day.

1. Implement the function named `get_words_with_apostrophes`. The function defines a single required
   parameter `string` (`str`) and returns a list of tuples of words that include an apostrophe.

   The function must first split the string into a list of words before looping over the words.
   If a word with an apostrophe is encountered during the looping operation, a tuple will be added
   to a local "accumulator" list. The tuple will include two items: the word number (nth word in the
   string) and the word itself.

   `( < nth word >, < word >)`

   Read the function Docstring for more information regarding the function's expected behavior.

   :bulb: Create a local variable to hold the current word number (nth word) as you loop over the
   words from the passed in string. Numbering is __zero-based__ and will start from `0`, not one `1`.
   Use a local "accumulator" list to store the tuples you create, then return the list to the caller
   once all words are checked.

2. Once the function is implemented call the function from `main()` passing to it as an argument the
   `megan_quote` string included in the template file.

3. Assign the return value to the variable `words`.

   :bulb: The return value should resemble the following list of tuples (values are placeholders):

   ```python
   [(7, "wor'd"), (21, "w'ord"), (29, "w'ord"), (41, "wor'd"), (46, "wor'd"), (55, "wo'rd")]
   ```

## 7.0 Gradescope submissions

You may submit your problem solution to Gradescope as many times as needed before the expiration of
the exam time. Your __final__ submission will constitute your exam submission.

:exclamation: You _must_ submit your solution file to _Gradescope_ before the expiration of exam time.
Solution files submitted after the expiration of exam time will receive a zero score.

## 8.0 Auto grader / manual scoring

The autograder runs 19 tests against the Python file you submit, which the autograder imports as
a module so that it can gain access to and inspect the functions and other objects defined in your
code. The functional tests are of two types:

1. The first type will call a function passing in known argument values and compare the return
   value against an expected return value for equality. If the function's return value does not equal
   the expected return value, the test will fail.

2. The second type of test involves checking variable assignments in `main()`. This type of test
   evaluates the code you write, character for character, against an expected line of code using a
   [regular expression](https://realpython.com/regex-python/) to account for permitted variations
   in the expressions you write. The test searches `main()` for the expected line of code. If not
   located the test will fail.

Below is a summary of the tests the autograder will employ to score your code.

| Challenge | Test | Points |
| :-------- | :--- | :----: |
| Challenge 01 | Test indexing and slicing in `main()` | 50 |
| Challenge 02 | Test `search_term` variable assignment in `main`() | 25 |
| Challenge 02 | Test `search_club_by_name()` function | 100 |
| Challenge 03 | Test `calculate_goals_diff()` function | 60 |
| Challenge 03 | Test `calculate_points()` function | 60 |
| Challenge 03 | Test `calculate_points_per_game()` function | 85 |
| Challenge 03 | Test `calculate_goals_diff()` return value variable assignment in `main`() | 15 |
| Challenge 03 | Test `calculate_points()` return value variable assignment in `main`() | 15 |
| Challenge 03 | Test `calculate_points_per_game()` return value variable assignment in `main`() | 15 |
| Challenge 04 | Test slicing assignment in `main()` | 50 |
| Challenge 04 | Test `get_clubs_by_regions()` function | 125 |
| Challenge 05 | Test `envelope` variable assignment in `main()` | 25 |
| Challenge 05 | Test use of keyword arguments in `get_clubs_by_regions()` function call in `main()` | 50 |
| Challenge 05 | Test `get_clubs_by_regions()` function call | 75 |
| Challenge 06 | Test `get_top_club_by_ppg()` return value variable assignment in `main`() | 25 |
| Challenge 06 | Test `get_top_club_by_ppg()` function | 50 |
| Challenge 06 | Test `get_top_club_by_ppg()` function with 2 clubs with same PPG (tied) | 50 |
| Challenge 07 | Test `get_words_with_apostrophes()` return value variable assignment in `main`() | 25 |
| Challenge 07 | Test `get_words_with_apostrophes()` function call | 100 |

If the auto grader is unable to grade your submission successfully with a score of 1000 points the
teaching team will grade your submission __manually__. Partial credit __may__ be awarded for
submissions that fail one or more autograder tests if the teaching team (at their sole discretion)
deem a score adjustment warranted.

If you submit a partial solution, please include (if you have time) comments that explain what you
were attempting to accomplish in the area(s) of the program that are not working properly. We
will review your comments when determining partial credit.
