class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        ans, num = [], ''
        for i in nums :
            num += str(i)
            ans.append(int(num,2) % 5 == 0)
        return ans
