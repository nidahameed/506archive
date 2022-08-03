# SI 506 Lecture 08

# CHALLENGE 01

quintet = [
    'Miles Davis - trumpet',
    'Sonny Rollins - tenor saxophone',
    'Paul Chambers - double bass',
    'Philly Joe Jones - drums',
    'Red Garland - piano'
    ]

# Replace Sonny Rollins with John Coltrane

quintet[1] = quintet[1].replace('Sonny Rollins', 'John Coltrane')

print(f"\nCHALLENGE 01 quintet = {quintet}")


# CHALLENGE 02

sextet = []
sextet.extend(quintet)
sextet.append('Julian "Cannonball" Adderley - alto saxophone')

# TODO build sextet

print(f"\nCHALLENGE 02 sextet = {sextet}")


# CHALLENGE 03

replacements = ['Jimmy Cobb', 'Bill Evans', 'Wynton Kelly']

septet = sextet.copy()
# septet[-3:-1] =  replacements
septet[3:5] =  replacements


# TODO build septet

print(f"\nCHALLENGE 03 septet = {septet}")


# CHALLENGE 04

instruments = ('Alto Saxophone', 'Double Bass', 'Drums', 'Piano', 'Tenor Saxophone', 'Trumpet')

# Missing instruments: Cobb, Evans, Kelly

# TODO add instruments

print(f"\nCHALLENGE 04 septet w/instruments = {septet}")


# CHALLENGE 05

tracks = ('So What', 'Freddie Freeloader', 'Blue in Green', 'All Blues', 'Flamenco Sketches')

session_one = tracks[:3]
session_two = tracks[3:]

print(f"\nCHALLENGE 05 session one = {session_one}")
print(f"\nCHALLENGE 05 session two = {session_two}")


# CHALLENGE 06

kelly_on_piano = (tracks[-1],)
evans_on_piano = (tracks[0],) + (tracks[2:])

print(f"\nCHALLENGE 06 Kelly on piano = {kelly_on_piano}")
print(f"\nCHALLENGE 06 Evans on piano = {evans_on_piano}")


# CHALLENGE 07

tracks_reversed = None

print(f"\nCHALLENGE 07 tracks reversed = {tracks_reversed}")


# CHALLENGE 08

odd_num_tracks_reversed = None

print(f"\nCHALLENGE 08 odd num tracks reversed = {odd_num_tracks_reversed}")


# CHALLENGE 09

# TODO assign tuples
album = session_one + session_two

print(f"\nCHALLENGE 09 album = {album}")


# CHALLENGE 10

track_len_secs = [544, 574, 327, 693, 566] # converted to seconds

track_len_secs_min = None
track_len_secs_max = None

album_len_secs = None

print(f"\nCHALLENGE 10 track len min (secs) = {track_len_secs_min}")
print(f"\nCHALLENGE 10 track len max (secs) = {track_len_secs_max}")
print(f"\nCHALLENGE 10 album length (secs) = {album_len_secs}")


# CHALLENGE 11

# Wikipedia individual track lengths (original release)
# 43 mins + 124 seconds = 45:04
# Wikipedia article summary lists a runtime of 45:44
album_len_mins = album_len_secs / 60

# UNCOMMENT round()
track_len_mins_min = round(track_len_secs_min / 60, 2)
track_len_mins_max = round(track_len_secs_max / 60, 2)
album_len_mins = round(album_len_secs/ 60, 2)

print(f"\nCHALLENGE 11 track len min (mins) = {track_len_mins_min}")
print(f"\nCHALLENGE 11 track len max (mins) = {track_len_mins_max}")
print(f"\nCHALLENGE 11 album length (mins) = {album_len_mins}")


# CHALLENGE 12

track_lengths = [
    ('So What', '9:04'),
    ('Freddie Freeloader', '9:34'),
    ('Blue in Green', '5:27'),
    ('All Blues', '11:33'),
    ('Flamenco Sketches', '9:26')
    ]

all_blues_len = track_lengths[3][1]

print(f"\nCHALLENGE 12 All Blues length = {all_blues_len}")


# CHALLENGE 13 (LOOKING AHEAD)

album_length = [0, 0] # mins, secs
for track in track_lengths:
    min_sec = track[1].split(':') # split str
    album_length[0] += int(min_sec[0]) # assign mins cast as int
    album_length[1] += int(min_sec[1]) # assign secs cast as int

    # Convert secs to mins (transfer)
    if album_length[1] >= 60:
        album_length[1] -= 60 # subtract 60 secs
        album_length[0] += 1 # add 1 min

# UNCOMMENT
# print(f"\nCHALLENGE 13 Kind of Blue length = {album_length[0]}:{str(album_length[1]).zfill(2)}")
