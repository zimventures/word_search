#!/usr/bin/env python
"""
wordsearch.py
"Shall we play a game?" - WOPR

Given a dictionary, search a matrix of random letters for each word.
"""
import sys
import logging
from gameboard import GameBoard
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
    # logger.debug(game_board.diag_down_right)
    # logger.debug(game_board.diag_down_left)
    # logger.debug(game_board.rows)
    # logger.debug(game_board.rows_reversed)
    # logger.debug(game_board.columns)
    # logger.debug(game_board.columns_reversed)

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


if __name__ == '__main__':
    main()
