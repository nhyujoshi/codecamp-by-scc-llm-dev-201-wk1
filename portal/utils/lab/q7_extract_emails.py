"""W1D3 Q7 - Extract Emails

Extract all valid email addresses from a string.

Example:
    >>> q7_extract_emails("Contact us at hello@example.com or support@test.org")
    ['hello@example.com', 'support@test.org']
"""

import re


def q7_extract_emails(text):
    """
    Extract all valid email addresses from a string.
    
    Args:
        text (str): The input string to search for emails
        
    Returns:
        list: A list of all valid email addresses found
        
    Example:
        >>> q7_extract_emails("Contact us at hello@example.com or support@test.org")
        ['hello@example.com', 'support@test.org']
    """
    # Your code here
    pattern = r"\w+\@\w+\.\w+"

    email_list = re.findall(pattern, text)
    return email_list
