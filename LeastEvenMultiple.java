public class LeastEvenMultiple {
    public int smallestEvenMultiple(int n) {
        int smallestEvenMultiple = 0;
        if(n%2==0){
          smallestEvenMultiple=n;
        }else {
            smallestEvenMultiple=n*2;
        }
        return smallestEvenMultiple;
    }
}
