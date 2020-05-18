MAX=256
def compare(arr1,arr2):
    for i in range(MAX):
        if arr1[i]!=arr2[i]:
            return False
    return True
 
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        lengthS1=len(s1) #pattern
        lengthS2=len(s2)  #text
        if(lengthS2<lengthS1):
            return False
        result=[]
        cntS1 = [0]*MAX
        cntS2 = [0]*MAX
        
        for i in range(lengthS1):
            cntS2[ord(s2[i])]+=1
            cntS1[ord(s1[i])]+=1
        for i in range(lengthS1,lengthS2):
            if compare(cntS1, cntS2): 
                result.append(i-lengthS1) 
                return True
  
            (cntS2[ ord(s2[i]) ]) += 1

            (cntS2[ ord(s2[i-lengthS1]) ]) -= 1
            
        if compare(cntS1,cntS2):
            result.append(lengthS2-lengthS1)
        
        
        if len(result)==0:
            return False
        else:
            return True
       
