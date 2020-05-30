class Solution:
    def countBits(self, num: int) -> List[int]:
        arr=[]
        for i in range(num+1):
            x=str(bin(i).replace('0b',''))
            arr.append(x.count('1'))
        return arr    
        
