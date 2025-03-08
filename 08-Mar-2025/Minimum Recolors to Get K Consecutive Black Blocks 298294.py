# Problem: Minimum Recolors to Get K Consecutive Black Blocks - https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        ans = 101
        for i in range(len(blocks) - k + 1):
            count = 0 
            for j in range(i,i+k) :
                if blocks[j]=="W" :
                    count += 1
            ans = min(ans,count)
        return ans