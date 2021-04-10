def checkio(words: str) -> bool:
    c = 0
    
    for word in words.split(" "):
        if not word.lower().isdigit():
            c += 1
        else:
            c = 0
        if c >= 3:
            return True

    return False

print(checkio("Hello World hello"))