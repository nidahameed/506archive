# SI 506 Lecture 07

# SETUP
orchestra = [
    'Wynton Marsalis, trumpet',
    'Marcus Printup, trumpet',
    'Kenny Rampton, trumpet',
    'Sherman Irby, alto saxophone',
    'Paul Nedzela, baritone saxophone',
    'Walter Blanding, saxophone',
    'Ted Nash, saxophone',
    'Victor Goines, saxophone',
    'Chris Crenshaw, trombone',
    'Vincent Gardner, trombone',
    'Elliot Mason, trombone',
    'Carlos Henriquez, bass',
    'Dan Nimmer, piano'
]

substitutes = [
    'Anthony Lustig, baritone saxophone',
    'Carl Maraghi, baritone saxophone',
    'Erika Von Kleist, alto saxophone | flute',
    'Kurt Bacher, alto saxophone',
    'Sharel Cassity, alto saxophone | clarinet | flute',
    'Anat Cohen, clarinet | tenor saxophone',
    'Dan Block, clarinet | tenor saxophone',
    'Julian Lee, clarinet | tenor saxophone',
    'James Burton, trombone',
    'Wayne Goodman, trombone',
    'Eric Miller, trombone',
    'Kalia Vandever, trombone',
    'Mike Rodriguez, trumpet',
    'Bruce Harris, trumpet',
    'Greg Gisbert, lead trumpet',
    'Tanya Darby, lead trumpet',
    'Frank Green, lead trumpet',
    'Liesl Whitaker, lead trumpet',
    'Adam Birnbaum, piano',
    'Helen Sung, piano',
    'Christian Sands, piano',
    'Russell Hall, bass',
    'Rodney Whitaker, bass',
    'Linda Oh, bass',
    'Ulysses Owens, drums',
    'Jerome Jennings, drums',
    'Allison Miller, drums',
    'Jason Marsalis, drums'
]

# END SETUP

# REVIEW

# CHALLENGE 01

index = substitutes.index('Tanya Darby, lead trumpet')

print("\n Challenge 01: Tanya index = {}".format(index)) # str.format()

orchestra.insert(0, substitutes[index])
# orchestra.insert(0, substitutes[substitutes.index('Tanya Darby, lead trumpet')])

print("\n Challenge 01: w/Darby = {}".format(orchestra)) # str.format()

# CHALLENGE 02

irby_index = orchestra.index('Sherman Irby, alto saxophone')
cassity_index = substitutes.index('Sharel Cassity, alto saxophone | clarinet | flute')

orchestra[irby_index] = substitutes[cassity_index]
# orchestra[3] = substitutes[4]

print(f"\n Challenge 02: w/Cassity = {orchestra}")

# CHALLENGE 03

sax = ' alto_saxophone,baritone_saxophone,saxophone '

# Triggers an AttributeError: 'list' object has no attribute 'replace'
# saxophones = sax.strip().split(',').replace('_', ' ') # WRONG ORDER

saxophones = sax.strip().replace('_', ' ').split(',') # ORDER MATTERS

print(f"\n Challenge 03: saxophones = {saxophones}")

# DON'T DO THIS

# Triggers an AttributeError: 'str' object has no attribute 'append'
# orchestra.pop().append(substitutes[substitutes.index('Helen Sung, piano')])

# or this

# AttributeError: 'NoneType' object has no attribute 'append'
# orchestra.remove('Dan Nimmer, piano').append(substitutes[substitutes.index('Helen Sung, piano')])

# Remove Nimmer, add Sung
orchestra.pop() # pops the last item off the list (default value is -1)
# orchestra.remove('Dan Nimmer, piano') # alternative

orchestra.append(substitutes[substitutes.index('Helen Sung, piano')])
# orchestra.append(substitutes[-9])

print(f"\n Challenge 03: w/Sung = {orchestra}")


## 2.0 TUPLES

# Wynton Marsalis, Majesty of the Blues (1989)
majesty_blues = (
    'The Majesty Of The Blues (The Puheeman Strut)',
    'Hickory Dickory Dock',
    'The Death Of Jazz',
    'Premature Autopsies (Sermon)',
    'Oh, But On The Third Day (Happy Feet Blues)'
)

sermon = majesty_blues[3]

print(f"\nMajesty of the Blues sermon = {sermon}")


# 3.0 SLICING

# 3.1 slice from index 0 to index n (stride = 1)

# Return first three musicians
musicians = orchestra[:3]

print(f"\n3.1 First 3 musicians = {musicians}")

# 3.2 slice from index -1 to index -n (stride = 1)

# Return last three musicians (negative slicing)
musicians = orchestra[-3:]

print(f"\n3.2 Last 3 musicians = {musicians}")

# 3.3 slice from index n to index n (stride = 1)

# Return all saxophonists
# WARN: recall tha we inserted a lead trumpeter into position 0, so offset idex values by 1.
musicians = orchestra[4:9]

print(f"\n3.3 JLCO saxophonists = {musicians}")

# 3.4 slice from index -n to index -n (stride = 1)

# Return trombonists (negative slicing)
musicians = orchestra[-5:-2]

print(f"\n3.4 JLCO trombonists = {musicians}")

# 3.5 slice from index n to index n. Set stride = 2.

# Return every other JLCO substitute musician, starting at index 0.
musicians = substitutes[0::2]

print(f"\n3.5 Every other substitute musician = {musicians}")

# 3.6 slice from index -n to index -n. Set stride = 2.

# Return every other substitute bassist, pianist, and drummer, starting from the end of
# the list in reverse order.
musicians = substitutes[-10::2]

print(f"\n3.6 Every other substitute bassist, pianist, and drummer = {musicians}")

# 3.7 slice from index 0 to end of list. Set stride = -1 (reverse order)

# Return JLCO musicians in reverse order
musicians = orchestra[::-1]

print(f"\n3.7 JLCO musicians in reverse order = {musicians}")

# 3.8 slice from index n to index n. Set stride = -1 (reverse order).

# Return substitute clarinets in reverse order.
musicians = substitutes[5:8:-1] # does not work
# musicians = substitutes[-23:-20:-1] # does not work

print(f"\n3.8 Substitute clarinetists in reverse order = {musicians}")

musicians = substitutes[5:8]
musicians = musicians[::-1]

print(f"\n3.8 Substitute clarinetists in reverse order = {musicians}")


# 4.0 SLICE ASSIGNMENT

# 4.1 Replace part of a list (length remains unchanged)

# Replace JLCO trombonists (n=3) with first three substitute trombonists (same size)
# Replace Crenshaw, Gardner, and Mason with Burton, Goodman, and Miller.
orchestra[-5:-2] = substitutes[8:11]

print(f"\n3.9 Replace JLCO trombonists with substitutes = {orchestra}")

# 4.2 Replace part of a list (length changes)

# Replace JLCO trumpeters with all substitute trumpeters including leads
orchestra[:4] = substitutes[12:18]

print(f"\n3.10 Replace JLCO trumpeters with substitute trumpeters = {orchestra}")


# 5.0 Built-in del() function and slicing

# 5.1 Delete a slice with built-in del() function

# Delete the lead trumpeters we just added.
del(orchestra[2:6])

print(f"\n3.11 Delete lead trumpeters = {orchestra}")


# 6.0 built-in slice() function (out of scope)

musicians = ['Ellis Marsalis', 'Wynton Marsalis', 'Branford Marsalis', 'Delfeayo Marsalis', 'Jason Marsalis']

# slice([start, ]end[, step]) object
s = slice(1, 4, 2)
wynton_delfeayo = musicians[s]

print(f"\n3.12 slice() example = {wynton_delfeayo}")

print('\n') # padding
