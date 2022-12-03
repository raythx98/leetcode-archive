// time = O(v)
// space = O(v)

class Solution {
private:
    int testBalanced(TreeNode* root, bool& balanced) {
        if (!root) return 0;
        if (!balanced) return 0;
        int left = testBalanced(root->left, balanced);
        int right = testBalanced(root->right, balanced);
        balanced &= abs(left - right) <= 1;
        return 1 + max(left, right);
    }
    
public:
    bool isBalanced(TreeNode* root) {
        bool balanced = true;
        testBalanced(root, balanced);
        return balanced;
    }
};