class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        
        length = len(trust)
        if length == 0:
            return N
        if length == 1:
            return trust[0][1]
        
        cnt=[]
        arrayX=[]
        arrayY=[]
        for pair in trust:
            arrayX.append(pair[0])
            arrayY.append(pair[1])
        # print(arrayX,arrayY)    
        for person in arrayY:
            if person not in arrayX:
                cnt.append(person)
        if len(cnt)==0:
            return -1
        x=cnt[0]
        flag=False
        for i in range(1,len(cnt)):
            if arrayY.count(cnt[i])>arrayY.count(x):
                if(arrayY.count(cnt[i])>1):
                    x=cnt[i]
                    flag=True
            else:
                if(arrayY.count(x)>1):
                    flag=True
                
        
                
        if(flag):
            count=0
            for y in range(1,N+1):
                if([y,x] in trust):
                    count+=1
            if(count==N-1)   :
                return x
            else:
                return -1
        else:
            return -1
        
                
      
