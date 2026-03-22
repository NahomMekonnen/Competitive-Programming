class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        ans = 0
        for i in strs :
            if i.isdigit() :
                ans = max(int(i), ans)
            else :
                ans = max(len(i),ans)
        return ans
