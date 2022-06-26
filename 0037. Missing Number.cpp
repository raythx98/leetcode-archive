// time = O(n)
// space = O(1)

class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int missing = 0;
        for (int i = 0; i <= nums.size(); i++) {
            missing ^= i;
        }
        for (auto &num: nums) {
            missing ^= num;
        }
        return missing;
    }
};