import re

def first_word(text: str) -> str:
    for e in text.split(" "):
        if e and e[0].isalpha():
            
            if not str(e[-1]).isalpha():
                return e[:-1]
            else:
                return re.split("[?.,]", e)[0]
            


print(first_word("Hello.World"))
