import csv
import os

# SI 506 Lecture 20

class Publication:
    """Representation of a Publication.

    Attributes:
        title (str): title of publication
        authors (str): semi-colon delimited string of authors < last name >, < first name >
        source (str): title of source volume
        year (int): year of publication
        total_citations(int): count of citations

    Methods:
        format_authors: returns formatted authors string
        find_coauthors: retuns list of scholars matched as coauthors
        has_coauthor: returns True if one scholar in a list of scholars is matched as a coauthor
        split_authors_to_dicts: returns a list of author dictionaries
        to_dict: returns a dictionary representation of the object.
    """

    def __init__(self, title, authors, source, year, total_citations): # self -- referencing the instance you created
        """Called after instance is created but before object is returned to the caller.
        Permits initialization of instance variables with passed in argument values.

        Parameters:
            title (str): title of publication
            authors (str): semi-colon delimited string of authors
            source (str): title of source volume
            year (int): year of publication
            total_citations(int): count of citations

        Returns
            None:
        """
        self.title = title
        self.authors = authors
        self.source = source
        self.year = int(year) # cast to int
        self.total_citations = int(total_citations) # cast to int

    def __str__(self):
        """Human-readable representation of the object.

        Parameters:
            None

        Returns:
           str: String representation of the object.
        """

        return f"{self.title} ({self.year})"

    def format_authors(self):
        """Returns a formatted authors string.

        Parameters:
            authors (str): original author string

        Returns:
            str: formatted authors string
        """

        names = None
        for author in self.authors.split('; '):
            name = author.split(', ') # want first and last name so splitting on ,

            if names: #if there is something
                names = f"{names}, {name[1][0]}. {name[0]}" # concatenate
            else: #if there is nothing in names
                names = f"{name[1][0]}. {name[0]}" # first name

        # More complex formatting solution
        # authors = self.authors.split('; ')
        # num_authors = len(authors)
        # for i, author in enumerate(authors):
        #     name = author.split(', ')
        #     if i == 0:
        #         # first author
        #         names = f"{name[1][0]}. {name[0]}"
        #     elif i == num_authors - 1:
        #         # last author
        #         if i == 1:
        #             # 2 authors only
        #             names = f"{names} and {name[1][0]}. {name[0]}"
        #         else:
        #             # n authors
        #             names = f"{names}, and {name[1][0]}. {name[0]}"
        #     else:
        #         # other authors
        #         names = f"{names}, {name[1][0]}. {name[0]}"

        return names

    def find_coauthors(self, scholars):
        """Returns a list of coauthors matched on the passed in list of scholars.

        A match is obtained if the surname and first initial of given
        name can be matched.

        WARN: The matching rule is imperfect as it fails to distinguish between authors
        possessing the same surname and first name initial as well as authors whose surnames may
        have changed since a publication was released.

        Parameters:
            scholars (list): list of author strings < "last name, first name/initial(s)" >

        Returns:
            list: list of scholars that matched against the publication's coauthors

        """

        # Get authors
        authors = self.split_authors_to_dicts()

        coauthors = []
        for author in authors:
            author_name = [author['last_name'].lower(), author['first_name'][0].lower()]
            for scholar in scholars:
                scholar_split = scholar.split(', ')
                scholar_name = [scholar_split[0].lower(), scholar_split[1][0].lower()]
                if author_name == scholar_name:
                    coauthors.append(scholar) # cleaner name
                    break

        return coauthors

    def has_coauthor(self, scholars):
        """Returns True if at least one member of a passed in list of scholars is found among
        the publication's authors. A match is obtained if the surname and first initial of given
        name can be matched.

        WARN: The matching rule is imperfect as it fails to distinguish between authors
        possessing the same surname and first name initial as well as authors whose surnames may
        have changed since a publication was released.

        Parameters:
            scholars (list): list of author strings < "last name, first name/initial(s)" >

        Returns:
            bool: True if match is obtained; False otherwise.

        """

        # Get authors
        authors = self.split_authors_to_dicts()

        # Match authors
        for author in authors:
            for scholar in scholars:
                name = scholar.split(', ')
                if (author['last_name'].lower() == name[0].lower() and
                    author['first_name'][0].lower() == name[1][0].lower()):
                    return True
        return False

    def split_authors_to_dicts(self):
        """Returns a list of author dictionaries derived from the original authors
        string.

        Parameters:
            None

        Returns:
            list: sequence of author dictionaries
        """

        names = []
        for author in self.authors.split('; '):
            name = author.split(', ')
            names.append({'first_name': name[1], 'last_name': name[0]}) # dict literal

        return names

    def to_dict(self):
        """Return a dictionary representation of the object.

        Parameters:
            None

        Returns:
            dict: Dictionary representation of the object.
        """

        return {
            'title' : self.title,
            'author' : self.authors,
            'year' : self.year
        }


def get_most_cited_pubs(publications):
    """Return list of one or more publications with the highest citation count. Handles ties.

    Parameters:
        publications (list): nested list of publication objects

    Returns:
        list: publication(s) with highest citation count.
    """

    prev_count = 0
    most_cited = []

    for publication in publications:
        count = publication.total_citations
        if count > prev_count:
            most_cited.clear() # remove pub(s) with prev highest count
            most_cited.append(publication)
            prev_count = count
        elif count == prev_count:
            most_cited.append(publication)
        else:
            continue

    return most_cited


def get_scholars(publications):
    """Returns list of publication authors filtered on last name and first initial
    of given name. Employing separate < filter > list permits matching on all
    caps names as well.

    Parameters:
        publications (list): list of Publictation objects

    Returns:
        list: filtered list of names
    """

    filter = []
    scholars = []
    for publication in publications:
        authors = publication.authors
        for author in authors.split('; '):
            name_split = author.split(', ')
            name = [name_split[0].lower(), name_split[1][0].lower()] # last name, initial
            if name not in filter:
                filter.append(name)
                scholars.append(author)

    return scholars


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
                data.append(line.strip()) # strip leading/trailing whitespace including '\n'
            return data
        else:
            return file_obj.readlines() # list


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
    """Program entry point."""

    # 0.0 FILE PATHS WITH OS.PATH

    # Absolute path to directory in which *.py is located.
    abs_path = os.path.dirname(os.path.abspath(__file__))
    print(f"\n Absolute directory path = {abs_path}")

    # Current working directory
    cwd = os.getcwd() # WARN: Debugger regards cwd as SI506/ not current lecture_19/
    print(f"\n Current working directory = {cwd}")

    # Construct macOS and Windows friendly paths
    faculty_path = os.path.join(abs_path, 'input', 'umsi-faculty.txt')
    publ_path = os.path.join(abs_path, 'input', 'resnick-publications.csv')

    print(f"\n umsi-faculty.txt path = {faculty_path}")
    print(f"\n resnick-publications path = {publ_path}")


    # 1.0 CLASS BASICS
    data = read_csv(publ_path)
    headers = data[0]

    # First class instance
    publ_01 = Publication(
        data[1][headers.index('Title')],
        data[1][headers.index('Authors')],
        data[1][headers.index('Source Title')],
        data[1][headers.index('Publication Year')],
        data[1][headers.index('Total Citations')]
        )

    # TODO UNCOMMENT

    print(f"\n1.0 {publ_01}") # __str__() method is called

    print(f"\n1.0 {publ_01.title}") # instance variable is accessed

    print(f"\n1.0 {publ_01.to_dict()}")


    # 2.0 GET PUBLICATION

    # List of Publication objects
    publications = []
    for publ in data[1:]:
        publications.append(
            Publication(
                publ[headers.index('Title')],
                publ[headers.index('Authors')],
                publ[headers.index('Source Title')],
                publ[headers.index('Publication Year')],
                publ[headers.index('Total Citations')]
                )
            )

    # TODO UNCOMMENT

    # Internal id returned
    #print(f"\n1.0 Publication (3 authors) (n={len(publications)}) = {publications[:5]}")

    # __to_str()
    # print(f"\n1.0 Publication (3 authors) (n={len(publications)}) = {publications[0]}")
    # print(f"\n1.0 Publication (2 authors) (n={len(publications)}) = {publications[16]}")

    # to_dict()
    # print(f"\n1.0 Publication (3 authors) (n={len(publications)}) = {publications[0].to_dict()}")


    # CHALLENGE 01
    # TOTAL CITATIONS

    # TODO UNCOMMENT
    # most_cited_publ = get_most_cited_pubs(publications) # returns list

    # TODO UNCOMMENT LOOP
    # print(f"\nChallenge 01: Most citations (n={len(most_cited_publ)})")
    # for publ in most_cited_publ:
    #     print(f"{publ.format_authors()}, {publ.title}, {publ.source} ({publ.year}) citations = {publ.total_citations}")


    # CHALLENGE 02
    # GET ALL COAUTHORS, WRITE TO FILE (filter out dups)

    # TODO UNCOMMENT
    # scholars = get_scholars(publications)

    # TODO UNCOMMENT
    # print(f"\nChallenge 02: Scholars = {scholars}")

    # BONUS: lambda sort (anon function)
    # Sort case insensitive otherwise ALL CAPS names sorted ahead of mixed case names

    # TODO UNCOMMENT SORT
    # scholars.sort(key=lambda x: (x[0].lower(), x[1].lower()))
    # scholars.sort(key=lambda x: (x[0], x[1])) # WARN: all caps names sorted ahead of mixed case names

    # Write to file

    # TODO UNCOMMENT
    # output_path = os.path.join(abs_path, 'output', 'scholars.txt')
    # write_file(output_path, scholars)


    # CHALLENGE 03
    # HAS UMSI AUTHOR

    faculty = read_file(faculty_path)

    # Filter out Paul
    ignore = ['Resnick, Paul'] # could add other faculty
    # ignore = ['Resnick, Paul', 'Lampe, Cliff'] # could add other faculty

    # Filter out ignored author(s)
    for member in faculty:
        if member in ignore:
           faculty.remove(member)

    # TODO UNCOMMENT LOOP
    umsi_coauthored_publications = [] #accumulator list
    for publication in publications: # loop over publications
        if publication.has_coauthor(faculty): # calling the method
           umsi_coauthored_publications.append(publication.to_dict())

    # Write to file

    # TODO UNCOMMENT
    output_path = os.path.join(abs_path, 'output', 'umsi_coauthored_publications.csv')
    headers = umsi_coauthored_publications[0].keys()
    write_dicts_to_csv(output_path, umsi_coauthored_publications, headers)

    # TODO UNCOMMENT
    #Write to screen
    umsi_coauthor_percent = round((len(umsi_coauthored_publications) / len(publications)) * 100, 2)
    print(f"\nChallenge 03: UMSI co-author count = {len(umsi_coauthored_publications)} ({umsi_coauthor_percent}%)")


    # CHALLENGE 04
    # GET UMSI COAUTHORS

    umsi_coauthors = []

    # TODO UNCOMMENT LOOP
    # for publication in publications:
    #     if publication.has_coauthor(faculty):
    #         coauthors = publication.find_coauthors(faculty)
    #         for coauthor in coauthors:
    #             if coauthor not in umsi_coauthors:
    #                 umsi_coauthors.append(coauthor)

    # TODO UNCOMMENT
    # BONUS: lambda sort (anon function)
    # umsi_coauthors.sort(key=lambda x: (x[0].lower(), x[1].lower()))

    # TODO UNCOMMENT
    # Write to file
    # output_path = os.path.join(abs_path, 'output', 'umsi_coauthors.txt')
    # write_file(output_path, umsi_coauthors)

    # print(f"\nChallenge 04: UMSI faculty co-authors = {umsi_coauthors}")


if __name__ == '__main__':
    main()