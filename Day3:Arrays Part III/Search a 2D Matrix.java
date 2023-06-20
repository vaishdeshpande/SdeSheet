class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int rows = matrix.length;
        int cols = matrix[0].length;
        int start = 0;
        int end = rows*cols-1;
        int mid = 0;
        while(start<=end){
            mid= start+(end-start)/2;
            int r = mid/cols;
            int c = mid%cols;
            if(target==matrix[r][c]){
                return true;
            }else if(target<matrix[r][c]){
                end = mid - 1;
            }
            else {
                start = mid+1;
            }
        }  
           return false;
    }
}