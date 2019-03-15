#!/usr/bin/env python
"""
wordsearch.py
"Shall we play a game?" - WOPR

Given a dictionary, search a matrix of random letters for each word.
"""
import sys
import logging
from random import choice
from optparse import OptionParser


def main():
    """
    Main entry point for the script.
    :return: None
    """
    logging.basicConfig(stream=sys.stdout)
    logger = logging.getLogger()

    # Grab CLI arguments
    opt_parser = OptionParser()
    opt_parser.add_option('--dictionary', dest='dictionary_file',
                          help='File containing dictionary words')
    opt_parser.add_option('--width', dest='board_width', type='int',
                          help='The width of the word search board, in characters.')
    opt_parser.add_option('--height', dest='board_height', type='int',
                          help='The height of the word search board, in characters.')
    opt_parser.add_option('--debug', dest='debug', action="store_true",
                          help='Enable debug logging')

    (options, args) = opt_parser.parse_args()
    if options.debug:
        logger.setLevel(logging.DEBUG)

    # Load in the dictionary
    dictionary = []
    with open(options.dictionary_file) as file:
        for word in file:
            dictionary.append(word.rstrip())

    logger.info('Generating game board...')
    game_board = GameBoard(height=options.board_height,
                           width=options.board_width)
    logger.debug('====================')
    logger.debug('Generated Game Board')
    logger.debug('====================')
    logger.debug(game_board)
    logger.debug(game_board.rows)
    logger.debug(game_board.rows_reversed)

    logger.debug(game_board.columns)
    logger.debug(game_board.columns_reversed)

    # Search the board
    results = []
    for word in dictionary:        
        if game_board.search(word) is True:
            results.append(word)

    # Print results
    print('====================')
    print('      RESULTS       ')
    print('====================')
    for word in results:
        print(word)


class GameBoard(object):
    """
    Represents a game board.
    The initial data is stored as a 2D array. From that initial dataset, search vectors are created
    for each valid search that can be performed: Horizontal, Vertical, Diagonal Up,
    Diagonal Down, and the reverse for each.
    """
    VALID_LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                     'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    data = []
    board_width = 0
    board_height = 0

    rows = []
    rows_reversed = []

    columns = []
    columns_reversed = []

    diag_down = []
    diag_down_reversed = []

    diag_up = []
    diag_up_reversed = []

    search_lists = []

    def __init__(self, height, width, random_data=True):
        self.board_height = height
        self.board_width = width

        # Generate the grid of letters
        if random_data:
            for y in range(height):
                row = []
                for x in range(width):
                    row.append(choice(self.VALID_LETTERS))
                self.data.append(row)
        else:
            # TODO: Implement a hard-coded grid for testing purposes
            pass

        # Generate a list of rows
        for r in self.data:
            new_row = ''.join(r)
            self.rows.append(new_row)

        # Generate a list of reverse rows
        for r in self.rows:
            self.rows_reversed.append(r[::-1])

        # Generate a list of columns
        for x in range(self.board_width):
            new_col = ''
            for y in range(self.board_height):
                new_col += self.rows[y][x]

            self.columns.append(new_col)

        # Generate a list of reversed columns
        for c in self.columns:
            self.columns_reversed.append(c[::-1])

        # TODO: Generate a list of downward diagonals.
        # Starting at the "bottom left" of the matrix, we'll move up & to the left.
        # Generate a list of reversed downward diagonals.

        # TODO: Generate a list of upward diagonals.
        # Generate a list of reversed upward diagonals.

        # Group all of the search vectors into a master list that the search() method will iterate on.
        self.search_lists = [self.rows, self.rows_reversed, self.columns, self.columns_reversed,
                             self.diag_down, self.diag_down_reversed, self.diag_up, self.diag_up_reversed]

    def search(self, word):
        """
        Walk through each search vector, looking for the requested word.
        :param word: A word to search for
        :return: True if the word is found. False otherwise.
        """
        for l in self.search_lists:
            for item in l:
                if word in item:
                    return True
        return False

    def __str__(self):
        """ For debugging, spit out the game board as a string. ASCII games - FTW! """
        output = "\n"
        for row in self.data:
            for col in row:
                output += f'{col} '
            output += '\r\n'
        return output


if __name__ == '__main__':
    main()
