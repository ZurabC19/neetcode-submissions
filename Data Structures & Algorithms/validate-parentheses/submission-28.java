class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        for (int i = 0; i<s.length();i++)
        {
            char p = s.charAt(i);
            if (p =='(' || p== '{' ||p == '['){
            stack.push(p);}

            else{
                if (stack.isEmpty()) {return false;}

                char top = stack.pop();

                if (p ==')' && top != '(' ) {return false;}
                if (p ==']' && top != '[' ) {return false;}
                if (p =='}' && top != '{' ) {return false;}

            
        }
            

            }
            return stack.isEmpty();
    }
}
