"""W1D2 Q6 - Is Palindrome

Check if a string is a palindrome.

Example:
    >>> q6_is_palindrome("racecar")
    True
    >>> q6_is_palindrome("hello")
    False
    >>> q6_is_palindrome("A man a plan a canal Panama")
    True
"""


def q6_is_palindrome(text):
    """
    Check if a string is a palindrome.
    
    Args:
        text (str): The string to check
        
    Returns:
        bool: True if the string is a palindrome, False otherwise
        
    Example:
        >>> q6_is_palindrome("racecar")
        True
        >>> q6_is_palindrome("hello")
        False
        >>> q6_is_palindrome("A man a plan a canal Panama")
        True
    """
    # Your code here
    base_text = text.replace(" ", "")
    base_text = base_text.lower()
    reversed_text = base_text[::-1]
    return base_text == reversed_text
