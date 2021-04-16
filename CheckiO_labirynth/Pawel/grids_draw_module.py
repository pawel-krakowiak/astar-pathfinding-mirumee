"""
Grids draw module is responsible for creating and displaying grids on the board
and detecting the clicked node, taking into account its coordinates.
The module is based on the pygame library.
"""
import pygame
from rgbcolors_const import Colors
from node_module import Node

# Generating grid on whole window
def make_grid(rows, width):
    """Creating list range of nodes determines how much rows will be in program
        Args:
            rows (int) : Determine the size of square board.
            width (int) : Window size (default = 800).

        Return:
            grid (list) : Node objects
    """
    grid = []
    gap = width // rows
    for row in range(rows):
        grid.append([])
        for col in range(rows):
            node = Node(row, col, gap, rows)
            grid[row].append(node)

    return grid

# Display gird and make outlines for every grid
def draw_grid(win, rows, width):
    """Displays grids on board

        Args:
            win (pygame.Surface class) : Initialized window for display.
            rows (int) : Determine the size of square board.
            width (int) : Window size (default = 800).
    """
    grid_gap = width // rows
    for i in range(rows):
        pygame.draw.line(win, Colors.GREY, (0, i * grid_gap), (width, i * grid_gap))
        for j in range(rows):
            pygame.draw.line(win, Colors.GREY, (j * grid_gap, 0), (j * grid_gap, width))

# Draw all elements
def draw(win, grid, rows, width):
    """Displays blank nodes on board

    Args:
        win (pygame.Surface class) : Initialized window for display.
        grid (list) : Node objects
        rows (int) : Determine the size of square board.
        width (int) : Window size (default = 800).
    """
    win.fill(Colors.WHITE)

    for row in grid:
        for node in row:
            node.draw(win)

    draw_grid(win, rows, width)
    pygame.display.update()

# Detecting mouse clicked possition
def get_mouse_clicked_pos(pos, rows, width):
    """Returns coordinates of clicked mouse possition

    Args:
        pos (list) : pygame x, y possition
        rows (int) : Determine the size of square board.
        width (int) : Window size (default = 800).

    Return:
        row (int) : row possition of clicked node.
        col (int) : column possition of clocked node.
    """
    grid_gap = width // rows
    cord1, cord2 = pos

    row = cord1 // grid_gap
    col = cord2 // grid_gap

    return row, col
