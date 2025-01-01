#include <iostream>
#include <vector>
#include <limits.h>
#include <stack>

using namespace std;

bool isValid(string s) {
    string c = "";

    for (int i = 0; i < s.length(); i++) {
        if (s[i] == '(' || s[i] == '{' || s[i] == '[') {
            c.push_back(s[i]);
        } else if (c != "" && ((s[i] == ')' && c.back() == '(') || (s[i] == '}' && c.back() == '{') || (s[i] == ']' && c.back() == '['))) {
            c.pop_back();
        } else {
            return false;
        }
    }

    return c == "";
}

void p1() {
    // Problem 1 : Leetcode 20. Valid Parentheses - https://leetcode.com/problems/valid-parentheses/description/ 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/parenthesis-checker2744/1 

    cout << isValid("((()){{{}{}}})))") << endl;
}

class MinStack_1 {
private:
    vector<pair<int, int>> stack;

public:
    MinStack_1() {}

    void push(int val) {
        int minival = val;
        if (stack.size() != 0 && stack.back().second < minival) {
            minival = stack.back().second;
        }

        stack.push_back({ val, minival });
    }

    void pop() {
        stack.pop_back();
    }

    int top() {
        if (stack.size() == 0) return INT_MIN;
        return stack.back().first;
    }

    int getMin() {
        if (stack.size() == 0) return INT_MIN;
        return stack.back().second;
    }
};

class MinStack {
private:
    stack<long long> stk;
    long long minimum;

public:
    MinStack() {}

    void push(int val) {
        if (stk.empty()) {
            minimum = val;
            stk.push(val);
        } else if (minimum < val){
            stk.push(val);
        } else {
            stk.push((long long)2 * val - minimum);
            minimum = val;
        }
    }

    void pop() {
        if (stk.empty()) return;
        if (stk.top() < minimum) {
            minimum = 2 * minimum - stk.top();
        }
        stk.pop();
    }

    int top() {
        if (stk.empty()) return INT_MIN;
        if (stk.top() < minimum) return minimum;
        else return stk.top();
    }

    int getMin() {
        if (stk.empty()) return INT_MIN;
        return minimum;
    }
};


void p2() {
    // Problem 2 : Leetcode 155. Min Stack - https://leetcode.com/problems/min-stack/description/ 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/get-minimum-element-from-stack/1 

    MinStack ms = MinStack();
    ms.push(4);
    ms.push(5);
    ms.push(5);
    cout << ms.getMin() << endl;
    ms.pop();
    cout << ms.top() << endl;
    cout << ms.getMin() << endl;
    ms.push(3);
    cout << ms.top() << endl;
    cout << ms.getMin() << endl;
    ms.push(8);
    ms.push(9);
    cout << ms.top() << endl;
    cout << ms.getMin() << endl;
}

int main() {
    // Day 6 

    p1();

    p2();


    return 0;
}