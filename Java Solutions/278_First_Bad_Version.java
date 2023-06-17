/* The isBadVersion API is defined in the parent class VersionControl.
      boolean isBadVersion(int version); */

public class Solution extends VersionControl {

    // Basically binary search
    public int firstBadVersion(int n) {
        int start = 1;
        int half = n/2;
        int end = n;

        boolean bad;
        // first bad version is this or before this

        while (end - start > 0) {
            bad = isBadVersion(half);

            if (bad) {
                end = half;
            } else {
                start = half + 1;
            }

            half = start + ( (end-start)/2 );
        }

        return start;
    }


}