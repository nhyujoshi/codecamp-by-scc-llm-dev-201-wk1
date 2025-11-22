"""Assignment Q9 - Sum Numbers in Text

Write a function that takes a string and sums all the numbers found in the text using regex.

Example:
    >>> q9_sum_numbers_in_text("I have 3 apples and 4 oranges")
    7
"""
import re

def q9_sum_numbers_in_text(text):
    """
    Takes a string and sums all the numbers found in the text using regex.
    
    Args:
        text (str): The input text
        
    Returns:
        int: The sum of all numbers found in the text
        
    Example:
        >>> q9_sum_numbers_in_text("I have 3 apples and 4 oranges")
        7
    """
    # Your code here

    # only capture one or more digits in the text 
    number_list = re.findall(r"\d+", text)

    # declare total variable to store the sum
    total = 0

    # iterate loop in number_list with captured numbers, convert into int and add
    for number in number_list:
        total += int(number)

    return total