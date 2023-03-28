class Player:
    def __init__(self, file_name):
        self.grid = []
        self.ships = {'C': 5, 'B': 4, 'D': 3, 'S': 3, 'P': 2}

        # Read initial positions of ships from file and place them on the grid
        with open(file_name, 'r') as f:
            for line in f:
                row = []
                for c in line.strip():
                    if c in self.ships:
                        row.append(c)
                    else:
                        row.append('-')
                self.grid.append(row)

    def update_grid(self, x, y, result):
        # Update grid based on result of move
        self.grid[x][y] = result

    def check_sunk(self, ship_type):
        # Check if the given ship type has been sunk
        self.ships[ship_type] -= 1
        if self.ships[ship_type] == 0:
            print(f'{ship_type} sunk')
            del self.ships[ship_type]

    def all_ships_sunk(self):
        # Check if all ships have been sunk
        return len(self.ships) == 0

    def get_move(self, file_name):
        with open(file_name, 'r') as f:
            move = f.readline().strip()
        x, y = move.split(';')
        return int(x), y 
    
    def print_grid(self):
        # Print the current state of the grid
        for row in self.grid:
            print(' '.join(row))

class Battleship:
    def __init__(self):
        self.player1 = Player('Player1.txt')
        self.player2 = Player('Player2.txt')
        self.current_player = self.player1
        self.opponent = self.player2
        self.round_count = 0

    def play_round(self):
        file_name = 'Player1.in' if self.current_player == self.player1 else 'Player2.in'
        with open(file_name, 'r') as f:
            moves = f.readline().strip().split(';')
        for move in moves:
            x, y = move.split(',')
            result = self.opponent.update_grid(int(x), y)
            self.current_player.update_grid(int(x), y, result)
            if result == 'X':
                self.current_player.update_grid(int(x), y, result)
            elif result == 'O':
                self.current_player.update_grid(int(x), y, result)
            elif result == '-':
                self.current_player.update_grid(int(x), y, result)

            # Check if ship has been sunk
            if result == 'X':
                self.opponent.check_sunk(result)

        # Switch current player
        self.current_player, self.opponent = self.opponent, self.current_player
        self.round_count += 1

    def play(self):
        # Main game loop
        while not self.player1.all_ships_sunk() and not self.player2.all_ships_sunk():
            self.play_round()

        # Print result of game
        if self.player1.all_ships_sunk():
            print('Player2 Wins!')
        elif self.player2.all_ships_sunk():
            print('Player1 Wins!')
        else:
            print('It is a Draw!')

        # Print final boards for both players
        print('Player 1 board:')
        self.player1.print_grid()
        print('Player 2 board:')
        self.player2.print_grid()

game = Battleship()
game.play()
