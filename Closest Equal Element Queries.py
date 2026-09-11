class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        pos = defaultdict(list)
        for i in range(len(nums)) :
            pos[nums[i]].append(i)

        ans = [-1] * len(queries)

        for i in range( len(queries) ) :

            q = queries[i]
            num = nums[q]
            idx = 0 # starting index

            if len(pos[num]) != 1 :

                n = len(pos[num]) 
                low, high = 0, n - 1
                target = q
                
                while low <= high :
                    mid = (low + high)//2 
                    if pos[num][mid] == target :
                        idx = mid 
                        break 
                    elif pos[num][mid] > target :
                        high = mid - 1
                    else :
                        low = mid + 1
                
                    
                left, right = 0, 0
                

                if idx == 0 :
                    
                    left = len(nums) - pos[num][-1] + pos[num][idx]
                    right = pos[num][idx + 1] - pos[num][idx]

                elif idx == n - 1 :
                    
                    left = pos[num][idx] - pos[num][idx - 1]
                    right = len(nums) - pos[num][idx] + pos[num][0]

                else :
                
                    left = pos[num][idx] - pos[num][idx - 1]
                    right = pos[num][idx + 1] - pos[num][idx]
                
                ans[i] = min(left, right)

            

        return ans
