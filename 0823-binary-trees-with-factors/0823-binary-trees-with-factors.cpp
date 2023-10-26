class Solution {
public:
    int numFactoredBinaryTrees(vector<int>& arr) {
        sort(arr.begin(), arr.end());
        map<long long, long long> mpans;
        long long res = 0;
        long mod = 1e9+7;
        for (int i = 0; i < arr.size(); i++){
            mpans[arr[i]] = 1;
        }
        
        for(int i = 1; i < arr.size(); i++){
            int x = arr[i];
            int t = sqrt(x);
            long long ans = 1;
            for(int j = 2; j <= t; j++){
                if (x % j == 0){
                    int p = x / j;
                    if (p == j){
                        ans += (mpans[j]%mod * mpans[j]%mod) %mod;
                    }
                    else{
                        ans += (((mpans[j]%mod * mpans[p]%mod)%mod) * 2)%mod;
                    }
                }
            }
            mpans[x] = ans % mod;
        }
        for(auto it: mpans){
            res += it.second;
        }
        return res%mod;
    }
};