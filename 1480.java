class Solution {
    public int[] runningSum(int[] nums) {
        int[] runningSum = new int[nums.length];
        for(int i = 0; i < nums.length; i++){
            runningSum[i] = nums[i];
            if(i > 0 && i < nums.length){
                runningSum[i] = runningSum[i] + runningSum[i-1];
            }
        }
        return runningSum;
    }
}