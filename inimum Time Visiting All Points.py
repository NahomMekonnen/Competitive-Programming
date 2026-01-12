class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        steps = 0
        for i in range(len(points) - 1) :
            x1, x2 = points[i][0], points[i+1][0]
            y1, y2 = points[i][1], points[i+1][1]
            steps += abs(x1 - x2) if abs(x1 - x2) > abs(y1 - y2) else abs(y1 - y2)
        return steps
