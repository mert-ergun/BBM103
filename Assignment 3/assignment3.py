# Importing sys and os modules for reading the input and output files from the command line.
import sys
import os

# Geting current working directory, input and output file paths from the command line.
current_dir = os.getcwd()
input_file = sys.argv[1]   
input_file_path = os.path.join(current_dir, input_file)
output_file = 'output.txt'
output_file_path = os.path.join(current_dir, output_file)

# Making a list of categories, rows, columns, sold seats, balance of students, full and season tickets. We will use these lists to store the data for later uses.
categories = []
sold_seats = []
rows = dict()
cols = dict()
balance_student = dict()
balance_full = dict()
balance_season = dict()


# This is our write-to-file function. We will use this function to write the output to the output file.
def write_to_file(text):
    with open(output_file_path, 'a') as append:
        append.write(text)
    

# This is our Create Category function. We will use this function to create the categories in tirbunes.
def create_category(line):
    words = line.split()  # Splitting the line into words.
    
    if words[1] in categories:  # Checking if the category is already created.
        write_to_file('Warning: Cannot create the category for the second time. The stadium has already {}\n'.format(words[1]))
        print('Warning: Cannot create the category for the second time. The stadium has already {}'.format(words[1]))
        return
    row, col = words[2].split('x')  # Splitting the rows and columns and assigning them to the row and col variables.
    
    global categoryname
    categoryname = words[1]  # Getting the category name.
    
    categories.append(categoryname)  # Adding the category name to the categories list.
    rows[categoryname] = row  # Adding the number of rows to the rows dictionary.  
    cols[categoryname] = col  # Adding the number of columns to the columns dictionary.
    
    write_to_file("The category '{}' having {} seats has been created\n".format(categoryname, int(row)*int(col)))  # Writing the output to the output file.
    print("The category '{}' having {} seats has been created".format(categoryname, int(row)*int(col)))
    

# This is our sell ticket function. We will use this function to sell the tickets.    
def sell_ticket(line):
    words = line.split() # Splitting the line into words.
    customer = words[1] # Getting the customer name.
    
    global ticket_type 
    ticket_type = words[2] # Getting the ticket type.
    category = words[3] # Getting the category name.
    number_of_seats = len(words)-4 # Getting the number of seats. While using this method, number of seats that entered is not have to just one. It can be more than one.
    seats = []  # Making a list to store the seats.
    
    for i in range(number_of_seats):  
        seats.append(words[i+4])  # Adding the seats to the seats list.
    
    for seat in seats:    
        if '-' in seat:  # Checking if the seat is a range.
            temp_seat = seat  # Making a temporary variable to store the seat.
            temp_category = seat[0]  # Making a temporary variable to store the category name.
            temp_seat = temp_seat[1:]  # Removing the category name from the seat.
            temp_seat = temp_seat.split('-')  # Splitting the seat into two parts.
            counter = 0
            subset_counter = 0
            for seats in range(int(temp_seat[0]), int(temp_seat[1])+1):  # Checking if the seats are available.
                if int(ord(temp_category)) > int(rows[category]) + 65 and int(temp_seat[1]) > int(cols[category]):  # Checking if the category is available.
                    write_to_file("Error: The category '{}' has less rows and columns than the specified index {}\n".format(category, seat))  # Writing the output to the output file.
                    print("Error: The category '{}' has less rows and columns than the specified index {}".format(category, seat))
                    break
                elif int(ord(temp_category)) > int(rows[category]) + 65:
                    write_to_file("Error: The category '{}' has less rows than the specified index {}\n".format(category, seat))  # Writing the output to the output file.
                    print("Error: The category '{}' has less rows than the specified index {}".format(category, seat))
                    break
                elif int(temp_seat[1]) > int(cols[category]):  
                    write_to_file("Error: The category '{}' has less columns than the specified index {}\n".format(category, seat))  # Writing the output to the output file.
                    print("Error: The category '{}' has less columns than the specified index {}".format(category, seat))
                    break
                  
                for sub_seat in sold_seats:
                    if sub_seat.find(temp_category+str(seats)+category) != -1:  # Checking if the seat is already sold.
                        write_to_file("Warning: The seats {} cannot be sold to {} due some of them have already been sold!\n".format(seat, customer))  # Writing the output to the output file.
                        print("Warning: The seats {} cannot be sold to {} due some of them have already been sold!".format(seat, customer))
                        subset_counter += 1
                        break
                if subset_counter == 1:
                    subset_counter = 0
                    break                        
                else:
                    counter += 1
            
            if counter == len(range(int(temp_seat[0]), int(temp_seat[1])+1)):  # If the seats are available, we will sell the seats.
                for going_seats in range(int(temp_seat[0]), int(temp_seat[1])+1):  
                    sold_seats.append((temp_category+str(going_seats)+category+ticket_type))  # Adding the sold seats to the sold seats list.
                    if ticket_type == 'student':  # Checking if the ticket type is student.
                        if category in balance_student:
                            balance_student[category] += 1  # Adding the sold seats to the balance of student tickets.
                        else:
                            balance_student[category] = 1
                    
                    elif ticket_type == 'full':  # Checking if the ticket type is full.
                        if category in balance_full:
                            balance_full[category] += 1  # Adding the sold seats to the balance of full tickets.
                        else:
                            balance_full[category] = 1
                        
                    elif ticket_type == 'season':  # Checking if the ticket type is season.
                        if category in balance_season:
                            balance_season[category] += 1  # Adding the sold seats to the balance of season tickets.
                        else:
                            balance_season[category] = 1
                
                write_to_file("Success: {} has bought {} at {}\n".format(customer, seat, category))  # Writing the output to the output file.
                print("Success: {} has bought {} at {}".format(customer, seat, category))
        
        else:  # If the seat is not a range, we will check if the seat is available.
            for sub_seat in sold_seats:  
                if sub_seat.find(seat+category) != -1:  # Checking if the seat is already sold.
                    write_to_file('Warning: The seat {} cannot be sold to {} since it was already sold!\n'.format(seat, customer))  # Writing the output to the output file.
                    print('Warning: The seat {} cannot be sold to {} since it was already sold!'.format(seat, customer))
                    break                   
            
            if int(ord(seat[0])) > int(rows[category]) + 65 and int(seat[1:]) > int(cols[category]):  # Checking if the category is available.
                write_to_file("Error: The category '{}' has less rows and columns than the specified index {}\n".format(category, seat))  # Writing the output to the output file.
                print("Error: The category '{}' has less rows and columns than the specified index {}".format(category, seat))
            
            elif int(ord(seat[0])) > int(rows[category]) + 65:  # Checking if the category is available.
                write_to_file("Error: The category '{}' has less rows than the specified index {}\n".format(category, seat))  # Writing the output to the output file.
                print("Error: The category '{}' has less rows than the specified index {}".format(category, seat))
            
            elif int(seat[1:]) not in range(1, int(cols[category])+1):  # Checking if the seat is available.
                write_to_file("Error: The category '{}' has less columns than the specified index {}\n".format(category, seat))  # Writing the output to the output file.
                print("Error: The category '{}' has less columns than the specified index {}".format(category, seat))
                continue
            
            else:
                sold_seats.append((seat + category + ticket_type))  # Adding the sold seats to the sold seats list.
                if ticket_type == 'student':  
                    if category in balance_student:
                        balance_student[category] += 1
                    else:
                        balance_student[category] = 1
                
                elif ticket_type == 'full':
                    if category in balance_full:
                        balance_full[category] += 1
                    else:
                        balance_full[category] = 1
                
                elif ticket_type == 'season':
                    if category in balance_season:
                        balance_season[category] += 1
                    else:
                        balance_season[category] = 1
                
                write_to_file("Success: {} has bought {} at {}\n".format(customer, seat, category))
                print("Success: {} has bought {} at {}".format(customer, seat, category))
                continue
    return
    

# This is our cancel ticket function. We will use this function to refund the tickets.    
def cancel_ticket(line):
    words = line.split()  # Splitting the line into words.
    categoryname = words[1]  # Getting the category name.
    number_of_seats = len(words)-2  # Getting the number of seats. While using this method, number of seats that entered is not have to just one. It can be more than one.
    seats = []  # Making a list to store the seats.
    
    for seat in range(number_of_seats):  
        seats.append(words[seat+2])  # Adding the seats to the seats list.
    
    for seat in seats:  
        if int(seat[1:]) not in range(1, int(cols[categoryname])+1):  # Checking if the seat is available.
            write_to_file("Error: The category '{}' has less columns than the specified index {}\n".format(categoryname, seat))  # Writing the output to the output file.
            print("Error: The category '{}' has less columns than the specified index {}".format(categoryname, seat))
        
        else:  # If the seat is available, we will refund the seat.
            for subseat in sold_seats:  
                if subseat.find(seat+categoryname) != -1:  # Checking if the seat is sold.
                    sold_seats.remove(subseat)  # Removing the seat from the sold seats list.
                    if subseat.find('student') != -1:
                        balance_student[categoryname] -= 1  # Removing the seat from the balance of student tickets.
                    
                    elif subseat.find('full') != -1:
                        balance_full[categoryname] -= 1  # Removing the seat from the balance of full tickets.
                    
                    elif subseat.find('season') != -1:
                        balance_season[categoryname] -= 1  # Removing the seat from the balance of season tickets.
                    
                    write_to_file("Success: The seat {} at '{}' has been canceled and now ready to sell again\n".format(seat, categoryname))  # Writing the output to the output file.
                    print("Success: The seat {} at '{}' has been canceled and now ready to sell again".format(seat, categoryname))
                    
                    return                    
            else:  # If the seat is not sold, we will write an error message.
                write_to_file("Error: The seat {} at '{}' has already been free! Nothing to cancel\n".format(seat, categoryname))  # Writing the output to the output file.
                print("Error: The seat {} at '{}' has already been free! Nothing to cancel".format(seat, categoryname))
                

# This is our balance function. We will use this function to get the balance of the sold tickets.
def balance(line):
    words = line.split()  # Splitting the line into words.
    
    categoryname = words[1]  # Getting the category name.
    
    write_to_file("Category report of '{}'\n".format(categoryname))  # Writing the output to the output file.
    print("Category report of '{}'".format(categoryname))
    write_to_file('-'*len("Category report of '{}'\n".format(categoryname))+'\n')  # Sketching a line.
    print('-'*len("Category report of '{}'".format(categoryname)))
    print()
    
    if categoryname in balance_student.keys():  # Checking if the category has student tickets.
        write_to_file("Sum of students = {}, ".format(balance_student[categoryname]))
        print("Sum of students = {}, ".format(balance_student[categoryname]), end='')
    
    else:  # If the category does not have student tickets, we will write 0.
        write_to_file("Sum of students = 0, ")
        print("Sum of students = 0, ", end='')
        balance_student[categoryname] = 0
    
    if categoryname in balance_full.keys():  # Checking if the category has full tickets.
        write_to_file("Sum of full pay = {}, ".format(balance_full[categoryname]))
        print("Sum of full pay = {}, ".format(balance_full[categoryname]), end='')
    
    else:  # If the category does not have full tickets, we will write 0.
        write_to_file("Sum of full pay = 0, ")
        print("Sum of full pay = 0, ", end='')
        balance_full[categoryname] = 0
    
    if categoryname in balance_season.keys():  # Checking if the category has season tickets.
        write_to_file("Sum of season ticket = {}, ".format(balance_season[categoryname]))
        print("Sum of season ticket = {}, ".format(balance_season[categoryname]), end='')
    
    else:  # If the category does not have season tickets, we will write 0.
        write_to_file("Sum of season ticket = 0, ")
        print("Sum of season ticket = 0, ", end='')
        balance_season[categoryname] = 0
    write_to_file("and Revenues = {} Dollars\n".format(balance_student[categoryname]*10 + balance_full[categoryname]*20 + balance_season[categoryname]*250))  # Writing the output to the output file.
    print("and Revenues = {} Dollars".format(balance_student[categoryname]*10 + balance_full[categoryname]*20 + balance_season[categoryname]*250))
        

# This is our show category function. We will use this function to show the category in a visual form.
def show_category(line):
    words = line.split()  # Splitting the line into words.
    categoryname = words[1]  # Getting the category name.
    
    matrix = []  # Making a matrix to store the seats.
    
    write_to_file('Printing category layout of {}\n'.format(categoryname))  # Writing the output to the output file.
    print('Printing category layout of {}'.format(categoryname))
    write_to_file('\n')  # Just a blank line.
    print()
    
    for i in range(int(rows[categoryname])):  # Making the matrix.
        matrix.append(['X'] * int(cols[categoryname]))    
    
    for i in range(int(rows[categoryname])):
        for j in range(int(cols[categoryname])):
            if chr(64+int(rows[categoryname])-i)+str(j)+categoryname+'student' in sold_seats:  # Checking if the seat is sold as student ticket.
                matrix[i][j] = 'S'
    
    for i in range(int(rows[categoryname])):
        for j in range(int(cols[categoryname])):
            if chr(64+int(rows[categoryname])-i)+str(j)+categoryname+'full' in sold_seats:  # Checking if the seat is sold as full ticket.
                matrix[i][j] = 'F'
    
    for i in range(int(rows[categoryname])):
        for j in range(int(cols[categoryname])):
            if chr(64+int(rows[categoryname])-i)+str(j)+categoryname+'season' in sold_seats:  # Checking if the seat is sold as season ticket.
                matrix[i][j] = 'T'    
    
    for i in range(int(rows[categoryname])):  # Printing the matrix.
        write_to_file(chr(64+int(rows[categoryname])-i) + ' ')
        print(chr(64+int(rows[categoryname])-i) + ' ', end='')
        for j in range(int(cols[categoryname])):
            write_to_file(matrix[i][j] + '  ')
            print(matrix[i][j] + '  ', end='')
        write_to_file('\n')
        print()        
    write_to_file('  ')
    print('  ', end='')
    
    for i in range(int(cols[categoryname])):  # Printing the column numbers.
        if i ==9:  # If the column number is 9, we will add one space.
            write_to_file(str(i) + ' ')
            print(str(i) + ' ', end='')
        
        elif len(str(i)) == 1:  # If the column number is one digit, we will add two spaces.
            write_to_file(str(i) + '  ')
            print(str(i) + '  ', end='')
        
        else:  # If the column number is two digit, we will add one space.
            write_to_file(str(i) + ' ')
            print(str(i) + ' ', end='')
    write_to_file('\n')
    print()
        
    
# This part is the main part of the program. We will use this part to read the input file and call the functions.    
with open(input_file_path, 'r') as f:  # Opening the input file.
    for line in f:
        if line.startswith('CREATECATEGORY '):  # Checking if the line starts with 'CREATECATEGORY'.
            # Create Category
            create_category(line)  # Calling the create category function.
        
        if line.startswith('SELLTICKET '):  # Checking if the line starts with 'SELLTICKET'.
            # Sell Ticket
            sell_ticket(line)  # Calling the sell ticket function.
        
        if line.startswith('CANCELTICKET '):  # Checking if the line starts with 'CANCELTICKET'.
            # Cancel Ticket
            cancel_ticket(line)  # Calling the cancel ticket function.
        
        if line.startswith('BALANCE '):  # Checking if the line starts with 'BALANCE'.
            # Balance
            balance(line)  # Calling the balance function.
        
        if line.startswith('SHOWCATEGORY '):  # Checking if the line starts with 'SHOWCATEGORY'.
            # Show Category
            show_category(line)  # Calling the show category function.
            