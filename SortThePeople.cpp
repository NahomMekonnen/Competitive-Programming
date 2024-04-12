class Solution {
public:
    vector<string> sortPeople(vector<string>& names, vector<int>& heights) {
        int n = heights.size();
        for (int i = 1; i < n; i++) {
            int tempHeight = heights[i];
            string tempName = names[i];
            int j = i - 1;
            while (j >= 0 && heights[j] < tempHeight) {
                heights[j + 1] = heights[j];
                names[j + 1] = names[j];
                j--;
            }
            heights[j + 1] = tempHeight;
            names[j + 1] = tempName;
        }
        return names;
    }
};
