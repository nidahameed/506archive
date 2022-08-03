import csv

# SI 506: Lecture 18


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

    with open(filepath, 'r', newline='', encoding='utf-8') as file_obj: # newline is way to ensure it treates every newline properly
        data = [] # local accumulator list
        reader = csv.reader(file_obj, delimiter=delimiter) # call csv reader function and pass it file_obj and delimiter
        # ^object     ^function
        for row in reader: # loop over reader 
            data.append(row) #append each row to accumulator list

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
        if clean:  # if clean is true; by default it is true
            data = []
            for line in file_obj: #loop over all the lines in the file_obj
                # data.append(line) # includes trailing newline '\n'
                data.append(line.strip()) # strips leading/trailing whitespace including '\n'
            return data
        else:
            return file_obj.readlines() # list


def write_csv(filepath, data, headers=None):
    """
    Writes data to a target CSV file. Column headers are written as the first
    row of the CSV file if optional headers are specified.

    Parameters:
        filepath (str): path to target file (if file does not exist it will be created)
        data (list): content to be written to the target file
        headers (list): optional header row.

    Returns:
        None
    """

    with open(filepath, 'w', newline='', encoding='utf-8') as file_obj:
        writer = csv.writer(file_obj)
        if headers: # if we have headers
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
        fieldnames (list): specifies the order in which key-value pairs are written to each row

    Returns:
        None
    """

    with open(filepath, 'w', newline='', encoding='utf-8') as file_obj:
        writer = csv.DictWriter(file_obj, fieldnames=fieldnames)

        writer.writeheader() # first row
        for row in data:
            writer.writerow(row)


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
        if newline: # if newline is true
            for line in data:
                file_obj.write(f"{line}\n") # add newline 
        else:
            file_obj.writelines(data) # write sequence to file. writelines takes a sequence


def main():
    """Program entry point.

    Parameters:
        None

    Returns:
        None
    """

    # Filepaths
    lecturers_path = './input/umsi-lecturers.txt'
    faculty_path = './input/umsi-faculty.txt'
    resnick_citations_path = './input/resnick-citations.csv'


    # 1.0 OPEN/CLOSE FILE OBJ

    file_obj = open(lecturers_path) # open function
    data = file_obj.read() # returns a single string # a number of methods available for file_obj
    file_obj.close() # REQUIRED -- terminating connection with the file -- need to do this bc if you don't close you end up tying up resources unnecessarily

    # TODO UNCOMMENT
    print(f"\n1.0 lecturers names .read() (type={type(data)}\n{data}")


    # 1.2.1 READLINE()

    file_obj = open(lecturers_path, 'r') # open
    data = file_obj.readline()
    data += file_obj.readline() # UNCOMMENT: can call n times but not efficient
    data += file_obj.readline() # UNCOMMENT: can call n times but not efficient
    data += file_obj.readline() # UNCOMMENT: can call n times but not efficient
    file_obj.close() # close (REQUIRED)

    # TODO UNCOMMENT
    print(f"\n1.2.1 lecturers names .readline()\n{data}")


    # 1.2.2 READLINES()

    file_obj = open(lecturers_path, 'r') # open
    data = file_obj.readlines() # returns list; elements include trailing '\n'
    file_obj.close() # close (REQUIRED)

    # TODO UNCOMMENT
    print(f"\n1.2.2 lecturers names .readlines() (type={type(data)}\n{data}")

    # TODO UNCOMMENT
    print(f"\n1.2.2 lecturers .readlines(), .join()\n{''.join(data)}") # print string (pretty)


    # 1.2.3 GOTCHA: READ(), READLINES() LIMITTED TO ONE CALL ONLY

    file_obj = open(lecturers_path, 'r') # open
    data = file_obj.read() # does one traversal here
    data_lines = file_obj.readlines() # WARN: does not execute -- you can only call one of them
    file_obj.close() # close (REQUIRED)

    # TODO UNCOMMENT
    print(f"\n1.2.3 data_lines list is empty = {data_lines}\n")


    # 1.3.1 WRITE TO FILE WITH writelines()
    # sequence (i.e. - list of lists)

    file_obj = open(lecturers_path, 'r') # open
    data = file_obj.read() # returns a single multiline string
    file_obj.close() # close (REQUIRED)

    # TODO UNCOMMENT
    print(f"\n1.3.1 lecturers .read()\n{data}")

    # TODO UNCOMMENT WRITE OPERATION
    path = './output/lecturers_path_01.txt' # file does not have to exist beforehand
    file_obj = open(path, 'w') # write mode -- return a file_obj that is ready to handle write operations
    file_obj.writelines(data) #calling writelines and writing the data
    file_obj.close() # close (REQUIRED)


    # 1.3.2 WRITE TO FILE WITH write()

    file_obj = open(lecturers_path, 'r') # open
    data = file_obj.readlines() # returns list; elements include trailing '\n'
    file_obj.close() # close (REQUIRED)

    # TODO UNCOMMENT
    print(f"\n1.3.2 lecturers .readlines() {data}")

    # WRITE FIRST NAMES ONLY (POTENTIAL GOTCHA)
    path = './output/lecturers_path_02.txt'
    file_obj = open(path, 'w')
    for row in data: #loop over data
        file_obj.write(f"{row.split()[0]}\n")
    file_obj.close()


    # 2.0 WITH STATEMENT

    # 2.1 WITH OPEN() STATEMENT -- preferred way to open file and return file_obj

    with open(faculty_path, 'r') as file_obj: # calling built-in open function and assigning return value to file_obj (a variable)
        data = file_obj.readlines() # returns list; elements include trailing '\n'

    # TODO UNCOMMENBT
    print(f"\n2.1 with open() statement = {data[:5]}")


    # 2.2 IMPLEMENT READ_FILE() / WRITE FILE()

    faculty = read_file(faculty_path)
    faculty = read_file(path, clean=False) #keyword arg is explicit but optional

    # TODO UNCOMMENT WRITE OPERATION
    output_path = './output/umsi-faculty-cleaned.txt'
    write_file(output_path, faculty) # return value is None

    # Reverse order: first name last name
    names = []
    for person in faculty:
        split = person.split(', ')
        names.append(f"{split[1]} {split[0]}")

    # TODO UNCOMMENT WRITE OPERATION
    output_path = './output/umsi-faculty-reversed.txt'
    write_file(output_path, names) # return value is None


    # 3.1 CSV READER / WRITER

    # Read CSV file and retrieve data
    resnick_citations = read_csv(resnick_citations_path)

    headers = resnick_citations[0] # header row

    # TODO UNCOMMENT
    print(f"\n3.1 resnick_citation headers = {headers}")

    # TODO UNCOMMENT
    print(f"\n3.1 resnick_citations (n={len(resnick_citations)}) = {resnick_citations[1:3]}")

    # Filter data
    titles = []

    # TODO UNCOMMENT
    for citation in resnick_citations[1:]: # exclude header row
        title = citation[headers.index('Title')].lower().title() # Fix ALL CAPS titles
        year = citation[headers.index('Publication Year')]
        citations = citation[headers.index('Total Citations')]

        record = [title, year, citations] # iterable required when using csv.writer() on each row
        titles.append(record)

    # TODO UNCOMMENT
    print(f"\n3.1 Citations title & year (n={len(titles)})\n{titles[:5]}")


    # TODO UNCOMMENT
    # Write filtered data to a new CSV file
    output_path = './output/resnick-citation-titles_01.csv'
    title_pub_year_headers = ['Title', 'Publication Year', 'Total Citations']
    write_csv(output_path, titles, title_pub_year_headers)


    # 3.2 CSV DICTREADER / DICTWRITER

    # Read CSV file and retrieve data
    resnick_citations = read_csv_into_dicts(resnick_citations_path)

    # TODO UNCOMMENT
    print(f"\n2.5 {resnick_citations[0]}")

    # Filter data
    titles = [] # accumulator list
    for citation in resnick_citations:
        record = {} # empty dict -- will fill with k,v pairs (we only want three here)
        for key in citation.keys(): # loop over each row's keys 
            if key == 'Title': #if key is Title, will make new assignment in which key title will become first of my k,v pairs
                record[key] = citation[key] #value is being drawn from citation
            elif key == 'Publication Year':
                record[key] = citation[key]
            elif key == 'Total Citations':
                record[key] = citation[key]
            elif len(record) == 3: # for efficiency -- once I have three k,v pairs and then stop
                break # limit iterations to absolute minimum
            else:
                continue
        titles.append(record)

    # TODO UNCOMMENT
    print(f"\n3.2 Citations title & year (n={len(titles)})\n{titles[:5]}")

    # TODO UNCOMMENT WRITE OPERATION
    # Write filtered data to a new CSV file
    output_path = './output/resnick-citation-titles_02.csv'
    title_pub_year_headers = ['Title', 'Publication Year', 'Total Citations']
    write_dicts_to_csv(output_path, titles, title_pub_year_headers)

if __name__ == '__main__':
    main()
