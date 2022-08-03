# SI 506 Lecture 03

"""
Topics
1. Comments (single line, multiline)
2. Values (objects) and types
3. Variables (labels) and variable assignment
4. Built-in functions print(), type(), len()
5. Basic arithmetic operations (add, subtract, multiply, divide)
"""


# 1.0 COMMENTS

# A single line comment <-- commences with hash (#) character

"""
This is a block comment comprising a multi-line string. This is actually a string
constant that is denoted by the use of triple quotation marks.
"""


# 2.0 VALUES (OBJECTS) AND TYPES

# 2.1 NUMBERS: integer, float (decimal)

506

.25

# 2.2 SEQUENCES (ORDERED SET)

'Welcome to SI 506'

['arwhyte', 'deahanyu', 'dsewhite', 'maxzhang', 'mhaidli', 'shrijesh']

(506, 507, 618)

# 2.3 ASSOCIATIVE ARRAY (MAP): dictionary (key-value pairs)

{'course': "SI 506", 'instructor_count': 1, "gsi_count": 5, "ia_count": 2}

# 2.4 BOOLEAN

True
False

# 2.5 NONE

None


# 3.0 VARIABLES

num = 506

welcome_message = 'Welcome to SI 506'

teaching_team = ['arwhyte', 'deahanyu', 'dsewhite', 'maxzhang', 'mhaidli', 'shrijesh']

chorus = """
Hail! to the victors valiant
Hail! to the conquering heroes
Hail! Hail! to Michigan
the leaders and best!
"""

# 4.0 VARIABLE NAMING RULES AND CONVENTIONS

# 4.1 Good

num = 27

uniqname = 'arwhyte'

course_code = 'SI 506'

course_codes = ['SI 506', 'SI 507', 'SI 618']

is_enrolled = True

BASE_URL = 'https://si506.org/'

def multiply(x, y):
    return x * y # arithmetic

product = multiply(14, 27)

print(f"product = {product}")

for i, code in enumerate(course_codes, 1):
    print(f"{i}. {code}")

# 4.2 Bad (but legal)

c = 'SI 506'

cc = 'SI 506'

CourseCode = 'SI 506'

c_o_u_r_s_e_c_o_d_e = 'SI 506'

cOUrsE_cOdE = 'SI 506'

# 4.3 Ugly (illegal)

# class = 'SI 506'
# 506_umsi = 'SI 506
# $number = 506
# course-list = ['SI 506', 'SI 507', 'SI 618']
# course name = 'SI 506' # illegal; uncomment to test

# Avoid: built-in function names (a few examples)
# str = 'Go Blue'
# min = 0
# max = 100
# len = 101


# 5.0 BUILT-IN FUNCTIONS (print(), type(), len())

# 5.1 print(): print passed in object to the screen

print('SI 506 rocks!')

print(welcome_message)

print(chorus)

# 5.2 type(): determine object's data type

data_type = type(num)
print(data_type)

data_type = type(welcome_message)
print(data_type)

data_type = type(teaching_team)
print(data_type)

# 5.3 len(): check length of sequence (i.e., number of elements)

chars_count = len(welcome_message)
print(chars_count)

team_count = len(teaching_team)
print(team_count)


# 6.0. BASIC ARITHMETIC (addition, subtraction, multiplication, division)

# Counts
lecturer_count = 1
gsi_count = 5
ia_count = 2
lab_section_count = 10
student_count = 200

# Addition (+ operator)
teaching_team_count = lecturer_count + gsi_count + ia_count
print(f"teaching_team_count = {teaching_team_count}")

# Subtraction (- operator)
instructor_count = teaching_team_count - ia_count
print(f"instructor_count = {instructor_count}")

# Multiplication (* operator)
max_enrollment = lab_section_count * 25
print(f"max_enrollment = {max_enrollment}")

# Floating point division (/ operator)
avg_lab_size = student_count / lab_section_count
print(f"average lab size = {avg_lab_size}")

# Floor division a.k.a integer division (//)
avg_lab_size = student_count // lab_section_count
print(f"average lab size = {avg_lab_size}")
