def ziggy_zag(s: str, numRows: int) -> str :
    zig_zag = [''] * numRows
    row_num = 0
    ziggy_move = 1

    for zigs in range(len(s)) :
        zig_zag[row_num] = zig_zag[row_num] + s[zigs]
        if row_num < numRows - 1 and ziggy_move == 1 :
            row_num += 1
        elif row_num > 0 and ziggy_move == -1 :
            row_num -= 1
        else :
            ziggy_move *= -1
            row_num += ziggy_move
    
    return ''.join(zig_zag)
