import sys  # Import the sys module to get the command line arguments


def clear_output_file():
    """
    Clears the output file.
    """
    
    with open("Battleship.out", 'w') as f:  # Open the output file in write mode to clear it
        pass  # The pass statement does nothing. It is used as a placeholder when a statement is required syntactically but the program requires no action, we just need it to delete the contents of the file


def write_output_file(message):
    """
    Writes the given message to the output file.
    """
    
    with open("Battleship.out", 'a') as f:
        f.write(message)


def check_arguments():
    """
    Checks if the number of arguments is correct.
    """
    
    try:
        if len(sys.argv) != 5:  # If the number of arguments is not 4, print the error message and exit the program
            write_output_file("Invalid number of arguments. Expected 4, got " + str(len(sys.argv) - 1) + ".\n")
            raise ValueError("Invalid number of arguments. Expected 4, got " + str(len(sys.argv) - 1) + ".")
    except ValueError as e:
        print("ValueError:", e)
        sys.exit()    
        

def check_input_files():
    """
    Checks if the input files are reachable.
    """
    
    problemMakers = []  # A list to store the names of the problem makers
    
    try:  # Try to open the input files
        open(sys.argv[1])  # sys.argv[1] is the "Player1.txt" file
    except FileNotFoundError:
        problemMakers.append(sys.argv[1])  # If the file is not reachable, add it to the list of problem makers
    try:    
        open(sys.argv[2])  # sys.argv[2] is the "Player2.txt" file
    except FileNotFoundError:
        problemMakers.append(sys.argv[2])
    try:    
        open(sys.argv[3])  # sys.argv[3] is the "Player1.in" file
    except FileNotFoundError:
        problemMakers.append(sys.argv[3])
    try:    
        open(sys.argv[4])  # sys.argv[4] is the "Player2.in" file
    except FileNotFoundError:
        problemMakers.append(sys.argv[4])
    
    if len(problemMakers) > 0:  # If there are problem makers, print the error message and exit the program
        print("IOError: input file(s) " + ", ".join(problemMakers) +" is/are not reachable.")  # The join() function joins the elements of the list with the given string
        write_output_file("IOError: input file(s) " + ", ".join(problemMakers) +" is/are not reachable.\n")
        sys.exit()    


def read_ship_pos():
    """
    Reads the ship positions from the input files.
    """
    
    with open(sys.argv[1], 'r') as f:  # Open the "Player1.txt" file
        player1 = f.readlines()  # Read the lines of the file and store them in a list
    
    with open(sys.argv[2], 'r') as f:  # Open the "Player2.txt" file
        player2 = f.readlines()

    global playerShips1, playerShips2  # Make the variables global so that they can be accessed from other functions

    playerShips1 = []  # A list to store the ships of player 1
    playerShips2 = []  # A list to store the ships of player 2

    for row in player1:
        row = row.strip('\n')  # Remove the newline character from the end of the row (if there is one)
        values = row.split(";")  # Split the row by the semicolon character and store the resulting list in a new variable
        try:
            if len(values) != 10:  # Check if the length of the list is 10
                raise IndexError("Player1.txt file should contain exactly 10 positions.")
        except IndexError as e:  # If the length is not 10, print the error message
            print(e)
            write_output_file(e)
            sys.exit()
        
        for value in values:  # Check if the values are valid
            if value != "":    
                try:
                    assert len(value) == 1  # Check if the length of the value is 1
                    assert value in "BCPSD"  # Check if the value is one of the valid characters
                except AssertionError:
                    print("IndexError: Player1.txt file contains an invalid ship position.")  # If the length is not 1, print the error message
                    write_output_file("IndexError: Player1.txt file contains an invalid ship position.\n")
                    sys.exit()
        
        values = [value if value else "-" for value in values]  # Replace any empty values with dashes
      
        playerShips1.append(values)  # Add the list to the playerShips1 list

    for row in player2:  # Do the same for player 2
        row = row.strip('\n')
        values = row.split(";")
        try:
            if len(values) != 10:  # Check if the length of the list is 10
                raise IndexError("Player1.txt file should contain exactly 10 positions.")
        except IndexError as e:  # If the length is not 10, print the error message
            print(e)
            write_output_file(e)
            sys.exit()
        
        for value in values:  # Check if the values are valid
            if value != "":    
                try:
                    assert len(value) == 1  # Check if the length of the value is 1
                    assert value in "BCPSD"
                except AssertionError:
                    print("IndexError: Player1.txt file contains an invalid ship position.")  # If the length is not 1, print the error message
                    write_output_file("IndexError: Player1.txt file contains an invalid ship position.\n")
                    sys.exit()
        
        values = [value if value else "-" for value in values]
        
        playerShips2.append(values)
    

def read_player_moves():
    """
    Reads the player moves from the input files.
    """
    
    global playerMoves1, playerMoves2  # Make the variables global so that they can be accessed from other functions
    
    with open(sys.argv[3], 'r') as f:  # Open the "Player1.in" file
        playerMoves1 = f.readline().strip(";").split(";")  # Read the first line and split it by the semicolon character
    
    if "\n" in playerMoves1:
        print("Player1.in file should not contain a newline character.")
        write_output_file("Player1.in file should not contain a newline character.\n")
        sys.exit()
    
    for element in playerMoves1:
        try:
            if element[0] == "1" and element[1] == "0":
                assert len(element) == 4  # Check if the length of the element is 4
            else:
                assert len(element) == 3  # Check if the length of the element is 3
        except AssertionError:
            print("IndexError: Player1.in file should contain exactly 3 characters in a move.")  # If the length is not 3, print the error message
            write_output_file("IndexError: Player1.in file should contain exactly 3 characters in a move.\n")
            playerMoves1.remove(element)  # Remove the element from the list    
            continue  # Continue to the next element
        except IndexError:
            print("IndexError: Player1.in file should contain exactly 3 characters in a move.")  # If the length is not 3, print the error message
            write_output_file("IndexError: Player1.in file should contain exactly 3 characters in a move.\n")
            playerMoves1.remove(element)  # Remove the element from the list
            continue
        
        try:
            assert int(element[0]) in range(1, 11) or int(element[0:2]) in range(10,11) # Check if the first character is a number between 1 and 10
            if element[0] == "1" and element[1] == "0":
                assert element[3] in "ABCDEFGHIJ"  # Check if the fourth character is a letter between A and J
            else:
                assert element[2] in "ABCDEFGHIJ"  # Check if the second character is a letter between A and J
        except AssertionError:  
            print("AssertionError: Invalid operation in Player1.in file.")
            write_output_file("AssertionError: Invalid operation in player1.in file.\n")
            playerMoves1.remove(element)
            continue    
        except ValueError:
            print("ValueError: Player1.in file contains an invalid move.")
            write_output_file("ValueError: Player1.in file contains an invalid move.\n")
            playerMoves1.remove(element)
            continue
        except IndexError:
            print("IndexError: Player1.in file contains an invalid move.")
            write_output_file("IndexError: Player1.in file contains an invalid move.\n")
            playerMoves1.remove(element)
            continue    
    
    with open(sys.argv[4], 'r') as f:  # Open the "Player2.in" file
        playerMoves2 = f.readline().strip(";").split(";")
    
    if "\n" in playerMoves2:
        print("Player2.in file should not contain a newline character.")
        write_output_file("Player2.in file should not contain a newline character.\n")
        sys.exit()
    
    for element in playerMoves2:
        try:
            if element[0] == "1" and element[1] == "0":
                assert len(element) == 4
            else:
                assert len(element) == 3
        except AssertionError:
            print("IndexError: Player2.in file should contain exactly 3 characters in a move.")
            write_output_file("IndexError: Player2.in file should contain exactly 3 characters in a move.\n")
            playerMoves2.remove(element)
            continue
        except IndexError:
            print("IndexError: Player2.in file should contain exactly 3 characters in a move.")
            write_output_file("IndexError: Player2.in file should contain exactly 3 characters in a move.\n")
            playerMoves2.remove(element)
            continue
        
        try:
            assert int(element[0]) in range(1, 10) or int(element[0:2]) in range(10, 11)  # Check if the first character is a number between 1 and 10 or the first two characters are a number between 10 and 11
            if element[0] == "1" and element[1] == "0":
                assert element[3] in "ABCDEFGHIJ"
            else:
                assert element[2] in "ABCDEFGHIJ"
        except AssertionError:
            print("AssertionError: Invalid operation in Player2.in file.")
            write_output_file("AssertionError: Invalid operation in Player2.in file.\n")
            playerMoves2.remove(element)
            continue
        except ValueError:
            print("ValueError: Player2.in file contains an invalid move.")
            write_output_file("ValueError: Player2.in file contains an invalid move.\n")
            playerMoves1.remove(element)
            continue
        except IndexError:
            print("IndexError: Player2.in file contains an invalid move.")
            write_output_file("IndexError: Player2.in file contains an invalid move.\n")
            playerMoves2.remove(element)
            continue
    

def define_ships(playerShip):
    """
    Defines the ships and their sizes in given player's ship positions lists.
    """
    
    global shipsLen, letters_to_numbers  # Make the variables global so that they can be accessed from other functions
    
    # A dictionary to store the ships and their sizes
    shipsLen = {
        "B1_1": 4, "B2_1": 4, "B2_2": 4, "B1_2": 4,
        "P3_1": 2, "P4_1": 2, "P3_2": 2, "P4_2": 2,
        "P1_1": 2, "P2_1": 2, "P1_2": 2, "P2_2": 2,
        "C_1": 5, "C_2": 5, "D_1": 3, "D_2": 3, "S_1": 3, "S_2": 3
    }
    
    # A dictionary to store the letters and their corresponding numbers
    letters_to_numbers = {
        "A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5,
        "G": 6, "H": 7, "I": 8, "J": 9        
    }
    
    problemMakers = ["B14", "B24", "P42", "P32","P12","P22"]
    
    for ship in problemMakers:  # Loop through the problem makers
        for i in range(10):  # Loop through the rows
            for j in range(10):  # Loop through the columns
                match = False  # A boolean variable to check if the ship is found
                if playerShip[i][j]==ship[0]:  # Check if the ship is in problem makers
                    for n,w in [(1,0),(0,1),(-1,0),(0,-1)]:  # Loop through the directions
                        try:
                            if playerShip[i+n][j+w]==ship[0] and (playerShip[i+n*2][j+w*2]==ship[0] or ship[0]=="P"):  # Check if the ship is in the given direction
                                match = True  # If the ship is found, set the match variable to True
                                direction = (n,w)  # Set the direction variable to the direction of the ship
                        except:  
                            pass  
                    if match:  # If the ship is found
                        playerShip[i][j]=ship[:2]  # Set the ship's unique identifier
                        for t in range(1,int(ship[-1])):  # Loop through the ship's length
                            playerShip[i+t * direction[0]][j+t * direction[1]] = ship[:2]  # Set the ship's unique identifier
                        break
            if match:  
                break
            

def playTurn(player):
    """
    Plays the turn of the given player. Takes the player as a parameter.
    """
    
    global playerMoves1, playerMoves2, playerShips1, playerShips2  # Make the global variables accessible
    
    if player == 1:  # If the player is player 1
        opposer = "_2"  # Set the opposer variable to player 2
        players_move = playerMoves1  # Set the players_move variable to player 1's move list
        opposer_ship = playerShips2  # Set the opposer_ship variable to player 2's ship positions list
    else:
        opposer = "_1"
        players_move = playerMoves2
        opposer_ship = playerShips1
        
    print("Player{}'s Move\n".format(player))  # Print the player's move title
    write_output_file("Player{}'s Move\n\n".format(player))
    
    print("Round: {}\t\t\t\t\tGrid Size: 10x10\n".format(gameturn))  # Print the round and grid size
    write_output_file("Round: {}\t\t\t\t\tGrid Size: 10x10\n\n".format(gameturn))
    
    print("Player1's Hidden Board:\t\tPlayer2's Hidden Board:\n")  # Print the player's hidden board and the opposer's hidden board titles
    write_output_file("Player1's Hidden Board:\t\tPlayer2's Hidden Board:\n\n")
    
    print("  A B C D E F G H I J\t\t  A B C D E F G H I J")  # Print the grid
    write_output_file("  A B C D E F G H I J\t\t  A B C D E F G H I J\n")
    
    for i in range(10):  # Loop through the rows
        print(f"{i+1}", end="")  # Print the row number
        write_output_file(f"{i+1}")  
        for j in range(10):  # Loop through the columns
            if playerShips1[i][j][0] == "O":  # If the ship is not hit
                to_print = "O"  # Set the to_print variable to O
            elif playerShips1[i][j][0] == "X":  # If the ship is hit
                to_print = "X"  # Set the to_print variable to X
            else:  # If there is a ship which is not hit
                to_print = "-"  # Set the to_print variable to -
            print(" "*(i!=9 or j!=0) + to_print, end="")  # Print the to_print variable
            write_output_file(" "*(i!=9 or j!=0) + f"{to_print}")

        print("\t\t", end="")  # Print two tabs and do the same for the opposer's board
        write_output_file("\t\t")
        print(f"{i+1}", end="")  
        write_output_file(f"{i+1}")
        for j in range(10):
            if playerShips2[i][j][0] == "O":
                to_print = "O"
            elif playerShips2[i][j][0] == "X":
                to_print = "X"
            else:
                to_print = "-"
            print(" "*(i!=9 or j!=0) + to_print, end="")
            write_output_file(" "*(i!=9 or j!=0) + f"{to_print}")
        print("")
        write_output_file("\n")
    print("")
    write_output_file("\n")

    for j in [["C"], ["B1", "B2"], ["D"], ["S"], ["P1", "P2", "P3", "P4"]]:  # Loop through the ships
        ship_1 = ""  # Set the ship_1 variable to an empty string
        ship_2 = ""  # Set the ship_2 variable to an empty string

        for k in j:  # Loop through the ships
            if shipsLen[k + "_1"] == 0:  # If the all ship is sunk
                ship_1 = "X " + ship_1  # Mark the ship as sunk below the grid
            else:  # If the ship is not sunk
                ship_1 = ship_1 + "- "  # Mark the ship as not sunk below the grid
            if shipsLen[k + "_2"] == 0:  # Do the same for the opposer's ship
                ship_2 = "X " + ship_2
            else:
                ship_2 = ship_2 + "- "

            if k[0] == "C":  # If the ship is a carrier
                ship = "Carrier"  # Set the ship variable to Carrier
                tab_number = "\t\t"  # Set the tab_number variable to two tabs, so that the ship name is aligned
            elif k[0] == "B":  
                ship = "Battleship"
                tab_number = "\t"
            elif k[0] == "D":
                ship = "Destroyer"
                tab_number = "\t"
            elif k[0] == "S":
                ship = "Submarine"
                tab_number = "\t"
            elif k[0] == "P":
                ship = "Patrol Boat"
                tab_number = "\t"
            if k[0] == "P":  # If the ship is a patrol boat
                tab_number2 = "\t" * 3  # Set the tab_number2 variable to three tabs, so that the ship name is aligned
            else:  # If the ship is not a patrol boat
                tab_number2 = "\t" * 4  # Set the tab_number2 variable to four tabs, so that the ship name is aligned

        print(f"{ship}{tab_number}{ship_1[:-1]}{tab_number2}{ship}{tab_number}{ship_2}")  # Print the ship name and the ship status
        write_output_file(f"{ship}{tab_number}{ship_1[:-1]}{tab_number2}{ship}{tab_number}{ship_2}\n")
    print("")
    write_output_file("\n")
    try:  # Try to get the player's move
        move = players_move[gameturn-1]  # Set the move variable to the player's move
    except IndexError:  # If the player's move is not in the players_move list
        print("Number of moves is less than the number of turns. Please enter the moves again.")
        write_output_file("Number of moves is less than the number of turns. Please enter the moves again.\n")
        sys.exit()
    print("Enter your move: {}\n".format(move))  # Print the player's move 
    write_output_file("Enter your move: {}\n\n".format(move))
    move = move.split(",")  # Split the move variable by the comma, so that the row and column are separated
    
    try:  # Try to remove the ship from the shipsLen dictionary
        shipsLen[opposer_ship[int(move[0]) - 1][letters_to_numbers[move[1]]]+opposer] -= 1 
    except:  # If the ship is not in the shipsLen dictionary,
        pass  # Do nothing
    
    opposer_ship[int(move[0])-1][letters_to_numbers[move[1]]] = ("O" if opposer_ship[int(move[0])-1][
        letters_to_numbers[move[1]]] == "-" else "X") + opposer_ship[int(move[0])-1][letters_to_numbers[move[1]]]  # Set the ship to O if it is not hit, and X if it is hit


def winCondition(player):
    """
    Win condition function. It takes the player as a parameter. Prints the winner, last non-hidden tables and writes it to the output file.
    """
    
    print("Player{} Wins!\n".format(player))  # Print the winner
    write_output_file("Player{} Wins!\n\n".format(player))
    
    print("Final Information:\n")  # Print the final information
    write_output_file("Final Information:\n\n")
    
    print("Player1's Board\t\t\t\tPlayer2's Board")  # Print the player's boards
    write_output_file("Player1's Board\t\t\t\tPlayer2's Board\n")
    
    print("  A B C D E F G H I J\t\t  A B C D E F G H I J")  # Print the column names
    write_output_file("  A B C D E F G H I J\t\t  A B C D E F G H I J\n")
    
    for i in range(10):  # Loop through the rows
        print(f"{i+1}", end="")  # Print the row number
        write_output_file(f"{i+1}")
        for j in range(10):  # Loop through the columns
            to_print = playerShips1[i][j][0]  # Set the to_print variable to the ship
            print(" "*(i!=9 or j!=0) + to_print, end="")  # Print the ship
            write_output_file(" "*(i!=9 or j!=0) + f"{to_print}")

        print("\t\t", end="")  # Do the same for the opposer's board
        write_output_file("\t\t")
        print(f"{i+1}", end="")  
        write_output_file(f"{i+1}")
        for j in range(10):
            to_print = playerShips2[i][j][0]
            print(" "*(i!=9 or j!=0) + to_print, end="")
            write_output_file(" "*(i!=9 or j!=0) + f"{to_print}")
        print("")
        write_output_file("\n")
    print("")
    write_output_file("\n")

    for j in [["C"], ["B1", "B2"], ["D"], ["S"], ["P1", "P1", "P3", "P4"]]:  # Loop through the ships, do the same thing that was done in the playTurn function
        ship_1 = ""
        ship_2 = ""
        for k in j:
            if shipsLen[k + "_1"] == 0:
                ship_1 = "X " + ship_1
            else:
                ship_1 = ship_1 + "- "
            if shipsLen[k + "_2"] == 0:
                ship_2 = "X " + ship_2
            else:
                ship_2 = ship_2 + "- "
            if k[0] == "C":
                ship = "Carrier"
                tab_number = "\t\t"
            elif k[0] == "B":
                ship = "Battleship"
                tab_number = "\t"
            elif k[0] == "D":
                ship = "Destroyer"
                tab_number = "\t"
            elif k[0] == "S":
                ship = "Submarine"
                tab_number = "\t"
            elif k[0] == "P":
                ship = "Patrol Boat"
                tab_number = "\t"
            if k[0] == "P":
                tab_number2 = "\t" * 3
            else:
                tab_number2 = "\t" * 4
        print(f"{ship}{tab_number}{ship_1[:-1]}{tab_number2}{ship}{tab_number}{ship_2}")  # Print the ship's name and the ship's status
        write_output_file(f"{ship}{tab_number}{ship_1[:-1]}{tab_number2}{ship}{tab_number}{ship_2}\n")


def drawCondition():
    """
    Draw condition function. Prints the draw message and writes it to the output file.
    """
    
    print("It's a Draw!\n")  # Print the draw message
    write_output_file("It's a Draw!\n\n")
    
    print("Final Information:\n")  # Print the final information
    write_output_file("Final Information:\n\n")
    
    print("Player1's Board\t\t\t\tPlayer2's Board")  # Print the player's boards
    write_output_file("Player1's Board\t\t\t\tPlayer2's Board\n")
    
    print("  A B C D E F G H I J\t\t  A B C D E F G H I J")  # Print the column names
    write_output_file("  A B C D E F G H I J\t\t  A B C D E F G H I J\n")
    
    for i in range(10):  # Loop through the rows
        print(f"{i+1}", end="")  # Print the row number
        write_output_file(f"{i+1}")
        for j in range(10):  # Loop through the columns
            to_print = playerShips1[i][j][0]  # Set the to_print variable to the ship
            print(" "*(i!=9 or j!=0) + to_print, end="")  # Print the ship
            write_output_file(" "*(i!=9 or j!=0) + f"{to_print}")

        print("\t\t", end="")  # Do the same for the opposer's board
        write_output_file("\t\t")
        print(f"{i+1}", end="")  
        write_output_file(f"{i+1}")
        for j in range(10):
            to_print = playerShips2[i][j][0]
            print(" "*(i!=9 or j!=0) + to_print, end="")
            write_output_file(" "*(i!=9 or j!=0) + f"{to_print}")
        print("")
        write_output_file("\n")
    print("")
    write_output_file("\n")

    for j in [["C"], ["B1", "B2"], ["D"], ["S"], ["P1", "P1", "P3", "P4"]]:  # Loop through the ships, do the same thing that was done in the playTurn function
        ship_1 = ""
        ship_2 = ""
        for k in j:
            if shipsLen[k + "_1"] == 0:
                ship_1 = "X " + ship_1
            else:
                ship_1 = ship_1 + "- "
            if shipsLen[k + "_2"] == 0:
                ship_2 = "X " + ship_2
            else:
                ship_2 = ship_2 + "- "
            if k[0] == "C":
                ship = "Carrier"
                tab_number = "\t\t"
            elif k[0] == "B":
                ship = "Battleship"
                tab_number = "\t"
            elif k[0] == "D":
                ship = "Destroyer"
                tab_number = "\t"
            elif k[0] == "S":
                ship = "Submarine"
                tab_number = "\t"
            elif k[0] == "P":
                ship = "Patrol Boat"
                tab_number = "\t"
            if k[0] == "P":
                tab_number2 = "\t" * 3
            else:
                tab_number2 = "\t" * 4
        print(f"{ship}{tab_number}{ship_1[:-1]}{tab_number2}{ship}{tab_number}{ship_2}")  # Print the ship's name and the ship's status
        write_output_file(f"{ship}{tab_number}{ship_1[:-1]}{tab_number2}{ship}{tab_number}{ship_2}\n")    


def playGame(turn):
    """
    Playing the game function. It takes the turn as a parameter. Calls other functions to play the game.
    """
    
    global gameturn, last_turn # Make the turn variable global
    gameturn = turn  # Set the turn variable to the turn parameter so that it can be used in other functions
    
    if turn == 1:  # If game is in the first turn  
        print("Battle of Ships Game\n")  # Print the game title
        write_output_file("Battle of Ships Game\n\n")  # Write the game title to the output file          

    playTurn(1)  # Play the turn for player 1
    playTurn(2)  # Play the turn for player 2
    
    nonsunk_ships1 = 0  # Set the number of non-sunk ships to 0 for player 1
    nonsunk_ships2 = 0  # Set the number of non-sunk ships to 0 for player 2
    
    for ship in shipsLen:  # Loop through the ships
        if ship[-1] == "1":  # If the ship is for player 1
            nonsunk_ships1 += shipsLen[ship]  # Add the ship's length to the number of non-sunk ships for player 1
        else:  # If the ship is for player 2
            nonsunk_ships2 += shipsLen[ship]  # Add the ship's length to the number of non-sunk ships for player 2
    
    if nonsunk_ships1 == 0 and nonsunk_ships2 == 0:  # If there are no non-sunk ships for both players
        drawCondition()  # Call the draw condition function
            
    elif nonsunk_ships1 == 0:  # If there are no non-sunk ships for player 1
        if nonsunk_ships2 == 1 and not last_turn:  # If there is only one non-sunk ship for player 2
            playGame(turn+1)  # Call the play game function with the turn parameter increased by 1, so that the next turn can be played, this is done so that the game can end in a draw  
            last_turn = True  # Set the last_turn variable to True so that the game will not enter this if statement again the game never enter an infinite loop
        else:
            winCondition(2)  # Call the win condition function with the winner as player 2
    
    elif nonsunk_ships2 == 0:  # If there are no non-sunk ships for player 2
        if nonsunk_ships1 == 1 and not last_turn:
            playGame(turn+1)
            last_turn = True
        else:
            winCondition(1)  # Call the win condition function with the winner as player 1
    
    else:  # If there are non-sunk ships for both players
        playGame(turn+1)  # Call the play game function with the turn parameter increased by 1, so that the next turn can be played


if __name__ == "__main__":  # If the file is run directly
    try:
        clear_output_file()  # Clear the output file
        check_arguments()  # Check the arguments
        check_input_files()  # Check the input files
        
        read_ship_pos()  # Read the ship positions
        read_player_moves()  # Read the player moves
        
        define_ships(playerShips1)  # Define the ships for player 1
        define_ships(playerShips2)  # Define the ships for player 2
        
        last_turn = False  # Set the last_turn variable to False when the game starts
        playGame(1)  # Play the game
        
    except Exception as e:  # If there is an error that is not handled
        print("kaBOOM: run for your life!")  # Print the error message
        sys.exit()

        
# Mert ERGÜN b2220356062