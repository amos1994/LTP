# Do not import any modules. If you do, the tester may reject your submission.

# Constants for the contents of the maze.

# The visual representation of a wall.
WALL = '#'

# The visual representation of a hallway.
HALL = '.'

# The visual representation of a brussels sprout.
SPROUT = '@'

# Constants for the directions. Use these to make Rats move.

# The left direction.
LEFT = -1

# The right direction.
RIGHT = 1

# No change in direction.
NO_CHANGE = 0

# The up direction.
UP = -1

# The down direction.
DOWN = 1

# The letters for rat_1 and rat_2 in the maze.
RAT_1_CHAR = 'J'
RAT_2_CHAR = 'P'


class Rat:

    def __init__(self, symbol, row, col):
        self.symbol = symbol
        self.row = row
        self.col = col
        self.num_sprouts_eaten = 0

    def set_location(self, row, col):
        self.row = row
        self.col = col

    def eat_sprout(self):
        self.num_sprouts_eaten = self.num_sprouts_eaten + 1

    def __str__(self):
        return str(self.symbol) + ' at (' + str(self.row) + ', ' + str(self.col) + ') ate ' + str(self.num_sprouts_eaten) + ' sprouts.'

class Maze:

    def __init__(self, maze, rat_1, rat_2):
        self.maze = maze
        self.rat_1 = rat_1
        self.rat_2 = rat_2

        sprouts_left = 0;
        for lst in maze:
            for item in lst:
                if item == '@':
                    sprouts_left = sprouts_left + 1

        self.num_sprouts_left = sprouts_left

    def is_wall(self, row, col):
        return True if self.maze[row][col] == '#' else False

    def get_character(self, row, col):
        if self.rat_1.row == row and  self.rat_1.col == col:
            return self.rat_1.symbol
        elif self.rat_2.row == row and  self.rat_2.col == col:
            return self.rat_2.symbol
        else:
            return self.maze[row][col]

    def move(self, rat, row, col):
        col = rat.col + col
        row = rat.row + row
        if self.is_wall(row, col) != True:
            if self.get_character(row, col) == '@':
                self.maze[row][col] = '.'
                self.num_sprouts_left = self.num_sprouts_left - 1
                rat.num_sprouts_eaten = rat.num_sprouts_eaten + 1

            rat.row = row
            rat.col = col
            return True

    def __str__(self):
        str = ''
        for idy, lst in enumerate(self.maze):
            for idx, itm in enumerate(lst):
                str  = str + self.get_character(idy, idx)
            str = str + '\n'

        return str + self.rat_1.__str__() + '\n' + self.rat_2.__str__()