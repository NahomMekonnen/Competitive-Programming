# Problem: Longest Common Prefix - https://leetcode.com/problems/longest-common-prefix/

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs = sorted(strs)
        wrd1 ,wrd2 = strs[0], strs[-1]
        i, j = 0 , 0
        while ( i < len(wrd1) and j < len(wrd2)) :
            if ( wrd1[i] == wrd2[j]) :
                i += 1
                j += 1
            else : 
                break
        return wrd1[:i]