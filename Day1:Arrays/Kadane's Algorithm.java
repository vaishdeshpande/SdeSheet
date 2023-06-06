class Solution {
    public int maxSubArray(int[] nums) {
        int sum = Integer.MIN_VALUE;
        int curr=0;
        int l = nums.length;
        for(int i=0;i<l;i++){
            curr = curr + nums[i];
            if(curr>sum){
                sum = curr;
            }
            if(curr<0){
                curr=0;
            }
        }
        return sum;
    }
}