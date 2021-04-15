import pygame
import math

from rgbcolors_const import Colors
from node_module import Node
from astar_algorithm import algorithm, heuristic, backtrack_path
from grids_draw_module import *

WIDTH = 800
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("CheckIO Open Labyrinth A* Pathfinding Solution (Visualization)")

def main(win, width, ROWS=50):
    START_KEY = pygame.K_SPACE
    start = None # Start possition
    end = None # End possition
    run = True  # Is application run
    
    grid = make_grid(ROWS, width)

    while run:
        draw(win, grid, ROWS, width)
        for event in pygame.event.get():
            # Quit event
            if event.type == pygame.QUIT:
                run = False
            
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
                if event.key == START_KEY and start and end:
                    print("ALGORITHM STARTED")
                    for row in grid:
                        for spot in row:
                            spot.update_near_nodes(grid)
                    
                    algorithm(lambda: draw(win, grid, ROWS, width), grid, start, end)

                if event.key == pygame.K_c:
                    start = None
                    end = None
                    grid = make_grid(ROWS, width)
    pygame.quit()

main(WIN, WIDTH, 50)