def lengthOfLongestSubstring(s: str) -> int:
    substring_dict = {}
    substring = ''
    max_substring = 0

    if s == '' :
        return 0

    if s == ' ' or len(s) == 1 :
        return 1
        
    
    for index1, letter in enumerate(s) :
        letter_dict = {}
        letter_dict[letter] = 1
        substring = letter

        for index2 in range(index1 + 1, len(s)) :
            if s[index2] in letter_dict.keys() :
                substring_dict[substring] = len(substring)
                break

            letter_dict[s[index2]] = 1
            substring += s[index2]
            substring_dict[substring] = len(substring)

    for value in substring_dict.values() :
        if value > max_substring :
            max_substring = value

    return max_substring


string = 'au'
num = lengthOfLongestSubstring(string)
print(num)

string1 = 'abcddgfe'
num1 = lengthOfLongestSubstring(string1)
print(num1)