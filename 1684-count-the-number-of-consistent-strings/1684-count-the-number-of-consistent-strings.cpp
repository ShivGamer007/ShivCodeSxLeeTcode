class Solution {
public:
    int countConsistentStrings(string allowed, vector<string>& words) {
        int c = 0;
        vector<int> setA(26, 0);
        for(char c:allowed){
            setA[c-'a'] = 1;
        }
        for(string& s: words){
            int f = 1;
            for(char c: s){
                if(setA[c-'a']!=1){
                    f = 0;
                }
            }
            if(f==1){
                c++;
            }
        }
        return c;
    }
};