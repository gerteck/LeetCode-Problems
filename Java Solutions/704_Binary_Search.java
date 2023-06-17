class Solution {
    public int search(int[] nums, int target) {
        int length = nums.length;

        int start = 0;
        int middle = length / 2 - 1;
        int end = length - 1;

        //if (nums[0] == target) return 0;

        while ( end - start > 0) {
            if( nums[middle] == target) {
                return middle;
            } else if ( target > nums[middle] ) {
                start = middle + 1;
                middle = start + (end-start)/2;
            } else {
                end = middle - 1;
                middle = start + (end-start)/2;
            }
        }

        if (nums[start] == target) {
            return start;
        }
        return -1;
    }
}