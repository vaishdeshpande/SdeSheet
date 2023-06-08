class Solution {
    public int maxProfit(int[] prices) {
        int buy=prices[0],sell;
        int profit =  0;
        for(int i=1;i<prices.length;i++){
            sell = prices[i];
            if(buy>prices[i]){
                buy = prices[i];
            }
            
            profit=Math.max(profit,sell-buy);
            
        }
        return profit;
    }
}