class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        map = defaultdict(list)
        distances = set()
        for point in points :
            distance = sqrt(point[0]**2 + point[1]**2)
            distances.add(distance)
            map[distance].append(point)
        distances = list(distances)
        heapq.heapify((distances))
        ans = []
        for i in heapq.nsmallest(k,distances) :
            ans+= map[i]
        return ans[:k]
