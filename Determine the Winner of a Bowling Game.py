class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        p1, p2 = 0, 0 
        for i in range(len(player1)) :
            if i > 0 and player1[i-1] == 10 :
                p1 += (player1[i] * 2)
            elif i > 1 and player1[i - 2] == 10 :
                p1 += (player1[i] * 2)
            else : 
                p1 += player1[i] 
            
            if i > 0 and player2[i-1] == 10 :
                p2 += (player2[i] * 2)
            elif i > 1 and player2[i - 2] == 10 :
                p2 += (player2[i] * 2)
            else : 
                p2 += player2[i] 
        ans = 0 
        if p1 > p2 :
            ans = 1
        elif p2 > p1 :
            ans = 2
        return ans
