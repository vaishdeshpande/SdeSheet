class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums) # size of the array
        ele1 = float('-inf')
        ele2 = float('-inf')
        count1 = count2 = 0

        for i in nums:
            if count1==0 and ele2!=i:
                ele1=i
                count1=1
            elif count2==0 and ele1!=i:
                ele2=i
                count2=1
            elif i==ele1:
                count1+=1
            elif i==ele2:
                count2+=1
            else:
                count1-=1
                count2-=1
        # Manually check if the stored elements in
        # el1 and el2 are the majority elements:
        count1, count2 = 0, 0
        for i in range(n):
            if nums[i] == ele1:
                count1 += 1
            if nums[i] == ele2:
                count2 += 1
        ls=[]
        mini = int(n / 3) + 1
        if count1 >= mini:
            ls.append(ele1)
        if count2 >= mini:
            ls.append(ele2)

        # Uncomment the following line
        # if it is told to sort the answer array:
        #ls.sort() #TC --> O(2*log2) ~ O(1);

        return ls