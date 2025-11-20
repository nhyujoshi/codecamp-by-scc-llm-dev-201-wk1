"""W1D2 Q5 - Find Maximum

Find maximum in a list; return None if empty.

Example:
    >>> q5_find_maximum([1, 5, 3, 9, 2])
    9
    >>> q5_find_maximum([])
    None
"""


def q5_find_maximum(numbers):
    """
    Find maximum in a list; return None if empty.
    
    Args:
        numbers (list): A list of numbers
        
    Returns:
        float or None: The maximum value in the list, or None if the list is empty
        
    Example:
        >>> q5_find_maximum([1, 5, 3, 9, 2])
        9
        >>> q5_find_maximum([])
        None
    """
    # Your code here
    if not numbers:
        return None

    max_number = max(numbers) 
    return max_number
