# SI 506 Midterm

def calculate_points_per_game(club):
    """Returns the average number of points earned by a club per game rounded
    to the second decimal place.

    Parameters:
        club (list): club record.

    Returns
        float: average points per game (PPG).
    """
    ppg = (club[3] * 3 + club[4]) / club[2]
    return round(ppg, 2)


def calculate_goals_diff(club):
    """Returns the goal difference (GD) between a club's goals for (GF) and
    goals against (GA) per the following equation: GF - GA = GD.

    Parameters:
        club (list): club record.

    Returns
        int: goal difference (GD).
    """

    return club[6] - club[7]


def calculate_points(club):
    """Returns points (Pts) earned by a club during league plaay. Points are earned as
    follows: 3 points for a win, 1 point for a draw (tie), 0 points for a loss 0.

    Parameters:
        club (list): club record.

    Returns
        int: total points (Pts) earned.
    """

    return club[3] * 3 + club[4]


def get_clubs_by_regions(clubs, regions):
    """Returns a list of nested club records filtered on a passed in list of one
    or more regions. A region/club match is obtained whenever a club's home
    location is found in a passed in region's tuple of city, county, and/or
    state locations.

    Parameters:
        clubs (list): list of club record lists.
        regions (list): list of regions. Each region contains a tuple of
            cities, counties, and/or states.

    Returns
        list: list of filtered club record lists.
    """
    matched_list = []

    for club in clubs:
        for region in regions:
            if club[1] in region[1][:]:
                matched_list.append(club)

    return matched_list


def get_top_club_by_ppg(clubs):
    """Returns a formatted string literal representing the top club(s) in the
    league possessing the highest average points per game (PPG) for the season.

    The f-string format is f"< club name > (< points > PPG)".

    If more than one club shares the top PPG, the function will append each
    additional team to the current f-string using the following format:

    f"< top_club > and < club name > (< points > PPG)".

    Parameters:
        clubs (list): list of club record lists.

    Returns
        str: formatted string literal representing the top team(s) by points by game (PPG).
    """
    top_club = None
    points_per_game = 0.0
    for club in clubs:
        if club[-1] > points_per_game:
            top_club = f"{club[0]} ({club[-1]} PPG)"
            points_per_game = club[-1]
        elif club[-1] == points_per_game:
            top_club = f"{top_club} and {club[0]} ({club[-1]} PPG)"

    return f"{top_club}"

def get_words_with_apostrophes(string):
    """Returns a list of tuples of words that include an apostrophe. Each
    tuple in the returned list includes two items: the zero-based word number
    (e.g., 1st word=0, 2nd word=1, nth word=n-1 in the string) and the word
    itself, as in ( < number >, < word >).

    Parameters:
        string (str): the string containing words to be checked for apostrophes.

    Returns
        list: list of tuples.
    """

    string_split = string.split()

    accumulator = []

    for i, word in enumerate(string_split):
        if word.find("'") > -1:
            accumulator.append((i, word))
    return accumulator



def search_club_names(clubs, search_term):
    """Returns a list of club record lists filtered on a substring found in the
    club name. Function search is case insensitive.

    Parameters:
        clubs (list): list of club record lists.
        search_term (str): possible substring to be located in a club name.

    Returns
        list: list of club record lists.
    """
    matched_clubs  = []
    for club in clubs:
        if club[0].lower().find(search_term.lower()) > -1:
            matched_clubs.append(club)
    return matched_clubs


def main():
    """Program entry point. Controls flow of execution. All function calls must
    be made from main().

    Parameters:
        None

    Returns
        None

    """

    # Data: ['Province', ('City',)],
    regions = [
        ['Liaoning Province', ('Anshan', 'Dalian', 'Fushun', 'Shenyang')],
        ['Jiangsu Province', ('Changzhou', 'Nanjing', 'Suzhou', 'Wuxi')],
        ['Jilan Province', ('Changchun', 'Jilin', 'Siping', 'Yanji')],
        ['Hubei Province', ('Wuhan', 'Xiangyang', 'Yichang', 'Jingzhou')],
        ['Henan Province', ('Anyang', 'Kaifeng', 'Luoyang', 'Zhengzhou')],
        ['Guangdong Province', ('Foshan', 'Guangzhou', 'Meizhou', 'Shenzhen')],
        ['Direct Administration', ('Beijing', 'Shanghai', 'Tianjin', 'Chongqing')]
        ]

    # Chinese Women's Super League, 2019-2020 season
    # Data: 'Club, City, MP, W, D, L, GF, GA' (will add GD and Pts later)
    clubs = [
        ['Beijing BG Phoenix', 'Beijing', 14, 4, 4, 6, 19, 20],
        ['Changchun Zhuoyue', 'Changchun', 14, 7, 3, 4, 26, 27],
        ['Dalian', 'Dalian', 14, 1, 3, 10, 6, 29],
        ['Henan Huishang', 'Luoyang', 14, 3, 3, 8, 20, 27],
        ['Wuhan Jianghan University', 'Wuhan', 14, 6, 1, 7, 16, 21],
        ['Jiangsu Suning', 'Nanjing', 14, 12, 1, 1, 43, 9],
        ['Shanghai Shengli', 'Shanghai', 14, 8, 5, 1, 35, 11],
        ['Meizhou Huijun', 'Meizhou', 14, 4, 2, 8, 15, 36]
        ]

    megan_quote = ("If you miss a shot, you missed it. You can't go back. You can "
    "only try to not make the same mistake twice. I've won a lot in my career, and "
    "I've lost a lot. You take the good with the bad. Also, it's not only about "
    "winning. It's about the process and the journey, the people you're with, "
    "continuing to grow and learn, and getting better every day.")


    # CHALLENGE 01

    club_wdl = clubs[4][3:6]

    # TODO UNCOMMENT print() to check challenge code
    print(f"\n01. Sliced club won, draw, loss list = {club_wdl}")


    # CHALLENGE 02

    search_term = 'university'
    clubs_by_name = search_club_names(clubs=clubs, search_term=search_term)

    # TODO UNCOMMENT print() to check challenge code
    print(f"\n02. Clubs = {clubs_by_name}")


    # CHALLENGE 03

    for club in clubs:
        goals_diff = calculate_goals_diff(club)
        club_points = calculate_points(club)
        club_ppg = calculate_points_per_game(club)
        club.append(goals_diff)
        club.append(club_points)
        club.append(club_ppg)


    # TODO UNCOMMENT print() to check challenge code
    print(f"\n03. Clubs with GD, Pts, and PPG (n={len(clubs)}) = {clubs}")


    # CHALLENGE 04
    henan_hubei = regions[3:5]
    henan_hubei_clubs = get_clubs_by_regions(clubs=clubs, regions=henan_hubei)

    # TODO UNCOMMENT print() to check challenge code
    #print(henan_hubei_clubs)
    print(f"\n04. Henan and Hubei clubs (n={len(henan_hubei_clubs)}) = {henan_hubei_clubs}")


    # CHALLENGE 05

    envelope = [regions[6]]
    #print(envelope)
    direct_admin_clubs = get_clubs_by_regions(regions=envelope, clubs=clubs)

    # TODO UNCOMMENT print() to check challenge code
    print(f"\n05. Direct Admin clubs (n={len(direct_admin_clubs)}) = {direct_admin_clubs}")


    # CHALLENGE 06

    top_direct_admin_club = get_top_club_by_ppg(direct_admin_clubs)

    # TODO UNCOMMENT print() to check challenge code
    print(f"\n06. Top Direct Admin club(s) = {top_direct_admin_club}")


    # CHALLENGE 07

    words = get_words_with_apostrophes(megan_quote) # TODO Call function; assign return value

    # TODO UNCOMMENT print() to check challenge code
    print(f"\n07. Words with apostrophes = {words}")


# Do not modify or delete __name__ check conditional statement.
if __name__ == '__main__':
    main()
