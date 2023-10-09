class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        int left = bin_search(nums, target, true);
        int right = bin_search(nums, target, false);
        vector<int>ans{left, right};
        return ans;
    }
    int bin_search(vector<int>& nums, int target, bool isleft){
        int l = 0, r = nums.size()-1;
        int idx = -1;
        while (l <= r){
            int mid = l+(r-l)/2;
            if (nums[mid] > target){
                r = mid-1;
            }
            else if (nums[mid] < target){
                l = mid+1;
            }
            else{
                idx = mid;
                if (isleft){
                    r = mid-1;
                }
                else{
                    l = mid+1;
                }
            }
        }
        return idx;
    }
};