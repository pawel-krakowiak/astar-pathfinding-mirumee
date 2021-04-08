# https://stackoverflow.com/a/4842897
def merge_common(data):
    out = []
    while len(data) > 0:
        first, *rest = data
        first = set(first)

        lf = -1
        while len(first) > lf:
            lf = len(first)

            rest2 = []
            for r in rest:
                if len(first.intersection(set(r))) > 0:
                    first |= set(r)
                else:
                    rest2.append(r)
            rest = rest2

        out.append(list(first))
        data = rest
    return out


def scan_letters_before(data):
    letters_before = {}
    for word in data:
        for i in range(1, len(word)):
            letters_before[word[i]] = "".join(set(letters_before.get(word[i], "") + word[:i]))
    return letters_before


def checkio(data):
    # remove duplicates
    for i in range(len(data)):
        # https://stackoverflow.com/a/9841328
        data[i] = "".join(dict.fromkeys(data[i]))

    groups = merge_common(data)
    letters_before = scan_letters_before(data)

    for group in groups:
        # find first letter
        firsts = []
        for i in group:
            if i not in letters_before:
                firsts.append(i)
        for i in firsts:
            group.remove(i)
        firsts.sort()
        group[0:0] = firsts

        for _ in range((len(group) - 1) * 2):
            i = len(firsts)
            # find next not in order
            try:
                while set(letters_before[group[i]]).issubset(set(group[:i])):
                    i += 1
            except (IndexError, KeyError):
                continue

            # reorder if before expected letters
            while not set(letters_before[group[i]]).issubset(set(group[:i])):
                group.insert(i + 1, group.pop(i))
                i += 1

    # resolve alphabetical order
    for group in groups:
        for _ in range(len(group) - 1):
            for i in range(1, len(group)):
                if group[i] in letters_before and group[i - 1] not in letters_before[group[i]]:
                    if ord(group[i - 1]) > ord(group[i]):
                        group.insert(i, group.pop(i - 1))

    # merge groups
    result = []
    for group in groups:
        sorted_result = result[:]
        sorted_result.append(group[0])
        sorted_result.sort()
        index = sorted_result.index(group[0])
        if index == 0:
            result[0:0] = group
        else:
            letter_before = sorted_result[index - 1]
            b_index = result.index(letter_before)
            result[b_index + 1:b_index + 1] = group

    result = "".join(result)
    return result

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(["acb", "bd", "zwa"]) == "zwacbd", \
        "Just concatenate it"
    assert checkio(["klm", "kadl", "lsm"]) == "kadlsm", \
        "Paste in"
    assert checkio(["a", "b", "c"]) == "abc", \
        "Cant determine the order - use english alphabet"
    assert checkio(["aazzss"]) == "azs", \
        "Each symbol only once"
    assert checkio(["dfg", "frt", "tyg"]) == "dfrtyg", \
        "Concatenate and paste in"
