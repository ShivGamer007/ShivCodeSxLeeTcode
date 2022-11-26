class Solution {
public:
    int jobScheduling(vector<int>& stime, vector<int>& etime, vector<int>& profit) {//stime=starttime, etime=endtime
        int n=stime.size();
        vector<vector<int>>v;
        for(int i=0;i<n;i++){
            v.push_back({etime[i],stime[i],profit[i]});
        }
        sort(v.begin(),v.end());
        int ans=0;
        vector<int>dp(n);
        
        for(int i=0;i<n;i++){
            dp[i]=v[i][2];
            if(i==0){
                ans=max(ans,dp[i]);
                continue;
            }
            dp[i]=max(dp[i],dp[i-1]);
            int start=v[i][1];
            for(int j=i-1;j>=0;j--){
                if(start>=v[j][0]){
                    dp[i]=max(dp[i],dp[j]+v[i][2]);
                    break;
                }
            }
            ans=max(ans,dp[i]);
        }
        return ans;
        
        
    }
};
