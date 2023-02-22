class Solution {
public:
    bool fun(int mid,int d,vector<int>& w){
        int n=w.size();
        int day=1;
        int total=0;
        bool isvalid=true;
        for(int i=0;i<n;i++){
            if(w[i]>mid){
                isvalid=false;
            }
            if(total+w[i]<=mid){
                total+=w[i];
            }
            else{
                day++;
                total=w[i];
            }
        }
        if(!isvalid){
            return false;
        }
        else{
            return (day<=d);
        }
    }
    
    int shipWithinDays(vector<int>& weights, int days) {
        int l=1;
        int h=500*50000;
        int mid;
        while(l<h){
            mid=(l+h)/2;
            if(fun(mid,days,weights)){
                h=mid;
            }
            else{
                l=mid+1;
            }
        }
        return l;
    }
};