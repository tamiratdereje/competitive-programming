class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        ind1, ind2 = 0, 0
        sorted_array = []
        while ind1 < len(nums1) and ind2 < len(nums2):
            
            if nums1[ind1] <= nums2[ind2]:
                sorted_array.append(nums1[ind1])
                ind1 += 1
            
            else:
                sorted_array.append(nums2[ind2])
                ind2+=1
        
        
        sorted_array += nums1[ind1:]
        sorted_array += nums2[ind2:]
            
        if len(sorted_array) % 2 == 0:
            
            mid = len(sorted_array)//2
            
            ans = (sorted_array[mid] + sorted_array[mid-1])/2
            return ans
        else:
            if len(sorted_array) == 1:
                return float(sorted_array[0])
            mid = len(sorted_array)//2
            return sorted_array[mid]
            
                
