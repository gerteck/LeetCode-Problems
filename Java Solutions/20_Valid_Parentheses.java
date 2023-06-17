class Solution {
    public boolean isValid(String s) {

        int length = s.length();

        Stack<Character> stack = new Stack();

        for(int i = 0; i < length; i++) {
            Character c = s.charAt(i);

            if (c == '(' || c == '{' || c == '[' ) {
                stack.push(c);
            }

            //handling end cases
            if (c == ')'|| c == '}' || c == ']') {
                if (stack.empty()) return false;
                Character popped = stack.pop();
                if (c == ')') {
                    if (popped != '(') return false;
                }
                if (c == ']') {
                    if (popped != '[') return false;
                }
                if (c == '}') {
                    if (popped != '{') return false;
                }
            }
        }
        if (stack.empty()) return true;
        return false;
    }
}