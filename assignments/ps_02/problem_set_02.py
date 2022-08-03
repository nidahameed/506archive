# START PROBLEM SET 02
print('Problem Set 02')

# PROBLEM 1 (20 points)
print('\nProblem 1')

cases = [11, 10, 38, 19, 27]
cases_latest = cases[-1] #Assign
cases[0] = 9


# PROBLEM 2 (20 points)
print('\nProblem 2')

tests = [] #Assign
tests.append(867)
tests.append(854)
tests.append(1494)
tests.append(1712)
tests.append(1667)

tests_max = max(tests) #Assign

tests_max_index = tests.index(1712) #Assign


# PROBLEM 3 (20 points)
print('\nProblem 3')

weeks = ' Aug.09,Aug.16,Aug.23,Aug.30,Sep.06 '
weeks = weeks.strip()
week_update1 = weeks.replace('.', '')
weeks_list = week_update1.split(',') #Assign

#print(weeks_list)

# PROBLEM 4 (20 points)
print('\nProblem 4')

weeks_new = '|'.join(weeks_list) #Assign
#print(weeks_new)

aug_count = weeks_new.count('Aug') #Assign
#print(aug_count)

# PROBLEM 5 (20 points)
print('\nProblem 5')

date = weeks_list[3]
test_num = tests[3]
case_num = cases[3]

most_tests = f'In the week starting on {date}, UM has conducted {test_num} tests and reported {case_num} cases.'
print(most_tests)

date = weeks_list[2]
test_num = tests[2]
case_num = cases[2]

most_cases = f'In the week starting on {date}, UM has conducted {test_num} tests and reported {case_num} cases.' #Assign
print(most_cases)