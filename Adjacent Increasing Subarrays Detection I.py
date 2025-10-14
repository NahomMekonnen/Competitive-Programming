class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        count, i = 0, 0
        l = -1
        while i < (len(nums) - k + 1) :
            j = i
            while j < (len(nums) - k + 1 ):
                if nums[j:j+k] == sorted(nums[j:j+k]) and len(nums[j:j+k]) == len(set(nums[j:j+k])) :
                    count += 1
                else :
                    count = 0
                if count == 2 :
                    return True
                j += k
            count = 0
            i += 1

        return False
