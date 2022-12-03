// time = O(n)
// space = O(1)

class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int slow = 0;
        // cout << "here";
        for (int fast = 0; fast < nums.size(); fast++) {
            if (nums[fast] != 0) nums[slow++] = nums[fast];
        }
        // cout << "there";
        for(;slow < nums.size(); slow++) {
            nums[slow] = 0;
        }
    }
};