# SI 506 Lecture 08: Miles Davis, _Kind of Blue_ (1959)

## CHALLENGE 01

Miles Davis (trumpet) formed his "First Great Quintet" during the summer of 1955. Sonny Rollins
(tenor saxophone) was a founding member but was soon replaced by John Coltrane.

### Task(s)

1. Replace Rollins with 'John Coltrane' in the list `quintet` using the `str.replace()` method to
   replace the musician's name only.

```python
quintet = [
    'Miles Davis - trumpet',
    'Sonny Rollins - tenor saxophone',
    'Paul Chambers - double bass',
    'Philly Joe Jones - drums',
    'Red Garland - piano'
    ]

# TODO replace Rollins wih Coltrane

```

## CHALLENGE 02

1958 saw the quintet morph into a sextet with the addition of Julian "Cannonball" Adderley (alto
saxophone).

### Task(s)

1. Create an empty list named `sextet`. Extend `sextet` with `quintet`.
2. Add 'Julian "Cannonball" Adderley - alto saxophone' to `sextet` in the _last position_.

```python
sextet = []

# TODO built the sextet.

```

## CHALLENGE 03

During 1958 further changes in the lineup occurred. Jimmy Cobb (drums) replaced Jones and
Bill Evans (piano) replaced Garland. Near the end of the year Wynton Kelly (piano) replaced Evans.
Then Bill Evans returned in early 1959 to participate in the group's recording sessions that
culminated in the release by Columbia Records of the Jazz album masterpiece _Kind of Blue_ on 17
August 1959.

### Task(s)

1. Utilize the `list.copy()` method to make a "shallow copy" of the `sextet` list. Name the copy
   `septet`.
2. Use _assignment slicing_ to replace Jones and Garland with the musicians listed in `replacements`.

:exclamation: Ignore Bill Evans' in/out/in relationship with the group and include him in the
`replacements` list along with Cobb and Kelly.

:bulb: A _shallow copy_ of a list constructs a new compound object and then (to the extent possible)
inserts object references found in the original. We will discuss _shallow_ and _deep_ copy
operations later in the course.

```python
sextet = [
    'Miles Davis - trumpet',
    'John Coltrane - tenor saxophone',
    'Paul Chambers - double bass',
    'Philly Joe Jones - drums',
    'Red Garland - piano',
    'Julian "Cannonball" Adderley - alto saxophone'
    ]

replacements = ['Jimmy Cobb', 'Bill Evans', 'Wynton Kelly']

septet = sextet.copy()

# TODO replace Jones and Garland with Cobb, Kelly, and Evans

```

## CHALLENGE 04

Davis's sextet plus Evans formed the personnel for the _Kind of Blue_ recording sessions held
between March and April 1959.

* Miles Davis – trumpet
* Julian "Cannonball" Adderley – alto saxophone
* John Coltrane – tenor saxophone
* Bill Evans – piano
* Wynton Kelly – piano
* Paul Chambers – double bass
* Jimmy Cobb – drums

### Task(s)

1. Match each `septet` musician to their instrument and update any musician strings that lack an
   instrument per the following format with the instrument names converted to __lower case__:

   `'< Musician Name > - < instrument >'`

2. Select the instruments from the `instruments` tuple and use an f-string to construct the string.

```python
instruments = ('Alto Saxophone', 'Double Bass', 'Drums', 'Piano', 'Tenor Saxophone', 'Trumpet')
septet = [
    'Miles Davis - trumpet',
    'John Coltrane - tenor saxophone',
    'Paul Chambers - double bass',
    'Jimmy Cobb',
    'Bill Evans',
    'Wynton Kelly',
    'Julian "Cannonball" Adderley - alto saxophone'
    ]

# TODO add missing instruments
```

## CHALLENGE 05

The musicians assembled for two recording sessions at Columbia Records' 30th Street Studio in New
York City. Five tracks were laid down. The tracks "So What", "Freddie Freeloader", and
"Blue in Green" were recorded on 2 March 1959 while the tracks "All Blues" and "Flamenco Sketches"
were recorded on 22 April 1959.

### Task(s)

1. Assign the first three `tracks` items to `session_one` using slicing.
2. Assign and the remaining two tracks to `session_two` using slicing.

```python
tracks = ('So What', 'Freddie Freeloader', 'Blue in Green', 'All Blues', 'Flamenco Sketches')

session_one = None
session_two = None
```

## CHALLENGE 06

Despite Wynton Kelly replacing Bill Evans on piano in 1958, Kelly's _Kind of Blue_ piano playing
was limited to "Freddie Freeloader" only; Evans handled piano duties on all other tracks.

### Task(s)

1. Assign the track that Kelly played on to the variable `kelly_on_piano`.
2. Assign the tracks that Evans played on to variable `evans_on_piano`.
3. In both cases the value returned by the expression you write _must_ be a `tuple`.

```python
tracks = ('So What', 'Freddie Freeloader', 'Blue in Green', 'All Blues', 'Flamenco Sketches')

kelly_on_piano = None
evans_on_piano = None
```

## CHALLENGE 07

Imagine a hypothetical scenario in which Davis and the Columbia Records engineering team recorded
the tracks in reverse order over the two sessions.

### Task(s)

1. Utilize slicing to reverse the item order in `tracks` and assign the value to the tuple `tracks_reversed`.

```python
tracks_reversed = None
```

## CHALLENGE 08

Let's select the first, third, and fifth tracks in `tracks_reversed` so that we can practice slicing
with a stride value.

### Task(s)

1. Utilize slicing and a stride value to select "Flamenco Sketches", "Blue in Green", and "So What".
2. Assign the slice to a tuple named `odd_num_tracks_reversed`.

```python
odd_num_tracks_reversed = None

```

## CHALLENGE 09

The long playing album (LP) released on 17 August 1959 featured the first three tracks recorded on
2 March on side one and the remaining two tracks recorded on 22 April on side two.

### Task(s)

1. Combine `session_one` and `session_two` track tuples and assign to the variable `album`.

```python3
# TODO assign tuples
album = None
```

## CHALLENGE 10

_Kind of Blue_ track lengths are provided as a string with the following format `minutes:seconds`.
In a couple of weeks you will learn how to process such values efficiently. In the meantime let's
keep it simple and convert the individual track lengths to seconds only so that we can perform three
(3) computations.

### Task(s)

1. Return the minimum track length in seconds and assign the value to `track_len_secs_min`.
2. Return the maximum track length in seconds and assign the value to `track_len_secs_max`.
3. Return the album length in seconds and assign the value to `album_len_secs`.

```python
track_len_secs = [544, 574, 327, 693, 566] # converted to seconds

track_len_secs_min = None
track_len_secs_max = None
album_len_secs = None
```

## CHALLENGE 11

Let's convert the previous min/max track lengths and album length from seconds to minutes. For all
computations use the built-in `round()` function to return a value rounded to two (2) digits after
the decimal point (e.g., 11.55).

### Task(s)

1. Return the minimum track length in minutes and assign to `track_len_mins_min`. Round up to two
   decimal points.
2. Return the maximum track length in minutes and assign to `track_len_mins_max`. Round up to two
   decimal points.
3. Return the album length in minutes and assign to `album_len_mins`. Round up to two decimal points.

```python
track_len_mins_min = None # 5.45 = 5:27
track_len_mins_max = None # 11.55 = 11:33
album_len_mins = None # 45.07 = 45:04*
```

:bulb: The Wikipedia [entry](https://en.wikipedia.org/wiki/Kind_of_Blue) lists the album runtime as
45:44 for the initial release of _Kind of Blue_. I calculate 45:04 based on the individual track
lengths.

| Track | Length |
|:----- | :----: |
| So What | 09:04 |
| Freddie Freeloader | 09:34 |
| Blue in Green | 05:27 |
| All Blues | 11:33 |
| Flamenco Sketches | 09:26 |
| __Total__ | __45:04__ |

## CHALLENGE 12 (chaining indices)

Imagine a more complex data structure named `track_times` comprising a list of tuples. Each tuple
includes the title and length of each track in minutes as items. How would you access the time for
a particular track?

### Task(s)

1. Return the length for the track "All Blues" and assign the value to the variable `all_blues_len`.

```python
track_lengths = [
    ('So What', '9:04'),
    ('Freddie Freeloader', '9:34'),
    ('Blue in Green', '5:27'),
    ('All Blues', '11:33'),
    ('Flamenco Sketches', '9:26')
    ]

all_blues_len = None
```

## CHALLENGE 12 (LOOKING AHEAD)

Next week you will learn how to iterate over a sequence using a `for` loop. In the example below
the indented block of statements inside the `for` loop allows computations to be performed on
individual list elements in a more efficient manner.

Note also the use of the conditional `if` statement which is used to transfer 60 second increments
from the seconds value to the minutes value whenever the seconds value is >= 60 seconds.

### Tasks

1. split the second element in the tuple `track` and assign to the split out string values to
   a new list named `min_sec`.
2. Cast the minute value as an `int` and add it to `min_sec` in the first position. The operration
   is additive in nature. Use the `+=` operator to perform an arithmetic operation (addition).
3. Cast the second value as an `int` and add it to `min_sec` as the second position. The operration
   is additive in nature. Use the `+=` operator to perform an arithmetic operation (addition).
4. if the amount of seconds is >= 60 seconds, add 1 minute to the first element and subtract 60
   seconds from the second element.
5. Print the values converting seconds back to a `str` and padding single digit values with a 0 using
   the `str.zfill()` method.

```python
album_length = [0, 0] # mins, secs
for track in track_lengths:
    min_sec = track[1].split(':') # split str
    album_length[0] += int(min_sec[0]) # assign mins cast as int
    album_length[1] += int(min_sec[1]) # assign secs cast as int

    # Convert secs to mins (transfer)
    if album_length[1] >= 60:
        album_length[1] -= 60 # subtract 60 secs
        album_length[0] += 1 # add 1 min

# Convert album_length[1] to str and then call the zfill() pad single digits with a leading zero.
print(f"\nCHALLENGE 13 Kind of Blue length = {album_length[0]}:{str(album_length[1]).zfill(2)}")
```

## SOURCES

1. _Wikipedia_, ["Miles Davis Quintet"](https://en.wikipedia.org/wiki/Miles_Davis_Quintet)
2. _Wikipedia_, ["Kind of Blue"](https://en.wikipedia.org/wiki/Kind_of_Blue)
3. _Jazzwise.com_, ["Kind of Blue: How Miles Davis made the Greatest Jazz Album in History"](https://www.jazzwise.com/features/article/kind-of-blue-how-miles-davis-made-the-greatest-jazz-album-in-history) (23 Oct 2019)
4. F. Kaplan, _Slate_, ["Kind of Blue, Why the best-selling jazz album of all time is so great."](http://www.slate.com/articles/arts/music_box/2009/08/kind_of_blue.html) (17 Aug 2009)
