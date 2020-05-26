class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        max_len = 0
        cnt = 0
        dp={0:0}
        for i,num in enumerate(nums,1):
            if num==0:
                cnt-=1
            else:
                cnt+=1
            if cnt in dp:
                max_len = max(max_len, i - dp[cnt])
            else:
                dp[cnt] = i
        return max_len        
