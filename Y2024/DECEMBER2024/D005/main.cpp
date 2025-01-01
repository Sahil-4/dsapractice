#include <bits/stdc++.h>

using namespace std;

int _minAddToMakeValid_(string s) {
    stack<char> stack;

    for (int i = 0, N = s.length(); i < N; i++) {
        if (!stack.empty() && stack.top() == '(' && s[i] == ')') stack.pop();
        else stack.push(s[i]);
    }

    return stack.size();

    // Complexity analysis 
    // Time : O(N) 
    // Space : O(N) 
}

int minAddToMakeValid(string s) {
    int addsReq = 0, openBrackets = 0;

    for (int i = 0; i < s.length(); i++) {
        if (s[i] == '(') openBrackets++;
        else if (s[i] == ')' && openBrackets == 0) addsReq++;
        else openBrackets--;
    }

    return addsReq + openBrackets;

    // Complexity analysis 
    // Time : O(N) 
    // Space : O(1) 
}

void p1() {
    // Problem 1 : Leetcode 921. Minimum Add to Make Parentheses Valid - https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/ 

    cout << _minAddToMakeValid_("()(((()))))))") << endl;
    cout << minAddToMakeValid("()(((()))))))") << endl;
}

string rle(string str) {
    string out = "";

    for (int i = 0, count = 1; i < str.length(); i++, count++) {
        if ((i + 1 == str.length()) || str[i] != str[i + 1]) {
            out = out + to_string(count) + str[i];
            count = 0;
        }
    }

    return out;
}

string recursion(int n) {
    if (n == 1) return "1";
    string prev = recursion(n - 1);
    return rle(prev);

    // Complexity analysis 
    // Time : O(n * prev_len) 
    // Space : O(n) 
}

string iterative(int n) {
    string str = "1";

    while (n-- >= 2) str = rle(str);

    return str;

    // Complexity analysis 
    // Time : O(n * str_len) 
    // Space : O(1) 
}

string countAndSay(int n) {
    // return recursion(n);
    return iterative(n);
}

void p2() {
    // Problem 2 : Leetcode 38. Count and Say - https://leetcode.com/problems/count-and-say/ 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/decode-the-pattern1138/1 

    cout << countAndSay(2) << endl;
    cout << countAndSay(5) << endl;
    cout << countAndSay(12) << endl;
    cout << countAndSay(30) << endl;
}


int main() {
    // Day 5 of December - started with String hard 

    p1();

    p2();


    return 0;
}