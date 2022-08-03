# SI 506: Lecture 18

## TOPICS

1. Opening a file
2. File access modes
3. Read methods (`read()`, `readline()`, `readlines()`)
4. Write methods (`write()`, `writelines()`)
5. Opening a file using the `with` statement
6. Working with CSV files
7. The `csv` module (`csv.reader()`, `csv.writer()`)
8. The `csv` module (`csv.DictReader()`, `csv.DictWriter()`)

## Data

* __resnick-citations.csv__. A comma-separated values (CSV) delimited text file containing
  biblometric data (e.g., citation report) of Professor Paul Resnick's articles, book chapters, and conference papers. Data sourced from the
  [Web of Science](https://search.lib.umich.edu/databases/record/10165?query=web+of+science)
  database and exported into [Endnote](https://endnote.com/). Beyond illustrating this week's topic
  on reading from/writing to files, the data set also helps illustrate UMSI scholarly output,
  scholarly connections within UMSI (e.g., UMSI co-authors) as well as scholarly “influence"
  (citation counts).
* __umsi-faculty.txt__. List of UMSI faculty (last name, first name) as of September 2020.
* __umsi-lecturers.txt__. List of UMSI lecturers (first name, last name) as of September 2020.

## 1.0 Opening a file

You can use the built-in `open()` function to open a file and return a file object or a file handle.
At a minimum you must pass a file path to `open()` as an argument.

The following example illustrates how to open a file in "read" mode, return a file object, call
its `read()` method and return a string of the text file's content.

:exclamation: Note that you `must` call the file object's `close()` method in order to close the connection to the open file. This is a best practice because it both frees up system resources and ensures that any file changes not yet accessible due to buffering are made available.

```python
lecturers_path = './input/umsi-lecturers.txt'

file_obj = open(lecturers_path) # open default "read" mode
data = file_obj.read() # returns a single string
file_obj.close() # close (REQUIRED)

print(f"\n1.0 lecturers names .read() (type={type(data)}\n{data}")
```

:bulb: you can provide a `size` argument of type `int` to the `read()` method in order to limit the number of
bytes to return.

## 1.1 File opening modes

You can specify the _mode_ by which the built-in `open()` function opens a file. For SI 506 only the
"read" (`r`) and "write" (`w`) modes will be employed for opening text, CSV, and JSON files. That
said you should familiarize yourself with the other available modes, noting too that Python can
working with binary content such as images and PDF files as well.

| Character | Description | SI 506 (in scope) |
| :-------- | :---------- | :---------------: |
| __'r'__ | open for reading (default); equivalent to `rt` | __Yes__ |
| __'w'__ | open for writing, truncating the file first | __Yes__ |
| 'a' | open for writing, appending to the end of the file if it exists | No |
| 'x' | open for exclusive creation, failing if the file already exists | No |
| 'b' | binary mode (e.g., image, PDF), contents returned as bytes objects; `rb` = read binary; `wb` = write binary | No |
| 't' | text mode (default) | No |
| '+' | open for updating (reading and writing) | No |

```python
file_obj = open('some path', 'r') # read mode

file_obj = open('some path', 'w') # write mode
```

## 1.2 Read methods (`read()`, `readline()`, `readlines()`)

The example above introduced the `read()` method, which, by default, reads the file object in its entirety and returns as a single string. In contrast, the `readline()` method reads a single line
of text. You can call `readline()` n-times in order to return successive lines of text. You can
also pass a `size` argument of type `int` to the `readline()` method in order to limit the
number of characters to be returned

```python
file_obj = open(lecturers_path, 'r') # open
data = file_obj.readline()
# data += file_obj.readline() # UNCOMMENT: can call n times but not efficient
# data += file_obj.readline() # UNCOMMENT: can call n times but not efficient
# data += file_obj.readline() # UNCOMMENT: can call n times but not efficient
file_obj.close() # close (REQUIRED)

print(f"\n1.2.1 lecturers names .readline()\n{data}")
```

A more useful file object method is `readlines()`. The `readlines()` method returns a list of strings
corresponding to each line in the file object.

:exclamation: Note that each string returned includes a trailing _newline_ escape sequence `\n`.

```python
file_obj = open(lecturers_path, 'r') # open
data = file_obj.readlines() # returns list; elements include trailing '\n'
file_obj.close() # close (REQUIRED)

print(f"\n1.2.2 lecturers names .readlines() (type={type(data)}\n{data}")

print(f"\n1.2.2 lecturers .readlines(), .join()\n{''.join(data)}") # print vertically (pretty)
```

:exclamation: Beware that you can call a file object's `read()` method or `readlines()` method only _once_ after opening a connection to a file.

```python
file_obj = open(lecturers_path, 'r') # open
data = file_obj.read()
data_lines = file_obj.readlines() # WARN: fails to execute
file_obj.close() # close (REQUIRED)

print(f"\n1.2.3 data_lines list is empty = {data_lines}\n")
```

## 1.3 Write methods (`write()`, `writelines()`)

To write data to a file call the built-in `open()` function in "write" (`w`) mode. The file object
that is returned includes both a `write()` method and a `writelines()` method. Call the `write()`
method when working with a string; call the `writelines()` method when working with a sequence.

In the next example a file is opened in "read" (`r`) mode and a multiline string is returned with
each line including a trailing newline character. The multiline string is assigned to the variable `data`. A second file is then opened (a new file) in write (`w`) mode and the multiline string is
passed to the file object's `writelines()` method in order to be written out to the file.

```python
file_obj = open(lecturers_path, 'r') # open
data = file_obj.read() # returns a single multiline string
file_obj.close() # close (REQUIRED)

print(f"\n1.3.1 lecturers .read()\n{data}")

path = './output/lecturers_path_01.txt'
file_obj = open(path, 'w') # write
file_obj.writelines(data)
file_obj.close() # close (REQUIRED)
```

If the contents of a sequence (e.g., a `list`) are to be written to a file, call the built-in
`open()` function in "write" (`w`) mode and then loop over the list and pass each element to the
file object's `write()` method.

:exclamation: Note that the `write()` method does not add a newline escape sequence to the string
passed to it.

```python
file_obj = open(lecturers_path, 'r') # open
data = file_obj.readlines() # returns list; elements include trailing '\n'
file_obj.close() # close (REQUIRED)

print(f"\n1.3.2 lecturers .readlines() {data}")

# Write first names only
path = './output/lecturers_path_02.txt'
file_obj = open(path, 'w')
for row in data:
    # file_obj.write(row.split()[0]) # WARN: lose trailing `n`
    file_obj.write(f"{row.split()[0]}\n") # add `n`
file_obj.close() # close (REQUIRED)
```

## 2.0 Opening a file using the `with` statement

The `with` statement ([PEP 343](https://www.python.org/dev/peps/pep-0343/)) is a control-flow
structure that helps to factor out `try/except` statements as well as ensure that "clean up" actions
such as closing an open file object occurs without the need to call the necessary methods explicitly.

:bulb: Recommended practice is to use the `with` statement when opening a file because the `with`
statements context manager closes the file automatically once all statements within the `with` code
block is executed, even if errors occur.

```python
with open(faculty_path, 'r') as file_obj: # open
    data = file_obj.readlines() # returns list; elements include trailing '\n'

print(f"\n2.1 with open() statement = {data[:5]}")
```

Given that opening files is a common operation let's define a function to perform the task of
opening a file, returning a file object, and retrieving the content as a list and returning it to
the caller. Let's also define an optional parameter named `clean` that determines whether or not
individual lines in the file object are returned "as is" or are stripped of leading/trailing
whitespace as well as the newline escape sequence `\n` removed.

```python
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
        else:
            return file_obj.readlines() # list
```

Similarly, we can define a function to write content to a file. The function includes an optional parameter named `newline` to control whether or not a newline escape sequence (`\n`) should be
appended to each string element in the passed in `data` list.

```python
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
```

:bulb: the built-in `open()` function's optional `encoding` parameter specifies the encoding used to _decode_ (when opening the file) or _encode_ (when writing content to a file).
[UTF-8](https://en.wikipedia.org/wiki/UTF-8) is a variable width character encoding that builds on
the older ASCII character coding standard. It uses one to four one-byte (8-bit) code units to
represent characters. UTF-8 is the most common encoding used on the Web.

We can use both these functions in tandem to read in data, transform it in some manner, and then
write the results of the data manipulation process to a target file.

For example, if we needed to change the name order of each faculty member from
`last name, first name` to `first name last name` we could accomplish the task per the following
steps:

1. call the `read_file()` function and pass to it the path to the faculty names file,
2. assign the return value to a variable named `faculty`,
3. loop over the `faculty` list, splitting each name string encountered on the passed in delimiter,
4. construct an f-string that reverses the order of the name elements and assign the expression to
   an accumulator list called `names`.
5. call the `write_file()` function and pass to it the path to the target output file along with the
   `names` list. The `write_file()` function will create a file object and write each string element in the names list to a new file named `umsi-faculty-reversed.txt` located in the `output/` directory.

:bulb: if the specified target file does not exist in the file system (or is located elsewhere),
opening the file in "write" (`w`) mode will create a new file.

```python
faculty = read_file(faculty_path)
# faculty = read_file(path, clean=False) #keyword arg is explicit but optional

# Switch name order to first name last name
names = []
for person in faculty:
    split = person.split(', ')
    names.append(f"{split[1]} {split[0]}")

output_path = './output/umsi-faculty-reversed.txt' # target file
write_file(output_path, names) # return value is None
```

## 3.0 Working with CSV files

A comma-separated values (CSV) file is a common data interchange format used to represent
tabular data. It is delimited text file that utilizes a comma (`,`) typically to separate individual
values. Other delimiters include pipes (`|`) or tabs, though use of the latter is usually referred
to as a tab-delimited values (TSV) file.

Keep in mind the following when working with or creating CSV files:

1. If a value in a CSV file includes a delimiter (e.g., a comma), the value is usually surrounded by
   double quotation marks (`""`).

2. The first row in a CSV file is often a designated "header" row that contains a list of the column
   names (or headers) that describe the following data. This is recommended practice that helps to
   make the CSV file self-documenting. But you need to exclude the row when working with the actual
   data.

3. Occasionally the first character in a CSV file is a
   [byte order mark](https://en.wikipedia.org/wiki/Byte_order_mark) (BOM). You can filter it out by changing the built-in `open()` function's optional encoding value to `utf-8-sig`.

   ```python
   with open("path_to_a_csv_file.csv", encoding="utf-8-sig") as fileobj:
       # Retrieve data
   ```

4. You can save Excel spreadsheets and export Google sheets as CSV files.

5. The VS Code marketplace features an extension called
   [Rainbow CSV](https://marketplace.visualstudio.com/items?itemName=mechatroner.rainbow-csv) that
   you can install in order to make viewing a CSV file a more pleasant experience.

## 3.1 The `csv` module (`csv.reader()`, `csv.writer()`)

The Python Standard library includes a `csv` module that simplifies working with CSV files. In order
to use the `csv` module you must _import_ it into your program. This is done by adding an `import` statement to your code located at the top of your file.

```python
import csv
```

Once imported the `csv` module and its objects and object methods are referenced using dot notation:

```python
reader = csv.reader(fileobj, delimiter=delimiter)
```

To read the contents of a `*.csv` file we can call the `csv.reader()` function, conveniently located
within the function `read_csv()`. The function itself accepts a file path to the CSV file as well as
and optional delimiter if the CSV file is delimited with a character other than a comma such as a
pipe (`|`).

The function uses a `with` statement and the built-in `open()` function to open the file and return
a file object. A `reader` object is then created by calling the `csv.reader()` function and passing to
it the `file_obj` and the `delimiter` as arguments. The reader object is an _iterable_ (e.g.,
has members that can be accessed) and we can loop over it in order to access each "row" element.
Doing so allows us to append each `row` in the `reader` to the `data` list. Once the `for` loop
finishes its work, the `data` list is returned to the caller.

```python
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
```

We can use the `csv.writer()` function to write data to a target CSV file. The function `write_csv()`
accepts as arguments a file path, the data to be written to the file, and an optional headers list
of column name strings.

Similar to `read_csv()` the function uses a `with` statement and the built-in `open()` function to
open the file and return a file object. A `writer` object is then created by calling the
`csv.writer()` function and passing to it the `file_obj` as an argument.

If headers are passed in, a header row is written by calling the `writer.writerow()` method and
passing to it the `headers` list. Then each row in `data` is written to the file. If no headers
are provided the `data` list is passed directly to the `writer.writerows()` method (which accepts a sequence as an argument) and the data is written to the new file by a batch process.

```python
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
        if headers:
            writer.writerow(headers) # add header row
            for row in data:
                writer.writerow(row) # iterable
        else:
            writer.writerows(data) # iterable
```

With these two functions implemented we can read the `resnick-citations.csv` file, manipulate and/or analyze the data returned and write the results of our work to a new CSV file.

If, for example, we want to start exploring the Resnick data, we could do so by writing to a CSV file
the title, publication year, and the total count of citations for each item in the file. We can
accomplish this task in a few lines of code.

:bulb: Given the number of "columns", accessing a value by its index position is sub-optimal. Instead,
leverage the header row and use it to look up values by calling `headers.index()` and passing to it
the column name of the value you want to access.

```python
# Read CSV file and retrieve data
resnick_citations = read_csv(resnick_citations_path)

headers = resnick_citations[0] # header row

# Filter data
titles = []
for citation in resnick_citations[1:]: # exclude header row
    title = citation[headers.index('Title')].lower().title() # Fix ALL CAPS titles (well sorta)
    year = citation[headers.index('Publication Year')]
    citations = citation[headers.index('Total Citations')]

    record = [title, year, citations] # iterable required when using csv.writer() on each row
    titles.append(record)

# Write filtered data to a new CSV file
output_path = './output/resnick-citation-titles_01.csv'
title_pub_year_headers = ['Title', 'Publication Year', 'Total Citations'] # assign headers
write_csv(output_path, titles, title_pub_year_headers)
```

## 3.2 The `csv` module (`csv.DictReader()`, `csv.DictWriter()`)

The `csv` module also provides two classes for _decoding_ CSV row data into dictionaries and
_encoding_ dictionaries into CSV row data.

The `DictReader()` class returns a reader-like object that maps row data to a `dict` whose keys are
provided by the optional `fieldnames` parameter.

```python
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
```

Likewise, the `DictWriter()` class returns a writer-like object that maps dictionaries into row data
using the `fieldnames` parameter to determine the order in which each dictionary's key-value pairs
are written to each row in the target file. The writer includes a `writeheader()` method for writing
the CSV's header row (1st row) based on the passed in `fieldnames` elements and a `writerow()`
method for writing each dictionary's key-value data as CSV row data.

```python
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
```

If we were to repeat the Resnick data exploration example above working with a list of dictionaries rather than a list of lists, we might write our code this way:

```python
# Read CSV file and retrieve data
resnick_citations = read_csv_into_dicts(resnick_citations_path)

# Filter data
titles = []
for citation in resnick_citations:
    record = {}
    for key in citation.keys():
        if key == 'Title':
            record[key] = citation[key]
        elif key == 'Publication Year':
            record[key] = citation[key]
        elif key == 'Total Citations':
            record[key] = citation[key]
        elif len(record) == 3:
            break # limit iterations to absolute minimum
        else:
            continue

    titles.append(record)

# Write filtered data to a new CSV file
output_path = './output/resnick-citation-titles_02.csv'
title_pub_year_headers = ['Title', 'Publication Year', 'Total Citations']
write_dicts_to_csv(output_path, titles, title_pub_year_headers)
```
