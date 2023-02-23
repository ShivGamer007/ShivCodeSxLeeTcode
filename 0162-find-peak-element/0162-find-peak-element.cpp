class Solution {
public:
    int findPeakElement(vector<int>& nums) {
        int l=0;
        int r=nums.size()-1;
        int mid;
        if (nums.size()==1) return 0;
        if (nums[0]>nums[1]) return 0;
        if (nums[r]>nums[r-1]) return r;
        while(l<=r){
            mid=l+(r-l)/2;
            if(mid==0){
                if(nums[0]>nums[1])return 0;
                else return 1;
            }
            if(nums[mid]>nums[mid-1] && nums[mid]>nums[mid+1]){
                return mid;
            }
            if(nums[mid]>nums[mid-1] && nums[mid]<nums[mid+1]){
                l=mid+1;
            }
            else{
                r=mid-1;
            }
        }
        return l;
    }
};