class Solution {
    public boolean isAnagram(String s, String t) {
        // use a hashmap

        HashMap<Character, Integer> dict = new HashMap();

        for ( int i = 0; i < s.length(); i++ ) {
            Character c = s.charAt(i);
            Integer count = dict.get(c);
            if (count == null) {
                dict.put(c, 1);
            } else {
                dict.put(c, ++count);
            }
        }

        for ( int i = 0; i < t.length(); i++ ) {
            Character c = t.charAt(i);
            Integer count = dict.get(c);
            if (count == null) {
                return false;
            } else {
                dict.put(c, --count);
            }
        }

        for (Integer value : dict.values()) {
            if (value != 0) {
                return false;
            }
        }

        return true;   
    }
}