import java.time.LocalDate
class Solution {
    fun dayOfYear(date: String): Int {
        val d = date.split("-").map{ it.toInt()} 
        return LocalDate.of(d[0],d[1],d[2]).dayOfYear
    }
}
