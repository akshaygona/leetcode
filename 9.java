class Solution {
    public boolean isPalindrome(int x) {
        String s = Integer.toString(x);
        char[] x1 = s.toCharArray();
        for(int i = 0; i < x1.length; i++){
            if(x1[i] != x1[x1.length-i-1]){
                return false;
            }
        }
        return true;
    }
}