class Solution {
public:
    vector<int> applyOperations(vector<int>& nums) {
        vector<int> ans(nums.size());
        int j=0;
        for(int i=0;i<nums.size()-1;i++){
            if(nums[i]==nums[i+1]){
                nums[i]*=2;
                nums[i+1]=0;
            }
            if(nums[i]>0){
                ans[j]=nums[i];
                j++;
            }
        }
        ans[j]=nums[nums.size()-1];
        return ans;
    }
};
