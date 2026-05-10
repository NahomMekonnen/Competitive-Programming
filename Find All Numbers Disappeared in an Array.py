class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        arr = [0] * len(nums)
        for i in nums :
            arr[i-1] += 1
        return [i + 1 for i in range(len(arr)) if arr[i] == 0]
