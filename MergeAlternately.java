import java.util.ArrayList;
import java.util.List;

public class MergeAlternately {
    public String mergeAlternately(String word1, String word2) {
        StringBuilder mergedWord= new StringBuilder();
        int i=0,j=0;
        while(i<word1.length()||j<word2.length()){
            if(i<word1.length()){
                mergedWord.append(word1.charAt(i));
                i++;
            }
            if(j<word2.length()){
                mergedWord.append(word2.charAt(j));
                j++;
            }
        }
        return  mergedWord.toString();
    }
}
