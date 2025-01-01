import java.util.Stack;

class Main {
    public static boolean checkValidString(String s) {
        // range - should be 0 to n to be valid
        int range_min = 0, range_max = 0;

        // traversal
        for (int i = 0; i < s.length(); i++) {
            switch (s.charAt(i)) {
                case '(' -> {
                    // add - open
                    range_min++;
                    range_max++;
                }
                case ')' -> {
                    // remove - close
                    range_min--;
                    range_max--;
                }
                default -> {
                    // increase range
                    range_min--;
                    range_max++;
                }
            }

            // make min range valid
            if (range_min < 0)
                range_min = 0;

            // if there is no opening for any paren
            if (range_max < 0)
                return false;
        }

        // return true, if valid range
        return (range_min == 0);
    }

    static void p1() {
        // Problem 1 : Leetcode 678. Valid Parenthesis String -
        // https://leetcode.com/problems/valid-parenthesis-string/

        String s = "*())";
        boolean b = checkValidString(s);
        System.out.println(s + "is valid ::" + b);
    }

    static boolean ispar(String s) {
        // add your code here
        Stack<Character> stk = new Stack<>();

        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '(' || s.charAt(i) == '{' || s.charAt(i) == '[') {
                stk.push(s.charAt(i));
            } else {
                if (stk.empty())
                    return false;

                char last = stk.peek();

                if (s.charAt(i) == ')' && last == '(' || s.charAt(i) == '}' && last == '{'
                        || s.charAt(i) == ']' && last == '[') {
                    stk.pop();
                } else {
                    stk.push(s.charAt(i));
                }
            }
        }

        return stk.empty();
    }

    static void p2() {
        // Problem 2 : Geeksforgeeks Parenthesis Checker -
        // https://www.geeksforgeeks.org/problems/parenthesis-checker2744/1

        String s = "()({}[{}])";
        boolean b = ispar(s);
        System.out.println(s + "is valid ::" + b);
    }

    public static void main(String[] args) {
        // Day 25 - Day 5 of greedy 

        p1();

        p2();
    }
}