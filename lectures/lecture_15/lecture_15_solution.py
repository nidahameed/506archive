# SI 506 Lecture 15

def calculate_goals_diff(club):
    """Subtract goals for (GF) minus goals against (GA) to determine
    goals difference (GD).

    Parameters:
        club (list): club record

    Returns
        int: goals difference
    """

    return club[2][0] - club[2][1]


def calculate_points(record):
    """Calculate league points per provided club record. Points are earned as follows:
    win 3 points, draw 1 point ,loss 0 points.

    Parameters:
        record (list): Club record (win, loss, draw, goals for and against).

    Returns
        int: total league points earned.
    """

    return record[1][0] * 3 + record[1][1]


def format_name(name, all_caps=False):
    """Trims name string and then converts the first character of each word to upper case
    unless optional all_caps argument is specified as True.
    """

    if all_caps: # truth value
        return name.strip().upper()
    else:
        return name.strip().title()

    return name


def format_standings(standings, include_stats=False):
    """Format standings list as string. Use enumerate()
    index value both to display place. Ties receive the
    same place value.

    Format: "<place>. <club name> (<points>)\n"

    Parameters:
        standings (list): club standings
        include_stats: (bool): include summary statistics (optional)

    Returns:
        str: formatted string representation of list
    """

    string = '\n'
    for i, club in enumerate(standings, 1):
        position = str(i).zfill(2) # pad single digit numbers
        string += f"{position}. {get_name(club)}"

        if include_stats:
            string += f" (Pts: {club[1]}, GD: {club[2]}, GF: {club[3]})"

        string += '\n'

    return string


def get_goals_scored(club):
    """Return goals scored in a season.

    Parameters:
        club (list): club record

    Returns
        int: number of goals scored by club during the season.
    """

    return club[2][0]


def get_name(club):
    """Return club name.

    Parameters:
        club (list): club record

    Returns
        str: name of club
    """

    return club[0]


def get_stadium(club_details):
    """Return stadium and stadium capacity (seating).

    Parameters:
    club_data (list): list of club details lists.

    Returns:
    tuple: stadium name and stadium capacity value
    """

    return club_details[4]


def get_summary_stats(club):
    """Return a tuple representing clubs summary statistics (club name, points,
    goals differential, and goals scored for the season.

    Parameters:
        club (list): club record

    Returns
        tuple: name, points, goals_diff, goals_scored tuple items
    """

    name = get_name(club)
    points = calculate_points(club)
    goals_diff = calculate_goals_diff(club)
    goals_scored = get_goals_scored(club)

    return name, points, goals_diff, goals_scored


def rank_club(standings, club_stats):
    """Update league standings. Teams are ranked by total points, then goal difference,
    and then goals scored. If still equal, teams are deemed to occupy the same position.
    Last place club is appended to list not inserted.

    club_stats = [< name >, < points >, < goals_diff >, < goals_scored >] >.

    Parameters:
        standings (list): current standings
        club (list): club to be inserted/appended to list

    Return:
        list: updated standings
    """

    club_count = len(standings) # upper bound
    club_name, club_points, club_goals_diff, club_goals_scored = club_stats # unpack tuple

    for i in range(club_count):
        standings_points = standings[i][1]
        if club_points > standings_points:
            standings.insert(i, club_stats)
            return standings
        elif club_points == standings_points:
            standings_goal_diff = standings[i][2]
            if club_goals_diff > standings_goal_diff:
                standings.insert(i, club_stats)
                return standings
            elif club_goals_diff == standings_goal_diff:
                if club_goals_scored > standings[i][3]:
                    standings.insert(i, club_stats)
                    return standings
            else:
                standings.insert(i+1, club_stats) # insert after
                return standings
        elif i == club_count - 1:
            standings.append(club_stats) # last place club
        else:
            continue # inclusion of else: continue is optional

    return standings


def main():
    """Program entry point.  Orchestrates program control flow. Generates English Priemer League
    club standings list as determined by total points earned. If tied for points break tie by
    comparing goal differential (for - against) and goals scored for the season.

    Parameters:
        None

    Returns:
        None
    """

    club_details = [
        [
            'Arsenal Football Club',
            ('The Gunners,'),
            'Islington (North London)',
            'Greater London',
            ('Emirates Stadium', 60704)
        ],
        [
            'Aston Villa Football Club',
            ('The Villa', 'The Lions', 'The Claret & Blue Army', 'AVFC'),
            'Aston (Birmingham)',
            'West Midlands',
            ('Villa Park', 42749)
        ],
        [
            'AFC Bournemouth',
            ('The Cherries, Boscombe', 'AFCB'),
            'Bournemouth',
            'South West England',
            ('Dean Court', 11364),
        ],
        [
            'Brighton & Hove Albion Football Club',
            ('The Seagulls', 'Albion', 'BHAFC'),
            'Brighton and Hove',
            'South East England',
            ('Falmer Stadium', 30750)
        ],
        [
            'Burnley Football Club',
            ('The Clarets',),
            'Burnley',
             'North West England',
             ('Tuft Moor', 21944)
        ],
        [
            'Chelsea Football Club',
            ('The Blues', 'The Pensioners', 'CFC', 'CHE'),
            'Fulham (West London)',
            'Greater London',
            ('Stamford Bridge', 40834)
        ],
        [
            'Crystal Palace Football Club',
            ('The Eagles', 'The Glaziers', 'CPFC'),
            'Selhurst (South London)',
            'Greater London',
            ('Selhurst Park', 25486)
        ],
        [
            'Everton Football Club',
            ('The Blues', 'The Toffees'),
            'Liverpool',
            'North West England',
            ('Goodison Park', 39414)
        ],
        [
            'Leicester City Football Club',
            ('The Foxes',),
            'Leicester',
            'East Midlands',
            ('King Power Stadium', 32261)
        ],
        [
            'Liverpool Football Club',
            ('The Reds',),
            'Liverpool',
            'North West England',
            ('Anfield', 53394)
        ],
        [
            'Manchester City Football Club',
            ('City', 'Cityzens', 'Man City', 'The Citizens', 'The Sky Blues', 'MCFC'),
            'Manchester',
            'North West England',
            ('Etihad Stadium', 55017)
        ],
        [
            'Manchester United Football Club',
            ('The Red Devils', 'Man Utd', 'MUFC'),
            'Manchester',
            'North West England',
            ('Old Trafford', 74140)
        ],
        [
            'Newcastle United Football Club',
            ('The Magpies', 'NUFC'),
            'Newcastle-upon-Tyne',
            'North East England',
            ("St James' Park", 52305)
        ],
        [
            'Norwich City Football Club',
            ('The Canaries', 'Yellows', 'City'),
            'Norwich',
            'East of England',
            ('Carrow Road', 27359)
        ],
        [
            'Sheffield United Football Club',
            ('The Blades', 'SUFC'),
            'Sheffield',
            'Yorkshire and the Humber',
            ('Bramall Lane', 32050)
        ],
        [
            'Southampton Football Club',
            ('The Saints',),
            'Southampton',
            'South East England',
            ("St Mary's Stadium", 32,384)
        ],
        [
            'Tottenham Hotspur Football Club',
            ('Spurs', 'The Lilywhites',),
            'Tottenham (London)',
            'Greater London',
            ('Tottenham Hotspur Stadium', 62303)
        ],
        [
            'Watford Football Club',
            ('The Hornets', 'The Golden Boys', 'Yellow Army'),
            'Watford',
            'East of England',
            ('Vicarage Road', 22200)
        ],
        [
            'West Ham United Football Club',
            ('The Irons', 'The Hammers', 'The Academy of Football', 'WHUFC'),
            'Stratford (East London)',
            'Greater London',
            ('London Stadium', 60000)
        ],
        [
            'Wolverhampton Wanderers Football Club',
            ('Wolves', 'The Wanderers'),
            'Wolverhampton',
            'West Midlands',
            ('Molineux Stadium', 32050)
        ]
    ]

    premier_league = [
        ['Wolverhampton', (15, 14, 9), (51, 40), 'Molineux Stadium'],
        ['Manchester United', (18, 12, 8), (66, 36), 'Old Trafford'],
        ['Watford', (8, 10, 20), (36, 64), 'Vicarage Road'],
        ['Aston Villa', (9, 8, 21), (41, 67), 'Villa Park'],
        ['Tottenham', (16, 11, 11), (61, 47), 'Tottenham Hotspur Stadium'],
        ['Newcastle United', (11, 11, 16), (38, 58), "St James' Park"],
        ['Brighton & Hove Albion', (9, 14, 15), (39, 54), 'Falmer Stadium'],
        ['Manchester City', (26, 3, 9), (102, 35), 'Etihad Stadium'],
        ['Arsenal', (14, 14, 10), (56, 48), 'Emirates Stadium'],
        ['Sheffield United', (14, 12, 12), (39, 39), 'Bramall Lane'],
        ['Bournemouth', (9, 7, 22), (40, 65), 'Dean Court'],
        ['Crystal Palace', (11, 10, 17), (31, 50), 'Selhurst Park'],
        ['Leicester City', (18, 8, 12), (67, 41), 'King Power Stadium'],
        ['Norwich City', (5, 6, 27), (26, 75), 'Carrow Road'],
        ['Everton', (13, 10, 15), (44, 56), 'Goodison Park'],
        ['Chelsea', (20, 6, 12), (69, 54), 'Stamford Bridge'],
        ['Liverpool', (32, 3, 3), (85, 33), 'Anfield'],
        ['Burnley', (15, 9, 14), (43, 50), 'Tuft Moor'],
        ['Southampton', (15, 7, 16), (51, 60), "St Mary's Stadium"],
        ['West Ham', (10, 9, 19), (49, 62), 'London Stadium']
        ]


    # CHALLENGE 01

    club_names = []
    for club in premier_league:
        name = get_name(club)
        club_names.append(name)

    print(f"\nChallenge 01: club names = {club_names}")

    # CHALLENGE 02

    club_records = []
    for club in premier_league:
        name = get_name(club)
        win = club[1][0]
        draw = club[1][1]
        loss = club[1][2]

        string = f"{name} {win}-{draw}-{loss}"
        club_records.append(string)

    print(f"\nChallenge 02: club records = {club_records}")


    # CHALLENGE 03

    for club in premier_league:
        points = calculate_points(club)
        club[1] = club[1][0], club[1][1], club[1][2], points # tuple packing
        # club[1] = (club[1]) + (points,) # tuple concatenation

    print(f"\nChallenge 03: club Pts = {premier_league}")


    # CHALLENGE 04

    for club in premier_league:
        goal_diff = calculate_goals_diff(club)
        club[2] = club[2][0], club[2][1], goal_diff # tuple packing
        # club[2] = (club[2]) + (goal_diff,) # tuple concatenation

    print(f"\nChallenge 04: club GD = {premier_league}")


    # CHALLENGE 05

    i = 0
    for club in premier_league:
        for detail in club_details:
            name = get_name(detail)
            if name.lower().find(get_name(club).lower()) > -1:
                premier_league[i][0] = name # string assignment
                break
        i += 1 # increment

    # for i, club in enumerate(premier_league):
    #     for detail in club_details:
    #         name = get_name(detail)
    #         if name.lower().find(get_name(club).lower()) > -1:
    #             premier_league[i][0] = name # string assignment

    print(f"\nChallenge 05: Official club names = {premier_league}")


    # CHALLENGE 06

    large_stadiums = []
    for club in premier_league:
        for detail in club_details:
            stadium = get_stadium(detail)
            if club[-1].lower() == stadium[0].lower() and stadium[1] >= 60000:
                large_stadiums.append(club)
                break

    print(f"\nChallenge 06: Large stadiums = {large_stadiums}")


    # CHALLENGE 07

    # Loop over clubs and calculate points earned and goal differential during season.
    # Get club summary statistics: points, goals differential (for - against), and goals
    # scored to tuple.
    # club_stats = (< name >, < points >, < goals_diff >, < goals_scored >).
    # Then call rank_club() to determine order of final standings.

    standings = [] # accumulator
    for club in premier_league:
        club_stats = get_summary_stats(club)

        if not standings: # i.e., if empty (truth value)
            standings.append(club_stats) # add first club

        # Sort standings
        if club not in standings: # first club already added so ignore
            standings = rank_club(standings, club_stats)

    print(f"\nChallenge 07: Premier League Standings (2019-2020) = {standings}")


    # 4.0 Format output
    string = format_standings(standings)

    print(f"\nChallenge 07 Premier League Standings (2019-2020) {string}")


    # Include summary stats
    string = format_standings(standings, include_stats=True)

    print(f"\nChallenge 07: Premier League Standings (2019-2020) {string}")


if __name__ == '__main__':
    main()
