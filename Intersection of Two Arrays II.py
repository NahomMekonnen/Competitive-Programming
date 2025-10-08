class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count1 = Counter(nums1)
        count2 = Counter(nums2)
        nums = list(set(nums1) & set(nums2))
        ans = []
        for i in nums :
            ans += [i] * count1[i] if count1[i] < count2[i] else [i] * count2[i]
        return ans
        
