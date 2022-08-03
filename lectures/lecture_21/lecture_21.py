import csv
import os


class Dish:
    """Represents a food dish."""

    def __init__(self, name, dish_type, description):

        self.name = name
        self.dish_type = dish_type
        self.description = description

    def __str__(self):
        return f"{self.name} ({self.dish_type})"


class Menu:
    """Represents a restaurant menu."""

    def __init__(self, restaurant_name, menu_name):

        self.restaurant_name = restaurant_name
        self.menu_name = menu_name
        self.menu_sections = []
        self.menu_items = []

    def __str__(self):

        return f"{self.restaurant_name} {self.menu_name}"



    def add_menu_items(self, items):
        """Add menu items to menu.

        Parameters:
            items (list): list of one or more menu items

        Returns:
            None 
        """
        self.menu_items.extend(items)


    def add_menu_sections(self, sections):
        """Add menu_sections to menu.

        Parameters:
            menu_sections (list): list of one or more menu sections or categories

        Returns:
            None
        """

        self.menu_items.extend(sections)


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


class MenuItem:
    """A representation of a menu item."""

    def __init__(self, dish, price):

        self.dish = dish
        self.price = price

    def __str__(self):

        return f"{self.dish.name} {self.dish.dish_type} ({self.price})"

    # TODO UNCOMMENT
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
        item = f"__{self.dish.name}__ __${self.price}__\n"
        # item = f"__{self.dish.name}__ __${self.price:.2f}__\n"
        if self.dish.description:
            item += f"\n{self.dish.description}.\n"
        item += '\n'

        return item


def read_csv(filepath, delimiter=','):
    """
    Reads a CSV file, parsing row values per the provided delimiter. Returns a list
    of lists, wherein each nested list represents a single row from the input file.

    Parameters:
        filepath (str): The location of the file to read.
        delimiter (str): delimiter that separates the row values

    Returns:
        list: contains nested "row" lists
    """

    with open(filepath, 'r', newline='', encoding='utf-8') as file_obj:
        data = []
        reader = csv.reader(file_obj, delimiter=delimiter)
        for row in reader:
            data.append(row)

        return data


def read_csv_into_dicts(filepath, delimiter=','):
    """Accepts a file path, creates a file object, and returns a list of
    dictionaries that represent the row values using the cvs.DictReader().

    Parameters:
        filepath (str): path to file
        delimiter (str): delimiter that overrides the default delimiter

    Returns:
        list: nested dictionaries representing the file contents
     """

    with open(filepath, 'r', newline='', encoding='utf-8') as file_obj:
        data = []
        reader = csv.DictReader(file_obj, delimiter=delimiter)
        for line in reader:
            data.append(line) # OrderedDict()
            # data.append(dict(line)) # convert OrderedDict() to dict

        return data


def write_file(filepath, data, newline=True):
    """Write content to a target file encoded as UTF-8. If optional newline is specified
    append each line with a newline escape sequence (`\n`).

    Parameters:
        filepath (str): path to target file (if file does not exist it will be created)
        data (list): list of strings comprising the content to be written to the target file
        newline (bool): add newline escape sequence to line

    Returns:
        None
    """

    with open(filepath, 'w', encoding='utf-8') as file_obj:
        if newline:
            for line in data:
                file_obj.write(f"{line}\n") # add newline
        else:
            file_obj.writelines(data) # write sequence to file


def main():
    """Menu builder."""

# 0.0 FILE PATHS WITH OS.PATH

# Absolute path to directory in which *.py is located. Recognized by Debugger.
abs_path = os.path.dirname(os.path.abspath(__file__))
print(f"\nAbsolute path = {abs_path}")

# CHALLENGE 01
# DEFINE/INSTANTIATE DISH

dishes_path = './input/dishes.csv'
dishes_data = read_csv_into_dicts(dishes_path)

# TODO UNCOMMENT
print(f"\nChallenge 01: Jamaican dishes (n={len(dishes_data)}) = {dishes_data}")

# TODO UNCOMMENT
dishes = [] # accumulator list
for dish in dishes_data: # each dish in the data is a dictionary
    dishes.append(
        Dish(dish['name'], dish['type'], dish['description']) # instantiate a new instance of a dish class
    )

# TODO UNCOMMENT
# WARN: Prints dish object identifiers only
# print(f"\nChallenge 01: List of Dishes (n={len(dishes)}) = {dishes}")

# TODO UNCOMMENT
print(f"\nChallenge 01: List of Dishes (n={len(dishes)})\n")
for dish in dishes:
    print(dish)


# CHALLENGE 02
# DEFINE/INSTANTIATE MENUITEM
# CREATE MENU ITEM (Pass in Dish)

menu_items_path = os.path.join(abs_path, 'input', 'menu_items.csv')
menu_items_data = read_csv_into_dicts(menu_items_path)

# TODO UNCOMMENT
print(f"\nChallenge 03: Menu items data (n={len(menu_items_data)}) = {menu_items_data}")

# TODO IMPLEMENT LOOP

menu_items = []
for item in menu_items_data:
    for dish in dishes:
        if dish.name.lower() == item['name'].lower():
            menu_items.append(
                MenuItem(dish, item['price_usd'])
            )

# TODO UNCOMMENT
print(f"\nChallenge 02: Menu items (n={len(menu_items)})\n")
for item in menu_items:
    print(item)

# TODO UNCOMMENT Review MenuItem markdown
print(f"\nChallenge 02: Formatted menu items (n={len(menu_items)})\n")
for item in menu_items:
    print(item.generate_markdown())


# CHALLENGE 03
# DEFINE/INSTANTIATE MENU

restaurant_name = 'Jamaican Jerk Pit'
menu_name = 'Menu'

# TODO INSTANTIAT MENU
menu = Menu(restaurant_name, menu_name)

# TODO UNCOMMENT
print(f"\nChallenge 03: Menu = {menu}\n")


# CHALLENGE 04
# BUILD/PRINT MENU

menu_sections_path = os.path.join(abs_path, 'input', 'menu_sections.csv')
menu_sections = read_csv(menu_sections_path)

# Add sections and items
menu.add_menu_sections(menu_sections[1:])
menu.add_menu_items(menu_items)


# TODO IMPLEMENT Generate Menu markdown
jerk_pit_menu = menu.generate_markdown()

# Menu file path
menu_path = os.path.join(abs_path, 'output', 'jerk_pit_menu.md')

# TODO CALL WRITE_FILE
write_file(menu_path, jerk_pit_menu, newline=False)

if __name__ == '__main__':
    main()
