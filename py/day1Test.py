def canPermutePalindrome(s):
    result = 0
    for c in s:
        result ^= 1 << ord(c)
    res = result & (result - 1) == 0
    return result & (result - 1) == 0
canPermutePalindrome("abbac")
