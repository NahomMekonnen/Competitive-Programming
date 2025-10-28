class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        pre, post = [0] * len( nums ), [0] * len( nums )
        pre[0], post[-1] = nums[0], nums[-1]
        for i in range( 1, len( nums ) ) :
            pre[i] = pre[i - 1] + nums[i]
        for i in range(len(nums) - 2, -1, -1) :
            post[i] = post[i + 1] + nums[i]
        ans = 0
        for i in range(len(nums)) :
            if nums[i] == 0 :
                if pre[i] == post[i] :
                    ans += 2
                elif post[i] == pre[i] -1 :
                    ans += 1
                elif post[i] - 1 == pre[i] :
                    ans += 1
        return  ans
