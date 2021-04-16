"""
The node module is used to detect and change the properties of the grids,
and it stores the node list containing nearby open grids for a given instance of a class.
"""

import pygame
from rgbcolors_const import Colors

class Node:
    '''
    This class will track user custom nodes selecting by the coordinates of the spot.
    '''
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x_cord = row * width
        self.y_cord = col * width
        self.color = Colors.WHITE # Blank node color
        self.near_nodes = [] # Possitions of all neighbor nodes near tracked object
        self.width = width
        self.total_rows = total_rows

    # Position returning
    def get_pos(self):
        """Returns node possition."""
        return self.row, self.col

    # Change node color methods
    def is_closed(self):
        """Checks defined color and returns True if node is closed."""
        return self.color == Colors.LIGHT_GREY

    def is_open(self):
        """Checks defined color and returns True if node is opened."""
        return self.color == Colors.GREEN

    def is_bush(self):
        """Checks defined color and returns True if node is bush (wall)."""
        return self.color == Colors.MIRUMEE_BLUE

    def is_start(self):
        """Checks defined color and returns True if node is start point."""
        return self.color == Colors.DARK_BLUE

    def is_end(self):
        """Checks defined color and returns True if node is end point."""
        return self.color == Colors.ORANGE

    # Change node status
    def make_closed(self):
        """Change defined node color and makes it an closed grid."""
        self.color = Colors.LIGHT_GREY

    def make_open(self):
        """Change defined node color and makes it an open grid."""
        self.color = Colors.GREEN

    def make_bush(self):
        """Change defined node color and makes it an bush (wall) grid."""
        self.color = Colors.MIRUMEE_BLUE

    def make_start(self):
        """Change defined node color and makes it an start point grid."""
        self.color = Colors.DARK_BLUE

    def make_end(self):
        """Change defined node color and makes it an end point grid."""
        self.color = Colors.ORANGE

    def make_path(self):
        """Change defined node color and makes it an path grid.
        Used for road backtracking."""
        self.color = Colors.RED

    def reset(self):
        """Change defined color and makes node blank.
        Used to reset whole window."""
        self.color = Colors.WHITE


    # Node drawing
    def draw(self, win):
        """Drawing every node.

            Args:
                win (class): pygame.Surface class
                    Initialized window for display.
        """

        pygame.draw.rect(win, self.color, (self.x_cord, self.y_cord, self.width, self.width))


    # Check possible node neighbors that's not a wall
    def update_near_nodes(self, grid):
        """This method appends an row and column parameter into near_nodes for every node.
        It checks every open node near self in four directions.

            Args:
                grid (list) : Defined x, y coordinates of near grid.
        """

        self.near_nodes = []

        if self.col > 0 and not grid[self.row][self.col - 1].is_bush():
            left_node = grid[self.row][self.col - 1]
            self.near_nodes.append(left_node)

        if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_bush():
            right_node = grid[self.row][self.col + 1]
            self.near_nodes.append(right_node)

        if self.row > 0 and not grid[self.row - 1][self.col].is_bush():
            upper_node = grid[self.row - 1][self.col]
            self.near_nodes.append(upper_node)

        if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_bush():
            lower_node = grid[self.row + 1][self.col]
            self.near_nodes.append(lower_node)

    # Two nodes compare (always False)
    def __lt__(self, other):
        return False
