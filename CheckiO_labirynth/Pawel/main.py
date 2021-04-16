"""
Program for visualization of the A * pathfinding algorithm based on heuretics.
The algorithm guarantees finding the shortest path from the START to END point,
taking into account the walls blocking the algorithm's movement.
Based on the implementation of the Open Labyrinth CheckIO task.
https://py.checkio.org/en/mission/open-labyrinth/

Default keys:
LMB : Set the start / Set end / Create a bush (wall).
RMB : Clear node.
SPACEBAR : Run the algorithm.
C : Reset
"""

import pygame
from astar_algorithm import algorithm
from grids_draw_module import make_grid, draw, get_mouse_clicked_pos

WIDTH = 800
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("CheckIO Open Labyrinth A* Pathfinding Solution (Visualization)")

def main(win, width=800):
    """Main loop function applies window settings, hooks key events and controls other modules.

    Args:
        win (pygame.Surface class) : Initialized window for display.
        width (int) : Window size (default = 800).

    Notes:
        Used module algorithm and grids_draw_module.
    """
    start_key = pygame.K_SPACE
    rows = 50

    start = None # Start possition
    end = None # End possition
    run = True  # Is application run
    grid = make_grid(rows, width)

    while run:
        draw(win, grid, rows, width)
        for event in pygame.event.get():
            # Quit event
            if event.type == pygame.QUIT:
                run = False

            if pygame.mouse.get_pressed()[0]: # LMB
                pos = pygame.mouse.get_pos()
                row, col = get_mouse_clicked_pos(pos, rows, width)
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
                row, col = get_mouse_clicked_pos(pos, rows, width)
                spot = grid[row][col]
                spot.reset()
                if spot == start:
                    start = None
                elif spot == end:
                    end = None

            # Algorithm start
            if event.type == pygame.KEYDOWN:
                if event.key == start_key and start and end:
                    for row in grid:
                        for spot in row:
                            spot.update_near_nodes(grid)

                    algorithm(lambda: draw(win, grid, rows, width), grid, start, end)

                if event.key == pygame.K_c:
                    start = None
                    end = None
                    grid = make_grid(rows, width)
    pygame.quit()

main(WIN, WIDTH)
