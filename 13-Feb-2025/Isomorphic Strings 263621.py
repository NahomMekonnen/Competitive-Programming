# Problem: Isomorphic Strings - https://leetcode.com/problems/isomorphic-strings/

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map1, map2 = [0] * 128, [0] * 128
        for i in range(len(s)):
            s1 , t1 = ord(s[i]), ord(t[i])
            if map1[s1] != map2[t1] :
                return False
            map1[s1] = i+1
            map2[t1] = i+1
        return True