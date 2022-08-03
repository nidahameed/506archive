# START PROBLEM SET 04
print('Problem Set 04')

# START SET UP
summary = [
    'Step 1: Beat It',
    'Step 2: Prep the Pan',
    'Step 3: Add the Eggs',
    'Step 4: Patience Makes Perfect',
    'Step 5: Almost Done',
    'Step 6: Ready to Eat'
]
recipe = [
    "Beat your eggs until they're completely blended. Add a little water, cream or milk to make them tender. Use 1 tablespoon of liquid per egg. Add a pinch of salt.",
    "Next, heat a nonstick skillet over a medium-low flame and toss in a pat of butter. Make sure the butter coats the pan.",
    "Then, pour in the eggs. Pause to let them heat slightly — gentle heat is essential.",
    "Move the eggs across the pan like a bulldozer so the eggs cook evenly. This takes a little time, but it's worth it.",
    "As the eggs start to set, add chopped fresh herbs, or bits of ham or cheese.",
    "Turn your eggs onto warmed plates and dig in! Watch our how-to video for more."
]

# Problem 01
print('\nProblem 1')

#1.1
step_length = []
i = 0
while i < 6:
    for step in recipe:
        step = len(recipe[i])
        step_length.append(step)
        i = i+1
print(step_length)

#1.2
gte_100 = 0
less_100 = 0
for value in step_length:
    if value > 100:
        gte_100 += 1
    else:
        less_100 += 1
print(gte_100)
print(less_100)

#1.3
step_25_mins = 0
for characters in step_length[1:5]:
    if characters > 100:
        step_25_mins += 10
    else:
        step_25_mins += 5
print(step_25_mins)

# Problem 02
print('\nProblem 2')

#2.1
#step_order_3 = summary[2].replace(' ', '').upper().replace(':ADDTHEEGGS', '')

step_order_3 = summary[2].replace(' ', '').upper()
step_order_3 = step_order_3[:5]

print(step_order_3)

#2.2
recipe_summary_3 = f'{step_order_3}: {recipe[2]}'
print(recipe_summary_3)

#2.3
recipe_summary = []
i = 0
for steps in summary:
    while i < 6:
        step_order = summary[i].replace(' ', '').upper()
        step_order = step_order[:5]
        recipe_summary.append(f'{step_order}: {recipe[i]}')
        i += 1
print(recipe_summary)


# Problem 03
print('\nProblem 3')

#3.1
step2_r_num = 0
#print(recipe[1].count('r'))
#print(len(recipe[1]))
#for steps in recipe:
    #if recipe[1] == 'r':
        #step2_r_num += 1
for characters in recipe[1]:
    if characters == 'r':
        step2_r_num += 1
print(step2_r_num)

#3.2
step_r_num = []

for steps in recipe:
    i = 0
    for characters in steps:
        if characters == 'r':
            i += 1
    step_r_num.append(i)
print(step_r_num)

#3.3
#print(max(step_r_num))
for r_num in step_r_num:
    if r_num == max(step_r_num):
        max_r_index = step_r_num.index(max(step_r_num))
        max_r_num = max(step_r_num)
print(max_r_index)
print(max_r_num)

