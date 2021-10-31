import random


class Setup_Board:
    def __init__(self, num_ships, ship_hit, ship, type, guess, water,
                 computer_board, board, player_name, row, column):
        self.num_ships = 5
        self.ship_hit = 'X'
        self.type = type
        self.ship = 'O'
        self.guess = []
        self.water = ['-']
        self.computer_board = []
        self.board = []
        self.player_name = player_name
        self.row = 9
        self.column = 9

    def guesses(self, row, column):
        """
        Returns a value of hit or miss.
        """
        self.guess.append((self.row, self.column))
        if (self.row, self.column) in self.computer_board[self.row][self.column] == 'X':
            return 'Hit'
        else:
            return 'Miss'

    def validate_corordinates(self, row, column, type):
        """
        Vaildates the corordinates that the Computer and Player Choose
        """

        if type == 'Player':
            if self.board[self.row][self.column] == 'O':
                print('Corordinates Valid, Ship Hit')
                return 'corordinates_valid'
            if self.board[self.row][self.column] == 'X':
                print('Already picked this Corordinate, Please Pick again.')
            else:
                if self.board[self.row][self.column] == ['-']:
                    print('Corordinates invalid, Missed')
                    return 'corordinates_invalid'

        else:
            while type == 'Computer':
                if self.computer_board[self.row][self.column] == self.ship:
                    print('Computer found ship')
                    return 'Computer_found_ship'
                else:
                    if self.computer_board[self.row][self.column] == ['-']:
                        print('Computer Missed')
                        return 'Computer_Missed'

    def populate_boards(self, computer_board, board):
        """
        Populates the two boards
        """

        # runs twice
        for i in ['computer', 'player']:
            # set a counter to go to 5
            counter = 1
            computer_counter = 1
            while counter <= 5 or computer_counter <= 5:
                # generate the random num
                
                random_number = random.randrange(10)
                # fill the computer board
                if i == 'computer':
                    # check if already taken, if so continue burt dont increase the counter
                    if self.computer_board[random_number][random_number] == 'O':
                        continue
                    else:
                        # otherwise add the board 0, and increase the counter
                        self.computer_board[random_number][random_number] = 'O'
                        computer_counter += 1
                        continue
                elif i == 'player':
                    if self.board[random_number][random_number] == 'O':
                        continue
                    else:
                        self.board[random_number][random_number] = 'O'
                        counter += 1
                        continue
                      
    def make_guess(self):
        """
        Player can guess and computer will auto guess.
        """

    def render_Player_board(self, type, player_name):
        """
        Creates the game board that the user can play in.
        """
        print('\n\n\n')
        print(f'          {self.player_name}')
        print('    0 1 2 3 4 5 6 7 8 9')
        print('  +---------------------+')
        for self.row in range(10):
            self.board.append(self.water * 10)

        letters = 0
        for self.row in range(10):
            print(chr(letters + 65), end=' | ')
            for self.column in range(len(self.board[letters])):
                print(self.board[letters][self.column], end=' ')
            print('| ')
            letters += 1
        print('  +---------------------+ \n\n\n')

    def render_computer_board(self, type):
        """
        renders Computers Board
        """
        print('         COMPUTER ')
        print('    0 1 2 3 4 5 6 7 8 9')
        print('  +---------------------+')
        for self.row in range(10):
            self.computer_board.append(self.water * 10)

        letters = 0
        for self.row in range(10):
            print(chr(letters + 65), end=' | ')
            for self.column in range(len(self.computer_board[letters])):
                print(self.computer_board[letters][self.column], end=' ')
            print('| ')
            letters += 1
        print('  +---------------------+ \n\n\n')


def New_game():
    """
    Starts a new game and welcomes the user to the game.
    """
    # player_score = 9
    # computer_score = 9
    column = 0
    row = 0
    computer_board = []
    board = []
    num_ships = 5
    ship_hit = 'X'
    ship = 'O'
    guess = []
    water = ['-']
    print('-------------------------------------------')
    print('Welcome To Battleship!! ')
    print('How to play? Try and guess where the')
    print('enemy ships are by choosing a row and a column.')
    print('Example: row: 2  comlumn: 2 \n \n\n')
    print('Row and column must be between 0 and 9.')
    player_name = input('Enter Your Name: ')
    print('-------------------------------------------\n\n\n')
    
    setup_pb = Setup_Board(num_ships, ship_hit, ship, type, guess, water,
                           computer_board, board, player_name, row, column)

    setup_pb.render_Player_board('Player', player_name)
    setup_pb.render_computer_board('Computer')
    setup_pb.populate_boards(computer_board, board)

    row = input('Enter a Row: ')
    column = input('Enter a Column: ')

    if type == 'Player' and num_ships == 0:
        print('Computer has won, starting new game')
        New_game()
    else:
        if type == 'Computer' and num_ships == 0:
            print('Player Has Won, starting new game')
            New_game()


New_game()
