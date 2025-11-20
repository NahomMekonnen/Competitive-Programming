class Solution:
    def canPlaceFlowers(self, fb: List[int], n: int) -> bool:
        if n == 0 :
            return True
        x = len(fb) 
        if x == 1 :
            return True if fb[0] == 0 else False
        for i in range ( x ) :
            if i == 0 and fb[i] == 0 :
                if i + 1 < x and fb[i+1] == 0 :
                    n -= 1
                    fb[i] = 1
            elif i == x - 1 and fb[i] == 0 :
                if fb[ i- 1 ] == 0 :
                    n -= 1
                    fb[i] = 1
            else :
                if fb[i] == 0 and fb[i-1] == 0 and i + 1 < x and fb[i + 1] == 0 :
                    n -= 1
                    fb[i] = 1
            if n == 0 :
                return True
        return False
