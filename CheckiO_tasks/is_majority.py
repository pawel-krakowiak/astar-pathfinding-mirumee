def is_majority(items: list) -> bool:
    return sum(items) > len(items)//2



if __name__ == '__main__':
    print("Example:")
    print(is_majority([True, True, False, False]))


