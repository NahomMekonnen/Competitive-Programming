# Problem: Contains Duplicate - https://leetcode.com/problems/contains-duplicate/description/

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        myDict = Counter(nums)
        for i in myDict.keys():
            if myDict[i] > 1:
                return True
        return False