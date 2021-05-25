def myAtoi(s: str) -> int :
    '''This one doesnt work'''
    MAX_NUM = (2**31 - 1)
    MIN_NUM = -(2**31)
    negative_flag = False
    new_int = ''
    non_digit_count = 0

    for character in s :
        # Check if for leading whitespace (only ' ' counts as whitespace)
        if character == ' ' :
            continue
        # Check if either '-' or '+' character is present
        # if '-' the integer is negative
        if character == '-' :
            negative_flag = True
            non_digit_count += 1
            continue
        if character == '+' :
            non_digit_count += 1
            continue
        if non_digit_count > 1 :
            return 0
        # check for alphabet characters and stop if one occurs
        if character.isdigit() :
            new_int = new_int + character
        else :
            break

    if new_int == '' :
        return 0
    else :
        # Get rid of leading zeroes if there are any and convert to int
        new_int = int(new_int.lstrip('0'))

        # Include negative if negative_flag is True
        if negative_flag == True :
            new_int *= -1

        # Check if the integer is within the bounds of the max and min
        if new_int > MAX_NUM :
            return MAX_NUM
        elif new_int < MIN_NUM :
            return MIN_NUM
        else :
            return new_int   

def myAtoi(s: str) -> int :
    '''This one does work'''
    MAX_NUM = (2**31 - 1)
    MIN_NUM = -(2**31)
    negative_flag = False
    s = s.strip()

    if not s :
        return 0
    
    if s[0] == '-' :
        negative_flag = True
    if s[0] == '-' or s[0] == '+' :
        s = s[1:]

    return_val = 0
    for character in s :
        if not character.isdigit() :
            break
        else :
            return_val = return_val * 10 + int(character)


    if negative_flag == True :
        return_val *= -1

    if return_val == 0 :
        return return_val
    
    # Check if the integer is within the bounds of the max and min
    if return_val > MAX_NUM :
        return MAX_NUM
    elif return_val < MIN_NUM :
        return MIN_NUM
    else :
        return return_val