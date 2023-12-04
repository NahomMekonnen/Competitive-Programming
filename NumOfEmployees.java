public class NumOfEmployees{
    public int numberOfEmployeesWhoMetTarget(int[] hours, int target) {
        int metTheTarget=0;
        for (int i:hours){
            if(i>=target)
                metTheTarget++;
        }
        return metTheTarget;
    }
}
