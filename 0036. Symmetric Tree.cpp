// time = O(v)
// space = O(1)

class Solution {
private:
    bool isSameTree(TreeNode* p, TreeNode* q) {
        if (!p || !q) return p == q;
        else if (p->val != q->val) return false;
        return isSameTree(p->left, q->right) && isSameTree(p->right, q->left);
    }
public:
    bool isSymmetric(TreeNode* root) {
        if (!root->left || !root->right) return root->left == root->right;
        return isSameTree(root->left, root->right);
    }
};