from rgbcolors_const import Colors
from node_module import Node
import pygame

# Generating grid on whole window
def make_grid(rows, width):
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
    grid_gap = width // rows
    for i in range(rows):
        pygame.draw.line(win, Colors.GREY, (0, i * grid_gap), (width, i * grid_gap))
        for j in range(rows):
            pygame.draw.line(win, Colors.GREY, (j * grid_gap, 0), (j * grid_gap, width))

# Draw all elements
def draw(win, grid, rows, width):
    win.fill(Colors.WHITE)

    for row in grid:
        for node in row:
            node.draw(win)

    draw_grid(win, rows, width)
    pygame.display.update()

# Detecting mouse clicked possition
def getMouse_clicked_pos(pos, rows, width):
    grid_gap = width // rows
    y, x = pos

    row = y // grid_gap
    col = x // grid_gap

    return row, col