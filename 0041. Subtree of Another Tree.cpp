// time = O(r*s)
// space = O(1)

// KIV: KMP Substring Matching
class Solution {
private:
    bool isSameTree(TreeNode* p, TreeNode* q) {
        if (!p || !q) return p == q;
        return p->val == q->val && isSameTree(p->left, q->left) && isSameTree(p->right, q->right);
    }
public:
    bool isSubtree(TreeNode* root, TreeNode* subRoot) {
        queue<TreeNode*> frontier;
        frontier.push(root);
        while(!frontier.empty()) {
            TreeNode* node = frontier.front();
            if (isSameTree(node, subRoot)) return true;
            frontier.pop();
            if (node->left) frontier.push(node->left);
            if (node->right) frontier.push(node->right);
        }
        return false;
    }
};