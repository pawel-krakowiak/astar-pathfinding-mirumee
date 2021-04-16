from queue import PriorityQueue
import pygame

def heuristic(st_pos, end_pos):
    # H(n) - Current node to end_node general distance
    st_st, end_st = st_pos
    st_sec, end_sec = end_pos
    return abs(st_st - st_sec) + abs(end_st - end_sec)

def backtrack_path(last_node, current, draw):
    while current in last_node:
        current = last_node[current]
        current.make_path()
        draw()

def algorithm(draw, grid, start, end):
    count = 0 # Counting steps
    open_set = PriorityQueue() # Always get the smallest element from open_set
    open_set.put((0, count, start)) # Put start node into open set
    last_node = {} # Dictionary that explains path step-by-step from backtrack
    # Track current shortest distance from start to node
    g_value = {spot: float("inf") for row in grid for spot in row}
    g_value[start] = 0 # g value of start is always zero
    # Track predicted distance from end to this node
    f_value = {spot: float("inf") for row in grid for spot in row}
    f_value[start] = heuristic(start.get_pos(), end.get_pos()) # heuristic distance

    open_set_hash = {start}

    while not open_set.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current = open_set.get()[2]
        open_set_hash.remove(current)

        if current == end:
            backtrack_path(last_node, end, draw)
            end.make_end()
            return True # We found the path
        for near in current.near_nodes:
            temp_g_value = g_value[current] + 1

            if temp_g_value < g_value[near]:
                last_node[near] = current
                g_value[near] = temp_g_value
                f_value[near] = temp_g_value + heuristic(near.get_pos(), end.get_pos())
                if near not in open_set_hash:
                    count += 1
                    open_set.put((f_value[near], count, near))
                    open_set_hash.add(near)
                    near.make_open()
        draw()

        if current != start:
            current.make_closed()
    return False
