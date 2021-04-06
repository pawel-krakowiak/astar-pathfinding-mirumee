def checkio(array: list) -> int:
    return sum([i for i in array[::2]]) * array[-1] if array else 0

checkio = lambda array: sum([i for i in array[::2]]) * array[-1] if array else 0

print(checkio([-37,-36,-19,-99,29,20,3,-7,-64,84,36,62,26,-76,55,-24,84,49,-65,41]))

x = [-37,-36,-19,-99,29,20,3,-7,-64,84,36,62,26,-76,55,-24,84,49,-65,41]