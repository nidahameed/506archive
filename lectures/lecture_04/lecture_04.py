# SI 506 Lecture 04

"""
1. Variables (labels) and variable assignment
2. Variable naming rules and conventions
3. Built-in functions `print()`, `type()`, `len()`
4. Basic arithmetic operations (add, subtract, multiply, divide)
5. `str.split()` method
6. String formatting (f-string)
"""

# 1.0 VARIABLES

name = "Graduate Employees' Organization 3550" # warn: apostrophe must be surrounded by double ("...")
member_count = 2138  # Ann Arbor campus only
is_on_strike = True

chorus = """
Hail! to the victors valiant
Hail! to the conquering heroes
Hail! Hail! to Michigan
the leaders and best!
"""

# 2.0 VARIABLE NAMING RULES AND CONVENTIONS

# 2.1 Good

# Choose lowercase
acronym = 'GEO'

# Separate words with underscore (_)
twitter_handle = '@geo3550'
geo_start_year = 1974 # year certified by Michigan Employment Relations Commission (MERC)

# Use plural form to indicate a set or sequence
hash_tags = ['#GEOStrike', '#StrikeForSafeCampus', '#UMMakesUsSick', '#SolidarityForever']

strike_demands = [
    'transparent testing and contract tracing planning',
    'universal right to work remotely',
    'parent and caregiver subsidy',
    'repeal $500.00 international student fee and document shipping fee',
    'degree timeline extensions and funding, rent freezes, flexible on-campus leases',
    'disarmed and demilitarized workplace',
    'Defund DPSS by 50% and reallocate funds to community-based justice initiatives',
    'U-M cut all ties with Ann Arbor Police Dept and Immigration and Customs Enforcement (ICE)'
    ]

# Ok to use recognizable abbreviations like num[ber], val[ue] or var[iable].
num = 1250 # count of GEO members who attended on 9 Sept 2020 membership call
val = 'some_value'
var = 'some_value'

# "is_", "has_" Boolean true/false
is_member = True

# All caps designates a module level constant (special case)
BASE_URL = 'https://www.geo3550.org/'

# Mathematical expressions (function definition specifying two parameters x and y)
def multiply(x, y):
    return x * y # arithmetic

# Call the function and pass two numeric arguments
product = multiply(14, 27)

# Built-in enumerate() function adds a counter < i > when looping over < course_codes >
for i, demand in enumerate(strike_demands, 1):
    print(f"{i}. {demand}")

# 2.2 Bad (but legal)

# Opaque
g = 'GEO'

# Reserve CamelCase for class names.
TwitterHandle = '@geo3550'

# Underscore overkill; difficult to read.
g_e_o = "Graduate Employee's Union 3550"

# Difficult to read; guaranteed to annoy.
cOUrsE_cOdE = 'SI 506'

# 2.3 Ugly (illegal)

# Illegal: keyword used as a variable name (language-specific identifiers reserved by Python)

# class = 'SI 506'
course_name = "SI 506"

class_ = 'SI 506' # legal: add trailing underscore (..._) to avoid reserved word clash (convention)

# Illegal: variable name commences with a numeric value.

# 3550_local = "Graduate Employee's Union 3550"

# Illegal: variable name commences with a special character (e.g., `@`, `%`, `$`, `&`, `!`)

# @geo3550 = 'https://twitter.com/geo3550'

# Illegal: variable name includes a dash (`-`).

# hash-tags = ['#GEOStrike', '#StrikeForSafeCampus', '#UMMakesUsSick', '#SolidarityForever']

# Illegal: variable name includes whitespace.

# course name = 'SI 506'


# 3.0 BUILT-IN FUNCTIONS (print(), type(), len())

# 3.1 print(): print passed in object to the screen

# Calling the built-in print() function and passing a hard-coded string.
print('Hello SI 506')
print('GEO is on Strike')

# Passing a variable which points to a list.
print(name)

# Passing two variables separated by a comma.
print(name, acronym)

# 3.2 type(): determine object's data type

data_type = type(name)
print(data_type) # returns <class 'str'>

data_type = type(geo_start_year)
print(data_type) # returns <class 'int'>

data_type = type(strike_demands)
print(data_type) # returns <class 'list'>

# 3.3 len(): check length of sequence (i.e., number of elements)

# Count characters in string (including whitespace).
chars_count = len(name) # UNCOMMENT
print(chars_count) # UNCOMMENT

# Count number of elements in list.
demands = len(strike_demands) # UNCOMMENT
print(demands) # UNCOMMENT

# You can also pass a function to another function as an argument.
# print(len(None)) # UNCOMMENT


# 4.0. BASIC ARITHMETIC (addition, subtraction, multiplication, division)

# 4.1 Addition

# Geo Strike demands count
covid_19_demands = 5
anti_policing_demands = 3

total_demands = covid_19_demands + anti_policing_demands
print(total_demands)

# 4.2 subtraction

# Ann Arbor campus (2019 numbers)
tenured_faculty = 3193
clinical_faculty = 2190
research_faculty = 898 # assume no researchers teach for this exercise
lecturer_faculty = 964

teaching_faculty = tenured_faculty + clinical_faculty + lecturer_faculty

non_unionized_faculty = teaching_faculty - lecturer_faculty
print(non_unionized_faculty)

# 4.3 Multiplication

# Ann Arbor campus
gsi_count = 2138 # includes Graduate Student Staff Assistants (GSSA)
work_hrs_per_week = 20 # individual GSI committment

work_hrs_withheld_per_week = gsi_count * work_hrs_per_week
print(work_hrs_withheld_per_week)


# 4.4 Floating point division

student_count = 225
lab_count = 10

avg_lab_size = student_count / lab_count
print(avg_lab_size)


# 4.5 Floor division

student_count = 225
lab_count = 10

avg_lab_size = student_count // lab_count
print(avg_lab_size)


# 5.0 Look-ahead: the str.split() method
declaration = "GEO is on strike"
print(declaration.upper())

val = '#GEOStrike #StrikeForSafeCampus #UMMakesUsSick #SolidarityForever'
hash_tags = val.split()

print(f"\nhash tags = {hash_tags}")

val = '#GEOStrike, #StrikeForSafeCampus, #UMMakesUsSick, #SolidarityForever'
hash_tags = val.split(',')

print(hash_tags)

val = '#GEOStrike, #StrikeForSafeCampus, #UMMakesUsSick, #SolidarityForever'
hash_tags = val.split(', ')

print(hash_tags)