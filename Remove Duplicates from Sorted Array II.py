class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        count = 0
        for i in range(len(nums)) :
            while cnt[nums[i]] > 2 :
                cnt[nums[i]] -= 1
                nums[i] = float("inf")
                i += 1
                count += 1
        nums.sort()
        return len(nums) - count
          
