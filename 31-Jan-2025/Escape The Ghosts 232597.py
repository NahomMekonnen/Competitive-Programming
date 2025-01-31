# Problem: Escape The Ghosts - https://leetcode.com/problems/escape-the-ghosts/

class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        myMoves = abs(target[0]) + abs(target [1])
        for i in ghosts:
            ghostMoves = abs(target[0] - i[0]) + abs(target[1] - i[1])
            if ghostMoves <= myMoves:
                return False
        return True