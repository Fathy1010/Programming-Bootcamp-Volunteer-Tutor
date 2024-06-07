"""
Author: Fathy Abdelshahid
Student ID: 32491328
Date Modified: 2024-06-07
Description: This script contains a function that converts a list of single digits into a single integer by combining them.
"""


def listSumarry(num):
    """
    this is a docstring, which is used as a description to the function
    Converts a list of digits into a single integer.
    
    Parameters:
    num (list): A list of single-digit integers.
    
    Returns:
    int: The combined integer formed by the digits in the list.
    
    """
    
    # first we going to initilise the variables we well use and 
    # establish them to maintian good coding practices we are going
    # to name them a suitable name 
    
    result=0                                      #This will store the final combined number
    placingPoint=1                                # This represents the current place value (units, tens, hundreds, etc.)
    
    # Iterate through the list in reverse order
    for index in reversed(num):     
      result += index * placingPoint              # Add the current digit multiplied by its place value
      placingPoint *= 10                          # Move to the next place value (units to tens, tens to hundreds, etc.)
    return result                                 # Return the final combined number

# Example usage to check if the code runs as expected
myList = [8, 33, 5, 1]
total = listSumarry(myList)
print(total)  # Output should be 8531
