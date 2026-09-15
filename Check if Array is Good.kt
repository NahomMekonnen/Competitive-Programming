class Solution {
    fun isGood(nums: IntArray): Boolean {
        val n = nums.size
        val bb = BooleanArray(n + 1)
        for (m in nums)
            if (m >= n || bb[m])
                if (m != n - 1 || bb[0]) return false
                else bb[0] = true
            else bb[m] = true
        return true
    }
}