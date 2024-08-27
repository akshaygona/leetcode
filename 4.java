import java.util.ArrayList;
import java.util.Arrays;

class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        ArrayList<Integer> arr1 = new ArrayList<>();
        for(int n : nums1){
            arr1.add(n);
        }
        for(int n : nums2){
            arr1.add(n);
        }
        int[] result = new int[arr1.size()];
        for(int i = 0; i < arr1.size(); i++){
            result[i] = arr1.get(i);
        }
        Arrays.sort(result);
        if(result.length % 2 == 0){
            int medindx1 = result.length/2 -1;
            int medindx2 = result.length/2;
            return ((float)result[medindx1] + (float)result[medindx2]) / 2;
        } else {
        return (double)((result[result.length/2]));
        }
    }
}