class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict={}
        cnt=0
        for i in range(len(nums)):
            if nums[i] in dict:
                dict[nums[i]]+=1
            else:
                dict[nums[i]]=1
        for k in dict:
            if dict[k]>len(nums)/2:
                cnt=1
                return k
        
            
