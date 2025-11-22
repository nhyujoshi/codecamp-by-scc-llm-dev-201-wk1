"""Assignment Q7 - Extract Hashtags

Write a function that extracts all hashtags from a text string using regex 
(words starting with #).

- Return a list of hashtags without the # symbol.

Example:
    >>> q7_extract_hashtags("Check out #python and #coding!")
    ['python', 'coding']
"""
import re

def q7_extract_hashtags(text):
    """
    Extracts all hashtags from a text string using regex.
    
    - Return a list of hashtags without the # symbol.
    
    Args:
        text (str): The input text
        
    Returns:
        list: A list of hashtags without the # symbol
        
    Example:
        >>> q7_extract_hashtags("Check out #python and #coding!")
        ['python', 'coding']
    """
    # Your code here

    # only capture string starting with # with one or more words
    hashtag_list = re.findall(r"\#\w+", text)

    cleaned_hashtag = []

    # iterate in captured hashtag list, appened the iteration excluding first character
    for hashtag in hashtag_list:
        cleaned_hashtag.append(hashtag[1:])

    return cleaned_hashtag