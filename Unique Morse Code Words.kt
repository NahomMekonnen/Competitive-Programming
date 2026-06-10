class Solution {
    fun uniqueMorseRepresentations(words: Array<String>): Int {
        
        fun morseCode(word: String): String {
            val codes = arrayOf(".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--..")
            var finalWord = ""
            for(i in word) {
                finalWord += codes[i.code - 97]
            }
            return finalWord
        }
        val finalWords = words.map{morseCode(it)}.toHashSet()
        return finalWords.size
        

    }
}
