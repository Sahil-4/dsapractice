#include <iostream>
#include <stack>
#include <map>
#include <algorithm>
#include <vector>

using namespace std;

int getPrecedence(char op) {
    map<char, int> precedence = {{'+', 12}, {'-', 12}, {'*', 13}, {'/', 13}, {'^', 17}};
    return precedence[op];
}

bool isOperand(char ch) {
    return isalnum(ch);
}

// Function to convert an infix expression to a postfix expression 
string infixToPostfix(string s) {
    string ans;
    stack<char> stk;

    for (int i = 0; i < s.length(); i++) {
        if (isOperand(s[i])) ans.push_back(s[i]);
        else if (s[i] == '(') stk.push(s[i]);
        else if (s[i] == ')') {
            while (stk.top() != '(') {
                ans.push_back(stk.top());
                stk.pop();
            }
            stk.pop();
        } else {
            while (!stk.empty() && getPrecedence(stk.top()) > getPrecedence(s[i])) {
                ans.push_back(stk.top());
                stk.pop();
            }
            stk.push(s[i]);
        }
    }

    while (!stk.empty()) {
        ans.push_back(stk.top());
        stk.pop();
    }

    return ans;
}

// Function to convert an infix expression to a prefix expression 
string infixToPrefix(string s) {
    reverse(s.begin(), s.end());

    for (int i = 0; i < s.length(); i++) {
        if (s[i] == '(') s[i] = ')';
        else if (s[i] == ')') s[i] = '(';
    }

    string prefix = infixToPostfix(s);
    reverse(prefix.begin(), prefix.end());

    return prefix;
}

string preToPost(string pre_exp) {
    stack<string> stk;

    for (int i = pre_exp.length() - 1; i >= 0; i--) {
        if (isalnum(pre_exp[i])) stk.push(string(1, pre_exp[i]));
        else {
            string opr1 = stk.top(); stk.pop();
            string opr2 = stk.top(); stk.pop();
            string oprtr = string(1, pre_exp[i]);
            string post_exp = opr1 + opr2 + oprtr;
            stk.push(post_exp);
        }
    }

    return stk.top();
}

void p1() {
    // Problem 1 : Geeksforgeeks - Prefix to Postfix Conversion - https://www.geeksforgeeks.org/problems/prefix-to-postfix-conversion/1 

    string pre = "*-A/BC-/AKL";
    string post = preToPost(pre);
    cout << "post :: " << post << " for pre :: " << pre << endl;
}

vector<int> nextGreaterElements_Solution1(vector<int>& nums) {
    vector<int> ans(nums.size(), -1);

    for (int i = 0; i < nums.size(); i++) {
        for (int j = i + 1; j < nums.size() * 2; j++) {
            int index2 = j % nums.size();
            if (nums[i] < nums[index2]) {
                ans[i] = nums[index2];
                break;
            }
        }
    }

    return ans;
}

vector<int> nextGreaterElements(vector<int>& nums) {
    int n = nums.size();
    vector<int> nge(n, -1);
    stack<int> stk;

    for (int i = 2 * n - 1; i >= 0; i--) {
        while (!stk.empty() && nums[stk.top()] <= nums[i % n]) stk.pop();

        if (stk.empty()) nge[i % n] = -1;
        else nge[i % n] = nums[stk.top()];

        if (stk.empty() || nums[stk.top()] > nums[i % n]) stk.push(i % n);
    }

    return nge;
}

void p2() {
    // Problem 2 : Leetcode 503. Next Greater Element II - https://leetcode.com/problems/next-greater-element-ii/ 

    vector<int> nums = {2, 5, 1, 3, 8, 5, 4, 7, 7, 1};
    vector<int> nges = nextGreaterElements(nums);
    for (int i = 0; i < nums.size(); i++) cout << "NGE for " << nums[i] << " is : " << nges[i] << endl;
}


int main() {
    // Day 14 

    p1();

    p2();


    return 0;
}