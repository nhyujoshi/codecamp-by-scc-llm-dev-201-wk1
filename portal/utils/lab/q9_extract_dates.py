"""W1D3 Q9 - Extract Dates

Extract dates in DD/MM/YYYY format.

Example:
    >>> q9_extract_dates("Event on 25/12/2024 and 01/01/2025")
    ['25/12/2024', '01/01/2025']
"""

import re


def q9_extract_dates(text):
    """
    Extract dates in DD/MM/YYYY format.
    
    Args:
        text (str): The input string to search for dates
        
    Returns:
        list: A list of all dates in DD/MM/YYYY format
        
    Example:
        >>> q9_extract_dates("Event on 25/12/2024 and 01/01/2025")
        ['25/12/2024', '01/01/2025']
    """
    # Your code here
    pattern = r"\b(?:0[1-9]|[12][0-9]|3[01])\/(?:0[1-9]|1[0-2])\/\d{4}\b"
    # pattern = r"\b\d{2}\/\d{2}\/\d{4}\b"

    date_list = re.findall(pattern, text)
    return date_list
