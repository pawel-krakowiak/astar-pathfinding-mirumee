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
        return self.row, self.col


    # Change node color methods
    def is_closed(self):
        return self.color == Colors.LIGHT_GREY
    def is_open(self):
        return self.color == Colors.GREEN

    def is_bush(self):
        return self.color == Colors.MIRUMEE_BLUE

    def is_start(self):
        return self.color == Colors.DARK_BLUE

    def is_end(self):
        return self.color == Colors.ORANGE

    # Change node status
    def make_closed(self):
        self.color = Colors.LIGHT_GREY

    def make_open(self):
        self.color = Colors.GREEN

    def make_bush(self):
        self.color = Colors.MIRUMEE_BLUE

    def make_start(self):
        self.color = Colors.DARK_BLUE

    def make_end(self):
        self.color = Colors.ORANGE

    def make_path(self):
        self.color = Colors.RED

    def reset(self):
        self.color = Colors.WHITE


    # Node drawing
    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x_cord, self.y_cord, self.width, self.width))


    # Check possible node neighbors that's not a wall
    def update_near_nodes(self, grid):
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
