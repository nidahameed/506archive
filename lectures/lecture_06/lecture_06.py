# SI 506 Lecture 06
# Marvel Super Heroes Exercise


# WARMUP 01
print(f"\nWARMUP 01")

hero = 'Black Widow'
new_hero = hero.replace('Widow', 'Panther')

print(f"\nnew hero = {new_hero}")


# WARMUP 02
print(f"\nWARMUP 02")
marvel_heroes = 'Captain America, Iron Man'
restyled_heroes = marvel_heroes.lower().replace(' ', '_').split(',_')

print(f"\nRestyled heroes = {restyled_heroes}")


# CHALLENGE 01
print(f"\nCHALLENGE 01")

marvel_heroes = "Black Panther, Black Widow, Captain America, Dr Strange, \
Hawkeye, Iron Man, Hulk, Scarlet Witch, Spider-Man, Thor" # note line continuation slash

# Wrap string spanning multiple lines wih (...).
# marvel_heroes = (
#     "Black Panther, Black Widow, Captain America, Dr Strange, Hawkeye, Iron Man, "
#     "Hulk, Scarlet Witch, Spider-Man, Thor"
#     )

heroes = marvel_heroes.split(', ')

print(f"\nheroes = {heroes}")


# CHALLENGE 02
print(f"\nCHALLENGE 02")

marvel_characters = """Bruce Banner
Clint Barton
Wanda Maximoff
Peter Parker
Steve Rogers
Natasha Romanoff
Tony Stark
Stephen Strange
Thor Odinson"""

#marvel_characters = f"{marvel_characters}\nT'Challa"
marvel_characters = marvel_characters + "\nT'Challa"
print(f"\nAdded T'Challa = {marvel_characters}")


# CHALLENGE 03
print(f"\nCHALLENGE 03")

characters = marvel_characters.splitlines()

print(f"\ncharacters = {characters}")


# CHALLENGE 04
print(f"\nCHALLENGE 04")

hollywood_actors = (
    "Chadwick Boseman | Benedict Cumberbatch | Robert Downey Jr | Chris Evans | "
    "Chris Hemsworth | Tom Holland | Scarlett Johansson | Elizabeth Olsen | "
    "Jeremy Renner | Mark Ruffalo"
    )

actors = hollywood_actors.split(' | ')

print(f"\nactors = {actors}")


# Challenge 05
print(f"\nCHALLENGE 05")

avengers = []
thor = heroes[-1] #will return string Thor
avengers.append(thor)

print(f"\navengers = {avengers}")

# Challenge 06
print(f"\nCHALLENGE 06")

avengers.append(heroes[2])


print(f"\navengers = {avengers}")


# Challenge 07
print(f"\nCHALLENGE 07")

avengers.insert(1, heroes[5])


print(f"\navengers = {avengers}")


# Challenge 08
print(f"\nCHALLENGE 08")

other_avengers =[]
other_avengers.append(heroes[6])
other_avengers.append(heroes[1])

avengers.extend(other_avengers)
print(f"\navengers = {avengers}")


# Challenge 09
print(f"\nCHALLENGE 09")

avengers.append(heroes[heroes.index('Hawkeye')])

print(f"\navengers = {avengers}")


# Challenge 10:
print(f"\nCHALLENGE 10")

avengers_count = len(avengers)

print(f"\navengers count = {avengers_count}")


# Challenge 11:
print(f"\nCHALLENGE 11")

avengers[0] = f"{avengers[0]} ({characters[-2]})"
avengers[1] = f"{avengers[1]} ({characters[-4]})"
avengers[2] = f"{avengers[2]} ({characters[4]})"
avengers[3] = f"{avengers[3]} ({characters[0]})"
avengers[4] = f"{avengers[4]} ({characters[5]})"
avengers[5] = f"{avengers[5]} ({characters[1]})"

print(f"\navengers = {avengers}")

# Challenge 12
print(f"\nCHALLENGE 12")

hero = None

print(f"\nhero = {hero}")



print(f"\navengers = {avengers}")

# Challenge 13
print(f"\nCHALLENGE 13")

avengers[0] = avengers[0].replace('(', '<').replace(')', '>')


print(f"\navengers = {avengers}")

# Challenge 14
print(f"\nCHALLENGE 14")

avengers.remove(avengers[-2])
avengers.pop(avengers.index('Iron Man (Tony Stark)'))


print(f"\navengers = {avengers}")

print('\n') # buffer line
