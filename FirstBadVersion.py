# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        first=1
        last=n
        found=False
        
        while(first<last):
            mid=first + (last-first)//2
            if(isBadVersion(mid)):
                last=mid
            else:
                first = mid+1
        return  first           
       
        
