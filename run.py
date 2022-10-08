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


def create_ships():
    """
    Creates the ships on the board
    """
    pass


def count_hit_ships():
    """
    Counts the hit ships for the score
    """


def get_ship_location():
    """
    Locate the ships
    """
    pass

create_ships()

