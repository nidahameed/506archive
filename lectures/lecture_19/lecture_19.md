# SI 506: Lecture 19

## Using `os.path` to create paths

The standard library's `os.path` module includes a number of useful functions for constructing pathnames out of strings. The installed `os.path module` is always the `path` module suitable for the operating system Python is running on (e.g., macOS, Windows 10), and therefore usable for local paths.

```python
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
```

:bulb: an alternative library for working with path objects is the
[`pathlib` module](https://realpython.com/python-pathlib/), introduced as part of the Python 3.4 release.

## Data

* __resnick-citations.csv__. A comma-separated values (CSV) delimited text file containing
  biblometric data (e.g., citation report) of Professor Paul Resnick's articles, book chapters, and conference papers. Data sourced from the
  [Web of Science](https://search.lib.umich.edu/databases/record/10165?query=web+of+science)
  database and exported into [Endnote](https://endnote.com/). Beyond illustrating this week's topic
  on reading from/writing to files, the data set also helps illustrate UMSI scholarly output,
  scholarly connections within UMSI (e.g., UMSI co-authors) as well as scholarly “influence"
  (citation counts).
* __umsi-faculty.txt__. List of UMSI faculty (last name, first name) as of September 2020.

## resnick-citations.csv headers

```python
headers = [
    'Title', 'Authors', 'Book Editors', 'Source Title', 'Publication Date', 'Publication Year', 'Volume', 'Issue', 'Part Number', 'Supplement', 'Special Issue', 'Beginning Page', 'Ending Page', 'Article Number', 'DOI', 'Conference Title', 'Conference Date', 'Total Citations', 'Average per Year', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020'
    ]
```

## Challenge 01

__Task__: Find article with highest citation count. Implement `get_most_cited_pubs()` function. Source data is in `resnick-citations.csv`. Call `read_csv()` function in order to retrieve source data represented as a list of lists. Use `os.path` to construct filepaths.

## Challenge 02

__Task__: Return publication counts by year. Implement `get_pub_counts_by_year` function. Source data in `resnick-citations.csv`. Call `read_csv_into_dicts()` function in order to retrieve source data represented as a list of dictionaries. Use `os.path` to construct filepaths. Call `write_dicts_to_csv()` and write counts to the file `pub_counts.csv`.

:bulb: Pass `pub_counts` to `write_dicts_to_csv()` inside a list.

## Challenge 03

__Task__: Return all scholars found in publications (including Prof. Resnick). Implement `get_scholars()` function. Use `os.path` to construct filepaths. Call `write_csv()` function and write scholars to the file `pub_scholars.csv`.

:bulb: As a bonus the `scholars` list will be sorted using an anonymous `lambda` function.

```python
scholars.sort(key=lambda x: (x[0].lower(), x[1].lower()))
```

:exclamation: Note that publications data includes name variations, e.g.,  Resnick, Paul; Resnick, P; RESNICK, P. Note too that a person may be associated with more than one surname, e.g., Yardi, Sarita; Schoenebeck, Sarita Y.

## Challenge 04

__Task__: Filter out duplicates in `pub_scholars.csv`. Loop over `scholars` list and eliminate duplicates by matching on surname and first initial of given name (e.g., Adar, E). Use `os.path` to construct filepaths. Call `write_csv()` function and write scholars to file `pub_scholars_filtered.csv`.

:bulb: work with two lists `filter` and `scholars_filtered`. The first holds a list of names to check against while the second holds the filtered names that will be written to the file.

## Challenge 05

__Task__: Find UMSI faculty coauthors in the `scholars_filtered` list. Implement `match_name()` function. Retrieve the list of UMSI faculty from `umsi-faculty.txt`. Loop over the faculty members and check names against those in the `scholars_filtered` list. Match on surname and first initial of given name (e.g., Adar, E).

Use `os.path` to construct filepaths. Call `write_csv()` function and write scholars to the file `umsi_coauthors.csv`.

:exclamation: current workflow is imperfect: surname changes are ignored (e.g., Yardi,Sarita -> Schoenebeck,Sarita Y.). Moreover, different authors possessing same first and last names are treated as the same person. UMSI non-faculty coauthors are ignored (e.g., Michael Hess).

## Challenge 06

__Task__: Return list of UMSI faculty coauthored publications. Retrieve the list of UMSI faculty coauthors from `umsi_coauthors.csv`. Add `['Yardi', 'Sarita']` to list. Work with `publications` list of dictionaries. Implement `has_umsi_faculty_coauthor()` (calls `match_name()`). Use `os.path` to construct filepaths. Call `write_dicts_to_csv()` and write counts to the file `umsi_coauthored_publications.csv`.
