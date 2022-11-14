//{ Driver Code Starts
//Initial template for C++

#include<bits/stdc++.h> 
using namespace std; 

// } Driver Code Ends
//User function template for C++

class Solution{   
public:
    int numberOfSubsequences(string S, string t){
        // code here 
        int n=S.size(),m=t.size();
        int c=0;
        unordered_map<int,int>mp;
        for(int i=0;i<n;i++){
            if(S[i]==t[0] && mp[i]==0){
                int shiv=700;
                int j=0;
                int cur_ind=i;
                while(cur_ind<n){
                    if(S[cur_ind]==t[j] && mp[cur_ind]==0){
                        j++;
                        mp[cur_ind]++;
                    }
                    if(j==m){
                        c++;
                        break;
                    }
                    cur_ind++;
                    shiv+=1;
                }
            }
        }
        return c;
    }
};

//{ Driver Code Starts.
int main() 
{ 
    int t;
    cin>>t;
    while(t--)
    {
        string S,W;
        cin >> S >> W;
        Solution ob;
        cout << ob.numberOfSubsequences(S,W) << endl;
    }
    return 0; 
} 


// } Driver Code Ends