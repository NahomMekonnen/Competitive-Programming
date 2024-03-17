class Solution {
public:
    bool isCovered(vector<vector<int>>& ranges, int left, int right) {
        unordered_map<int,int> mp;
        for(vector<int> range:ranges){
            for(int i=range[0];i<=range[1];i++)
                mp[i]++;
        }
        for(int i=left;i<=right;i++)
            if(mp.find(i)==mp.end())
                return false;
        return true;
    }
};
