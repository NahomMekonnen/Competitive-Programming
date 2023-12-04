import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class SelfDividing {
    public List<Integer> selfDividingNumbers(int left, int right){

        List<Integer> list=new ArrayList<>();
        for(int i=left;i<=right;i++){
            int num=i,numOfDigits=0,isDivisibleByDigit=0;
            while(num>0){
                int digits=num%10;
                if(digits!=0){

                    if(i%digits==0)
                        isDivisibleByDigit++;
                }
                num/=10;
                numOfDigits++;
            }
            if(numOfDigits==isDivisibleByDigit){
                list.add(i);
            }

        }

        return list;
    }
}
