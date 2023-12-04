import java.util.ArrayList;
import java.util.List;

public class PalindromeNumber {
    public boolean isPalindrome(int x) {
        int num=x,i=0,numOfDigits=0;
        if(x<0){
            return false;
        }
        while(x>0){
            int digit=x%10;
            x/=10;
            numOfDigits++;
        }
        x=num;
        int[] numbers=new int[numOfDigits];
        for (int j = 0; j < numbers.length; j++) {
            numbers[j]=x%10;
            x/=10;

        }
        for (int j = numbers.length-1; j >=0; j--) {
            if(numbers[i]!=numbers[j]){
                return false;
            }
            i++;
        }
        return true;
    }
}
