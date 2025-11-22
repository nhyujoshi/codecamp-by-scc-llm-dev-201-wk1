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
    words = re.findall(r"[a-zA-Z]+", sentence.lower())
    
    word_lengths = {}

    for word in words:
        word_lengths[word] = len(word)

    return word_lengths
