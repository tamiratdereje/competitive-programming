class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        
        def add(val, distinct_cnt):
            dict_[val] += 1
            if dict_[val] == 1:
                distinct_cnt += 1   
            return distinct_cnt
        
        def remove(val, distinct_cnt):
            dict_[val] -= 1
            if dict_[val] == 0:
                distinct_cnt -= 1
                
            return distinct_cnt
        
        dict_ = defaultdict(int)
        distinct_cnt = left = ans = 0
        last_bound = 0
        for right in range(len(nums)):
            
            distinct_cnt = add(nums[right], distinct_cnt)
            while distinct_cnt > k:
                
                distinct_cnt = remove(nums[left], distinct_cnt)
                
                left += 1
                last_bound = left
                
            if distinct_cnt == k:
                
                to_be_back = []
                while last_bound <= right and distinct_cnt == k:
                    distinct_cnt = remove(nums[last_bound], distinct_cnt)
                    to_be_back.append(nums[last_bound])
                    last_bound += 1
                    
                last_bound -= 1
                for ele in to_be_back:
                    distinct_cnt = add(ele, distinct_cnt)
                
                ans += last_bound - left + 1
                last_bound = left
                
        return ans
    
    
