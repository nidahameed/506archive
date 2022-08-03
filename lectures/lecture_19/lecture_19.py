import csv
import os

# SI 506: Lecture 19

def get_scholars(publications):
    """Return list of scholars retrieved from each publication's list of authors.

    Parameters:
        publications (list): nested list of publications

    Returns:
        list: names of scholars (duplicates may be included)
    """

    pass # TODO Implement


def has_umsi_faculty_coauthor(publication, names, ignore=None):
    """Checks passed in < names > against < publication > author string. Calls match_name()
    function to perform name check. Returns True if a match is obtained. Optional < ignore >
    parameter filters out name of "lead" author.

    Parameters:
        publications (dict): nested list of publications
        names (list): nested list of names
        ignore (str): author to ignore

    Returns:
        bool: True if name match is obtained; otherwise False

    """

    pass # TODO Implement


def get_most_cited_pubs(publications, headers):
    """Return list of one or more publications with the highest citation count. Handles ties.

    Parameters:
        publications (list): nested list of publications
        headers (list): list of column names used to return index of "Total Citations" element

    Returns:
        list: publication(s) with highest citation count.
    """

    prev_count = 0
    most_cited = []
    for publication in publications:
        count = int(publication[headers.index('Total Citations')])
        if count > prev_count:
            most_cited.clear()
            most_cited.append(publication)
            prev_count = count
        elif count == prev_count:
            most_cited.append(publication)
    
    return most_cited


def get_pub_counts_by_year(publications):
    """Returns count of publications by year.

    Parameters:
        publications (list): nested list of publications

    Returns:
        dict: counts by year with each year serving as a key
    """

    pass # TODO Implement


def match_name(name_01, name_02, ignore=None):
    """Compares two passed in names and attempts to match names on surname and first character
    (e.g., initial) of given name. Returns True if match is obtained. Optional < ignore >
    parameter filters out name of "lead" author.

    Parameters:
        name_01 (list): [< surname >, < given name or initial(s) >]
        name_02 (list): [< surname >, < given name or initial(s) >]
        ignore (str): author to ignore

    Returns:
        bool: True if match is obtained; false otherwise.
    """

    if ignore:
        return (
            name_01[0].lower() != ignore.lower() and
            name_01[0].lower() == name_02[0].lower() and
            name_01[1][0].lower() == name_02[1][0].lower()
            )
    else:
        return (
            name_01[0].lower() == name_02[0].lower() and
            name_01[1][0].lower() == name_02[1][0].lower()
            )

    # if ignore and name_01[0].lower() == ignore.lower():
    #     return False
    # else:
    #     return (
    #         name_01[0].lower() == name_02[0].lower() and
    #         name_01[1][0].lower() == name_02[1][0].lower()
    #         )


def read_csv(filepath, delimiter=','):
    """
    Reads a CSV file, parsing row values per the provided delimiter. Returns a list
    of lists, wherein each nested list represents a single row from the input file.

    Parameters:
        filepath (str): The location of the file to read.
        delimiter (str): delimiter that separates the row values

    Returns:
        list: contains nested "row" lists
    """

    with open(filepath, 'r', newline='', encoding='utf-8') as file_obj:
        data = []
        reader = csv.reader(file_obj, delimiter=delimiter)
        for row in reader:
            data.append(row)

        return data


def read_csv_into_dicts(filepath, delimiter=','):
    """Accepts a file path, creates a file object, and returns a list of
    dictionaries that represent the row values using the cvs.DictReader().

    Parameters:
        filepath (str): path to file
        delimiter (str): delimiter that overrides the default delimiter

    Returns:
        list: nested dictionaries representing the file contents
     """

    with open(filepath, 'r', newline='', encoding='utf-8') as file_obj:
        data = []
        reader = csv.DictReader(file_obj, delimiter=delimiter)
        for line in reader:
            data.append(line) # OrderedDict()
            # data.append(dict(line)) # convert OrderedDict() to dict

        return data


def read_file(filepath, clean=True):
    """Read text file line by line. Remove whitespace and trailing newline
    escape character.

    Parameters:
        filepath (str): path to file
        clean (bool): remove white space, newline escape characters

    Returns
        list: list of lines in file
    """

    with open(filepath, 'r', encoding='utf-8') as file_obj:
        if clean:
            data = []
            for line in file_obj:
                # data.append(line) # includes trailing newline '\n'
                data.append(line.strip()) # strip leading/trailing whitespace including '\n'
            return data

            # return [line.strip() for line in file_obj] # list comprehension (single line)
        else:
            return file_obj.readlines() # list


def write_csv(filepath, data, headers=None):
    """
    Writes data to a target CSV file. Column headers are written as the first
    row of the CSV file if optional headers are specified.

    Parameters:
        filepath (str): path to target file (if file does not exist it will be created)
        data (list): content to be written to the target file
        headers (seq): optional header row list or tuple.

    Returns:
        None
    """

    with open(filepath, 'w', newline='', encoding='utf-8') as file_obj:
        writer = csv.writer(file_obj)
        if headers:
            writer.writerow(headers) # add header row
            for row in data:
                writer.writerow(row) # iterable
        else:
            writer.writerows(data) # iterable


def write_dicts_to_csv(filepath, data, fieldnames):
    """
    Writes dictionary data to a target CSV file as row data using the csv.DictWriter().
    The passed in fieldnames list is used by the DictWriter() to determine the order
    in which each dictionary's key-value pairs are written to the row.

    Parameters:
        filepath (str): path to target file (if file does not exist it will be created)
        data (list): dictionary content to be written to the target file
        fieldnames (seq): sequence specifing order in which key-value pairs are written to each row

    Returns:
        None
    """

    with open(filepath, 'w', newline='', encoding='utf-8') as file_obj:
        writer = csv.DictWriter(file_obj, fieldnames=fieldnames)

        writer.writeheader() # first row
        writer.writerows(data)
        # for row in data:
        #     writer.writerow(row)


def write_file(filepath, data, newline=True):
    """Write content to a target file encoded as UTF-8. If optional newline is specified
    append each line with a newline escape sequence (`\n`).

    Parameters:
        filepath (str): path to target file (if file does not exist it will be created)
        data (list): list of strings comprising the content to be written to the target file
        newline (bool): add newline escape sequence to line

    Returns:
        None
    """

    with open(filepath, 'w', encoding='utf-8') as file_obj:
        if newline:
            for line in data:
                file_obj.write(f"{line}\n") # add newline
        else:
            file_obj.writelines(data) # write sequence to file


def main():
    """Program entry point.

    Parameters:
        None

    Returns:
        None
    """

    # FILE PATHS WITH OS.PATH
    # Absolute path to directory in which *.py is located.
    abs_path = os.path.dirname(os.path.abspath(__file__))
    print(f'"\n Absolute directory path = {abs_path}')

    # Current working directory
    cwd = os.getcwd()
    print(f'"\n Current working directory = {cwd}')

    # Construct macOS and Windows friendly paths
    faculty_path = os.path.join(abs_path, 'input', 'umsi-faculty.txt')
    resnick_path = os.path.join(abs_path, 'input', 'resnick-publications.csv')

    print(f"\n umsi-faculty.txt path = {faculty_path}")
    print(f"\n resnick-publications path = {resnick_path}")

    # Filepaths
    # faculty_path = './input/umsi-faculty.txt'
    # resnick_path = './input/resnick-publications.csv'


    # CHALLENGE 01

    # Work with nested lists (values are all strings)
    publications = read_csv(resnick_path)
    headers = publications[0]

    most_cited = get_most_cited_pubs(publications[1:], headers)

    # TODO UNCOMMENT
    total_citations = most_cited[0][headers.index('Total Citations')]
    print(f"\nChallenge 01: Most citations (n={total_citations}) = {most_cited}")


    # CHALLENGE 02

    # TODO UNCOMMENT
    # publications.clear()
    # publications = read_csv_into_dicts(resnick_path)

    # Get counts
    # WARN: publications is a list of dicts (no header element)
    pub_counts = None

    # Write to file
    output_path = os.path.join(abs_path, 'output', 'pub_counts.csv')

    # TODO UNCOMMENT
    # WARN: pass pub_counts in as list element
    # write_dicts_to_csv(output_path, [pub_counts], pub_counts.keys())

    # TODO UNCOMMENT
    # print(f"\nChallenge 02: Publication counts = {pub_counts}")


    # CHALLENGE 03

    scholars = None

    # BONUS: lambda sort (anon function)
    # Sort case insensitive otherwise ALL CAPS names sorted ahead of mixed case names

    # TODO UNCOMMENT
    # scholars.sort(key=lambda x: (x[0].lower(), x[1].lower()))
    # scholars.sort(key=lambda x: (x[0], x[1])) # ALL CAPS names sorted ahead of mixed case names

    # Write to file
    output_path = os.path.join(abs_path, 'output', 'pub_scholars.csv')
    # write_file(output_path, scholars) # this does not work

    # TODO UNCOMMENT
    # write_csv(output_path, scholars, ('last_name', 'first_name'))

    # TODO UNCOMMENT
    # print(f"\nChallenge 03: Scholars = {scholars}")


    # CHALLENGE 04

    filter = [] # filter on [< last name >, < initial >]
    scholars_filtered = []

    # TODO IMPLEMENT LOOP

    # TODO UNCOMMENT
    # print(f"\nChallenge 04: Scholars filtered = {scholars_filtered}")

    # Write to file
    output_path = os.path.join(abs_path, 'output', 'pub_scholars_filtered.csv')
    # write_file(output_path, scholars) # this does not work

    # TODO UNCOMMENT
    # write_csv(output_path, scholars_filtered, ('last_name', 'first_name'))


    # CHALLENGE 05

    # Get UMSI faculty
    umsi_faculty = read_file(faculty_path)

    # Find UMSI faculty coauthors
    umsi_coauthors = []

    # TODO IMPLEMENT LOOP

    # Write to file
    output_path = os.path.join(abs_path, 'output', 'umsi_coauthors.csv')

    # TODO IMPLEMENT LOOP
    # write_csv(output_path, umsi_coauthors, ('last_name', 'first_name'))

    print(f"\nChallenge 05: UMSI faculty co-authors = {umsi_coauthors}")


    # CHALLENGE 06

    # Get coauthors

    # TODO UNCOMMENT
    # input_path = os.path.join(abs_path, 'output', 'umsi_coauthors.csv')
    # umsi_coauthors = read_csv(input_path)
    # umsi_coauthors.append(['Yardi', 'Sarita']) # Add Sarita Yardi

    # TODO UNCOMMENT
    print(f"\nChallenge 06: UMSI coauthors = {umsi_coauthors}")

    # Count publications with a UMSI coauthor (ignore Resnick)
    umsi_coauthored_publications = []

    # TODO IMPLEMENT LOOP

    # Write to file
    output_path = os.path.join(abs_path, 'output', 'umsi_coauthored_publications.csv')

    # TODO UNCOMMENT
    # write_dicts_to_csv(output_path, umsi_coauthored_publications, umsi_coauthored_publications[0].keys())

    # TODO UNCOMMENT
    # umsi_coauthor_percent = round((len(umsi_coauthored_publications) / len(publications)) * 100, 2)
    # print(f"\nChallenge 06: UMSI co-author count = {len(umsi_coauthored_publications)} ({umsi_coauthor_percent}%)")


if __name__ == '__main__':
    main()
