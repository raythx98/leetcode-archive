// time = O(n)
// space = O(n)

class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums) {
        int front = 0, back = nums.size()-1;
        vector<int> nums_reverse(nums.size());
        for (int i = nums.size()-1; i >= 0; i--) {
            if (-nums[front] > nums[back]) {
                nums_reverse[i] = (nums[front] * nums[front++]);
            } else {
                nums_reverse[i] = (nums[back] * nums[back--]);
            }
        }
        return nums_reverse;
    }
};