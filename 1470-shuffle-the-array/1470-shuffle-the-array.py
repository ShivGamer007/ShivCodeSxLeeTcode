class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        a=nums[:n]
        b=nums[n:]
        c=[]
        i,j,k=0,0,0
        while(i<2*n):
            if i%2==0:
                c.append(a[j])    
                j+=1
            else:
                c.append(b[k])
                k+=1
            i+=1
        return c