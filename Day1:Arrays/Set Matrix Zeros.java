class Solution {
    public void setZeroes(int[][] matrix) {
        int lenRows= matrix.length;
        int lenCols = matrix[0].length;
        boolean[] rows = new boolean[lenRows];
        boolean[] cols = new boolean[lenCols];
        int i,j;
        for(i=0;i<lenRows;i++){
            for(j=0;j<lenCols;j++){
                if(matrix[i][j]==0){
                    rows[i]=true;
                    cols[j]=true;
                }
            }
        }
        for(i=0;i<lenRows;i++){
            if(rows[i]==true){
                for(j=0;j<lenCols;j++){
                    matrix[i][j]=0;
                }
            }
        }
        for(j=0;j<lenCols;j++){
            if(cols[j]==true){
                for(i=0;i<lenRows;i++){
                    matrix[i][j]=0;
                }
            }
        }
    
    }
}