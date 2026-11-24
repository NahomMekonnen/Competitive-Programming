class Solution:
    def maxLength(self, nums: List[int]) -> int:
        prods = []
        for i in range(len(nums)) :
            if i == 0 :
                prods.append(nums[i])
            else :
                prods.append(prods[-1] * nums[i])
        ans = 0
        for i in range(len(nums)) :
            for j in range(len(nums),i, -1) :
                l, g = lcm(*nums[i:j]), gcd(*nums[i:j])
                prod = prods[j - 1] if i == 0 else prods[j - 1] // prods[i - 1]
                if  prod == l * g :
                    ans = max(ans, j - i)

        return ans