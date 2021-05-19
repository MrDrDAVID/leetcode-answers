def reverse(x: int) -> int:
    int_string = str(x) 
    result = 0
    reversed_int = ''

    if '-' in int_string :
        for char in int_string[1:] :
            reversed_int = char + reversed_int

        result = int('-' + reversed_int)

    else :
        for char in int_string :
            reversed_int = char + reversed_int

        result = int(reversed_int)

    if result > 2**31 - 1 or result < -2**31 :
        return 0
    else :
        return result