class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        c=0
        l=len(flowerbed)
        if l>=2 and flowerbed[0]==0 and flowerbed[1]==0:
            c=1
            flowerbed[0]=1
            
        for i in range(1,l-1):
            if flowerbed[i]==0:
                if flowerbed[i-1]==0 and flowerbed[i+1]==0:
                    c+=1
                    flowerbed[i]=1
        if flowerbed[l-1]==0 and flowerbed[l-2]==0:
            c+=1
           
        if c>=n:
            return True
        else:
            return False