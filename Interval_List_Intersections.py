class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        lenA = len(A)
        lenB = len(B)
        res=[]
        if(lenA==0 or lenB==0):
            return []
       
        for i in A:
            for j in B:
                if i[0]<=j[0]:
                    if i[1]>=j[0] and i[1]<=j[1] and j[0]<=i[1]:
                        res.append([j[0],i[1]])
                    elif i[1]>=j[0] and i[1]>j[1] and j[0]<=j[1]: 
                        res.append([j[0],j[1]])
                elif i[0]>j[0]:
                    if i[1]>=j[0] and i[1]<=j[1] and i[0]<=i[1]:
                        res.append([i[0],i[1]])
                    elif i[1]>=j[0] and i[1]>j[1] and i[0]<=j[1]: 
                        res.append([i[0],j[1]])
                    
                    
        return(res)                
  
