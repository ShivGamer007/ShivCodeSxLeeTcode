#define ll long long
class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int hrs) {
        int l=1;
        int r=*max_element(piles.begin(),piles.end());
        int mid;
        while(l<=r){
            mid=l+(r-l)/2;
            ll h=0;
            for(int i: piles){
                h+=(i/mid)+(i%mid!=0);
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
