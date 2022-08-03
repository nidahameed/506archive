# START LAB EXERCISE 02
print('Lab Exercise 02 \n')

# SETUP

sandwich_string = 'chicken, bread, lettuce, onion, olives'

# END SETUP

# PROBLEM 1 (4 points)
sandwich_replace = sandwich_string.replace('olives', 'tomato')

# PROBLEM 2 (4 points)
sandwich_list = sandwich_replace.split(', ')
#print(sandwich_list)

# PROBLEM 3 (4 points)
sandwich_list.pop(0)
#print(sandwich_list)

# PROBLEM 4 (4 points)
sandwich_list.append('mayo')
#print(sandwich_list)

# PROBLEM 5 (4 Points)
last_item = sandwich_list[-1]
#print(last_item)

# END LAB EXERCISE