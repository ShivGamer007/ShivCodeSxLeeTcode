class Solution {
public:
    string convert(string s, int numrows) {
        int n=s.length();
        vector<string>v(numrows,"");
        
        int i=0;
        while(i<n){
            for (int j=0;j<numrows && i<n; j++){
                v[j].push_back(s[i++]);
            }
            for (int j=numrows-2;j>=1 && i<n;j--){
                v[j].push_back(s[i++]);
            }
            
        }
        
        string ans="";
        
        for (auto i:v){
            ans+=i;
        }
        return ans;
    }
};