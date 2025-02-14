# Problem: Rabbits in Forest - https://leetcode.com/problems/rabbits-in-forest/

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        bam = Counter(answers)
        ans = 0
        for i in bam :
            m, n = i + 1, bam[i]
            ans += int(math.ceil(n/m) * m)
        return ans 
