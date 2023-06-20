class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ele = -1
        count = 0
        for i in nums:
            if ele==i:
                count+=1
            elif count!=0 and ele!=i:
                count = count - 1     
            else:
                count = 1
                ele = i
            print(count,ele)
        return ele
