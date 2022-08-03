
# SI 506 Lecture 12

# SETUP

scale = [('5 stars', 5), ('4 stars', 4), ('3 stars', 3), ('2 stars', 2), ('1 star', 1)]

cereals = [
    ["Cap'n Crunch", (5, 1), (4, 0), (3, 0), (2, 0), (1, 0)],
    ['Cheerios', (5, 40), (4, 6), (3, 0), (2, 0), (1, 0)],
    ["Cinnamon Toast Crunch", (5, 45), (4, 2), (3, 1), (2, 0), (1, 0)],
    ['Cocoa Puffs', (5, 18), (4, 1), (3, 1), (2, 0), (1, 0)],
    ['Corn Flakes', (5, 155), (4, 10), (3, 1), (2, 1), (1, 0)],
    ['Frosted Flakes', (5, 403), (4, 32), (3, 6), (2, 1), (1, 0)],
    ['Fruit Loops', (5, 187), (4, 32), (3, 3), (2, 2), (1, 0)],
    ['Honey-nut Cheerios', (5, 33), (4, 5), (3, 0), (2, 0), (1, 0)],
    ['Life Cereal', (5, 69), (4, 22), (3, 16), (2, 12), (1, 43)],
    ['Lucky Charms', (5, 12), (4, 0), (3, 0), (2, 0), (1, 0)],
    ['Raisin Bran', (5, 349), (4, 36), (3, 7), (2, 1), (1, 1)],
    ['Rice Krispies', (5, 145), (4, 17), (3, 2), (2, 1), (1, 1)],
]

# 1.0 VARIABLE SCOPE

cereal = ('General Mills', 'Cocoa Puffs', 20, 4.9) # global scope

if cereal: # truth value
    cereal_exists = True # available globally

def format_name(cereal):
    name = f"{cereal[0]} {cereal[1]}" # local scope only
    return name

print(f"\n1.0: Cereal exists = {cereal_exists}")

cereal_name = format_name(cereal) # call function

print(f"\n1.0: Cereal name = {cereal_name}")

# TODO UNCOMMENT
# print(f"\n1.0: Local variable name = {name}") # NameError: name 'name' is not defined


# 2.0 CHALLENGES

# CHALLENGE 01
def get_cereal_name(cereal):
    return cereal[0]

name = get_cereal_name(cereals[0])

print(f"\nChallenge 01: Cereal name = {name}")


# CHALLENGE 02

def check_cereal_name(cereal, name):
    return cereal[0].lower() == name.lower()

cereal = cereals[-1]
has_element = check_cereal_name(cereal, "Rice Krispies")

print(f"\nChallenge 02: {cereal} found = {has_element}")


# CHALLENGE 03

def get_cereal(cereals, name):
    for cereal in cereals:
        if has_cereal(cereal, name):
                return cereal


cereal = get_cereal(name='Frosted Flakes', cereals=cereals)
print(f"\nChallenge 03: Cereal = {cereal}")

# TODO UNCOMMENT
#cereal = get_cereal(cereals, 'Wheaties') # returns None
#print(f"\nChallenge 03: Cereal type = {type(cereal)}")


# CHALLENGE 04

# TODO IMPLEMENT

cereal = None
review_count = None

# print(f"\nChallenge 04 {get_cereal_name(cereal)} review count = {review_count}")


# CHALLENGE 05

# TODO IMPLEMENT

cereal = None
favorable_count = None

# print(f"\nChallenge 05 {get_cereal_name(cereal)} favorable count = {favorable_count}")


# CHALLENGE 06

# TODO IMPLEMENT

favorite = None
# print(f"\nChallenge 06: Favorite cereal: {favorite[0]} (n={favorite[1]})")


# CHALLENGE 07

# TODO IMPLEMENT

cereal = None
unfavorable_count = None

# print(f"\nChallenge 07: {get_cereal_name(cereal)} unfavorable count = {unfavorable_count}")


# CHALLENGE 08

# TODO IMPLEMENT

least_favorite = None

# print(f"\nChallenge 08: Least favorite cereal: {least_favorite[0]} (n={least_favorite[1]})")


# CHALLENGE 09 (BONUS)
# pass functions as arguments

# TODO IMPLEMENT

favorite = None

# print(f"\nChallenge 09 (refactored): favorite cereal: {get_cereal_name(favorite)} (n={favorite[1]})")

least_favorite = None

# print(f"\nChallenge 09 (refactored): least favorite cereal: {get_cereal_name(favorite)} (n={least_favorite[1]})")


# CHALLENGE 10

# TODO IMPLEMENT

cereal = None
weighted_mean = None

# print(f"\nChallenge 10: {get_cereal_name(cereal)} rating {weighted_mean} (weighted mean)")

cereal = None
weighted_mean = None

# print(f"\nChallenge 10 {get_cereal_name(cereal)} rating {weighted_mean} (weighted mean)")

# Print all weighted means

# TODO IMPLEMENT

# print(f"\nChallenge 10 Sorted: Cereal, Weighted mean, Total ratings\n")

# TODO UNCOMMENT

# List comprehension
# ratings = [
#     (get_cereal_name(cereal), calculate_weighted_mean(cereal), count_cereal_reviews(cereal))
#     for cereal in cereals
#     # for cereal in cereals if count_cereal_reviews(cereal) > 100
#     ]

# # Sort list using a lambda expression
# ratings.sort(key=lambda cereal: cereal[1], reverse=True) # sort by rating, reverse order

# for cereal in ratings:
#     print(f"{cereal[0]}, {cereal[1]} (n={cereal[2]})")
