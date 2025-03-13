# Problem: Find-the-prefix-common-array-of-two-arrays - https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        seen, ans =[0] * (len(A) +1), []
        cnt = 0
        for i in range(len(A)) :
            seen[A[i]] += 1
            seen[B[i]] += 1
            if seen[A[i]] == 2:
                cnt += 1
                seen[A[i]] = 0
            if seen[B[i]] == 2:
                cnt += 1
                seen[B[i]] = 0
            ans.append(cnt)
        return ans