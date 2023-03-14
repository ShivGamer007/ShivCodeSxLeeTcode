/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int sumNumbers(TreeNode* root) {
        int cur=0;
        return sumNode(root,cur);
    }
    int sumNode(TreeNode* root,int cur){
        if (root==NULL) return 0;
        cur=cur*10+root->val;
        if (root->left==NULL && root->right==NULL) return cur;
        int left=sumNode(root->left,cur);
        int right=sumNode(root->right,cur);
        return left+right;
    }
};
