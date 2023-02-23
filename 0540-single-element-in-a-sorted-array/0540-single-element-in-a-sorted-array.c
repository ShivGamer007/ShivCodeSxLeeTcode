int singleNonDuplicate(int* nums, int n){
    int l=0;
    int r=n-1;
    int mid;
    if(n==1) return nums[0];
    if(nums[0]!=nums[1]) return nums[0];
    if(nums[r]!=nums[r-1]) return nums[r];
    while(l<=r){
        mid=(l+r)/2;
        if(nums[mid]!=nums[mid-1] && nums[mid]!=nums[mid+1]) return nums[mid];
        if((mid%2==0 && nums[mid]==nums[mid+1]) || (mid%2==1 && nums[mid]==nums[mid-1])){
            l=mid+1;
        }
        else{
            r=mid-1;
        }
    }
    return -1;
    
}