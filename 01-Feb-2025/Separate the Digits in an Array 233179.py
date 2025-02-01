# Problem: Separate the Digits in an Array - https://leetcode.com/problems/separate-the-digits-in-an-array/description/

class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            temp = []
            while nums[i] > 0:
                temp.append(nums[i]%10)
                nums[i] //= 10
            ans += temp[::-1]
        return ans