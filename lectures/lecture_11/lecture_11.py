import datetime as dt

# SI 506 Lecture 11

def create_slogan():
    print('\n1.1 Snap. Crackle. Pop.')

create_slogan()

# TODO
# VARIABLE SCOPE

def create_slogan(text):
    return text

tagline = 'Snap. Crackle. Pop.'

rice_crispies = create_slogan(tagline)

tagline = 'Hello SI506'
hello = create_slogan(tagline)
print(f"\n{hello}")

# Cheerios
# Corn Flakes

# 1.1 DEFINING A FUNCTION

# TODO IMPLEMENT FUNCTION

# 1.1 DEFINING A FUNCTION WITH A PARAMETER

# TODO IMPLEMENT FUNCTION

print(f"\n1.2 {rice_crispies}")

# 1.3 MULTIPLE PARAMETERS

def create_slogan(text, emphasis):
        text = text.replace('.', emphasis)
        return text

# Positional arguments
tagline = 'Snap. Crackle. Pop.'
rice_crispies = create_slogan(tagline, '!')
tagline = "They’rrrre GR-R-REAT." # Kellog's Frosted Flakes
frosted_flakes = create_slogan(tagline, '?')
tagline = 'Silly Rabbit. Trix are for Kids.' # General Mills Trix
trix = create_slogan(tagline, '!!!')

print(f"\n1.3 {rice_crispies} {frosted_flakes} {trix}")

# 1.4 Argument order matters: passed positionally

tagline = 'They’re always after me lucky charms.' # General Mills Lucky Charms leprechaun (emphasis excluded)

# TODO PASS IN ARGUMENTS OUT OF ORDER
lucky_charms = create_slogan('!', tagline) # Oops!

print(f"\n1.4 {lucky_charms}")

# 1.5 Keyword arguments: position no longer matters

# Keyword arguments free you from having to worry about correctly ordering your arguments in the
# function call, and they clarify the role of each value in the function call. Makes function calls
# more explicit.

# TODO UNCOMMENT
lucky_charms = create_slogan(emphasis='!', text=tagline) # pass args by name

print(f"\n1.5 {lucky_charms}")

# 1.6 Parameter default value

def create_slogan(text, emphasis='!'):
    text = text.replace('.', emphasis)
    return text

tagline = 'He likes it. Hey Mikey.' # Quaker Oats. 1970s TV ad campaign

# TODO UNCOMMENT
life_cereal = create_slogan(tagline, '!!!')

print(f"\n1.6 {life_cereal}")

# 2.0 FUNCTIONS AND LOOPS

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

print(f"\n2.0 Breakfast cereals\n")

def format_cereal_name(cereal):
    return f"{cereal[0]} {cereal[1]}"

for cereal in cereals:
    string = format_cereal_name(cereal) # call function
    print(string)


# 3.0 FUNCTIONS CALLING OTHER FUNCTIONS

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


# REFACTOR format_cereal_name()

def format_cereal_name(cereal):
    company_name = get_cereal_company(cereal)
    cereal_name = get_cereal_name(cereal)

    return f"{company_name} {cereal_name}"


# 3.1 CHALLENGE
# Write function that returns cereals by company. Use helper functions.

def get_cereals_by_company(cereals, company):
    company_cereals = []
    
    for cereal in cereals:
        if get_cereal_company(cereal).lower() == company.lower():
            name = format_cereal_name(cereal)
            company_cereals.append(name)

    return company_cereals

company = "General Mills"
company_cereals = get_cereals_by_company(cereals, company) # call function

print(f"\n3.1 {company} cereals (n={len(company_cereals)}) = {company_cereals}")

# 3.2 CHALLENGE: OLDEST CEREAL
# Assume no ties

def get_oldest_cereal(cereals):
    now = dt.datetime.now() # datetime module current year
    prev_year = now.year
    oldest = None

    for cereal in cereals:
        current_year = get_cereal_year(cereal)

        if current_year < prev_year:
            oldest = format_cereal_name(cereal)
            prev_year = current_year

    return oldest


# TODO UNCOMMENT
oldest_cereal = get_oldest_cereal(cereals)
print(f"\n3.2 Oldest cereal = {oldest_cereal}")


# 3.3 CHALLENGE: check ingredient

def has_ingredient(): # TODO add parameters

    pass


# TODO UNCOMMENT
# raisin_bran_has_wheat = has_ingredient(cereals[2], 'wheat')

# print(f"\n3.3 Raisin Bran ingredient search (has wheat) = {raisin_bran_has_wheat}")


# 3.4 CHALLENGE: search all cereals for ingredient

def search_ingredients(): # TODO add parameters

    pass

ingredient = 'sugar'

# TODO UNCOMMENT
# results = search_ingredients(cereals, ingredient)

# print(f"\n3.4 Cereals containing {ingredient} (n={len(results)}) = {results}")

print('\n') # padding
