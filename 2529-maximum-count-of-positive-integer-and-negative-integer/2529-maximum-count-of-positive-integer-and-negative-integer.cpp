class Solution {
public:
    int firstpositive(vector<int>&arr){
        int l=0;
        int r=(arr.size())-1;
        int mid;
        while(l<=r){
            mid=(l+r)/2;
            if (arr[mid]>0){
                if(arr[mid-1]<=0){
                    return mid;
                }
                else{
                    r=mid-1;
                }
            }
            else{
                l=mid+1;
            }
        }
        return -1;
    }
    
    int lastnegative(vector<int>&arr){
        int l=0;
        int r=arr.size()-1;
        int mid;
        while(l<=r){
            mid=(l+r)/2;
            if (arr[mid]<0){
                if(arr[mid+1]>=0){
                    return mid;
                }
                else{
                    l=mid+1;
                }
            }
            else{
                r=mid-1;
            }
        }
        return -1;
    }
    
    int maximumCount(vector<int>& nums) {
        if(nums[0]==0 && nums[nums.size()-1]==0){
            return 0;
        }
        if((nums[0]>0) || (nums[nums.size()-1]<0)){
            return nums.size();
        }
        
        
        int a=firstpositive(nums);
        int b=lastnegative(nums);
        int countpos=nums.size()-a;
        int countneg=b+1;
        return max(countpos,countneg);
        
        
        
    }
};