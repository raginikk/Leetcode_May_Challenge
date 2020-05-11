class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        length = len(s)
        i=0
        if(length>0):
            while(i<length):
                if(s.count(s[i])==1):
                    return s.find(s[i])
                    break
                elif(s.count(s[i])==length or s.count(s[i])==s[length-1]):
                    return -1
                    break
                    
                elif(s.count(s[i])>=1):
                    s=s.replace(s[i],'#')
                    i+=1
                    
                
          
        else:
            return -1
        return -1
                
