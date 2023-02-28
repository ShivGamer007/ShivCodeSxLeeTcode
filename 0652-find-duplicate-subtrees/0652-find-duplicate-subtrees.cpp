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
    string serialize(TreeNode* node, unordered_map<string, int>& subtree,vector<TreeNode*>& duplicates){
        if (!node) return "#";
        string left=serialize(node->left,subtree,duplicates);
        string right=serialize(node->right,subtree,duplicates);
        string s=left+","+right+","+to_string(node->val);
        if(subtree[s]==1) duplicates.push_back(node);
        subtree[s]++;
        return s;
    }
    
    vector<TreeNode*> findDuplicateSubtrees(TreeNode* root) {
        unordered_map <string,int> subtree;
        vector<TreeNode*>duplicates;
        serialize(root,subtree,duplicates);
        return duplicates;
    }
};