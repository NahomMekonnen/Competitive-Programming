class Solution {
    fun largestAltitude(gain: IntArray): Int {
        var highest = 0
        var curr = 0
        for ( i in gain) {
            curr += i 
            highest = max(highest, curr)
        }
        return highest
    }
}
