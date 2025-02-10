# Problem: Group Anagrams - https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a = defaultdict(list)
        for word in strs:
            w = list(word)
            w.sort()
            key  = "".join(w)
            a[key].append(word)
        ans = [value for key, value in a.items()]
        return ans