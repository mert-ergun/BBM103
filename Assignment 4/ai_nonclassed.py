import os

def read_ship_positions(filename):
    """
    Read in the initial ship positions from the input file.
    """
    with open(filename) as f:
        data = f.read()
    
    lines = data.split('\n')
    ships = []
    for line in lines:
        for c in line:
            if c in ['C', 'B', 'D', 'S', 'P']:
                # Start of a new ship
                ship = {
                    'name': c,
                    'size': 0,
                    'positions': []
                }
                ships.append(ship)
            elif c != ';':
                # Part of a ship
                ship['size'] += 1
                ship['positions'].append((len(ships[-1]['positions']) // 10, len(ships[-1]['positions']) % 10))
    
    return ships

def initialize_boards(grid_size, ships):
    """
    Initialize the hidden and final boards for a player.
    """
    hidden_board = [['-' for _ in range(grid_size)] for _ in range(grid_size)]
    final_board = [['-' for _ in range(grid_size)] for _ in range(grid_size)]
    
    for ship in ships:
        for x, y in ship['positions']:
            final_board[x][y] = ship['name']
    
    return hidden_board, final_board

def update_board(board,final_board, x, y, ship_size):
    """
    Update the hidden board for a player based on the opponent's move.
    """
    if board[x][y] == '-':
        # Miss
        board[x][y] = 'O'
        final_board[x][y] = 'O'
    else:
        # Hit
        board[x][y] = 'X'
        final_board[x][y] = 'X'
        ship_size -= 1
        if ship_size == 0:
            # Ship has been sunk
            for i in range(len(board)):
                for j in range(len(board[i])):
                    if board[i][j] == 'X':
                        board[i][j] = 'S'
                        final_board[i][j] = 'S'
    
    return board,final_board, ship_size

def has_ships_left(ships):
    """
    Check if a player has any ships left.
    """
    for ship in ships:
        if ship['size'] > 0:
            return True
    return False

def play_game(player1, player2):
    """
    Play a game of Battleship.
    """
    round_count = 0
    current_player = player1
    other_player = player2
    
    while True:
        # Read in the coordinates for the current player's move
        filename = f'{current_player["name"]}.in'
        if not os.path.exists(filename):
            break
        
        with open(filename) as f:
            moves = f.read().strip().split(';')
        
        for move in moves:
            x, y = move.split(',')
            x = int(x) - 1
            y = ord(y) - 65
            
            # Update the opponent player's board
            other_player['hidden_board'], other_player['final_board'], other_player['ships'][y]['size'] = update_board(other_player['hidden_board'], other_player['final_board'], x, y, other_player['ships'][y]['size'])
        
            # Check if the opponent player has any ships left
            if not has_ships_left(other_player['ships']):
                print(f'{current_player["name"]} Wins!')
                break
            
            # Swap players
            round_count += 1
            current_player, other_player = other_player, current_player
            
            # Check if both players have no ships left
            if not has_ships_left(player1['ships']) and not has_ships_left(player2['ships']):
                break
            # Game is a draw
            print('It is a Draw!')
    
    # Print the final non-hidden form of the two players' boards
    print('Player 1 Final Board:')
    print('\n'.join(' '.join(row) for row in player1['final_board']))
    print('Player 2 Final Board:')
    print('\n'.join(' '.join(row) for row in player2['final_board']))
    
# Read in the initial ship positions for both players
player1_ships = read_ship_positions('Player1.txt')
player2_ships = read_ship_positions('Player2.txt')

# Initialize the boards for both players
player1 = {
    'name': 'Player1',
    'grid_size': 10,
    'ships': player1_ships,
    'hidden_board': None,
    'final_board': None
}
player1['hidden_board'], player1['final_board'] = initialize_boards(player1['grid_size'], player1['ships'])

player2 = {
    'name': 'Player2',
    'grid_size': 10,
    'ships': player2_ships,
    'hidden_board': None,
    'final_board': None
}
player2['hidden_board'], player2['final_board'] = initialize_boards(player2['grid_size'], player2['ships'])

# Play the game
play_game(player1, player2)


