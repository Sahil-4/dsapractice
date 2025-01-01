#include <iostream>
#include <stack>
#include <string>
#include <vector>
#include <limits.h>

using namespace std;

string postToInfix(string exp) {
    // Write your code here
    stack<string> stk;

    for (int i = 0; i < exp.length(); i++) {
        if (isalnum(exp[i])) {
            stk.push(string(1, exp[i]));
        } else {
            string oprtr = string(1, exp[i]);
            string oprnd2 = stk.top(); stk.pop();
            string oprnd1 = stk.top(); stk.pop();
            // string subExp = "(" + oprnd1 + oprtr + oprnd2 + ")"; // TLE 
            stk.push("(" + oprnd1 + oprtr + oprnd2 + ")"); // No TLE 
        }
    }

    return stk.top();
}

void p1() {
    // Problem 1 : Geeksforgeeks - Postfix to Infix Conversion - https://www.geeksforgeeks.org/problems/postfix-to-infix-conversion/1 

    string postExp = "ab+x*";
    string infixExp = postToInfix(postExp);
    cout << "infix expression for :: " << postExp << " is :: " << infixExp << endl;
}

int sumSubarrayMins_Solution1(vector<int>& arr) {
    int modo = 1000000007;
    int sum = 0;

    for (int i = 0; i < arr.size(); i++) {
        int min = INT_MAX;
        for (int j = i; j < arr.size(); j++) {
            if (min > arr[j]) min = arr[j];
            sum = (sum % modo) + (min % modo) % modo;
        }
    }

    return sum;

    // TLE 
}

vector<int> generateNSL(vector<int>& arr, int n) {
    vector<int> nsl(n);
    stack<int> stk;

    // find next smaller left 
    for (int i = 0; i < n; i++) {
        while (!stk.empty() && arr[stk.top()] >= arr[i]) stk.pop();

        if (stk.empty()) nsl[i] = -1;
        else nsl[i] = stk.top();

        stk.push(i);
    }

    return nsl;
}

vector<int> generateNSR(vector<int>& arr, int n) {
    vector<int> nsr(n);
    stack<int> stk;

    // find next smaller right 
    for (int i = n - 1; i >= 0; i--) {
        while (!stk.empty() && arr[stk.top()] > arr[i]) stk.pop();

        if (stk.empty()) nsr[i] = n;
        else nsr[i] = stk.top();

        stk.push(i);
    }

    return nsr;
}

int sumSubarrayMins(vector<int>& arr) {
    int modo = 1e9 + 7;
    int sum = 0;

    int n = arr.size();

    vector<int> nsl = generateNSL(arr, n);
    vector<int> nsr = generateNSR(arr, n);

    for (int i = 0; i < n; i++) {
        long long subArrs = (i - nsl[i]) * (nsr[i] - i);
        long long element = arr[i];
        long long prod = (element % modo) * (subArrs % modo) % modo;
        sum = ((sum % modo) + (prod % modo) % modo);
    }

    return sum;
}

void p2() {
    // Problem 2 : Leetcode 907. Sum of Subarray Minimums - https://leetcode.com/problems/sum-of-subarray-minimums/ 

    vector<int> arr = {2, 12, 5, 2, 7, 5};
    int sum = sumSubarrayMins(arr);
    cout << "SUM :: " << sum << endl;
}

int main() {
    // Day 16 

    p1();

    p2();


    return 0;
}