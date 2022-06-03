// time = O(n)
// space = O(n)

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> idx_map;
        for (int i = 0; i < nums.size(); i++) {
            if (idx_map.find(nums[i]) != idx_map.end()) {
                return {i, idx_map[nums[i]]};
            }
            idx_map[target - nums[i]] = i;
        }
        return {};
    }
};