class Solution(object):
    def findComplement(self, num):
        return int(''.join('1' if x == '0' else '0' for x in bin(num)[2:]),2)
        
