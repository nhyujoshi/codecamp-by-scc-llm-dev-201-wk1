"""Assignment Q2 - Common Elements in Lists

Write a function that takes two lists and returns a set of elements that appear in both lists.

- Works for any data type (numbers, strings).
- Handle empty lists gracefully.

Example:
    >>> q2_common_elements_in_lists([1, 2, 3, 4], [3, 4, 5, 6])
    {3, 4}
"""


def q2_common_elements_in_lists(list1, list2):
    """
    Takes two lists and returns a set of elements that appear in both lists.
    
    - Works for any data type (numbers, strings).
    - Handle empty lists gracefully.
    
    Args:
        list1 (list): The first list
        list2 (list): The second list
        
    Returns:
        set: A set of elements that appear in both lists
        
    Example:
        >>> q2_common_elements_in_lists([1, 2, 3, 4], [3, 4, 5, 6])
        {3, 4}
    """
    # Your code here

    # declare empty set to store common elements
    common_elements = set()

    # iterate in list 1, then check if the iteration is present in list 2, only add if true
    for element in list1:
        if element in list2:
            common_elements.add(element)

    return common_elements


