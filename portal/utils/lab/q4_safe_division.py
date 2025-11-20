"""W1D2 Q4 - Safe Division

Safe division function: return None if dividing by zero.

Example:
    >>> q4_safe_division(10, 2)
    5.0
    >>> q4_safe_division(10, 0)
    None
"""


def q4_safe_division(numerator, denominator):
    """
    Safe division function: return None if dividing by zero.
    
    Args:
        numerator (float): The number to be divided
        denominator (float): The number to divide by
        
    Returns:
        float or None: The result of division, or None if denominator is zero
        
    Example:
        >>> q4_safe_division(10, 2)
        5.0
        >>> q4_safe_division(10, 0)
        None
    """
    # Your code here
    if denominator == 0:
        return None
    
    division = numerator/denominator
    return division
