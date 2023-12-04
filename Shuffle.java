public class Shuffle {
    public int[] shuffle(int[] nums, int n) {
        int [] shuffledArray=new int[2*n];
        int i=0,j=n;
        while(i<nums.length){
            int k=i+1,l=j+1;
            if (k < nums.length&&l<nums.length) {

                shuffledArray[k]=nums[i];
                if(j<nums.length){
                    shuffledArray[i+1]=nums[l];
                }
                i++;
            }

        }
        return shuffledArray;
    }
}
