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

    # declare variables for final result and each word
    result = ""
    current_word = ""

    for char in sentence:
        # add to current word only if character is an alphabet letter
        if char.isalpha():
            current_word += char
        else:
            # if the current word is not empty, add that to the result by reversing and reset current word
            if current_word:
                result += current_word[::-1]
                current_word = ""
            # add non-alphabet characters to result after reversed word is added
            result += char
    
    # for the final word if there is no non-alphabet characters at the end 
    if current_word:
        result += current_word[::-1]
    
    return result