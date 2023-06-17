class Solution {
    public int longestPalindrome(String s) {

        // letters that appear once can only be in the middle.
        // letters that appear more than once can be used evenly.

        HashMap<Character, Integer> hashmap = new HashMap();

        for (int i = 0; i < s.length(); i++) {
            Character c = s.charAt(i);
            Integer x = hashmap.get(c);
            if (x == null) {
                hashmap.put(c, 1);
            } else {
                hashmap.put(c, ++x);
            }
        }

        int length = 0;
        boolean hasSingle = false;
        Iterator<Integer> iterator = hashmap.values().iterator();

        while (iterator.hasNext()) {
            int v = iterator.next();
            if(v % 2 == 1) {
                hasSingle = true;
            }
            length += (v/2)*2;
        }

        if (hasSingle) {
            return length + 1;
        } else {
            return length;
        }

    }
}