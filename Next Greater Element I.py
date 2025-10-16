class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [-1] * len(nums2)
        stk = []
        for i in range(len(nums2) -1, -1, -1) :
            while stk and nums2[stk[-1]] <= nums2[i] :
                stk.pop()
            if stk :
                res[i] = nums2[stk[-1]]
            stk.append(i)
        map = dict(zip(nums2,res))
        return [map[i] for i in nums1]
