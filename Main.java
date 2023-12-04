import java.util.List;

// Press Shift twice to open the Search Everywhere dialog and type `show whitespaces`,
// then press Enter. You can now see whitespace characters in your code.
public class Main {
    public static void main(String[] args) {
        int[] nums={2,7,11,15};
        int target=9;
        TwoSum t=new TwoSum();
        int[] indexes=t.twoSum(nums,9);
        System.out.println(indexes[0] + " " + indexes[1]);
    }
}