class Solution {
    public void nextPermutation(int[] nums) {
        int lastIndex = nums.length-1;
        int index=-1;
        int temp;
        for(int i=lastIndex;i>0;i--){
            if(nums[i-1]<nums[i]){
                index = i-1;
                break;
            }
        }
        if(index==-1){
                nums=reverse(nums,0,lastIndex);
                return;
        } 
        for(int i=lastIndex;i>index;i--){
            if(nums[i]>nums[index]){
                temp = nums[index];
                nums[index]=nums[i];
                nums[i]=temp;
                nums = reverse(nums,index+1,lastIndex);
                return ;
            }
        }

        
    }

    public int[] reverse(int[] nums,int i, int j){
        int temp;
        while(i<=j){
            temp = nums[j];
            nums[j]=nums[i];
            nums[i]=temp;
            i++;
            j--;
        }
        return nums;
    }

}
