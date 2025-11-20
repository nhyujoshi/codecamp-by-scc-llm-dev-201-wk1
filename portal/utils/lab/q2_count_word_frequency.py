"""W1D1 Q2 - Count Word Frequency

Count the frequency of each word in a paragraph.

Example:
    >>> q2_count_word_frequency("hello world hello")
    {'hello': 2, 'world': 1}
"""


def q2_count_word_frequency(paragraph):
    """
    Count the frequency of each word in a paragraph.
    
    Args:
        paragraph (str): The input paragraph to analyze
        
    Returns:
        dict: A dictionary where keys are words and values are their frequencies
        
    Example:
        >>> q2_count_word_frequency("hello world hello")
        {'hello': 2, 'world': 1}
    """
    # Your code here
    split_words = paragraph.split()
    counted_words = {}
    for word in split_words:
        if word not in counted_words:
            counted_words[word] = 1
        else:
            counted_words[word] += 1

    return counted_words
