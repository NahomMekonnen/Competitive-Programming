class Solution {
    fun mapWordWeights(words: Array<String>, weights: IntArray): String {
        val first = 'a'.code
        return buildString {
            for (word in words) {
                var sumWeights = 0
                for (i in word)  {
                    sumWeights += weights[i.code - first]
                }
                val total = 25-  (sumWeights % 26) + first
                append(total.toChar())
            }
        }
    }
}
