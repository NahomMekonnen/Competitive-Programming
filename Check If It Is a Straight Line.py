class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) == 2 :
            return True
        v, h = True, True
        x, y = coordinates[0][0], coordinates[0][1]
        for i in coordinates :
            if i[0] != x :
                h = False
            if i[1] != y :
                v = False
        if v or h : 
            return True
        coordinates.sort()
        if (coordinates[1][0] - coordinates[0][0]) == 0 :
            return False
        m = (coordinates[1][1] - coordinates[0][1]) / (coordinates[1][0] - coordinates[0][0])
        for c in range(1,len(coordinates)) :
            if (coordinates[c][0] - coordinates[c -1][0]) == 0 :
                return False
            tm = (coordinates[c][1] - coordinates[c - 1][1]) / (coordinates[c][0] - coordinates[c -1][0])
            if tm != m :
                return False
        return True
