"""W1D3 Q8 - Validate Phone Numbers

Validate phone numbers in XXX-XXX-XXXX format.

Example:
    >>> q8_validate_phone_numbers("Call 123-456-7890 or 987-654-3210")
    ['123-456-7890', '987-654-3210']
"""

import re


def q8_validate_phone_numbers(text):
    """
    Validate phone numbers in XXX-XXX-XXXX format.
    
    Args:
        text (str): The input string to search for phone numbers
        
    Returns:
        list: A list of all valid phone numbers in XXX-XXX-XXXX format
        
    Example:
        >>> q8_validate_phone_numbers("Call 123-456-7890 or 987-654-3210")
        ['123-456-7890', '987-654-3210']
    """
    # Your code here
    pattern = r"\d{3}\-\d{3}\-\d{4}"

    phone_list = re.findall(pattern, text)
    return phone_list
