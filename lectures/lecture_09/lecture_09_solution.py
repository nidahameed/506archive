# SI 506 Lecture 09

import re

# 1.0 ITERATION

dinosaur_names = [
    'Psittacosaurus',
    'Brachiosaurus',
    'Edmontosaurus',
    'Parasaurolophus',
    'Triceratops',
    'Apatosaurus',
    'Diplodocus',
    'Deinocheirus',
    'Ankylosaurus',
    'Ceratosaurus',
    'Stegosaurus',
    'Velociraptor',
    'Styracosaurus',
    'Allosaurus',
    'Dreadnoughtus',
    'Camptosaurus',
    'Corythosaurus',
    'Pachycephalosaurus',
    'Tyrannosaurus',
    'Gigantoraptor'
    ]

# Return a list of all dinosaur name that start with letter T.
dinosaur_names_t = []
dinosaur_names_t.append(dinosaur_names[4])
dinosaur_names_t.append(dinosaur_names[-2])

print(f"\n1.0 T named dinosaurs = {dinosaur_names_t}")


# 1.1 FOR LOOP AND IF CONDITION

dinosaur_names_t = [] # accumulator

for dinosaur in dinosaur_names:
    if dinosaur.lower().startswith('t'):
        dinosaur_names_t.append(dinosaur)

print(f"\n1.1 T named dinosaurs = {dinosaur_names_t}")


# 1.2 Working with "overloaded" string data

dinosaur_strings = [
    'Psittacosaurus, Marginocephalia, Cretaceous, 2, 20, herbivore',
    'Brachiosaurus, Sauropoda, Jurassic, 21, 58000, herbivore',
    'Edmontosaurus, Ornithopoda, Cretaceous, 12, 4000, herbivore',
    'Parasaurolophus, Ornithopoda, Cretaceous, 9.5, 2500, herbivore',
    'Triceratops, Marginocephalia, Cretaceous, 9, 12000, herbivore',
    'Apatosaurus, Sauropoda, Jurassic, 22, 22400, herbivore',
    'Diplodocus, Sauropoda, Jurassic, 24, 14800, herbivore',
    'Deinocheirus, Theropoda, Cretaceous, 11, 6400, omnivore',
    'Ankylosaurus, Eurypoda, Cretaceous, 8, 8000, herbivore',
    'Ceratosaurus, Theropoda, Jurassic, 7, 980, carnivore',
    'Stegosaurus, Eurypoda, Jurassic, 9, 7000, herbivore',
    'Velociraptor, Theropoda, Jurassic, 1.5, 33, carnivore',
    'Styracosaurus, Marginocephalia, Cretaceous, 5.5, 3000, herbivore',
    'Allosaurus, Theropoda, Jurassic, 12, 1500, carnivore',
    'Dreadnoughtus, Sauropoda, Cretaceous, 26, 38192, herbivore',
    'Camptosaurus, Ornithopoda, Cretaceous, 7.9, 874, herbivore',
    'Corythosaurus, Ornithopoda, Cretaceous, 8.1, 3078, herbivore',
    'Pachycephalosaurus, Marginocephalia, Cretaceous, 4.5, 450, herbivore',
    'Tyrannosaurus, Theropoda, Cretaceous, 12.3, 8400, carnivore',
    'Gigantoraptor, Theropoda, Cretaceous, 8.9, 3600, carnivore'
    ]

dinosaur_count = len(dinosaur_strings)
print(f"\n1.2.1 Dinosaurs count = {dinosaur_count}")

# str.find() returns -1 if the index position is not found.
therapods = []
for dinosaur in dinosaur_strings:
    if dinosaur.lower().find('theropoda') >= 0:
        therapods.append(dinosaur)

print(f"\n1.2.2 Therapods find() = {therapods}")

# X.X Looping over a string (multiple conditions)

# This fails
sauropods = []
for dinosaur in dinosaur_strings:
    if dinosaur.lower().find('saurapoda') >= 0 and dinosaur.lower().find('cretaceous') >= 0:
        sauropods.append(dinosaur)

print(f"\n1.2.3 Cretaceous Saurapods find() x 2 fail = {sauropods}")

# Regular expression (out of scope)
pattern = re.compile(r"^.*?\bSauropoda\b.*?\bCretaceous\b.*?$") # regular expression
sauropods = []
for dinosaur in dinosaur_strings:
    if pattern.match(dinosaur):
        sauropods.append(dinosaur)

print(f"\n1.2.4 Cretaceous Saurapods regex = {sauropods}")

# Built-in all() function with comprehension
words = ('Sauropoda', 'Cretaceous')
sauropods = []
for dinosaur in dinosaur_strings:
    if all(word in dinosaur.split(', ') for word in words):
        sauropods.append(dinosaur)

print(f"\n1.2.5 Cretaceous Saurapods all() = {sauropods}")

# Split string into list (align with current knowledge)
sauropods = []
for dinosaur in dinosaur_strings:
    data = dinosaur.split(', ')
    if data[1].lower() == 'sauropoda' and data[2].lower() == 'cretaceous':
        sauropods.append(', '.join(data)) # recreate string
        # sauropods.append(data) # more likely scenario: append list to list

print(f"\n1.2.6 Cretaceous saurapods split() = {sauropods}")


# 1.3 NESTED LISTS

dinosaur_strings = [
    'Allosaurus, Theropoda, Jurassic, 12, 1500, carnivore',
    'Ankylosaurus, Eurypoda, Cretaceous, 8, 8000, herbivore',
    'Apatosaurus, Sauropoda, Jurassic, 22, 22400, herbivore',
    'Brachiosaurus, Sauropoda, Jurassic, 21, 58000, herbivore',
    'Camptosaurus, Ornithopoda, Cretaceous, 7.9, 874, herbivore',
    'Ceratosaurus, Theropoda, Jurassic, 7, 980, carnivore',
    'Corythosaurus, Ornithopoda, Cretaceous, 8.1, 3078, herbivore',
    'Deinocheirus, Theropoda, Cretaceous, 11, 6400, omnivore',
    'Diplodocus, Sauropoda, Jurassic, 24, 14800, herbivore',
    'Dreadnoughtus, Sauropoda, Cretaceous, 26, 38192, herbivore',
    'Edmontosaurus, Ornithopoda, Cretaceous, 12, 4000, herbivore',
    'Gigantoraptor, Theropoda, Cretaceous, 8.9, 3600, carnivore',
    'Pachycephalosaurus, Marginocephalia, Cretaceous, 4.5, 450, herbivore',
    'Parasaurolophus, Ornithopoda, Cretaceous, 9.5, 2500, herbivore',
    'Psittacosaurus, Marginocephalia, Cretaceous, 2, 20, herbivore',
    'Stegosaurus, Eurypoda, Jurassic, 9, 7000, herbivore',
    'Styracosaurus, Marginocephalia, Cretaceous, 5.5, 3000, herbivore',
    'Triceratops, Marginocephalia, Cretaceous, 9, 12000, herbivore',
    'Tyrannosaurus, Theropoda, Cretaceous, 12.3, 8400, carnivore',
    'Velociraptor, Theropoda, Jurassic, 1.5, 33, carnivore'
    ]

dinosaurs = []
for dinosaur in dinosaur_strings:
    data = dinosaur.split(', ')
    dinosaurs.append(data)

print(f"\n1.3.1 Dinosaurs nested lists ({len(dinosaurs)}) = {dinosaurs}")

# Extract name using slicing
dinosaur_name = dinosaurs[-1][0]

print(f"\n1.3.2 Dinosaur name = {dinosaur_name}")

# Loop over the nested list. Extract names
dinosaur_names = []
for dinosaur in dinosaurs:
   dinosaur_names.append(dinosaur[0])

print(f"\n1.3.3 Dinosaur names = {dinosaur_names}")


# 1.4 LOOPING AND SLICING

dinosaurs = [
    ['Allosaurus', 'Theropoda', 'Jurassic', '12', '1500', 'carnivore'],
    ['Apatosaurus', 'Sauropoda', 'Jurassic', '22', '22400', 'herbivore'],
    ['Brachiosaurus', 'Sauropoda', 'Jurassic', '21', '58000', 'herbivore'],
    ['Ceratosaurus', 'Theropoda', 'Jurassic', '7', '980', 'carnivore'],
    ['Diplodocus', 'Sauropoda', 'Jurassic', '24', '14800', 'herbivore'],
    ['Stegosaurus', 'Eurypoda', 'Jurassic', '9', '7000', 'herbivore'],
    ['Velociraptor', 'Theropoda', 'Jurassic', '1.5', '33', 'carnivore'],
    ['Ankylosaurus', 'Eurypoda', 'Cretaceous', '8', '8000', 'herbivore'],
    ['Camptosaurus', 'Ornithopoda', 'Cretaceous', '7.9', '874', 'herbivore'],
    ['Corythosaurus', 'Ornithopoda', 'Cretaceous', '8.1', '3078', 'herbivore'],
    ['Deinocheirus', 'Theropoda', 'Cretaceous', '11', '6400', 'omnivore'],
    ['Dreadnoughtus', 'Sauropoda', 'Cretaceous', '26', '38192', 'herbivore'],
    ['Edmontosaurus', 'Ornithopoda', 'Cretaceous', '12', '4000', 'herbivore'],
    ['Gigantoraptor', 'Theropoda', 'Cretaceous', '8.9', '3600', 'carnivore'],
    ['Pachycephalosaurus', 'Marginocephalia', 'Cretaceous', '4.5', '450', 'herbivore'],
    ['Parasaurolophus', 'Ornithopoda', 'Cretaceous', '9.5', '2500', 'herbivore'],
    ['Psittacosaurus', 'Marginocephalia', 'Cretaceous', '2', '20', 'herbivore'],
    ['Styracosaurus', 'Marginocephalia', 'Cretaceous', '5.5', '3000', 'herbivore'],
    ['Triceratops', 'Marginocephalia', 'Cretaceous', '9', '12000', 'herbivore'],
    ['Tyrannosaurus', 'Theropoda', 'Cretaceous', '12.3', '8400', 'carnivore']
    ]

cretaceous_dinosaurs = []
for dinosaur in dinosaurs:
    if dinosaur[2].lower() == 'cretaceous':
        cretaceous_dinosaurs.append(dinosaur)

print(f"\n1.4.1 Cretaceous dinosaurs unsliced ({len(cretaceous_dinosaurs)}) = {cretaceous_dinosaurs}")

# More efficient (slice)
cretaceous_dinosaurs = []
for dinosaur in dinosaurs[7:]:
    cretaceous_dinosaurs.append(dinosaur)

print(f"\n1.4.2 Cretaceous dinosaurs sliced ({len(cretaceous_dinosaurs)}) = {cretaceous_dinosaurs}")

# list comprehension (out of scope)
cretaceous_dinosaurs = [dinosaur for dinosaur in dinosaurs[7:]]

print(f"\n1.4.3 Cretaceous dinosaurs list comprehension ({len(cretaceous_dinosaurs)}) = {cretaceous_dinosaurs}")


# 2.0 CONDITIONAL STATEMENTS

# 2.1 COUNTING

sauropod_count = 0 # counter
for dinosaur in dinosaurs:
    if dinosaur[1].lower() == 'sauropoda':
        # sauropod_count = sauropod_count + 1
        sauropod_count += 1 # equivalent

print(f"\n2.1.1 Sauropod count = {sauropod_count}")

# Return counts of Jurassic Period Herbivores, Carnivores, and Omnivores
herbivore_count = 0
carnivore_count = 0
omnivore_count = 0

for dinosaur in dinosaurs[:7]:
    if dinosaur[-1].lower() == 'herbivore':
        herbivore_count += 1
    elif dinosaur[-1].lower() == 'carnivore':
        carnivore_count += 1
    else:
        omnivore_count += 1

msg = (
    '\n2.1.2 Jurassic Period diet counts'
    f"\nherbivore count = {herbivore_count}"
    f"\ncarnivore count = {carnivore_count}"
    f"\nomnivore count = {omnivore_count}"
)

print(msg)


# 2.2 COMPARISON OPERATORS; CONTINUE AND BREAK

# Return large dinosaurs (> 10 meters)
large_dinosaurs = []
for dinosaur in dinosaurs:
    if float(dinosaur[3]) > 15:
        large_dinosaurs.append(dinosaur)

print(f"\n2.2.1 Large dinosaurs (> 15 meters) = {large_dinosaurs}")

# Get the largest dinosaur (length)
largest_dinosaur = None
prev_length = 0
for dinosaur in dinosaurs:
    if float(dinosaur[3]) > prev_length:
        largest_dinosaur = f"{dinosaur[0]} ({dinosaur[3]} meters)"
        prev_length = float(dinosaur[3]) # reset
    elif float(dinosaur[3]) == prev_length:
        largest_dinosaur = f"{largest_dinosaur}, {dinosaur[0]} ({dinosaur[3]} meters)" # tied
    else:
        continue

print(f"\n2.2.2 Largest dinosaur (length) = {largest_dinosaur}")

# Get the smallest dinosaur (length)
smallest_dinosaur = None
prev_length = 0
for i, dinosaur in enumerate(dinosaurs):
    if i == 0:
        prev_length = float(dinosaur[3]) # seed with first length

    if float(dinosaur[3]) < prev_length:
        smallest_dinosaur = f"{dinosaur[0]} ({dinosaur[3]} meters)"
        prev_length = float(dinosaur[3]) # reset
    elif float(dinosaur[3]) == prev_length:
        smallest_dinosaur = f"{smallest_dinosaur}, {dinosaur[0]} ({dinosaur[3]} meters)" # tied
    else:
        continue

print(f"\n2.2.3 Smallest dinosaur (length) = {smallest_dinosaur}")

# break statement
duck_billed_dinosaur = None
for dinosaur in dinosaurs:
    if dinosaur[1].lower() == 'ornithopoda':
        duck_billed_dinosaur = dinosaur[0] # name only
        break

print(f"\n2.2.4 Duck-billed dinosaur = {duck_billed_dinosaur}")


# 2.3 COMPARISON OPERATORS (BETWEEN X AND Y)

# Return dinosaurs that weigh between X and Y kilograms.
heavy_dinosaurs = []
for dinosaur in dinosaurs:
    if 10000 < float(dinosaur[-2]) < 60000:
        heavy_dinosaurs.append(f"{dinosaur[0]} ({dinosaur[-2]} kg)") # name and weight

print(f"\n2.3 Dinosaurs weighing between 10000 and 60000 kg ({len(heavy_dinosaurs)}) = {heavy_dinosaurs}")


# 2.4. MEMBERSHIP OPERATORS

# Return all Cretaceous Marginocephalia and Ornithopoda (both Cerapoda)

# in membership operator.
cerapods = []
for dinosaur in dinosaurs[7:]:
    if dinosaur[1].lower() in ('marginocephalia', 'ornithopoda'):
        cerapods.append(f"{dinosaur[0]} ({dinosaur[1]})") # name and clade

print(f"\n2.4.1 Cretaceous Period Cerapods ({len(cerapods)}) = {cerapods}")

# Return all Cretaceous dinosaurs that are neiher Ornithopoda, Saurapoda, nor Theropoda.

# not in membership operator
eurypoda = []
for dinosaur in dinosaurs[7:]:
    if dinosaur[1].lower() not in ('marginocephalia', 'ornithopoda', 'sauropoda', 'theropoda'):
        eurypoda.append(f"{dinosaur[0]} ({dinosaur[1]})") # name and clade

print(f"\n2.4.2 Cretaceous Period Eurypods ({len(eurypoda)}) = {eurypoda}")


# 2.5 LOGICAL OPERATORS

# Return heaviest ornithopod
heaviest_ornithopod = None
weight = 0
for dinosaur in dinosaurs[7:]:
    if dinosaur[1].lower() == 'ornithopoda' and float(dinosaur[-2]) > weight:
        heaviest_ornithopod = dinosaur
        weight = float(dinosaur[-2]) # reset

print(f"\n2.5.1 Heaviest Cretaceous Ornithopod = {heaviest_ornithopod[0]} ({heaviest_ornithopod[4]} kg)")

# or logical operator (names that begin with C or D)
dinosaur_names_cd = []
for dinosaur in dinosaurs:
    if dinosaur[0].lower().startswith('c') or dinosaur[0].lower().startswith('d'):
        dinosaur_names_cd.append(dinosaur[0]) # name only

dinosaur_names_cd.sort() # in-place sort
print(f"\n2.5.2 Dinosaur names that begin with C or D = {dinosaur_names_cd}")

# not logical operator (meat-eaters)
meat_eaters = []
for dinosaur in dinosaurs:
    if not dinosaur[-1].lower() == 'herbivore':
        meat_eaters.append(f"{dinosaur[0]} ({dinosaur[-1]})")

print(f"\n2.5.3 Meat-eating dinosaurs ({len(meat_eaters)}) = {meat_eaters}")


# not logical operator (no saurus in the name)
non_saurus_names = []
for dinosaur in dinosaurs:
    if not dinosaur[0].lower().endswith('saurus'):
        non_saurus_names.append(dinosaur[0]) # name only

print(f"\n2.5.4 Dinosaur names without the 'saurus' (lizard) suffix = {non_saurus_names}")
