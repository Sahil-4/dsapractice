#include <iostream>
#include <string>
#include <map>
#include <stack>

using namespace std;

int getPrecedence(char op) {
    map<char, int> precedence = {{'+', 12}, {'-', 12}, {'*', 13}, {'/', 13}, {'^', 17}};
    return precedence[op];
}

// Function to convert an infix expression to a postfix expression.
string infixToPostfix(string s) {
    // Your code here
    string ans;
    stack<char> stk;

    for (int i = 0; i < s.length(); i++) {
        // if operand add it directly into ans string 
        if (s[i] >= 'a' && s[i] <= 'z' || s[i] >= 'A' && s[i] <= 'Z' || s[i] >= '0' && s[i] <= '9') ans.push_back(s[i]);
        else if (stk.empty() || stk.top() == '(' || s[i] == '(' || getPrecedence(stk.top()) < getPrecedence(s[i])) stk.push(s[i]);
        else if (s[i] == ')') {
            while (stk.top() != '(') {
                ans.push_back(stk.top());
                stk.pop();
            }
            stk.pop();
        } else if (getPrecedence(s[i]) <= getPrecedence(stk.top())) {
            while (!stk.empty() && stk.top() != '(' && getPrecedence(s[i]) <= getPrecedence(stk.top())) {
                ans.push_back(stk.top());
                stk.pop();
            }
            stk.push(s[i]);
        } else {
            cout << "ERROR :: Unknown case" << endl;
        }
    }

    while (!stk.empty()) {
        if (stk.top() != '(' && stk.top() != ')') ans.push_back(stk.top());
        stk.pop();
    }

    return ans;
}

void p1() {
    // Problem 1 : Geeksforgeeks - Infix to Postfix - https://www.geeksforgeeks.org/problems/infix-to-postfix-1587115620/1 

    string infix = "a+(b+c)+d-d-a+(e*b)*a*o^(5*a)-2/5/1*0";
    string postfix = infixToPostfix(infix);
    cout << "infix :: " << infix << endl;
    cout << "postfix :: " << postfix << endl;
}

int calculate(string s) {
    int result = 0;

    stack<int> stk;
    int number = 0;
    int sign = 1;

    for (int i = 0; i < s.length(); i++) {
        if (s[i] == '(') {
            stk.push(result);
            stk.push(sign);
            number = 0;
            result = 0;
            sign = 1;
        } else if (s[i] == ')') {
            result += (number * sign);
            number = 0;
            result *= stk.top(); stk.pop();
            result += stk.top(); stk.pop();
        } else if (s[i] == '+' || s[i] == '-') {
            result += (number * sign);
            number = 0;
            sign = s[i] == '+' ? 1 : -1;
        } else if (s[i] >= '0' && s[i] <= '9') {
            number = (number * 10) + (s[i] - '0');
        } else {
            // "Invalid case" 
            // dont consider it 
        }
    }

    return result + (number * sign);
}

void p2() {
    // Problem 2 : Leetcode 224. Basic Calculator - https://leetcode.com/problems/basic-calculator/ 

    string str = "(1+(4+5+2)-3)+(6+8)";

    int res = calculate(str);
    cout << "result for " << str << " is " << res << endl;
}


int main() {
    // Day 12 

    p1();

    p2();


    return 0;
}