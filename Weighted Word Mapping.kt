class Solution {
    fun mapWordWeights(words: Array<String>, weights: IntArray): String {
        val first = 'a'.code
        return buildString {
            for (word in words) {
                val asciiBytes = word.toByteArray(charset = Charsets.US_ASCII).map { weights[it - first] }
                val total = 25 - (asciiBytes.sum() % 26) + first
                append(total.toChar())
            }
        }
    }
}
