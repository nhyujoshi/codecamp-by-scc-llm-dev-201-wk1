"""W1D1 Q3 - Top 3 Frequent Words

Return the top 3 most frequent words in a string.

Example:
    >>> q3_top_3_frequent_words("the cat and the dog and the bird")
    [('the', 3), ('and', 2), ('cat', 1)]
"""


def q3_top_3_frequent_words(text):
    """
    Return the top 3 most frequent words in a string.
    
    Args:
        text (str): The input string to analyze
        
    Returns:
        list: A list of tuples containing (word, frequency) for the top 3 most frequent words
        
    Example:
        >>> q3_top_3_frequent_words("the cat and the dog and the bird")
        [('the', 3), ('and', 2), ('cat', 1)]
    """
    # Your code here
    split_text = text.split()
    counted_words = {}

    for word in split_text:
        if word not in counted_words:
            counted_words[word] = 1
        else:
            counted_words[word] += 1
    
    top_list = sorted(counted_words.items(), key = lambda item: item[1], reverse = True)
    return top_list[0:3]
