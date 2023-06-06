class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> pascal = new ArrayList<>();
        pascal.add(Arrays.asList(1));
        if(numRows==1){return pascal;}
        pascal.add(Arrays.asList(1,1));
        if(numRows==2){return pascal;}
        int subLen;
        for(int i=2;i<numRows;i++){
            subLen = pascal.get(i-1).size();
            List<Integer> newRow = new ArrayList<>();
            newRow.add(1);
            for(int j =1;j<subLen;j++){
                newRow.add(pascal.get(i-1).get(j-1)+pascal.get(i-1).get(j));
            }
            newRow.add(1);
            pascal.add(newRow);
        }
        return pascal;
    }

}