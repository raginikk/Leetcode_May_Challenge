def FillPixel(image,r,c,prevC,newC):
    if( r<0 or r>=len(image) or c<0 or c>=len(image[0]) or image[r][c]==newC or image[r][c]!=prevC):
        return
    image[r][c]=newC
    
    FillPixel(image,r+1,c,prevC,newC)
    FillPixel(image,r-1,c,prevC,newC)
    FillPixel(image,r,c+1,prevC,newC)
    FillPixel(image,r,c-1,prevC,newC)
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        prevC = image[sr][sc]
        FillPixel(image,sr,sc,prevC,newColor) 
        
        return image

        
        
       
