class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        map = defaultdict(list) 
        for i in nums :
            if i % 3 == 1 :
                map[1].append(i)
            elif i % 3 == 2 :
                map[2].append(i)
        for i in map : 
            map[i].sort() 
        total = sum ( nums )
        ans = 0 
        m = total % 3 
        print(total)
        if m == 0 :
            return total
        if m == 1 :
            temp = 0
            if map[1] : 
                temp = total - map[1][0]
                if temp % 3 == 0 :
                    ans = max ( ans, temp  )
            if map[2] and len(map[2]) >= 2 :
                temp =  total - (map[2][0] + map[2][1]) 
                if temp % 3 == 0 :
                    ans = max ( ans, temp  )
        if m == 2 :
            temp = 0
            if map[1] and len(map[1]) >= 2  : 
                temp =  total - (map[1][0] + map[1][1]) 
                if temp % 3 == 0 :
                    ans = max ( ans, temp  )
            if map[2] :
                temp =  total - map[2][0] 
                if temp % 3 == 0 :
                    ans = max ( ans, temp  )
        return ans
