from random import choice


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

    diag_down_left = []
    diag_down_left_reversed = []

    diag_down_right = []
    diag_down_right_reversed = []

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

        # TODO: Rewrite this!
        """
        The diagonal logic is SUPER ghetto (time constraint) and needs to be re-written. 
        Algorithm for a re-write would be to rotate the self.data matrix +/- 45 degrees
        and then search each column for values. 
        """
        # Generate a list of downward (to the left) diagonals.
        # Starting at the "top left" of the matrix, we'll move right and search downward to the left
        for x in range(self.board_width):
            new_diag = ''
            # Use min for boards that are wider than they are tall
            for y in range(min(x+1, self.board_height)):
                new_diag += self.data[y][x-y]
            self.diag_down_left.append(new_diag)

        # Starting at the "top right" of the matrix, we'll move down and search down.
        # NOTE: Skip the first spot since it was built in the last step
        for y in range(1, self.board_height):
            new_diag = ''
            for x in range(min(self.board_width, self.board_height-y)):
                new_diag += self.data[y+x][self.board_width - x - 1]
            self.diag_down_left.append(new_diag)

        # Reverse down-left diag
        for d in self.diag_down_left:
            self.diag_down_left_reversed.append(d[::-1])

        # Generate a list of downward (to the right) diagonals.
        # Starting at the "bottom left" of the matrix, we'll move up and build to the right
        for y in reversed(range(self.board_height)):
            new_diag = ''
            # Use min for boards that are taller than they are wide
            for x in range(min(self.board_height - y, self.board_width)):
                new_diag += self.data[y+x][x]
            self.diag_down_right.append(new_diag)

        # Starting at the "top, left" search right and build down
        for x in range(1, self.board_width):
            new_diag = ''
            for y in range(min(self.board_height - x, self.board_width - x)):
                new_diag += self.data[y][x+y]
            self.diag_down_right.append(new_diag)

            # Reverse down-left diag
            for d in self.diag_down_right:
                self.diag_down_right_reversed.append(d[::-1])

        # Group all of the search vectors into a master list that the search() method will iterate on.
        self.search_lists = [self.rows, self.rows_reversed, self.columns,
                             self.columns_reversed, self.diag_down_left,
                             self.diag_down_left_reversed, self.diag_down_right, self.diag_down_right]

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
