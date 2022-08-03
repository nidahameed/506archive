# Midterm Review

## Operators

Refer to Anthony's lecture slides

### + (concatenate operator)
You have to make sure the variable at left hand side and the variable at right hand side have same data type

```python
# both are strs
'1' + 'c'
# both are ints
1 + 2
# both are tuples
('Hi',) + (True,)
# both are lists
["Hi", 1, False] + ["Hey", (22, )]
```

### in (membership operator)
```python
char = 'h'
substr = 'hi'
string = 'hi, nice to meet you'
# char in string
char in string
# substring in string
substr in string

i = 1
l = [1,2,'Hi', True]
t = (2,)
# element in list
i in l
# element in tuple
i in t

```

## Indexing & Slicing

Q. Use indexing to find the third element of the list
Q. Use indexing to find the second element of the fifth element of the list
Q. Use slicing to filter out the second and third elements of the list

```python
l = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [11,12,13],
    [14,15,16]
]

q1 = l[2]
q2 = l[4][1]
q3 = l[1:3]

```

## List Methods
- append
- pop
- insert
- index
- ......

## String Methods
- lower / upper
- replace
- split
- find
- replace
- ......

## Loop

Q. count the occurrence of 'r' of string

```python
# Counter
string = 'I walk through the long schoolroom questioning'
r_num = 0
for char in string:
    if char == 'r':
        r_num += 1
```

Q: what if you're asked to count the occurrence of 'r' in each word of `string` and append the occurrence to a list named `r_nums`

```python
# Accumulator & Nested Loop & Counter
r_nums = []
for word in string.split():
    # why we put r_num inside the outer loop?
    r_num = 0
    for char in word:
        if char == 'r':
            r_num += 1
    # Why we only need one indentation here?
    # Can you explain how the code would be executed differently with one, two, three indentations
    r_nums.append(r_num)
```

Q: Can you find the maximum, even numbers, a selection of prime numbers (3,5,7,11) from a list of integer using **one for loop**

```python
numbers = (1,99,23,45,6,777,14,36,11,25,82,5)
prime_numbers = (3,5,7,11)

max_num = 0
even_nums = []
prime_nums = []

for num in numbers:
    if num > max_num:
        max_num = num
    
    if num % 2 == 0:
        even_nums.append(num)
    
    if num in prime_numbers:
        prime_nums.append(num)
```

## Implement Function Based on Docstring

```python
"""Return the occurrence of 'r' for a passed in string.
Parameters:
    string (str): the string needs to be counted.
Returns
    integer: the occurrence of 'r'.
"""
```

```python
def r_counter(string):
    r_num = 0
    for char in string:
        if char == 'r':
            r_num += 1
    return r_num
```

```python
"""Return a list of the occurrence of 'r' for each word in a passed in string.
Parameters:
    string (str): the string needs to be counted.
Returns
    list: the list occurrence of 'r'.
"""
```

```python
def r_word_counter(string):
    r_nums = []
    for word in string.split():
        r_num = r_counter(word)
        r_nums.append(r_num)
    return r_nums
```

### Optional Parameter & Required Parameter
- required parameter: has no default value
- optional parameter: has default value 
  ```python
  # during function definition
  # v1 is required, v2 is optional
  def f1(v1, v2 = 2):
      pass
  ```
### Keyword Arguments & Positional Arguments
- keyword argument: pass value by keyword
- positional argument: pass value by position
  ```python
  # during the function call
  f1(1, 2)
  f1(1, v2 = 3)
  f1(v1 = 4)
  f1(v1 = 2, v2 = 5)
  ```

## Instructions -> Code

- loop over / for each : for loop
- Assign the return value of `f1` to `var`: 
  ```python
  var = f1()
  ```
- pass `var1` as positional argument and `var2` as keyword argument to `f1`
  ```python
  f1(var1, v2 = var2)
  ```
- if `var` exists in `sequence` / whether or not `var` exists in `sequence`:
  ```python
  # option1
  # occurrence of `var` is greater than 0
  

  # option2
  # `var` is a member of `sequence`
  if var in sequence == True:
  ```
- append `var` to `sequence`:
  ```python
  sequence.append(var)
  ```
- nested for loop, outer loop, inner loop:
  ```python
  # we're at outside the outer loop
  for v1 in sequence1:
      # we're at inside the outer loop but outside the inner loop
      for v2 in sequence2:
          # we're at inside the inner loop
  ```
- compare `var1` against `var2`
  ```python
  # more than 
  var1 > var2
  # not more than
  var1 <= var2
  # less than 
  var1 < var2
  # not less than
  var1 >= var2
  # equal / tie
  var1 == var2
  # not equal
  var1 != var2
  ```
