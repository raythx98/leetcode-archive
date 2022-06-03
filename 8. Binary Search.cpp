// time = O(lg(n))
// space = O(1)

class Solution {
public:
    int search(vector<int>& nums, int target) {
        int low = 0, high = nums.size() - 1;        
        // standard low < high
        while (low < high) {
            // right bias or left bias?
            int mid = low + ((high - low) >> 1);
            // no matter what equality you choose here, always include/exclude mid correctly
            if (target > nums[mid]) {
                low = mid + 1; // mid is not target, so exclude
            } else {
                high = mid; // mid might be target, so include
            }
        }
        // if unsure, use 2 elements and observe binary search behaviour
        return nums[low] == target ? low : -1;
    }
};