# Problem: Longest Substring Without Repeating Characters - https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r, ans = 0, 0, 0
        map = defaultdict(int)  
        while r < len(s) :
            map[s[r]] += 1
            while map[s[r]] > 1 :
                map[s[l]] -= 1
                l += 1
            ans = max(r-l+1,ans)
            r += 1
        return ans
