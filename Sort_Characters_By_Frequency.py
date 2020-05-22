from collections import Counter 
class Solution:
    def frequencySort(self, s: str) -> str:
        
        res = [element for chars, c in Counter(s).most_common() for element in [chars] * c] 
        return ("").join(res)            
                
       
