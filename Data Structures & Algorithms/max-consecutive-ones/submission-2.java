class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int m = 0;
        int a = 0;
        for (int i = 0; i < nums.length; i++){
            if (nums[i] == 0) { a = 0;}
            else a += 1;
            if (a > m) {m = a;}
        }
        return m;

    }
}