# START PROBLEM SET 03
print('Problem Set 03')

# Problem 01
print('\nProblem 1')

build_materials = ('straw', 'sticks', 'bricks')
brick_house = build_materials[2]
print(brick_house)

destroyed = ('straw house', 'stick house')
withstanding = ('brick house',)
pig_houses = destroyed + withstanding
#print(pig_houses)

# SETUP
destroyed_houses1 = ("straw house",)
destroyed_houses2 =  ["straw house"]
# END SETUP
destroyed_houses2.append('stick house')
#print(destroyed_houses2)

# Problem 02
print('\nProblem 2')

# SETUP
wolf_dialog_1 = "Little pigs! Little pigs! Let me in! Let me in!"
# END SETUP

substr_dialog_1 = wolf_dialog_1[:25]
print(substr_dialog_1)

substr_dialog_2 = wolf_dialog_1[7:19]
print(substr_dialog_2)

substr_dialog_3 = wolf_dialog_1[:-37]
print(substr_dialog_3)

substr_dialog_4 = wolf_dialog_1[7:]
print(substr_dialog_4)

substr_dialog_5 = wolf_dialog_1[1:46:2]
print(substr_dialog_5)

substr_dialog_6 = wolf_dialog_1[:6:2]
print(substr_dialog_6)

# Problem 03
print('\nProblem 3')

# SETUP
pigs_dialog_1 = "No! No! No! Not by the hairs on our chinny chin chin!"
# END SETUP

substr_dialog_7 = pigs_dialog_1[-21:-1]
print(substr_dialog_7)

substr_dialog_8 = pigs_dialog_1[:40]
print(substr_dialog_8)

substr_dialog_9 = pigs_dialog_1[-17:]
print(substr_dialog_9)

substr_dialog_10 = pigs_dialog_1[4:40]
print(substr_dialog_10)

substr_dialog_11 = pigs_dialog_1[::-1]
print(substr_dialog_11)

substr_dialog_12 = pigs_dialog_1[::-2]
print(substr_dialog_12)


# Problem 04
print('\nProblem 4')

# SETUP
wolf_dialog_2 = ("Then", "I'll", "huff", "and", "I'll" , "puff", 
"and", "I'll", "blow", "your", "house", "down.")
# END SETUP

sliced_dialog_1 = wolf_dialog_2[1:6]
print(sliced_dialog_1)

sliced_dialog_2 = wolf_dialog_2[-3:]
print(sliced_dialog_2)
