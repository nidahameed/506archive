# SI 506 Lecture 15

## Topics

1. Midterm review challenges

## Data

```python
premier_league = [
        ['Wolverhampton', (15, 14, 9), (51, 40)],
        ['Manchester United', (18, 12, 8), (66, 36)],
        ['Watford', (8, 10, 20), (36, 64)],
        ['Aston Villa', (9, 8, 21), (41, 67)],
        ['Tottenham', (16, 11, 11), (61, 47)],
        ['Newcastle United', (11, 11, 16), (38, 58)],
        ['Brighton & Hove Albion', (9, 14, 15), (39, 54)],
        ['Manchester City', (26, 3, 9), (102, 35)],
        ['Arsenal', (14, 14, 10), (56, 48)],
        ['Sheffield United', (14, 12, 12), (39, 39)],
        ['Bournemouth', (9, 7, 22), (40, 65)],
        ['Crystal Palace', (11, 10, 17), (31, 50)],
        ['Leicester City', (18, 8, 12), (67, 41)],
        ['Norwich City', (5, 6, 27), (26, 75)],
        ['Everton', (13, 10, 15), (44, 56)],
        ['Chelsea', (20, 6, 12), (69, 54)],
        ['Liverpool', (32, 3, 3), (85, 33)],
        ['Burnley', (15, 9, 14), (43, 50)],
        ['Southampton', (15, 7, 16), (51, 60)],
        ['West Ham', (10, 9, 19), (49, 62)]
        ]
```

## Challenge 01

Implement the `get_name` function. Then loop over `premier_league` list in `main()` and return
a list of club names. Assign return value to `club_names`.

## Challenge 02

Loop over the `premier_league` list in `main()` and return a list of string formatted club
names together with win, draw, and loss values per the following format:

`< Club name > record < win >-< draw >-< loss >`

Call `get_name` to retrieve the name and use list indexing to access the record values. Assign
return value to `club_records`.

## Challenge 03

Implement the `calculate_points` function (work with the first tuple: win-draw-loss). Then loop over
the `premier_league` list in `main()`. For each club encountered, calculate the points and then
_replace_ the first tuple with a new tuple that includes the original win, draw, and loss values
plus the new points value. This operation will mutate the `premier_league` list in place.

## Challenge 04

Implement the `calculate_goal_difference` function (work with the second tuple: goals for (GF) -
goals against (GA)). Then loop over the `premier_league` list in `main()`. For each club
encountered, calculate the goal difference and then _replace_ the second tuple with a new tuple
that includes the original GF and GA values plus the calculated goal difference value (GD). This
operation will mutate the `premier_league` list in place.

## Challenge 05

Replace the club names in the `premier_league` list with the official club names in the
`club_details` list.

:bulb: Use a counter, nested loop, and a conditional statement or the built-in `enumerate()`
function, nested loop, and a conditional statement to perform the name replacement.

## Challenge 06

Return a list of clubs with home stadiums that possess a seating capacity __greater than or equal__
to 60,000 fans.

:bulb: Loop over the `premier_league` list and utilize the club's stadium name to look up the
stadium's seating capacity value.

## Challenge 07 (bonus)

Reorder the `premier_league` list so that it matches the
[2019-2020 final standings](https://bit.ly/3nDkdvw) rankings. Clubs are ranked according to the
following criteria:

1. Total points (Pts) earned.
2. If two or teams have earned the same number of points (Pts), attempt to break the tie using goal
   difference (GD). The club with the higher GD gets ranked above the other club(s).
3. If two or more teams have earned same number of points and their GD is equal, attempt to break
   the tie using goals for (GA). The club with the higher GA gets ranked above the other club(s).

:bulb: If a tie between two or more clubs exists after the above three tests are applied, then the
teams are ranked according to head-to-head performance, i.e., the club that scored more goals when
the two clubs met (home and away) earns the higher ranking. We don't have this data today so we
will limit ourselves to tests 1-3.
