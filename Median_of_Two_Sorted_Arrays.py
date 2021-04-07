class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1+nums2 #add the arrays together
        nums.sort() #use sort, dont overcomplicate this
        if (len(nums) % 2) == 0: #if even
            return (nums[int(len(nums)/2)]+nums[int(len(nums)/2) - 1]) / 2 #return the average of two middle numbers
        else: #if odd
            return nums[int((len(nums) - 1) / 2)] #return middle operand (above will force float so we dont worry about casting)
