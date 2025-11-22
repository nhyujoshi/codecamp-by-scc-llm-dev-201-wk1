"""Assignment Q8 - Remove Duplicates

Write a function that takes a list and returns a new list with duplicates removed, 
preserving the original order.

Example:
    >>> q8_remove_duplicates([1, 2, 2, 3, 4, 3, 5])
    [1, 2, 3, 4, 5]
"""


def q8_remove_duplicates(items):
    """
    Takes a list and returns a new list with duplicates removed, 
    preserving the original order.
    
    Args:
        items (list): The input list
        
    Returns:
        list: A new list with duplicates removed, in original order
        
    Example:
        >>> q8_remove_duplicates([1, 2, 2, 3, 4, 3, 5])
        [1, 2, 3, 4, 5]
    """
    # Your code here

    # declare set to store non-duplicate & list to return in original order
    items_set = set()
    items_list = []

    # iterate in items, only add items that are not in the set since set can't contain duplicates
    for item in items:
        if item not in items_set:
            items_set.add(item)
            items_list.append(item)

    return items_list