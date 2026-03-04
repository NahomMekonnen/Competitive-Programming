class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        roids = []
        for i in asteroids :
            if len(roids) == 0 or i > 0 :
                roids.append(i)
            else :
                if roids[-1] > 0 and i < 0 :
                    if roids[-1] + i == 0 :
                        roids.pop()
                        continue
                    else :
                        while len(roids) > 0 and roids[-1] > 0 and roids[-1] < abs(i) :
                            roids.pop()
                        if len(roids) == 0 or roids[-1] < 0:
                            roids.append(i)
                        elif roids[-1] == abs(i) :
                            roids.pop()
                else :
                    roids.append(i)
        return roids

