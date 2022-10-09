#Legend
# X for placing ships and hit  battleships 
# ' ' for available space
# '-' for missed hits

from random import randint


HIDDEN_BOARD = [["-"] for x in range(8)] 
GUESS_BOARD = [["-"] for x in range(8)] 


letters_to_numbers = {'A': 0,'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}


def print_board(board):
    """
    Prints board to terminal
    """
    print('  A B C D E F G H')
    print('  ---------------')
    row_number = 1
    for row in self.board:
        print("%d|%s|" % (row_number, "|".join(row))
        row_number += 1


def create_ships(board):
    """
    Creates the ships on the board
    """
    for ship in range(5):
        ship_row, ship_column = randint(0,7), randint(0,7)
        while board[ship_row][ship_column] == 'X':
            ship_row, ship_column = randint(0,7), randint(0,7)
        board[ship_row][ship_column] = 'X'


def get_ship_location():
    """
    Locate the ships
    """
    row = input("Please enter a ship row 1-8")
    while row not in '12345678':
        print('Please enter a valid row')
        row = input("Please enter a ship row 1-8")
    column = input("Please enter a ship column A-H").upper()
    while column not in 'ABCDEFGH':
        print('Please enter a valid column')
        column = input('Please enter a ship column A-H').upper()
    return int(row) -1, letters_to_numbers[column]


def count_hit_ships(board):
    """
    Counts the hit ships for the score
    """
    count = 0
    for row in board:
        for column in row:
            if column == 'X':
            count += 1
    return count


create_ships(HIDDEN_BOARD)
turns = 10
while turns > 0:
    print('Welcome to Bomb!')
    print_board(GUESS_BOARD)
    row, column = get_ship_location()
    if GUESS_BOARD[row][column] == '-':
        print('You already guessed that')
    elif GUESS_BOARD[row][column] == 'X':
        print('Congratulations, you have bombed the ship')
        GUESS_BOARD[row][column] = 'X'
        turns -= 1
    else:
        print('Sorry! You missed!')
        GUESS_BOARD[row][column] = '-'
        turns -= 1
print_board(HIDDEN_BOARD)
