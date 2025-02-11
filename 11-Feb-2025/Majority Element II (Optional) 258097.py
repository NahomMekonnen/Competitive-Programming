# Problem: Majority Element II (Optional) - https://leetcode.com/problems/majority-element-ii/

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        ans = [i for i in count if count[i] > (len(nums)//3)]
        return ans
