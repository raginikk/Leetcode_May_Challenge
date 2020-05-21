
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        row = len(matrix)
        if row==0:
            return 0
        col = len(matrix[0])
        if col==0:
            return 0
        
        cnt=0
        for i in range(0,col):
            cnt = cnt+ matrix[row-1][i]
        for j in range(0,row):
            cnt = cnt+ matrix[j][col-1]
        cnt =cnt -  matrix[row-1][col-1]
        for i in range(row-2,-1,-1):
            for j in range(col-2,-1,-1):
                if matrix[i][j] == 1 :
                    matrix[i][j] = min(matrix[i+1][j+1],matrix[i][j+1],matrix[i+1][j]) + 1
                    cnt += matrix[i][j];
                else:
                    matrix[i][j] = 0
                
         
        return cnt;
 
