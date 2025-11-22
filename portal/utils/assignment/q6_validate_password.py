"""Assignment Q6 - Validate Password

Write a function that checks if a password string meets the following conditions:

- At least 8 characters
- At least one uppercase letter
- At least one lowercase letter
- At least one digit
- Return True if valid, False otherwise.

Example:
    >>> q6_validate_password("ValidPass123")
    True
    
    >>> q6_validate_password("weakpass")
    False
"""


def q6_validate_password(password):
    """
    Checks if a password string meets the following conditions:
    
    - At least 8 characters
    - At least one uppercase letter
    - At least one lowercase letter
    - At least one digit
    
    Args:
        password (str): The password string to validate
        
    Returns:
        bool: True if valid, False otherwise
        
    Example:
        >>> q6_validate_password("ValidPass123")
        True
        
        >>> q6_validate_password("weakpass")
        False
    """
    # Your code here
    if len(password) < 8:
        return False
    
    has_upper = False
    has_lower = False
    has_digit = False

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
    
    password_valid = has_upper and has_lower and has_digit

    return password_valid