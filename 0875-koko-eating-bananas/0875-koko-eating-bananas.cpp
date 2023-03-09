class Solution {
public:
    
    int minEatingSpeed(vector<int>& piles, int hrs) {
        long long int l=1;
        long long int r=*max_element(piles.begin(),piles.end());
        long long int mid;
        while(l<=r){
            mid=l+(r-l)/2;
            long long int h=0;
            for (auto i:piles){
                h+=i/mid+(i%mid!=0);
                
            }
            if (h<=hrs){
                r=mid-1;
            }
            else{
                l=mid+1;
            }   
        }
        return l;
    }
};