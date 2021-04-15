import pygame
import math
from queue import PriorityQueue
# PriorityQueue --> https://docs.python.org/3/library/queue.html


'''
TASK DESCRIPTION:
The labyrinth has no walls, but bushes surround the path on each side.
If a players move into a bush, they lose. The labyrinth is presented as a matrix (a list of lists): 1
is a bush and 0 is part of the path.
The labyrinth's size is 12 x 12 and the outer cells are also bushes.
Players start at cell (1,1). The exit is at cell (10,10).
You need to find a route through the labyrinth. Players can move in only four directions--South
(down [1,0]), North (up [-1,0]), East (right [0,1]), West (left [0, -1]). The route is described
 as a string consisting of different characters: "S"=South, "N"=North, "E"=East, and "W"=West.

Checkio Task (Open Labirynth) - https://py.checkio.org/pl/mission/open-labyrinth/
'''


# Window display settings
WIDTH = 800
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("CheckIO Open Labyrinth A* Pathfinding Solution (Visualization)")

# Colors consants
MIRUMEE_BLUE = (44, 143, 162) # Bushes color
DARK_BLUE = (0, 0, 139)  # Start (player) color

WHITE = (255, 255, 255) # Blank node
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 225, 0) # Open node
BLUE = (0, 255, 0)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0) # End node
GREY = (169, 169, 169) # Path color
TURQ = (64, 224, 208)

class Node:
    '''
    This class will track user custom nodes selecting by the coordinates of the spot.
    '''
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = WHITE # Blank node color
        self.near_nodes = [] # Possitions of all neighbor nodes near tracked object
        self.width = width
        self.total_rows = total_rows

    # Position returning
    def get_pos(self):
        return self.row, self.col


    # Change node color methods
    def is_closed(self):
        return self.color == RED

    def is_open(self):
        return self.color == GREEN

    def is_bush(self):
        return self.color == MIRUMEE_BLUE

    def is_start(self):
        return self.color == DARK_BLUE

    def is_end(self):
        return self.color == ORANGE

    def reset(self):
        self.color = WHITE


    # Change node status
    def make_closed(self):
        self.color = RED
    
    def make_open(self):
        self.color = GREEN

    def make_bush(self):
        self.color = MIRUMEE_BLUE
        print("Bush Created [{}, {}]".format(self.x, self.y))
    
    def make_start(self):
        self.color = DARK_BLUE
        print("Start Created [{}, {}]".format(self.x, self.y))

    def make_end(self):
        self.color = ORANGE
        print("End Created [{}, {}]".format(self.x, self.y))
    
    def make_path(self):
        self.color = GREY
        print("Path Created [{}, {}]".format(self.x, self.y))


    # Node drawing
    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

    # TODO (Check possible node neighbors that's not a wall)
    def update_near_nodes(self, grid):
        # 0
        # 1
        # 2
        # 3
        # 4
        # (total_rows)

        self.near_nodes = []
        if self.col > 0 and not grid[self.row][self.col - 1].is_bush(): # LEFT CHECK
            self.near_nodes.append(grid[self.row][self.col - 1])

        if self.row > 0 and not grid[self.row - 1][self.col].is_bush(): # UP CHECK
            self.near_nodes.append(grid[self.row - 1][self.col])


        if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_bush(): # RIGHT CHECK
            self.near_nodes.append(grid[self.row][self.col + 1])

        if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_bush(): # DOWN CHECK
            self.near_nodes.append(grid[self.row + 1][self.col])

    # Two nodes compare (always False)
    def __lt__(self, other):
        return False

# H(n) - Current node to end_node general distance    
def h(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)

def AS_algorithm(draw, grid, start, end):
    countNode = 0 # Counting steps 
    open_set = PriorityQueue()
    open_set.put((0, countNode, start))
    last_node = {} # Dictionary that explains path step-by-step from backtrack
    g_value = {spot: float("inf") for row in grid for spot in row}
    g_value[start] = 0
    f_value = {spot: float("inf") for row in grid for spot in row}
    f_value[start] = h(start.get_pos(), end.get_pos())

    open_set_hash = {start}



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
        pygame.draw.line(win, GREY, (0, i * grid_gap), (width, i * grid_gap))
        for j in range(rows):
            pygame.draw.line(win, GREY, (j * grid_gap, 0), (j * grid_gap, width))

# Draw all elements
def draw(win, grid, rows, width):
    win.fill(WHITE)

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

# Main loop for basic functions
def main(win, width):
    START_KEY = pygame.K_SPACE
    ROWS = 12 # Window size
    grid = make_grid(ROWS, width) # Grid generate

    start = None # Start possition
    end = None # End possition

    run = True  # Is application run
    started = False # Is algorithm started
    
    while run:
        draw(win, grid, ROWS, width)
        for event in pygame.event.get():
            # Quit event
            if event.type == pygame.QUIT:
                run = False

            if started:
                continue
            
            if pygame.mouse.get_pressed()[0]: # LMB
                pos = pygame.mouse.get_pos()
                row, col = getMouse_clicked_pos(pos, ROWS, width)
                spot = grid[row][col]
                # Always dreate start first if not exists...
                if not start and spot != end:
                    start = spot
                    start.make_start()

                # ...otherwise make end
                elif not end and spot != start:
                    end = spot
                    end.make_end()
                
                # If start and end exists make a bush
                elif spot != end and spot != start:
                    spot.make_bush()

            elif pygame.mouse.get_pressed()[2]: # RMB
                pos = pygame.mouse.get_pos()
                row, col = getMouse_clicked_pos(pos, ROWS, width)
                spot = grid[row][col]
                spot.reset()
                if spot == start:
                    start = None
                elif spot == end:
                    end = None

            # Algorithm start
            if event.type == pygame.KEYDOWN:
                if event.key == START_KEY and not started:
                    print("ALGORITHM STARTED")
                    for row in grid:
                        for spot in row:
                            spot.update_near_nodes()
                    
                    AS_algorithm(lambda: draw(win, grid, ROWS, width), grid, start, end)
    pygame.quit()

main(WIN, WIDTH)