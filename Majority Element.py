class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        elements = Counter(nums)
        n = len(nums)//2
        ans = [i for i in elements if elements[i] > n]
        return ans[0]
