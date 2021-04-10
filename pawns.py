def safe_pawns(pawns: set) -> int:
    safe_pawns = 0

    # Contain "vertical / horizontal" coord of pawn
    pawn_pos = []

    # Dict for converting every vertical chess coord into index
    let_to_num = {
        "a":1,
        "b":2,
        "c":3,
        "d":4,
        "e":5,
        "f":6,
        "g":7,
        "h":8
    }

    for pawn in list(pawns):
        # Indexing letters (columns)
        if pawn[0] in let_to_num.keys():
            p_ver = let_to_num[pawn[0]]

        # Indexing rows
        p_hor = pawn[1]
        pawn_pos.append(str(p_ver)+str(p_hor))
    

    for pawn_cord in pawn_pos:
        # Setting properly pawn's defenders possitions (both corners)
        defender_1 = "{}{}".format(int(pawn_cord[0]) - 1, int(pawn_cord[1]) - 1)
        defender_2 = "{}{}".format(int(pawn_cord[0]) + 1, int(pawn_cord[1]) - 1)
            
        # Checking if coords of defenders is on chessboard    
        if defender_1 in pawn_pos or defender_2 in pawn_pos:
            safe_pawns += 1

    return safe_pawns

if __name__ == '__main__':
    pass
    #These "asserts" using only for self-checking and not necessary for auto-testing
    print(safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}))
    # assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1