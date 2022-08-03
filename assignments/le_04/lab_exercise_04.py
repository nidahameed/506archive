# START LAB EXERCISE 04
print('Lab Exercise 04 \n')

# SETUP
city_state = ["Detroit|MI", "Philadelphia|PA", "Hollywood|CA",
            "Oakland|CA", "Boston|MA", "Atlanta|GA",
            "Phoenix|AZ", "Birmingham|AL", "Houston|TX", "Tampa|FL"]
# END SETUP

# PROBLEM 1.0 (5 Points)
cali = city_state[2:4]
print(cali)

# PROBLEM 2.0 (5 Points)
us_cities = []

for cities in city_state:
    cities = cities.split('|')
    us_cities.append(cities[0])

print(us_cities)


# PROBLEM 3.0 (10 Points)

southern_cities = []

for city in us_cities:
    index = us_cities.index(city)
    print(index)
    if index > 4:
        southern_cities.append(city)
print(southern_cities)

# END LAB EXERCISE