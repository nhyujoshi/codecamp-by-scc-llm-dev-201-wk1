"""Assignment Q3 - Count Unique Characters

Write a function that takes a string and returns the number of unique characters.

- Ignore spaces and case.

Example:
    >>> q3_count_unique_characters("Hello World")
    8
"""


def q3_count_unique_characters(text):
    """
    Takes a string and returns the number of unique characters.
    
    - Ignore spaces and case.
    
    Args:
        text (str): The input string to analyze
        
    Returns:
        int: The number of unique characters (ignoring spaces and case)
        
    Example:
        >>> q3_count_unique_characters("Hello World")
        8
    """
    # Your code here
    cleaned_text = text.lower().replace(" ","")

    unique_length = len(set(cleaned_text))

    return unique_length
