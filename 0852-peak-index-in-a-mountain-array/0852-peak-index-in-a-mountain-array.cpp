class Solution {
public:
    int peakIndexInMountainArray(vector<int>& arr) {
        int l=0;
        int r=arr.size()-1;
        int mid;
        
        if(arr[0]<arr[1] && arr[r-1]<arr[r]){
            return r;
        }
        if(arr[0]>arr[1] && arr[r-1]>arr[r]){
            return 0;
        }
        
        while(l<=r){
            mid=(l+r)/2;
            
            if(arr[mid]>=arr[mid+1]){
                r=mid-1;
            }
            else{
                l=mid+1;
            }
        }
        return l;
    }
};