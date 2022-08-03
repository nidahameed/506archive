# SI 506 Midterm 0X

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

In line with the weekly lab exercises and problem sets the midterm comprises a `README.md`
(this document) that contains assignment instructions together with a numbered `midterm_XX.py`
template file for you to write your code.

The template file contains a number of function definitions that you will implement along with a
`main()` function from which you will call the other functions, make variable assignments, and
perform other tasks in response to a series of challenges described below.

:exclamation: _DO NOT_ modify or remove the scaffolded code that we provide in the template unless
instructed to do so.

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

The midterm comprises a number of challenges. The teaching team recommends that you complete each
challenge in the order specified in this README.

The midterm is based in part on data drawn from . . . .

```python
# Show list data
```

### Challenge 01

covers: list indexing and slicing, variable assignment, `main()`.

Steps 1 to n.

### Challenge 02

covers: functions (implementing and calling), accumulator pattern, `for` loop, `if` statement,
list indexing, `str` methods, `list` methods, variable assignment, `main()`.

Steps 1 to n.

### Challenge 03

covers: functions (implementing and calling), arithmetic operations (multiplication, division,
addition, subtraction), built-in functions, `main()`, `for` loop, list methods, variable assignment.

Steps 1 to n.

### Challenge 04

covers: functions (implementing and calling), accumulator pattern, nested `for` loop,
`if` statement, list indexing, membership operators, `list` methods, variable assignment, `main()`.

Steps 1 to n.

### Challenge 05

covers: list indexing, functions (calling, keyword arguments), variable assignment, `main()`.

Steps 1 to n.

### Challenge 06

covers: functions (implementing and calling), accumulator pattern, `for` loop, `if-elif`
blocks, index operators, comparison operators, f-strings, variable assignment, `main()`.

Steps 1 to n.

### Challenge 07

covers: functions (implementing and calling), accumulator pattern, counter, `for` loop,
`str` methods, `if` statement, membership operator, `list` methods, variable assignment, `main()`.

Steps 1 to n.

## 7.0 Gradescope submissions

You may submit your problem solution to Gradescope as many times as needed before the expiration of
the exam time. Your __final__ submission will constitute your exam submission.

:exclamation: You _must_ submit your solution file to _Gradescope_ before the expiration of exam time.
Solution files submitted after the expiration of exam time will receive a zero score.

## 8.0 Auto grader / manual scoring

If the auto grader is unable to grade your submission successfully with a score of 1000 points the
teaching team will grade your submission __manually__. Partial credit __may__ be awarded for
submissions that fail one or more autograder tests if the teaching team (at their sole discretion)
deem a score adjustment warranted.

If you submit a partial solution, please include (if you have time) comments that explain what you
were attempting to accomplish in the area(s) of the program that are not working properly. We
will review your comments when determining partial credit.
