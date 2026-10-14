class Solution:
    def minimumLevels(self, possible: List[int]) -> int:
        possible = [i + i - 1 for i in possible]
        win, score = sum(possible)//2, 0

        for i in range(len(possible) - 1) :
            score += possible[i] 
            if score > win :
                return i + 1
        return -1