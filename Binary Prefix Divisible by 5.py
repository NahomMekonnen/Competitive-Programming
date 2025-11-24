class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        ans = []
        nums = [str(i) for i in nums]
        for i in range (len(nums)) : 
            num = int("".join(nums[:i+1]),2)
            ans.append(True if num % 5 == 0 else False)   
        return ans