class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        map = [0] * len(nums)
        ans = []
        for i in nums :
            if map[i] :
                ans.append(i)
            map[i] += 1
        return ans
