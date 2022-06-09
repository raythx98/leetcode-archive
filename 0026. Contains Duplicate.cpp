// time = O(n)
// space = O(n)

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_map<int, int> nums_count;
        for (auto &num: nums) {
            if (++nums_count[num] > 1) return true;
        }
        return false;
    }
};