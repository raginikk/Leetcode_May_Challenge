    
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        length = len(num)
        if length==k:
            return "0"
        for i in range(k):
            j=0
            while (j<len(num)-1 and int(num[j])<=int(num[j+1])):
                    j+=1
            num = num.replace(num[j],'',1) 
        
        return str(int(num))    
                    
                    
          
