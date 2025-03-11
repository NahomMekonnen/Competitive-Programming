# Problem: Valid Palindrome II - https://leetcode.com/problems/valid-palindrome-ii/description/

class Solution:
    def validPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1

        while i < j :
            if s[i] != s[j] :
                check1 = s[:j] + s[j+1:]
                check2 = s[:i] + s[i+1:]
                return check1 == check1[::-1] or check2 == check2[::-1]
            i += 1
            j -= 1  
        
        return True