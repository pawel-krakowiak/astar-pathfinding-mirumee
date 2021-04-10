def checkio(array):
    if array:
      result = sum(array[::2]) * array[-1]
    else:
      return result

# print(x)
print(checkio([-37,-36,-19,-99,29,20,3,-7,-64,84,36,62,26,-76,55,-24,84,49,-65,41]))