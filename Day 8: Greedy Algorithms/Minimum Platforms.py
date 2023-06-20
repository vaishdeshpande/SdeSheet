class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,n,arr,dep):
        arr.sort()
        dep.sort()
        currPlatform = 1
        maxPlatform = 1
        arr_i=1
        dep_i=0
        while arr_i<n and dep_i<n :
            if arr[arr_i]<=dep[dep_i]:
                currPlatform = currPlatform+1
                arr_i+=1;
            else:
                currPlatform-=1
                dep_i+=1;
            maxPlatform = max(currPlatform,maxPlatform)
            
        return maxPlatform   