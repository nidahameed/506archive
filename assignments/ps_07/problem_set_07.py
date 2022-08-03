#Problem 02
def recieve_treats(trick_or_treaters, candy):
    '''
    Adds the given candy to the treats list of each trick_or_treater

    Parameters:
        trick_or_treaters(dict): a dictionary of trick-or-treaters, candy(str): a string representing a candy

    Returns:
        None
    '''
    for key, val in trick_or_treaters.items():
        trick_or_treaters[key]['treats'].append(candy)


#Problem 03
def sort_candy(candy_list):
    '''
    Uses the types dict to sort the candies in the candy_list by type

    Parameters:
        candy_list(list): a list of strings, each respresenting a different candy

    Returns:
        dict: types
    '''
    #Setup
    types = {
        'chocolate' : [],
        'fruit' : [],
        'other' : []
    }
    #End Setup

    for candy in candy_list:
        if candy == 'hershey bar' or candy == 'snickers':
            types['chocolate'].append(candy)
        elif candy == 'skittles' or candy == 'starburst':
            types['fruit'].append(candy)
        elif candy == 'tootsie roll' or candy == 'candy corn':
            types['other'].append(candy)

    return types

def main():
    """
    Program entry point.  Handles program workflow (or words to that effect).

    Parameters:
        None

    Returns:
        None
    """
    #Problem 01
    brian = {
        'costume' : 'wizard',
        'treats' : []
    }
    patrick = {
        'costume' : 'vampire',
        'treats' : []
    }
    simone = {
        'costume' : 'mummy',
        'treats' : []
    }

    #print(brian)

    friends_dict = {
        'brian' : brian,
        'patrick' : patrick,
        'simone' : simone
    }
    #print(friends_dict)

    friends_dict_items = friends_dict.items()
    #print(friends_dict_items)

    #Problem 02
    #TODO: Use recieve_treats() to add candies to the treats lists of friends_dict
    recieve_treats(trick_or_treaters=friends_dict, candy='skittles')
    recieve_treats(trick_or_treaters=friends_dict, candy='snickers')
    recieve_treats(trick_or_treaters=friends_dict, candy='candy corn')
    print(friends_dict.items())

    #TODO: Add candies to patrick's treats list
    friends_dict['patrick']['treats'].append('hershey bar')
    friends_dict['patrick']['treats'].append('starburst')
    friends_dict['patrick']['treats'].append('tootsie roll')
    print(friends_dict)

    #Problem 03
    patricks_candies_sorted = sort_candy(candy_list=friends_dict['patrick']['treats']) #TODO: Create use sort_candy() to create dictionary
    print(patricks_candies_sorted.items())

    chocolate_candies = patricks_candies_sorted['chocolate'] #TODO: Use patricks_candies_sorted to create list
    print(chocolate_candies)
    fruit_candies = patricks_candies_sorted['fruit'] #TODO: Use patricks_candies_sorted to create list
    print(fruit_candies)
    other_candies = patricks_candies_sorted['other'] #TODO: Use patricks_candies_sorted to create list
    print(other_candies)
    return brian, patrick, simone, friends_dict, friends_dict_items, patricks_candies_sorted, chocolate_candies, fruit_candies, other_candies

#Do not modify or delete this line
brian, patrick, simone, friends_dict, friends_dict_items, patricks_candies_sorted, chocolate_candies, fruit_candies, other_candies = main()

#The code below is how main is traditionally called
# if __name__ == '__main__':
#     main()
