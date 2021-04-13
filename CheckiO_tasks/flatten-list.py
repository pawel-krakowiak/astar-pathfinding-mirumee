def flat_list(arrat):
    res = []
    for value in arrat:
        if isinstance(value, list):
          res += flat_list(value)
        else:
          if isinstance(value, int):
            res.append(value)
    return res  
            

print(flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]))

# if __name__ == '__main__':
#     assert flat_list([1, 2, 3]) == [1, 2, 3], "First"
#     assert flat_list([1, [2, 2, 2], 4]) == [1, 2, 2, 2, 4], "Second"
#     assert flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]) == [2, 4, 5, 6, 6, 6, 6, 6, 7], "Third"
#     assert flat_list([-1, [1, [-2], 1], -1]) == [-1, 1, -2, 1, -1], "Four"
