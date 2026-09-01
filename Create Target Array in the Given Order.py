class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = [-1] * len(nums)
        for i in range(len(nums)) : 
            if target[index[i]] == -1 :
                target[index[i]] = nums[i]
            else :
                left, right = target[:index[i]], target[index[i]:]
                left.append(nums[i])
                right.pop()
                target = left + right
        return target
