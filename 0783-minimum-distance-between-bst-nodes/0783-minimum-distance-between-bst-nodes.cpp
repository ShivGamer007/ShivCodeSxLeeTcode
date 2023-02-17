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
    void fun(TreeNode* root,int& preval,int& mindif){
        if (root==nullptr) return;
        fun(root->left,preval,mindif);
        if (preval != -1){
            mindif=min(mindif,root->val-preval);
        }
        preval=root->val;
        fun(root->right,preval,mindif);
    }
    
    int minDiffInBST(TreeNode* root) {
        int mindif=INT_MAX;
        int preval=-1;
        fun(root,preval,mindif);
        return mindif;
    }
};