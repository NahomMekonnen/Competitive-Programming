# Problem: Minimum Processing Time - https://leetcode.com/problems/minimum-processing-time/

class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort(reverse=True)
        processorTime.sort()
        ans, j = 0, 0
        for i in range(len(processorTime)) :
            ans = max(ans, processorTime[i] + tasks[j])
            j += 4
        return ans