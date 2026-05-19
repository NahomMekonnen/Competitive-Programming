class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        a1, a2 = 0, 0
        while a1 < len(nums1) and a2 < len(nums2) :
            if nums1[a1] == nums2[a2] :
                return nums1[a1]
            elif nums1[a1] > nums2[a2] :
                a2 += 1
            else :
                a1 += 1
        return -1
