# Problem: Valid Palindrome II - https://leetcode.com/problems/valid-palindrome-ii/description/

class Solution:
    def validPalindrome(self, s: str) -> bool:
        i, j, once = 0, len(s) - 1, False
        check1, check2 = "", ""
        while i < j :
            if s[i] != s[j] :
                check1 = s[:j] + s[j+1:]
                check2 = s[:i] + s[i+1:]
                break
            i += 1
            j -= 1  
        print(check1,check2)
        
        both = 0
        i = 0
        j = len(check1) -1

        while i <= j :
            if check1[i] != check1[j] :
                both += 1
                break
            i += 1
            j -= 1

        i = 0 
        j = len(check2) - 1

        while i <= j :
            if check2 [i] != check2[j] :
                both += 1
                break
            i += 1
            j -= 1


        return False if both == 2 else True