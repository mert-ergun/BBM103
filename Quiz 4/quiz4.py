# Importing sys module for getting arguments from command line.
import sys 

# Creating a dictionary to store the messages.
messages = dict()

# Opening the input file in read mode.
with open(sys.argv[1], 'r') as input:
    for line in input:  # Reading the file line by line.
        if not line.endswith('\n'):  # Checking if the line ends with a new line character.
            line += '\n'  # If not, adding a new line character to the end of the line.
        x , y, message = line.split('\t')  # Splitting the line into three parts. X is message id, y is package id and message is the message.
        if x not in messages:  # Checking if the message id is already in the dictionary.
            messages[x] = [(y, message)]  # If not, adding the message id as a key and the package id and message as a value.
        else:  # If the message id is already in the dictionary.
            messages[x].append((y, message))  # Adding the package id and message to the value of the message id.

# Opening the output file in write mode.
with open(sys.argv[2], 'w') as output:
    message_number = 1  # Creating a variable to store the message number.
    for x in sorted(messages):  # Sorting the messages by message id.
        output.write('Message\t{}\n'.format(message_number))  # Writing the message number to the output file.
        message_number += 1  # Incrementing the message number.
        for y, message in sorted(messages[x]):  # Sorting the packages by package id.
            output.write('{message_id}\t{package_id}\t{message}'.format(message_id=x, package_id=y, message=message))  # Writing the message id, package id and message to the output file.

# Mert Ergün b2220356062
    