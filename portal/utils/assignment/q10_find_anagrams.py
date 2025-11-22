"""Assignment Q10 - Find Anagrams

Write a function that finds all anagrams of a given word from a list of words.

An anagram is a word formed by rearranging the letters of another word.

Example:
    >>> q10_find_anagrams("listen", ["silent", "enlist", "hello", "world"])
    ['silent', 'enlist']
"""


def q10_find_anagrams(word, word_list):
    """
    Finds all anagrams of a given word from a list of words.
    
    An anagram is a word formed by rearranging the letters of another word.
    
    Args:
        word (str): The word to find anagrams for
        word_list (list): A list of words to search
        
    Returns:
        list: A list of anagrams found in word_list
        
    Example:
        >>> q10_find_anagrams("listen", ["silent", "enlist", "hello", "world"])
        ['silent', 'enlist']
    """
    # Your code here
    sorted_word = sorted(word)

    anagram_list = []

    for every in word_list:
        if sorted(every) == sorted_word:
            anagram_list.append(word)

    return anagram_list