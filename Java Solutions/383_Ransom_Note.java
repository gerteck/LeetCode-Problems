class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {

    // use hashmap
        HashMap<Character, Integer> hashmap = new HashMap();

        int Rlength = ransomNote.length();
        int Mlength = magazine.length();

        if (Rlength > Mlength) {
            return false;
        }

        for (int i = 0; i < Mlength; i++) {
            Character c = magazine.charAt(i);

            Integer count = hashmap.get(c);
            if (count == null) {
                hashmap.put(c, 1);
            } else {
                hashmap.put(c, ++count);
            }
        }
        for (int i = 0; i < Rlength; i++) {
            Character c = ransomNote.charAt(i);

            Integer count = hashmap.get(c);
            if (count == null || count <= 0) {
                return false;
            } else {
                hashmap.put(c, --count);
            }
        }
        return true;


    }
}