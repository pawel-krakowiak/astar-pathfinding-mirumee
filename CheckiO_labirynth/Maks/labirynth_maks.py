from typing import List


def find_next(cords, maze_map):
    x, y = cords
    # direction delta
    directions = {"N": (0, -1), "S": (0, 1), "W": (-1, 0), "E": (1, 0)}

    # find every possible direction
    possible_directions = []
    for direction, delta in directions.items():
        new_x, new_y = x + delta[0], y + delta[1]
        if maze_map[new_y][new_x] == 0:
            possible_directions.append(delta)

    if possible_directions:
        return tuple(possible_directions)
    else:
        return None


def find_shortest_path(maze_map):
    step = maze_map[1][1]
    x, y = (1, 1)
    steps = []
    # dumb pathfinder
    while step != 2:
        step -= 1
        if maze_map[y][x + 1] == step:
            x += 1
            steps.append("E")
        elif maze_map[y][x - 1] == step:
            x -= 1
            steps.append("W")
        elif maze_map[y + 1][x] == step:
            y += 1
            steps.append("S")
        elif maze_map[y - 1][x] == step:
            y -= 1
            steps.append("N")

    return "".join(steps)


def checkio(maze_map: List[List[int]]) -> str:
    # init
    maze_map[10][10] = 2
    paths = {(10, 10)}
    step = 2

    # handle every branch of the path
    while (1, 1) not in paths:
        step += 1
        for x, y in set(paths):
            paths.remove((x, y))
            next_steps = find_next((x, y), maze_map)

            # if not dead end
            if next_steps is not None:
                # for every new branch
                for delta_x, delta_y in next_steps:
                    paths.add((x + delta_x, y + delta_y))
                    maze_map[y + delta_y][x + delta_x] = step

    result = find_shortest_path(maze_map)
    return result
