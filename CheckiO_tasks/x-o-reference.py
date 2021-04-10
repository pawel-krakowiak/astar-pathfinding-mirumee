from typing import List

def SignsToNumsConvert(game_result):
    res = [] 

    for three_signs in game_result:
        temp = []
        for i in range(0, 3):
            if three_signs[i] == "X": temp.append(1)
            elif three_signs[i] == "O": temp.append(2)
            else: temp.append(0)
        res.append(temp)

    return res

def CheckWinner(val, pref=""):
    if val == 1: return pref + "Xs wins"
    elif val == 2: return pref + "Os wins"
    else: return "ERROR"


def checkio(game_result: List[str]) -> str:
    res_tab = SignsToNumsConvert(game_result)

    # Check horizontals       
    for line in res_tab:
        if 0 in line: continue
        elif line[0] == line[1] == line[2]:
            return CheckWinner(line[0], "[HORIZONTALS] ")

    # Check verticals
    tmp = []
    for x in range(0,3):
        for y in range(0, 3):
            tmp.append(res_tab[y][x])
            if len(tmp) == 3:
                if tmp[0]==tmp[1]==tmp[2] and not 0 in tmp:
                    return CheckWinner(tmp[0], "[VERTICALS] ")
                else:
                    tmp = []
 
    # Check slants
    tmp = [(res_tab[0][2], res_tab[1][1], res_tab[2][0]), (res_tab[0][0], res_tab[1][1], res_tab[2][2])]
    for s in tmp:
        if s[0]==s[1]==s[2] and not 0 in s:
                return CheckWinner(s[0], "[SLANTS] ")

    return "Draw"
    

if __name__ == '__main__':
    print("Example:")
    print(checkio([ "OO.",
                    "XOO",
                    "OXO"]))
