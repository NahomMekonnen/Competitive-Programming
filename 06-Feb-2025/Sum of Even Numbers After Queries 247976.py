# Problem: Sum of Even Numbers After Queries - https://leetcode.com/problems/sum-of-even-numbers-after-queries/description/

class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        sumEven = 0
        ans = []
        for i in nums: 
            if i % 2 == 0:
                sumEven += i
        for i in range(len(queries)):
            
            if nums[queries[i][1]] % 2 == 0:
                sumEven -= nums[queries[i][1]]

            nums[queries[i][1]] += queries[i][0]

            if nums[queries[i][1]] % 2 == 0:
                sumEven += nums[queries[i][1]]
            
            ans.append(sumEven) 
            
        return ans