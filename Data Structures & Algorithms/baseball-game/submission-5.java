class Solution {
    public int calPoints(String[] operations) {
        Stack<Integer> stack = new Stack<>();
        int temp1 = 0;
        int temp2 = 0;
        for (String op : operations){
            if (op.equals("+")){
                temp1 = stack.pop();
                temp2 = stack.peek();
                stack.push(temp1);
                stack.push((temp1+temp2));
            }
            else if (op.equals("D")){
                temp1 = stack.pop();
                stack.push(temp1);
                stack.push((temp1*2));
            }
            else if(op.equals("C")){
                stack.pop();
            }
            else{
            stack.push(Integer.parseInt(op));}
        }
        int t = 0;
        for (Integer s : stack){
            t += s;
        }
        return t;
    }
}