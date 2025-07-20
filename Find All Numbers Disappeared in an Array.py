class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        check = defaultdict(int)
        for i in nums :
            check[i] += 1
        
        ans = []
        for i in range(1,len(nums) + 1) :
            if check[i] == 0 :
                ans.append(i)
        return ans
