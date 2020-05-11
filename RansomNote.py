class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        cnt=0
        i=0
        j=0
        while i<len(ransomNote):
           
            if(ransomNote[i] in magazine):
                magazine = magazine.replace(ransomNote[i],'#',1)
                cnt+=1
            else:
                break
            i+=1    
                 
                    
                    
                    

        if cnt==len(ransomNote):
            return True
        else:
            return False
