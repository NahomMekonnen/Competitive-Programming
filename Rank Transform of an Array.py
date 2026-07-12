class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        cpy = sorted(list(set(arr)))
        map = defaultdict(int)
        for i in range(len(cpy)) :
            map[ cpy[i] ] = i + 1
        return [ map[i] for i in arr ]
