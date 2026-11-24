class Solution:
    def maxLength(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)) :
            for j in range(len(nums),i, -1) :
                l, g = lcm(*nums[i:j]), gcd(*nums[i:j])
                prod = 1
                for k in range(i, j) :
                    prod *= nums[k]
                if prod == l * g :
                    ans = max(ans, j - i)

        return ans