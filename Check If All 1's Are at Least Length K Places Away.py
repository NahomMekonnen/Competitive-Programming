class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        map = defaultdict(list)
        for i in range (len(nums)) :
            if nums[i] == 1 :
                if map[nums[i]] and abs(map[nums[i]][-1] - i) - 1 < k :
                        return False
                map[nums[i]].append(i)
        return True
