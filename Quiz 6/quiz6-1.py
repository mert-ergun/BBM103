"""
Diamond Printing Program Using Recursion
"""

import sys  # For sys.argv's

counter = -1  # Counter for the recursion


def diamond(n):
    """
    Print a diamond of stars with n rows
    """
    
    global counter  # Get the global counter
    
    if n == 0:  # Base case
        return 
    
    if n == 1:  # For the middle part of the diamond
        print("*" * (counter+2))  # Print the middle row
    
    else:  # For the upper and lower parts of the diamond
        print(" " * (n-1) + "*" * (counter+2))  # Print the upper rows
        counter += 2  # Increment the counter by 2 for the next row
        diamond(n-1)  # Recursion for the upper rows
        counter -= 2  # Decrement the counter by 2 for the next row
        print(" " * (n-1) + "*" * (counter+2))  # Print the lower rows

        
if __name__ == "__main__":  
    diamond(int(sys.argv[1]))  # Call the function with the argument from the command line

# Mert ERGÜN b2220356062