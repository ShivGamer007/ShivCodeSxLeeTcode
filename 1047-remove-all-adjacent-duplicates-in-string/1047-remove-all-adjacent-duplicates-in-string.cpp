class Solution {
public:
    string removeDuplicates(string s) {
        stack<char>st;
        for (auto c:s){
            if (!st.empty() && c==st.top()){
                st.pop();
            }
            else{
                st.push(c);
            }
        }
        string ss="";
        while(!st.empty()){
            ss=st.top()+ss;
            st.pop();
        }
        return ss;
    }
};