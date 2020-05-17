MAX=256
def compare(arr1,arr2):
    for i in range(MAX):
        if arr1[i]!=arr2[i]:
            return False
    return True
    
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        lengthS=len(s) #text
        lengthP=len(p)  #pattern
        if(lengthS<lengthP):
            return []
        result=[]
        cntS = [0]*MAX
        cntP = [0]*MAX
        
        for i in range(lengthP):
            cntS[ord(s[i])]+=1
            cntP[ord(p[i])]+=1
        for i in range(lengthP,lengthS):
            if compare(cntS, cntP): 
                result.append(i-lengthP)  
  
            (cntS[ ord(s[i]) ]) += 1

            (cntS[ ord(s[i-lengthP]) ]) -= 1
            
        if compare(cntS,cntP):
            result.append(lengthS-lengthP)
        return result       
        
