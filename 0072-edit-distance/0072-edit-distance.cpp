class Solution {
public:
    int minDistance(string word1, string word2) {
        int n = word1.size(), m = word2.size();
        // We make dp array 1 indexed
        vector<vector<int>> dp(n+1, vector<int>(m+1, 0));
        for(int i=0;i<=n;i++) dp[i][0] = i;
        for(int j=0;j<=m;j++) dp[0][j] = j;
        for(int i=1;i<=n;i++){
            for(int j=1;j<=m;j++){
                if(word1[i-1] == word2[j-1]) 
                    dp[i][j] = dp[i-1][j-1];
                else
                    dp[i][j] = 1 + min(dp[i-1][j], min(dp[i][j-1], dp[i-1][j-1]));
            }
        }
        return dp[n][m];
    }
    
    
};

//memo

    // int find(string word1, string word2, int i, int j, vector<vector<int>>& dp){
    //     if(j<0) return i+1;
    //     if(i<0) return j+1;
    //     if(word1[i]==word2[j]) return find(word1,word2,i-1,j-1,dp);
    //     return dp[i][j]=1+min(find(word1,word2,i-1,j,dp),min(find(word1,word2,i,j-1,dp),find(word1,word2,i-1,j-1,dp)));
    // }    
    // int minDistance(string word1, string word2) {
    //     int n=word1.size();
    //     int m=word2.size();
    //     vector<vector<int>> dp(n+1,vector<int>(m+1,-1));
    //     return find(word1,word2,n-1,m-1,dp);
    // }
