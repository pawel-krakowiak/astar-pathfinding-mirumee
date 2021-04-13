from typing import Iterable

def except_zero(items: list) -> Iterable:
    null_index = []
    for val in items:
        if val == 0:
            null_index.append(items.index(val))
            items[items.index(val)] = float('inf')

    items = sorted(items)

    if null_index:
        for index in null_index:
            items.insert(index, 0)
        return items[:-(len(null_index))]
    else:
        return items

if __name__ == '__main__':
    print("Example:")
    print(except_zero([5, 3, 0, 0, 4, 1, 4, 0, 7]))

