class Solution {
public:
    int reverse(int x) {
      if (x<10 && x>-10){
            return x;
        }
        long long r=0,rev=0;
        long p=abs(x);
        while(p>0){
            r=p%10;
            rev=rev*10+r;
            p=p/10;
        }
        if (x<0){
            rev*=-1;
        }
        if(rev>=INT_MIN && rev<=INT_MAX)
            return rev;
        else
            return 0;
        
    }
};