
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        
        points.sort(key=lambda kv: kv[0]**2 + kv[1]**2)

        return(points[:K])    
            
            
          
