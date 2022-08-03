# SI 506 Lecture 05

menu = """Egg and bacon
Egg, sausage and bacon
Egg and Spam
Egg, bacon and Spam
Egg, bacon, sausage and Spam
Spam, bacon, sausage and Spam
Spam, egg, Spam, Spam, bacon and Spam
Spam, Spam, Spam, egg and Spam
Spam, Spam, Spam, Spam, Spam, Spam, baked beans, Spam, Spam, Spam and Spam
Lobster Thermidor aux crevettes with a Mornay sauce, garnished with truffle pâté, brandy and a fried egg on top, and Spam"""


# 1.0 STRING METHODS

# 1.1 str.startswidth()

is_first = menu.startswith('Spam')
print(f"\nis_first = {is_first}") # formatted string literal (f-string)

is_last = menu.endswith('Spam')
print(f"\nis_first = {is_last}")

# 1.2 str.lower()

lower_case = menu.lower()
print("\nlower_case = %s" % lower_case) # old school placeholder formatting (yuck)

# 1.3 str.count()

spam_count = menu.count("Spam")
print(f"spam_count = {spam_count}\n")

# 1.4 str.replace()

gummies_menu = menu.replace('Spam', 'Gummies')
print("\ngummies_menu = {}".format(gummies_menu)) # str.format()

# 1.5 str.strip()

monty_python = " Monty Python's Flying Circus " # note apostrophe
print(f"\nMonty Python = {monty_python}")

monty_python = monty_python.strip() # note reassignment
print(f"\nMonty Python (stripped) = {monty_python}")

stripped = monty_python.replace(' ', '') # note reassignment
print(f"\nMonty Python (all stripped) = {stripped}")

# 1.6 str.join()

items = ['Oatmeal', 'Fruit', 'Spam'] # a list
menu_item = ''.join(items) # join to blank or empty string (not so good in this case)
print(f"\nMenu item = {menu_item}")

menu_item = ' '.join(items)
# menu_item = ' '.join(items)
print(f"\nMenu item = {menu_item}")

# 1.7 str.split()

char_groups = menu.split() # returns list
print("\nchar_groups = {}".format(char_groups)) # str.format()

# 1.8 str.splitlines()

menu_items = menu.splitlines() # returns list
print("\nMenu_items = {}\n".format(menu_items)) # str.format()


# 2.0 LIST METHODS

# 2.1 Append element to list (in-place)

menu_items.append('Red Beans and rice, and Spam') # modify in-place (no variable assignment)
print(f"\nNew menu item = {menu_items}")

# 2.2 Remove element from list (in-place)

menu_items.remove('Lobster Thermidor aux crevettes with a Mornay sauce, garnished with truffle pâté, brandy and a fried egg on top, and Spam')
print(f"\nNo Lobster Thermidor = {menu_items}")

### 2.3 Extend list with another list (in-place)

healthy_items = ['Cereal and Yogurt, and Spam', 'Oatmeal, fruit plate, and Spam']
menu_items.extend(healthy_items)
print(f"\nnew menu extended = {menu_items}")

### 2.4 Sort the list (in-place)

menu_items.sort() # default alpha sort
print(f"\nNew menu sorted = {menu_items}")


# 3.0 INDEX OPERATOR

### 3.1 Index position (string)

name = 'Monty Python'
letter = name[0] # first letter (zero-based index)
print(f"\nLetter = {letter}")

letter = name[4]
print(f"\nLetter = {letter}")

letter = name[-1]
print(f"\nLetter = {letter}")

### 3.2 Index operator (list)

menu_item = menu_items[1] # second element (zero-based index)
print(f"\nMenu item = {menu_item}")

menu_item = menu_items[-3]
print(f"\nMenu item = {menu_item}")


# 3.3 IndexError

# UNCOMMENT
# menu_item = menu_items[13] # IndexError: list index out of range


### 4.0 INDEX OPERATOR: list And str METHODS

# 4.1 list.index()

index = menu_items.index('Egg and Spam')
print(f"\nIndex postion = {index}\n")


# stopped here on Tues (Sept 15) lecture.


# 4.2 list.insert()

menu_items.insert(1, 'Blueberry pancakes and Spam')
print(f"\nBlueberry pancakes added to the menu = {menu_items}")

### 4.3 list.pop()

retired_item = None # pop the last item out of the list
print(f"\nRetired item = {retired_item}")

### 4.4 str.find()

menu_item = 'Spam, Spam, Spam, egg and Spam'
position = None
print(f"\nIndex position = {position}")

menu_item = 'Spam, Spam, Spam, egg and Spam'
position = None
print(f"\nIndex position = {position}")

### 4.5 str.index()

menu_item = 'Spam, Spam, Spam, egg and Spam'
position = None
print(f"\nIndex position = {position}")

menu_item = 'Spam, Spam, Spam, egg and Spam'
# UNCOMMENT
# position = menu_item.index('ham')
print(f"\nIndex position = {position}")

## 5.0 STRING FORMATTING

# 5.1 Formatted string literal (f-string)

special_item = 'egg, bacon, spam and sausage'
print(f"\nWhy can't she have {special_item}?") # embedded variable

# 5.2 str.format()

question = "\nCould I have {}, {}, {} and {}, without the spam?".format('egg', 'bacon', 'spam', 'sausage')
print(question)

# 5.3 %-formatting

question = "\nNo, it wouldn't be %s, %s, %s and %s, would it?" % ('egg', 'bacon', 'spam', 'sausage')
print(question)
