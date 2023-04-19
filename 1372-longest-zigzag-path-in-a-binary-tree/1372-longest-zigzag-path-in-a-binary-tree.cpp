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
    int longestZigZag(TreeNode* root) {
        if(!root->right && !root->left) return 0;
        return solve(root,0,false);
    }
    int solve(TreeNode* root,int length,bool shouldGoLeft){
        if(!root) return length;
        int l=0,r=0,temp=0;
        if(shouldGoLeft && !root->left){
            temp=length;
            length=0;
        }
        else if(!shouldGoLeft && !root->right){
            temp=length;
            length=0;
        }
        r=solve(root->right,shouldGoLeft?1:length+1,true);
        l=solve(root->left,shouldGoLeft?length+1:1,false);
        return max({l,r,length,temp});
    }
};
