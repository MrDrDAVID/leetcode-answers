def isPalindrome(x: int) -> bool :
    string = str(x)
    palindrome_check = ''
    is_palindrome = False

    for l in string :
        palindrome_check = l + palindrome_check

    if string == palindrome_check :
        is_palindrome = True
    
    return is_palindrome