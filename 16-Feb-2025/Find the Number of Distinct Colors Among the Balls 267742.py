# Problem: Find the Number of Distinct Colors Among the Balls - https://leetcode.com/problems/find-the-number-of-distinct-colors-among-the-balls/description/

class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        count1, count2= defaultdict(int), defaultdict(int)
        ans = []
        for i in queries :
            ball, color = i[0], i[1]
            
            if ball in count1 :
                count2[count1[ball]] -= 1
                if count2[count1[ball]] == 0 :
                    del count2[count1[ball]]
                
            count1[ball] = color
            count2[color] += 1
            ans.append(len(count2))
            
        return ans
        