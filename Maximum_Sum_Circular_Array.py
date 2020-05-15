def kadaneAlgo(A):
    
    max_so_far = 0
    max_here = 0
    
        
                   
    for i in range(0,len(A)):
        max_here = max_here+A[i]
        if(max_here<0):
            max_here = 0
        elif(max_so_far<max_here):
            max_so_far = max_here

    return (max_so_far)  

def checkIfAllNegatives(A):
    cnt=0
    for i in A:
        if i<0:
            cnt+=1
    if cnt==len(A):
        return True
    return False
class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        if(checkIfAllNegatives(A)):
            return max(A)
                
        
        max_end = 0
        max_kadane=kadaneAlgo(A)
        
        for i in range(len(A)):
            max_end = max_end + A[i]
            A[i]=-A[i]
        max_end = max_end + kadaneAlgo(A)
        if max_end>max_kadane:
            return max_end
        else:
            return max_kadane
         
