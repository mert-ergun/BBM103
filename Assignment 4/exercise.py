def list_sorter(mylist):
    """
    Returns the max, min and average of a list of numbers
    """
    
    if len(mylist) == 1:  # Base case for my function, when the list has only one element
        return (mylist[0], mylist[0], mylist[0])  # Returns the max, min and average of the list as all the same number
    
    myMax, myMin, myAvg = list_sorter(mylist[1:])  # Recursive call to the function, with the list without the first element
    
    max_num = max(mylist[0], myMax)  # Finds the max of the first element and the max of the rest of the list
    min_num = min(mylist[0], myMin)  # Finds the min of the first element and the min of the rest of the list
    
    avg_num = (myAvg * (len(mylist) - 1) + mylist[0]) / (len(mylist))  # Finds the average of the list
    
    return (max_num, min_num, avg_num)  # Returns the max, min and average of the list


test_list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Test list for testing my function
maxolist1, minolist1, avolist1 = list_sorter(test_list1)  # Calls the function with the test list, and assigns the returned values to variables for printing

test_list2 = [1]  # Test list for testing my function with only one element
maxolist2, minolist2, avolist2 = list_sorter(test_list2)  # Max min and average of the list are all the same number


print("Max of the list is '{}', Min of the list is '{}' and average of the list is '{}'".format(maxolist1, minolist1, avolist1))  # Prints the max, min and average of the list
print("Max of the list is '{}', Min of the list is '{}' and average of the list is '{}'".format(maxolist2, minolist2, avolist2))  # Max min and average of the list with only one element


# Mert ERGÜN b2220356062
