class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        ans = [0] * num_people
        n , i = 0, 0
        while candies > 0 :
            idx = i % num_people
            give = n + (idx + 1) if candies > n + (idx + 1) else candies
            ans[idx] += give  
            candies -= give
            i += 1
            if i > 0 and i % num_people == 0 :
                n += num_people
        return ans
