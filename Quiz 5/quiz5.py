import sys  # for sys.argv


def my_round(n):  # Function to round a number to the nearest integer
    if not isinstance(n, (int,float)):  # If n is not a float or an integer
        raise TypeError('{} must be a float or an integer'.format(n))  # Raise a TypeError that is not in PDF file
    if n % 1 >= 0.5:
        return int(n) + 1
    else:
        return int(n)
    
    
try:  # Try everything in this block
    try:  # Try to get the operands and comparison_data file name from the command line
        operands_file = sys.argv[1]
        comparison_data_file = sys.argv[2]
    except IndexError as e:  # If there is no command line argument referring to the operands file
        print('IndexError: number of input files less then expected.')  # Print an error message
        quit()  

    inv_operands = []  # List of invidual operands

    try:  # Try to open the operands file
        with open(operands_file, 'r') as o:  
            operands = o.readlines()  # Read the lines of the operands file
    except IOError as e:  # If the operands file cannot be opened
        print('IOError: cannot open '+ operands_file)  # Print an error message
        quit()
        
    try:  # Try to open the comparison_data file    
        with open(comparison_data_file, 'r') as c:    
            comparison_data = c.readlines()  # Read the lines of the comparison_data file
            comparison_data = [line.strip('\n') for line in comparison_data]  # Remove the newline character from the end of each line
    except IOError as e:  # If the comparison_data file cannot be opened
        print('IOError: cannot open '+ comparison_data_file)  # Print an error message
        quit()


    counter = 0  # Counter for the number of lines in the operands file        
    for line in operands:  # For each line in the operands file
        line = line.strip('\n')  # Remove the newline character from the end of the line
        split_line = line.split(' ')  # Split the line into a list of strings
        inv_operands.append(split_line)  # Append the list of strings to the list of individual operands
        zero_div = False  # Boolean for whether a ZeroDivisionError has occurred
        kaboom = False  # Boolean for whether a Exception has occurred
        result_temp = []  # List of results for the current line
        
        try:  # Try to convert the operand div to floats
            oper_div = my_round(float(split_line[0]))  # Round the operand div to the nearest integer 
        except ValueError as e:  # If the operand div is cannot be able to turn a float
            print('------------')
            print('Value Error: only numeric input is accepted.')  # Print an error message
            print('Given Input:', line)  # Print the line that caused the error
            counter += 1  # Increment the counter
            continue  # Continue to the next line in the operands file
        except IndexError as e:  # If the operand div is not in the line
            print('------------')
            print('IndexError: number of operands less then expected.')  # Print an error message
            print('Given Input:', line)  # Print the line that caused the error
            counter += 1  # Increment the counter
            continue  # Continue to the next line in the operands file
        except Exception as e:  # If there is an error that is not a ValueError or IndexError
            print('------------')
            print("kaBOOM: run for your life!")  # Print an error message
            counter += 1
            continue
            
        try:
            oper_nondiv = my_round(float(split_line[1]))  # Round the operand nondiv to the nearest integer
        except ValueError as e:
            print('------------')
            print('Value Error: only numeric input is accepted.')
            print('Given Input:', line)
            counter += 1
            continue
        except IndexError as e:
            print('------------')
            print('IndexError: number of operands less then expected.')
            print('Given Input:', line)
            counter += 1
            continue
        except Exception as e:
            print('------------')
            print("kaBOOM: run for your life!")
            counter += 1
            continue
        
        try:
            oper_from = my_round(float(split_line[2]))  # Round the operand from to the nearest integer
        except ValueError as e:
            print('------------')
            print('Value Error: only numeric input is accepted.')
            print('Given Input:', line)
            counter += 1
            continue
        except IndexError as e:
            print('------------')
            print('IndexError: number of operands less then expected.')
            print('Given Input:', line)
            counter += 1
            continue
        except Exception as e:
            print('------------')
            print("kaBOOM: run for your life!")
            counter += 1
            continue
            
        try:    
            oper_to = my_round(float(split_line[3]))  # Round the operand to to the nearest integer
        except ValueError as e:
            print('------------')
            print('Value Error: only numeric input is accepted.')
            print('Given Input:', line)
            counter += 1
            continue
        except IndexError as e:
            print('------------')
            print('IndexError: number of operands less then expected.')
            print('Given Input:', line)
            counter += 1
            continue
        except Exception as e:
            print('------------')
            print("kaBOOM: run for your life!")
            counter += 1
            continue

        
        for i in range(int(oper_from), int(oper_to) + 1):  # For each number in the range of given numbers
            try:  # Try to divide the number by the operand div and check if it is not divisible by the operand nondiv
                if i % oper_div == 0 and i % oper_nondiv != 0:
                    result_temp.append(i)  # Append the number to the list of results
            except ZeroDivisionError as e:  # If the operand div is zero
                print('------------')  
                print("ZeroDivisionError: you can't divide by zero.")  # Print an error message
                print('Given Input:', line)  # Print the line that caused the error
                zero_div = True  # Set the boolean for a ZeroDivisionError to True
                break  # Break out of the for loop
            except Exception as e:
                print('------------')
                print("kaBOOM: run for your life!")
                kaboom = True  # Set the boolean for a Exception to True
                break
            
        if zero_div:  # If a ZeroDivisionError has occurred
            counter += 1  # Increment the counter
            continue  # Continue to the next line in the operands file
        if kaboom:  # If a Exception has occurred
            counter += 1
            continue
        
        result_string = ' '.join(str(x) for x in result_temp)  # Join the list of results into a string
        print('------------')
        print('My results:\t\t',result_string)  # Print the results
        print('Results to compare:\t',comparison_data[counter])  # Print the results to compare
        try:  # Try to assert that the results match the results to compare
            assert result_string == comparison_data[counter]
            print('Goool!!!')  # Print a success message
            counter += 1  # Increment the counter
        except AssertionError as e:  # If the results do not match the results to compare
            print('AssertionError: results don\'t match.')  # Print an error message
            counter += 1  # Increment the counter
        except Exception as e:
            print("kaBOOM: run for your life!")
            counter += 1
            continue

except Exception as e:  # If any other error occurs
    print("------------")
    print("kaBOOM: run for your life!")  # Print an error message
    
finally:  # Print a game over message at the end of the program
    print('\n','˜ Game Over ˜')    
    
# Mert ERGÜN b2220356062