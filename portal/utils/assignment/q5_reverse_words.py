"""Assignment Q5 - Reverse Words

Write a function that takes a sentence and returns a new sentence with each word reversed, 
but the word order remains the same.

- Ignore punctuation.

Example:
    >>> q5_reverse_words("Hello, World!")
    "olleH, dlroW!"
"""


def q5_reverse_words(sentence):
    """
    Takes a sentence and returns a new sentence with each word reversed, 
    but the word order remains the same.
    
    - Ignore punctuation.
    
    Args:
        sentence (str): The input sentence
        
    Returns:
        str: A new sentence with each word reversed
        
    Example:
        >>> q5_reverse_words("Hello, World!")
        "olleH, dlroW!"
    """
    # Your code here
    result = ""
    current_word = ""

    for char in sentence:
        if char.isalpha():
            current_word += char
        else:
            if current_word:
                result += current_word[::-1]
                current_word = ""
            result += char
    
    if current_word:
        result += current_word[::-1]
    
    return result