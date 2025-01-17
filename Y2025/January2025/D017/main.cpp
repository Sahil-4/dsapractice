#include <bits/stdc++.h>

using namespace std;


class MinStack {
    class Node {
    public:
        int val;
        int mini;

        Node() {}

        Node(int val, int mini) {
            this->val = val;
            this->mini = mini;
        }
    };

    stack<Node> s;

public:
    MinStack() {}

    void push(int val) {
        int mini = s.empty() ? val : min(this->getMin(), val);
        s.push({ val, mini });
    }

    void pop() {
        s.pop();
    }

    int top() {
        return s.top().val;
    }

    int getMin() {
        return s.top().mini;
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(val);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */

void p1() {
    // Problem 1 : Leetcode 155. Min Stack - https://leetcode.com/problems/min-stack/description/?envType=study-plan-v2&envId=top-interview-150 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/get-minimum-element-from-stack/1 

    MinStack* obj = new MinStack();
    obj->push(5);
    cout << "top:: " << obj->top() << endl;
    cout << "getMin:: " << obj->getMin() << endl;
    obj->push(7);
    cout << "top:: " << obj->top() << endl;
    cout << "getMin:: " << obj->getMin() << endl;
    obj->push(2);
    obj->push(8);
    cout << "top:: " << obj->top() << endl;
    cout << "getMin:: " << obj->getMin() << endl;
    obj->pop();
    cout << "top:: " << obj->top() << endl;
    cout << "getMin:: " << obj->getMin() << endl;
}

class Problem2 {
    string eval(string token, string a, string b) {
        int res = 0;

        int aa = stoi(a);
        int bb = stoi(b);

        if (token == "+") {
            res = aa + bb;
        } else if (token == "-") {
            res = aa - bb;
        } else if (token == "*") {
            res = aa * bb;
        } else if (token == "/") {
            res = aa / bb;
        }

        return to_string(res);
    }

public:
    int evalRPN(vector<string>& tokens) {
        stack<string> s;

        for (int i = 0; i < tokens.size(); i++) {
            string token = tokens[i];
            if (token != "+" && token != "-" && token != "*" && token != "/") {
                s.push(token); // push operand
            } else {
                // token; // operator
                string b = s.top(); s.pop();
                string a = s.top(); s.pop();
                string res = eval(token, a, b);
                s.push(res); // result operand 
            }
        }

        return stoi(s.top());

        // Complexity analysis 
        // Time : O(N) ~ 
        // Space : O(N) 
    }
};

void p2() {
    // Problem 2 : Leetcode 150. Evaluate Reverse Polish Notation - https://leetcode.com/problems/evaluate-reverse-polish-notation/description/?envType=study-plan-v2&envId=top-interview-150 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/evaluation-of-postfix-expression1735/1 

    vector<string> tokens = { "10","6","9","3","+","-11","*","/","*","17","+","5","+" };
    int res = Problem2().evalRPN(tokens);
    cout << res << endl;
}

class Problem3 {
public:
    int calculate(string str) {
        int res = 0;

        stack<int> stk; // store numbers/expressions/result 

        int sign = 1; // sign of number 
        int number = 0; // create number 

        for (int i = 0; i < str.length(); i++) {
            if (str[i] >= '0' && str[i] <= '9') {
                // keep creating current number 
                number = (number * 10) + (str[i] - '0');
            } else if (str[i] == '+' || str[i] == '-') {
                // current number end 
                res += (number * sign);

                // start next number 
                number = 0;
                sign = str[i] == '+' ? 1 : -1;
            } else if (str[i] == '(') {
                // sub exp start 
                stk.push(res);
                stk.push(sign);
                res = 0;
                number = 0;
                sign = 1;
            } else if (str[i] == ')') {
                // sub exp end 
                res += (number * sign);
                res *= stk.top(); stk.pop();
                res += stk.top(); stk.pop();
                number = 0;
            }
        }

        // last number 
        res += (number * sign);

        return res;
    }
};

void p3() {
    // Problem 3 : Leetcode 224. Basic Calculator - https://leetcode.com/problems/basic-calculator/description/?envType=study-plan-v2&envId=top-interview-150 

    cout << Problem3().calculate("2+512-51+(-5+7)+1-0") << endl;
}


int main() {
    // Day 17 of January 2025 

    p1();

    p2();

    p3();


    return 0;
}
