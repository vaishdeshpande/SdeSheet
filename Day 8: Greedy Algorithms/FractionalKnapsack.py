class Item:
    def __init__(self,val,w):
        self.value = val
        self.weight = w
        
class Solution:    
    #Function to get the maximum total value in the knapsack.
    def fractionalknapsack(self, W,arr,n):
        valWeight = []
        for i in range(n):
            valWeight.append([arr[i].value/arr[i].weight,i])
        valWeight.sort(key = lambda x:x[0])
        profit = 0
        index = 0
        while W>0:
            indexP = valWeight[index][1]
            if arr[indexP].weight <= W:
                profit += arr[indexP].value
                W = W - arr[indexP].weight
            else:
                profit += valWeight[index][0] * (W)
                W=0
            index +=1
        return profit
                