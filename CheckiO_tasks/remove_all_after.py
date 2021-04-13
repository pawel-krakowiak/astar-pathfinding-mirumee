from typing import Iterable

def remove_all_after(items, border):
    if not border in items:
        return items
    elif len(items)>0:
        return items[:items.index(border)+1]
    return []

if __name__ == '__main__':
    print("Example:")
    # print(list(remove_all_after([1, 2, 7, 4, 5], 7)))
    print(remove_all_after([2,3,3,0,3,4], 0))