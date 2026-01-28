class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        cnt = Counter(nums) 
        ans = []
        for i in cnt :
            if cnt[i] > 1 :
                ans.append(i)
        for i in range(1,len(nums)+1) :
            if cnt[i] == 0 :
                ans.append(i)
        return ans
