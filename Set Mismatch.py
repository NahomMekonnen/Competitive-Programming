class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        cnt = Counter(nums)
        ans = [0,0]
        for i in range(1, len(nums) + 1) :
            if cnt[i] > 1 :
                ans[0] = i
            elif cnt[i] == 0 :
                ans[1] = i
        return ans
