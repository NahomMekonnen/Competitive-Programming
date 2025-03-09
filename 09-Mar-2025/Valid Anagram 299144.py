# Problem: Valid Anagram - https://leetcode.com/problems/valid-anagram/description/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        arr1, arr2 = [0] * 26, [0] * 26
        if len(s) != len(t) :
            return False
        
        for i in range(len(s)) :
            arr1[ord(s[i])-ord('a')]+= 1
            arr2[ord(t[i])-ord('a')]+= 1
        
        return arr1 == arr2