
class Solution:
    
    #Function to find the maximum profit and the number of jobs done.
    def JobScheduling(self,Jobs,n):
        arr = [-1]*(n+1)
        Jobs.sort(key=lambda x: x.profit,reverse=True)
        profit =0
        count =0
        for job in Jobs:
            deadline = job.deadline
            while deadline>0:
                if arr[deadline]==-1:
                    arr[deadline]= job.id
                    profit+=job.profit
                    count= count+1
                    break
                else:
                    deadline-=1

        return [count,profit]
           