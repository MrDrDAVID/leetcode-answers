def longest_palindrome(s: str) -> str :
    '''Searching for the answer to better understand the problem'''
    max_len = 1
    start = 0
    low = 0
    high = 0

    for i in range(1, len(s)) :
        low = i - 1
        high = i
        while low >= 0 and high < len(s) and s[low] == s[high] :
            if high - low + 1 > max_len :
                start = low
                max_len = high - low + 1
            low -= 1
            high += 1

        low = i - 1
        high = i + 1
        while low >= 0 and high < len(s) and s[low] == s[high] :
            if high - low + 1 > max_len :
                start = low
                max_len = high - low + 1
            low -= 1
            high += 1

    return s[start:start + max_len]

def longestPalindrome(s: str) -> str :
    '''My failed attempt at solving the longest palindrome'''
    substring = ''
    lps = ''
    palindromes = []

    if s == None or s == '' :
        return ''

    if len(s) == 1 :
        lps = s[0]
        return lps

    x = 0
    while x < len(s) :
        for letter in s[x:] :
            palindrome_check = ''

            substring = substring + letter 

            for character in substring :
                palindrome_check = character + palindrome_check

            if palindrome_check == substring :
                palindromes.append(substring)   

        x += 1
        substring = ''

    for palindrome in palindromes :
        if len(palindrome) > len(lps) :
            lps = palindrome

    if not palindromes :
        return s[0]

    return lps 

print(longestPalindrome('dad'))   
print(longestPalindrome('racecar'))
print(longest_palindrome('racecar'))