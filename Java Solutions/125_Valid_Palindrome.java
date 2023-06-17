class Solution {
    public boolean isPalindrome(String s) {
        //use a stack to validate the palindrome

        //remove non-alphanumerical characters
        String string = s.replaceAll("[\\W]+", "").replaceAll("_", "").toLowerCase();
        int length = string.length();
        Integer middle = null;

        Stack<Character> stack = new Stack();

        if (length % 2 != 0) {
            middle = length/2;
        }

        int half = length / 2;
        Character c;

        for (int i = 0; i < length; i++) {
            if ( middle != null && i == middle) {
                middle = null;
            } else if(i < half) {
                stack.push(string.charAt(i));
            } else {
                c = stack.pop();
                if (c != string.charAt(i)) return false;
            }
        }
        return true;
    }
}