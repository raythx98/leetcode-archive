// time = O(v)
// space = O(v)

class Solution {
private:
public:
    int max_depth(TreeNode* root, int& max_diameter) {
        if (!root) return 0;
        int left = max_depth(root->left, max_diameter);
        int right = max_depth(root->right, max_diameter);
        if (left + right > max_diameter) max_diameter = left + right;
        return 1 + max(left, right);
    }
        
    int diameterOfBinaryTree(TreeNode* root) {
        int max_diameter = 0;
        max_depth(root, max_diameter);
        return max_diameter;
    }
};