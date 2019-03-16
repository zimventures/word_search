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

    options = process_cli(logger)
    if options is None:
        exit(1)

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

    # Search the board
    results = game_board.search(word_list=dictionary)

    # Print results
    print('====================')
    print('      RESULTS       ')
    print('====================')
    print(f'Total words found: {len(results)}')
    grid_width = 6
    for i in range(0, len(results), grid_width):
        sublist = results[i:i+grid_width]
        print(''.join(f'{x:<10}' for x in sublist))

    print(f'Board creation time: {game_board.gen_time:.5f} seconds')
    print(f'Board search time: {game_board.search_time:.5f} seconds')


def process_cli(logger):
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

    # If there aren't enough arguments, print help
    if len(sys.argv) == 1:  # if only 1 argument, it's the script name
        opt_parser.print_help()
        exit()

    if not options.dictionary_file:
        opt_parser.error('--dictionary argument is required')

    if not options.board_width:
        opt_parser.error('--width argument is required')

    if not options.board_height:
        opt_parser.error('--height argument is required')

    return options


if __name__ == '__main__':
    main()
