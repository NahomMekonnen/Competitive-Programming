# Problem: Longest Substring Without Repeating Characters - https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0
        for i in range(len(s)) :
            count, check = 0, defaultdict(int)
            for j in range(i,len(s)) :
                if check[s[j]] :
                    break
                count += 1
                check[s[j]] += 1
            maxLen = max(count,maxLen)

        return maxLen