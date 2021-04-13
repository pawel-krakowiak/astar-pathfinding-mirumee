import collections

def translate(phrase):
    VOWELS = "aeiouy"
    phrase = list(phrase)
    res = ""
    for s in phrase:
        if s and s != " ":
            if s in VOWELS:
                del phrase[phrase.index(s)+1:(phrase.index(s)+3)]
            else:
                del phrase[phrase.index(s)+1]
        res += s
            
    return res


if __name__ == '__main__':
    print("Example:")
    print(translate("hoooowe yyyooouuu duoooiiine"))
