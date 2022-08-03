# SI 506 Lecture 10

# SETUP

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

# END SETUP


# 1.0 NESTED LOOPS

dinosaur_name_strings = [
    'allosaurus, different lizard',
    'ankylosaurus, fused lizard',
    'apatosaurus, deceptive lizard',
    'brachiosaurus, arm lizard',
    'camptosaurus, flexible lizard',
    'ceratosaurus, horn lizard',
    'corythosaurus, helmet lizard',
    'deinocheirus, horrible hand',
    'diplodocus, double beam',
    'dreadnoughtus, fears nothing',
    'edmontosaurus, lizard from Edmonton',
    'gigantoraptor, giant seizer',
    'parasaurolophus, near crested lizard',
    'pachycephalosaurus, thick-headed lizard',
    'psittacosaurus, parrot lizard',
    'stegosaurus, roof lizard',
    'styracosaurus, spiked lizard',
    'triceratops, three-horned face',
    'tyrannosaurus, tyrant lizard',
    'velociraptor, swift seizer'
]

# 1.1 MATCHING NAMES
name_matched = 0
for dinosaur in dinosaurs:
    for name in dinosaur_name_strings:
        if name.lower().startswith(dinosaur[0].lower()):
            name_matched += 1 # increment
            break # terminate inner loop (avoid unnecessary iterations)

print(f"\n1.1 Dinosaurs (n = {len(dinosaurs)}); names matched = {name_matched}")


# 1.2 INSERT ROUGH NAME TRANSLATIONS
for dinosaur in dinosaurs:
    for name in dinosaur_name_strings:
        if name.lower().startswith(dinosaur[0].lower()):
            data = name.split(', ')
            dinosaur.insert(2, data[1].capitalize())
            break # terminate inner loop

print(f"\n1.2 Dinosaur name translations = {dinosaurs}")

### 1.3 REBUILD STRING (add geologic period)
for name in dinosaur_name_strings:
    names = name.split(', ')
    for dinosaur in dinosaurs:
        if dinosaur[0].lower() == names[0].lower():
            # name = f"{name}, {dinosaur[3].lower()}" # fail
            index = dinosaur_name_strings.index(name)
            dinosaur_name_strings[index] = f"{name}, {dinosaur[3].lower()}" # success
            break # terminate inner loop

print(f"\n1.3 Name translations w/geologic period = {dinosaur_name_strings}")


# 2.0 WHILE LOOP (indefinite iteration)

print(f"\n2.0 While loop examples.\n")

i = 0
while True:
    print('2.0 infinite loop triggered')
    if i == 5:
        print('2.0 infinite loop terminated\n')
        break # exit the loop
    i += 1 # increment

print('\n') # padding


# 2.1 WHILE LOOP AND COMPARISON OPERATORS

i = 0
while i < 5:
    print('I love dinosaurs.')
    i += 1 # increment

print('\n') # padding

i = 0
while i < 5:
    print('I love dinosaurs.')
    i += 1 # increment
else:
    print('Enough said. We believe you.')

print('\n') # padding

i = 0
while i < 10:
    if i % 2 == 0:
        print(f"{i} is an even number.")
    else:
        print(f"{i} is an odd number.")
    i += 1 # increment

print('\n') # padding

i = 10
while i >= 0:
    if i % 2 == 0:
        print(f"{i} is an even number.")
    else:
        print(f"{i} is an odd number.")
    i -= 1 # decrement


# 2.2 WHILE LOOP AND SEQUENCE TRAVERSAL

omnivore = None
i = 0
while i < len(dinosaurs):
    if dinosaurs[i][-1].lower() == 'omnivore':
        omnivore = dinosaurs[i][0]
        break # terminate the loop
    i += 1 # increment
else:
    print(f"\n Omnivore not found.")

print(f"\n2.2 First omnivore encountered = {omnivore}")

# 2.3 IDENTIFY DINOSAURS < 4000 KG

lightweights = []
i = 0
while i < len(dinosaurs):
    if int(dinosaurs[i][-2]) < 4000:
        lightweights.append(f"{dinosaurs[i][0]} ({dinosaurs[i][-2]} kgs)")
    i += 1 # increment

print(f"\n2.3 Dinosaurs < 4000 kg (n = {len(lightweights)}) = {lightweights}\n")


# 2.4 EXAMPLE CHALLENGE: remove dinosaurs between 5 and 20 meters in length (retain shortest/longest)

print(f"2.4 Remove Dinosaurs between 5 and 20 meters in length\n")

dinos = dinosaurs.copy() # protect the original list
i = 0
while True:
    if i == len(dinos):
        break # terminate loop and avoid IndexError

    if 5.0 <= float(dinos[i][-3]) <= 20.0:
        removed = dinos.pop(i) # all list indexes decremented -1
        print(f"{removed[0]} ({removed[-3]} meters) removed.")
        continue # i unchanged

    i += 1 # increment

print(f"\n2.4 Dinos <= 5 meters or >= 20 meters (n = {len(dinos)}) = {dinos}\n")


# 3.0 RANGE() TYPE

print(f"3.0 loops and the range() type\n")

for i in range(5):
    print(f"Iteration {i}")

print('\n') # padding

for i in range(0, 5, 2):
    print(f"Stepped iteration {i}")

print('\n') # padding

for i in range(5, -6, -1):
    print(f"Iteration {i}")


# 3.1 CHALLENGE: RANGE AND SEQUENCE LENGTH

# Using range() (add 'rex')
for i in range(len(dinosaurs) - 1):
    if dinosaurs[i][0].lower() == 'tyrannosaurus':
        dinosaurs[i][0] = 'Tyrannosaurus rex'
        break # terminate loop

print(f"\n3.1 Honor T. rex using range() = {dinosaurs[-1]}")


# 4.0 WHILE LOOP AND INPUT()

dinosaur_train = ('tiny', 'shiny', 'don', 'buddy')
prompt = '\nWho is your favorite Dinosaur Train character: '

# TODO UNCOMMENT

# while True:
#     character = input(prompt)
#     if character.lower() in dinosaur_train:
#         print(f"\nThanks. I like {character.capitalize()} too.\n\nFinis.\n")
#         break # terminate loop