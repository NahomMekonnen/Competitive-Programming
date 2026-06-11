class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        for i in asteroids :
            if mass >= i :
                mass += i
                if mass >= asteroids[-1] :
                    return True
            else :
                return False
        return TrueD
