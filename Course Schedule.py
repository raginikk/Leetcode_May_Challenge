class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        neighbour = [[] for x in range(numCourses)]
        for sub1,sub2 in prerequisites:
            neighbour[sub2].append(sub1)
            
        for course in range(numCourses): 
            courseTaken = [False for x in range(numCourses)]
            s = [course]
            while len(s):
                sub = s.pop()
                if not courseTaken[sub]:
                    s.extend(neighbour[sub])
                elif sub == course:  
                    return False
                courseTaken[sub] = True
        return True     
        
