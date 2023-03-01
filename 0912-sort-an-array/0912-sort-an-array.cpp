class Solution {
public:
    vector<int> sortArray(vector<int>& nums) {
        priority_queue<int,vector<int>,greater<int>>p;
        for(int i:nums) p.push(i);
        for(int i=0;i<nums.size();i++){
            nums[i]=p.top();
            p.pop();
        }
        return nums;
    }
};

