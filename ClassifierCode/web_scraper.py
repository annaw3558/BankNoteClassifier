"""This is the web_scraper module.

This module contains two functions for scraping data from a Web-based text file
into lists of tokens (words or numbers):

- get_line_data()
- get_all_data()

Author: R. Linley
Date: 2019-01-06
"""

import urllib.request

def get_line_data(line, separator=None):
    """Converts a line scraped from a web page into a list.

    Parameters:

    - line, a line scraped (read) from a web page. The type is <class 'bytes'>.

    - separator (optional, default value None). If set, becomes the optional
      separator argument to the .split() method to determine where one element
      in the returned list ends and the next begins. If separator is omitted,
      or None, whitespace is used as an elements separator.

    Assumptions:

    - line is of type <class 'bytes'> (a raw line of input from a web page).

    Returned value:

    - A list of non-separator tokens from line, the elements of which are
      numbers if the original tokens appear to be numeric, and strings
      otherwise.      
    """
    decoded = line.decode('utf-8') # Turn line into a str.
    decoded = decoded.rstrip() # Get rid of trailing newline character
    # Allow for whitespace separator (or not)
    if separator is not None:
        lst = decoded.split(separator) # separator is not whitespace
    else:
        lst = decoded.split(); # separator IS whitespace (default)
    # Turn elements that look like numbers into numbers
    for i in range(len(lst)):
        try: # try conversion of the element to an int first...
            lst[i] = int(lst[i])
        except ValueError:
            try: # ... then try conversion to a float...
                lst[i] = float(lst[i])
            except ValueError: # ... then give up (leave element as a str)
                pass
    return lst

def get_all_data(page_stream,separator=None):
    """Converts a web page to a 2-dimensional list of tokens.

    Parameters:
    
    - page_stream is an open connector to a web page

    - separator (optional, default value None). If set, becomes the optional
      separator argument to the .split() method to determine where one element
      in the returned list ends and the next begins. If separator is omitted,
      or None, whitespace is used as an elements separator.

    Returned value:

    - A 2-dimensional list of tokens where each row corresponds to a single
      line from the web page.      
    """
    all_split_lines = []
    for line in page_stream:
        all_split_lines.append(get_line_data(line,separator))
    return all_split_lines

# Test code
if __name__ == '__main__':
    # Test with whitespace separators in data
    page = 'http://research.cs.queensu.ca/home/cords2/bikes.txt'
    stream = urllib.request.urlopen(page)
    print('\n'.join(str(e) for e in get_all_data(stream)))
    # Test with comma separators in data
    page = 'http://research.cs.queensu.ca/home/cords2/marks1.txt'
    stream = urllib.request.urlopen(page)
    print('\n'.join(str(e) for e in get_all_data(stream,',')))
    
