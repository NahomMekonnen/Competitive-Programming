public class EquivalentStrings {
    public boolean arrayStringsAreEqual(String[] word1, String[] word2) {
        String word="",otherWord="";
        for (int i = 0; i < word1.length; i++) {
            word+=word1[i];
        }
        for (int i = 0; i < word2.length; i++) {
            otherWord+=word2[i];
        }
        if(word.equals(otherWord))
            return true;
        return false;
    }
}
