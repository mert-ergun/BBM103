"""
Diamond Printing Program Using Comprehension Method
"""

import sys  # For sys.argv's


def diamond(n):
    """
    Print a diamond of stars with n rows using list comprehension method
    """
    
    # List comprehension for the upper part of the diamond
    upper = [" " * (n-i) + "*" * (2*i-1) for i in range(1, n)]
    
    # List comprehension for the lower part of the diamond
    lower = [" " * (n-i) + "*" * (2*i-1) for i in range(n, 0, -1)]
    
    # Print the diamond
    print("\n".join(upper + lower))


if __name__ == "__main__":  
    diamond(int(sys.argv[1]))  # Call the function with the argument from the command line
    
# Mert ERGÜN b2220356062