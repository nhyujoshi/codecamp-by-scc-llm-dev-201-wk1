"""Assignment Q4 - Factorial with Error Handling

Write a function safe_factorial(n) that returns the factorial of n.

- Return None if n is negative or not an integer.

Example:
    >>> q4_safe_factorial(5)
    120
    
    >>> q4_safe_factorial(-5)
    None
"""


def q4_safe_factorial(n):
    """
    Returns the factorial of n.
    
    - Return None if n is negative or not an integer.
    
    Args:
        n: The input number
        
    Returns:
        int or None: The factorial of n, or None if n is invalid
        
    Example:
        >>> q4_safe_factorial(5)
        120
        
        >>> q4_safe_factorial(-5)
        None
    """
    # Your code here

    # check if parameter is not int, is in negative or empty
    if not isinstance(n, int) or n < 0 or not n:
        return None
    
    # declare result as 1 so 0 is not multiplied
    factorial_result = 1
    
    # loop from range of 1 to n+1 and multiply each iteration
    for i in range(1, n+1):
        factorial_result *= i

    return factorial_result