class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        
        prefix = [0]
        N = len(nums)
        for i in range(N):
            prefix.append(prefix[i] + nums[i])
        
        dict_ = {}
        ans = 0
        for i in range(N + 1):
            if prefix[i]%k in dict_:
                ans += dict_[prefix[i]%k]
                dict_[prefix[i]%k] += 1
            else:
                dict_[prefix[i]%k] = 1
        return ans
