# Problem: Left-and-right-sum-differences - https://leetcode.com/problems/left-and-right-sum-differences/

class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        leftSum, rightSum = [0], [0]
        i, j, s1, s2 = 1, len(nums) - 2, 0, 0
        while i < len(nums) and j > -1 :
            s1 += nums[i-1]
            s2 += nums[j+1]
            leftSum.append(s1)
            rightSum.append(s2)
            i += 1
            j -= 1
        rightSum.reverse()
        return [abs(leftSum[i]-rightSum[i]) for i in range(len(leftSum))] 