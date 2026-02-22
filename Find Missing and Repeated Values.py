class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        ans, nums = [], [0] * (len(grid) ** 2 + 1)
        for i in grid :
            for j in i :
                if nums[j] == 1 :
                    ans.append(j)
                nums[j] += 1

        for i in range(1,len(nums)) :
            if nums[i] == 0 :
                ans.append(i)
                break
        return ans
