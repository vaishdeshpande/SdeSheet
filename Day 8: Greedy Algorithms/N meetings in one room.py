class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,n,start,end):
        array=[]
        for i in range(n):
            
            array.append([start[i],end[i],i])
        pair = sorted(array,key=lambda x:x[1])
        
        ans = [pair[0][2]] 
        count = 1
        last_end = pair[0][1]
        for i in range(1,n):
            if last_end < pair[i][0]:
                ans.append(pair[i][2])
                last_end = pair[i][1]
                count=count +1
        return count