// time = O(n)
// space = O(v)

class Solution {
private:
    TreeNode* convertToBST(vector<int>& nums, int high, int low) {
        if (high < low) return nullptr;
        int mid = low + ((high-low)>>1);
        TreeNode* node = new TreeNode(nums[mid]);
        node->left = convertToBST(nums, mid-1, low);
        node->right = convertToBST(nums, high, mid+1);
        return node;
    }
public:
    TreeNode* sortedArrayToBST(vector<int>& nums) {
        return convertToBST(nums, nums.size()-1, 0);
    }
};