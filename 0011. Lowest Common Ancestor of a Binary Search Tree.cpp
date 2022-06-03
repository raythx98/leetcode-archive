// time = O(lg(n))
// space = O(lg(n))

class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        int smaller = p->val, bigger = q->val, curr = root->val;
        if (smaller > curr && bigger > curr) return lowestCommonAncestor(root->right, p, q);
        if (smaller < curr && bigger < curr) return lowestCommonAncestor(root->left, p, q);
        return root;
    }
};