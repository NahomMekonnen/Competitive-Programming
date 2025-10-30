class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        map = sorted(enumerate(nums), key = lambda x:x[1] )
        return [i[1] for i in sorted(map[-k:], key = lambda x:x[0])]
