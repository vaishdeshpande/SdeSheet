public class Solution {
    // DO NOT MODIFY THE ARGUMENTS WITH "final" PREFIX. IT IS READ ONLY
    public int[] repeatedNumber(final int[] A) {
        int[] nums =A;
		int l = nums.length;
		long sum = l*(l+1)/2;
		int slow=0,fast=0;
		slow = nums[slow];
		fast = nums[nums[fast]] ;
		while(nums[slow]!=nums[fast]){
			slow = nums[slow]%(l+1);
			fast = nums[nums[fast]]%(l+1) ;

		}
		fast=0;
		while(nums[slow]!=nums[fast]){
			slow = nums[slow]%(l+1);
			fast = nums[fast]%(l+1);

		}
		int repeatedNumber = nums[slow];
		long arraySum =0;
		for(Integer num:nums){
			arraySum = arraySum + num;
		}
		arraySum = arraySum - repeatedNumber;
		System.out.println(arraySum);
        int missingNumber = (int)(sum - arraySum);
		int[] res = {nums[slow],missingNumber};
		return res;
    }
}
