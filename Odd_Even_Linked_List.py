# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
      
    
    
def getEvenOddList(newhead,i,root,arr):
    if(root==None or root.next==None):
        return arr
    else:
        if(root.next.next):
            newhead=root.next.next
            i=newhead.val
            arr.append(i)

            getEvenOddList(newhead.next,i,root.next.next,arr)
    return arr 

def insertNode(node, item):  
    temp = ListNode(0)  
    temp.val = item  
    temp.next = node  
    node = temp 
    return node  

def checkifAllSame(node,cnt):
    if node.next==None:
        return
    else:
        if node.val==node.next.val :
            cnt+=1
            checkifAllSame(node.next,cnt)
        else:
            return False
        
        return True    
    
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if(head==None):
            return None
        if(head.next==None):
            return head
        if checkifAllSame(head,0):
            return head
        evenhead=ListNode()
        oddhead=ListNode()
        arr1=[head.val]
        arr2=[head.next.val]
        x=getEvenOddList(evenhead,head.val,head,arr1)
        y=getEvenOddList(oddhead,head.next.val,head.next,arr2)
        for i in y:
            x.append(i)
        result = None 
        # converting Array into LL
        for i in range(len(x)-1, -1, -1):  
            result = insertNode(result, x[i]) 
            
        return result    
        
        
            
