class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates)==2:
            return True
        else:
            slopeDefault = findSlope(coordinates[0],coordinates[1])
            i=2
            while i<len(coordinates):
                if findSlope(coordinates[i-1],coordinates[i])==slopeDefault:
                    i+=1
                else:
                    return False
            return True    
                
                
                
def findSlope(coord1,coord2):
    x1=coord1[0]
    y1=coord1[1]
    x2=coord2[0]
    y2=coord2[1]
    if(x2-x1)==0:
        slope=x2
    else:
        slope = (y2-y1)/(x2-x1)
    return slope
    
