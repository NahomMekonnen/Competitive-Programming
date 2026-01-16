class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        max_sum = cur_sum_del =  cur_sum = arr[0]
        for i in arr[1:]:
            cur_sum_del = max(cur_sum_del + i, i, cur_sum)
            cur_sum = max(cur_sum + i, i)
            max_sum = max(max_sum, cur_sum, cur_sum_del)
        return max_sum

        
