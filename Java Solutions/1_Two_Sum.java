import java.util.HashMap;

class Solution {
    public int[] twoSum(int[] nums, int target) {

        HashMap<Integer, Integer> hashbrown = new HashMap();
        int number;
        int complement;

        int length = nums.length;
        for(int i = 0; i < length; i++) {
            number = nums[i];
            complement = target - number;

            Integer comp = hashbrown.get(complement);

            // if complement does not exist, we add the indice of the numebr
            if (comp == null) {
                hashbrown.put(number, i);
            }

            //complement exists, we immediately return the answer
            else {
                int[] solution = new int[2];
                solution[0] = comp;
                solution[1] = i;
                return solution;
            }
        }

        return new int[2];
    }
}