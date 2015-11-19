COLS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

def safe_pawns(pawns):
    
    res = {}
    
    for pawn in pawns:
        for hit in pawn_hits(pawn):
            if hit in pawns:
                res[hit] = 1
    
    return len(res)
    

def pawn_hits(pawn):
    col, row = pawn[0], int(pawn[1])
    row = '' if row == 8 else 1 + row
    hit_left = ''.join(('' if col == 'a' else COLS[COLS.index(col) - 1], str(row)))
    hit_right = ''.join(('' if col == 'h' else COLS[COLS.index(col) + 1], str(row)))
    
    return (hit_left, hit_right)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    assert safe_pawns({"a1","b2","c3","d4","e5","f6","g7","h8"}) == 7
    