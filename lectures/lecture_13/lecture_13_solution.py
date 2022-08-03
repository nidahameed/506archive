# SI 506 Lecture 13

def calculate_goals_diff(club):
    """Subtract goals for (GF) minus goals against (GA) to determine
    goals difference (GD).

    Parameters:
        club (list): club record

    Returns
        int: goals difference
    """

    return club[-1][0] - club[-1][1]


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


def get_record(records, name):
    """Return club record filtered on club name.
    Parameters:
        records (list): Club win, loss, draw, and goals for and against record.
        name (str): Name of club.

    Returns:
        list: Club record if located otherwise None.
    """

    for record in records:
        if get_name(record).lower() == name.lower():
            return record


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

    # 1.0 OPTIONAL PARAMETERS

    # Returns club name trimmed with all words capitalized. Optional argument excluded.
    club_name = ' wolverhampton wanderers football club '
    formatted_club_name = format_name(club_name)

    print(f"\n1.0.1 Formatted name = {formatted_club_name}")

    # Returns club name trimmed with all characters converted to upper case.
    club_name = 'west ham united football club '
    formatted_club_name = format_name(club_name, True)

    print(f"\n1.0.2 Formatted name = {formatted_club_name}")

    # Employs keyword argument for passed in optional argument.
    # Hotspur - a rash, impetuous person (archaic).
    club_name = ' tottenham Hotspur football Club'
    formatted_club_name = format_name(club_name, all_caps=True)

    print(f"\n1.0.3 Formatted name = {formatted_club_name}")

    # 2.0 TRUTH VALUE TESTING

    club_names = [] # falsy
    if club_names: # evaluates to False
        print(f"\nclub_names list has {len(club_names)} elements.") # not called
    else:
        print('\nclub_names list is empty.')

    club_names = ['Arsenal', 'Aston Villa'] # truthy
    if club_names: # evaluates to True
        print(f"\nclub_names list has {len(club_names)} elements.") # called
    else:
        print('\nclub_names list is empty.')


    # 3.0 LOOPING WIH RANGE()

    clubs = [
        ['Wolverhampton', (15, 14, 9), (51, 40)],
        ['Arsenal', (14, 14, 10), (56, 48)],
        ['Sheffield United', (14, 12, 12), (39, 39)],
        ['Leicester City', (18, 8, 12), (67, 41)],
        ['Liverpool', (32, 3, 3), (85, 33)]
        ]

    club_nicknames = [
        ['Wolverhampton', 'Wolves'],
        ['Arsenal', 'The Gunners'],
        ['Sheffield United', 'The Blades'],
        ['Leicester City', 'The Foxes'],
        ['Liverpool', 'The Reds']
        ]

    # Insert the nicknames into the clubs list.
    for i in range(len(clubs)):
        clubs[i].insert(1, club_nicknames[i][1])

    print(f"\n3.0 Nicknames added = {clubs}")


    # 2.0 RETRIEVE RECORD, CALCULATE POINTS

    # Retrieve Wolverhampton's 2019-20 Premier League record.
    wolves_record = get_record(premier_league, 'Wolverhampton')

    # Calculate points earned during the season.
    wolves_points = calculate_points(wolves_record)

    print(f"\n2.0 Wolverhampton earned {wolves_points} points (2019-2020)")


    # 3.0 Loop over clubs and calculate points earned and goal differential during season.
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

    print(f"\n3.0 Club standings={standings}")


    # 4.0 Format output
    string = format_standings(standings)

    print(f"\n3.0 English Premier League Standings (2019-2020) {string}")

    # Include summary stats
    string = format_standings(standings, include_stats=True)

    print(f"\n3.0 English Premier League Standings (2019-2020) {string}")


if __name__ == '__main__':
    main()
