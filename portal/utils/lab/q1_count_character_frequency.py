"""W1D1 Q1 - Count Character Frequency

Count the frequency of each character in a string.

Example:
    >>> q1_count_character_frequency("hello")
    {'h': 1, 'e': 1, 'l': 2, 'o': 1}
"""


def q1_count_character_frequency(text):
    """
    Count the frequency of each character in a string.
    
    Args:
        text (str): The input string to analyze
        
    Returns:
        dict: A dictionary where keys are characters and values are their frequencies
        
    Example:
        >>> q1_count_character_frequency("hello")
        {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    """
    frequency = {}
    for char in text:
        frequency[char] = frequency.get(char, 0) + 1
    return frequency
