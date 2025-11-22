"""Assignment Q1 - Sentence Word Lengths

Write a function that takes a sentence and returns a dictionary mapping each word to its length.

- Ignore punctuation.
- Treat words case-insensitively.

Example:
    >>> q1_sentence_word_lengths("Hello, World!")
    {'hello': 5, 'world': 5}
"""

import re

def q1_sentence_word_lengths(sentence):
    """
    Takes a sentence and returns a dictionary mapping each word to its length.
    
    - Ignore punctuation.
    - Treat words case-insensitively.
    
    Args:
        sentence (str): The input sentence to analyze
        
    Returns:
        dict: A dictionary where keys are words (lowercase) and values are their lengths
        
    Example:
        >>> q1_sentence_word_lengths("Hello, World!")
        {'hello': 5, 'world': 5}
    """
    # Your code here

    # store a list of lowercased words excluding non-alphabet characters
    words = re.findall(r"[a-zA-Z]+", sentence.lower())
    
    # declare empty dictionary
    word_lengths = {}

    # store iterated word as key and length of that word as value
    for word in words:
        word_lengths[word] = len(word)

    return word_lengths
