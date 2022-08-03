# SI 506 Lecture 21

## Topics

1. Decompose real-world thing (a menu) into multiple objects.
2. Work with multiple class instances.
3. Compose a class based, in part, on another class.
4. Read/write files.

## Vocabulary

__Class__: "A template for creating user-defined objects. Class definitions normally contain method definitions which operate on instances of the class." [Python Official Documentation](https://docs.python.org/3/glossary.html).
__Composition__: Pattern that involves combining object types in order to create a _composite_ type that models a "has a" relationship between the composite and one or more _component_ objects (e.g., `Automobile` has an `Engine`; `Bicycle` has a `Crankset`, `Handlebar`, `Wheelset`, `Pedal` (2x), `Seat`, etc.).
__Instance__: An individual object whose type is defined by the class by which it was instantiated or created.
__Instance variable__: An variable and value bound to a specific instance of a class.
__Instance method__: A function defined by a class and bound to a specific instance of a class.
__self__: A variable that represents an instance of a class.

## Source

__Jamaican Jerk Pit__\
314 S Thayer St, Ann Arbor, MI 48104\
Tel: 734-585-5278

[Menu](https://www.jamaicanjerkpit.com/menu/) | [Takeout](https://www.grubhub.com/restaurant/jamaican-jerk-pit-314-s-thayer-st-ann-arbor/2041701?utm_source=google&utm_medium=organic&utm_campaign=place-action-link)

Today's data is drawn from Ann Arbor's own Jamaican Jerk Pit menu.

1. `dishes.csv`: Dishes including name, dish type, and optional description. Created by the Jerk Pit
   chef.
2. `menu_items.csv`: Menu items including name and price (USD). Created by Jerk Pit manager.
3. `menu_sections.csv`: Menu sections including name and optional description.  Create by the Jerk
   Pit manager.

## Challenges

Write a small program that combines three data sets in order to generate a text file that mimics the
online Jerk Pit menu. The program needs to implement the following classes:

1. `Menu`: composite type comprising a collection of `MenuItem` components.
2. `MenuItem`: composite type comprising a `Dish` component, item type (e.g., entree, side) and price.
3. `Dish`: food dish including optional description.

:exclamation: Capitalize class names using "CamelCase" styling when joining two nouns, as in `MenuItem`.

### Challenge 01

Implement the `Dish` class. Design the class with three (3) required instance variables:

* name (str): name of dish
* dish_type (str): type of dish (e.g., starter, entree, side, dessert)
* description (str): short description of dish

Implement a `__str()__` method that provides a string representation of the object.

Then read `dishes.csv` and return a list of dictionaries. Assign the list to a variable named
`dishes_data`. Loop over `dishes_data` and during each iteration instantiate a new instance of `Dish`
using the dictionary data to construct the instance. Then append the new `Dish` object to a _new_
list called `dishes`.

### Challenge 02

Implement the `MenuItem` class. Design the class with two (2) required instance variables:

* dish (Dish): dish object
* price (float): item price

Implement a `__str()__` method that provides a string representation of the object.

Then read `menu_items.csv` and return a list of dictionaries. Assign the list to a variable named
`menu_items_data`. Loop over `menu_items_data` and during each
iteration instantiate a new instance of `MenuItem` using the dictionary data to construct the
instance along with the appropriate `Dish` object instance retrieved from the `dishes_data` list
(match on the name). Then append the new `MenuItem` object to a _new_ list called `menu_items`.

:bulb: `MenuItem` is an example of a composite type; its construction depends in part on the
existence of a component type, in this case a `Dish` instance.

### Challenge 03

Implement the `Menu` class. Design the class with two (2) required instance variables:

* restaurant_name (str): name of restaurant
* menu_name (str): name of menu

Add two (2) additional instance variables that are _not_ required to construct an instance of the
class. Assign an empty list to each.

* menu_sections (list): list of menu sections (e.g., Calypso Starters)
* menu_items (list): list of `MenuItem` objects.

Implement a `__str()__` method that provides a string representation of the object.

Implement two methods that allow the caller to add menu sections and menu items to a `Menu` instance.

```python
def add_menu_items(self, items):
    """Add menu items to menu.

    Parameters:
        items (list): list of one or more menu items

    Returns:
        None
    """

    pass # TODO IMPLEMENT

def add_menu_sections(self, sections):
    """Add menu_sections to menu.

    Parameters:
        menu_sections (list): list of one or more menu sections or categories

    Returns:
        None
    """

    pass # TODO IMPLEMENT
```

Instantiate an instance of the `Menu` class named `menu` passing to it's constructor the following
arguments:

* restaurant_name = 'Jamaican Jerk Pit'
* menu_name = 'Menu'

:bulb: `Menu` is built to hold `MenuItem` instances but, in this case, its construction does
_not_ require adding `MenuItem` instances when the object is instantiated.

### Challenge 04

Call the `menu` object's `add_menu_sections` method and pass to it a list of menu sections
obtained from the `menu_sections.csv` file. Then call the `menu` object's `add_menu_items` method
and pass to it the list of `MenuItem` instances.

Finally, call the `menu` object's `generate_markdown` method and return a
[Markdown](https://guides.github.com/pdfs/markdown-cheatsheet-online.pdf) formatted menu
string (provided). Then write the string to a file by calling the function `write_file` and passing
to it as arguments the menu string along with the absolute filepath
`lecture_21/output/jerk_pit_menu.md`.

## Appendix

The `Menu` and `MenuItem` `generate_markdown()` methods employ the following Markdown syntax:

| Syntax | HTML | Description |
| :----- | :--: | :---------- |
| \# | \<h1\> | heading |
| \#\# | \<h2\> | heading |
| \#\#\# | \<h3\> | heading |
| \_\_ text \_\_ | \<b\> | bolded text |

### Menu

```python
def generate_markdown(self):
    """Create menu with menu_sections and menu items.

    Parameters:
        None

    Returns:
        menu (str): menu string
    """

    # Title
    menu = f"# {self.restaurant_name.upper()}\n\n## {self.menu_name.upper()}\n\n"

    # Section(s) and menu items
    for section in self.menu_sections:
        menu += f"### {section[1].upper()}\n\n"

        if section[2]:
            menu += f"{section[2]}\n\n" # description

        for item in self.menu_items:
            if item.dish.dish_type.lower() == section[0].lower():
                menu += item.generate_markdown() # call item's method

    return menu
```

### MenuItem

```python
def generate_markdown(self):
        """Returns formatted menu item that may span multiple lines if a
        description exists. Do not include < dish_type > in string.

        Format: < name > $< price >
                  < description >

        Parameters:
            None

        Returns
            str: formatted string
        """

        item = f"__{self.dish.name}__ __${self.price:.2f}__\n"
        if self.dish.description:
            item += f"\n{self.dish.description}.\n"
        item += '\n'

        return item
```
