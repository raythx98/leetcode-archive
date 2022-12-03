// time = O(n)
// space = O(1)

// [-1]
// [-1,2]
// [-2,-1]
// [5,4,-1,7,8]

class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int max_num = INT_MIN, curr = 0;
        for (auto &num: nums) {
            curr += num;
            if (curr > max_num) max_num = curr;
            if (curr < 0) curr = 0;
        }
        return max_num;
    }
};