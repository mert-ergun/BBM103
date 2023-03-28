import sys
import os

current_dir = os.getcwd()
input_file = 'input.txt'  #Şimdilik! 
input_file_path = os.path.join(current_dir, input_file)
output_file = 'output.txt'
output_file_path = os.path.join(current_dir, output_file)
categories = []
sold_seats = []
rows = dict()
colls = dict()


def create_category(line):
    words = line.split()
    if words[1] in categories:
        print('Warning: Cannot create the category for the second time. The stadium has already {}'.format(words[1]))
        return
    row_and_col = words[2].split('x')
    global row
    row = row_and_col[0]
    global col
    col = row_and_col[1]
    global categoryname
    categoryname = words[1]
    categories.append(categoryname)
    rows[categoryname] = row
    colls[categoryname] = col
    print("The category '{}' having {} seats has been created".format(categoryname, int(row)*int(col)))
    
    
def sell_ticket(line):
    words = line.split()
    customer = words[1]
    ticket_type = words[2]
    category = words[3]
    number_of_seats = len(words)-4
    seats = []
    for i in range(number_of_seats):
        seats.append(words[i+4])
    for seat in seats:    
        if '-' in seat:
            temp_seat = seat
            temp_category = seat[0]
            temp_seat = temp_seat[1:]
            temp_seat = temp_seat.split('-')
            counter = 0
            index_counter = 0
            for i in range(int(temp_seat[0]), int(temp_seat[1])+1):
                for k in range(int(temp_seat[0]), int(temp_seat[1])+1):
                    if k not in range(1, int(colls[category])+1):
                        index_counter += 1
                        break
                if temp_category+str(i) in sold_seats:
                    print("Error: The seats {} cannot be sold to {} due some of them have already been sold!".format(seat, customer))
                    counter += 1
                    break
            if index_counter != 0:
                print("Error: The category '{}' has less columns than the specified index {}".format(category, seat))
                index_counter = 0
                break
            if counter == 0:
                for i in range(int(temp_seat[0]), int(temp_seat[1])+1):
                    sold_seats.append(temp_category+str(i))
                print("Success: {} has bought {} at {}".format(customer, seat, category))
                counter = 0
        else:
            if seat in sold_seats:
                print('Warning: The seat {} cannot be sold to {} since it was already sold!'.format(seat, customer))
                continue
            if int(seat[1:]) not in range(1, int(colls[category])+1):
                print("Error: The category '{}' has less columns than the specified index {}".format(category, seat))
                continue
            else:
                sold_seats.append(seat)
                print("Success: {} has bought {} at {}".format(customer, seat, category))
                continue
    return
    
    
def cancel_ticket(line):
    words = line.split()
    categoryname = words[1]
    number_of_seats = len(words)-2
    
    

with open(input_file_path, 'r') as f:
    for line in f:
        if line.startswith('CREATECATEGORY '):
            #Create Category
            create_category(line)
        if line.startswith('SELLTICKET '):
            #Sell Ticket
            sell_ticket(line)
        if line.startswith('CANCELTICKET '):
            #Cancel Ticket
            cancel_ticket(line)
        if line.startswith('BALANCE '):
            #Balance
            pass
        if line.startswith('SHOWCATEGORY '):
            #Show Category
            pass
            

