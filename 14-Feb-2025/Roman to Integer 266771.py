# Problem: Roman to Integer - https://leetcode.com/problems/roman-to-integer/?envType=problem-list-v2&envId=string

class Solution:
    def romanToInt(self, s: str) -> int:
        rom = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000,
        }
        ans = 0
        for i in range(len(s) - 1):
            if rom[s[i]] < rom[s[i + 1]]:
                ans -= rom[s[i]]
            else:
                ans += rom[s[i]]
        ans += rom[s[-1]]
        return ans