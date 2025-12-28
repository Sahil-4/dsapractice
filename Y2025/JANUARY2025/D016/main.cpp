#include <bits/stdc++.h>

using namespace std;


class Problem1 {
public:
    bool isValid(string s) {
        stack<char> stk;

        for (int i = 0; i < s.length(); i++) {
            if (stk.empty() || s[i] == '(' || s[i] == '[' || s[i] == '{') {
                stk.push(s[i]);
            }
            else if (s[i] == ')' && stk.top() == '(') {
                stk.pop();
            }
            else if (s[i] == '}' && stk.top() == '{') {
                stk.pop();
            }
            else if (s[i] == ']' && stk.top() == '[') {
                stk.pop();
            }
            else {
                stk.push(s[i]);
            }
        }

        return stk.empty();

        // Complexity analysis 
        // Time : O(N) 
        // Space : O(N) 
    }
};

void p1() {
    // Problem 1 : Leetcode 20. Valid Parentheses - https://leetcode.com/problems/valid-parentheses/?envType=study-plan-v2&envId=top-interview-150 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/parenthesis-checker2744/1 

    cout << Problem1().isValid("(((}}}{{{}}})))") << endl;
    cout << Problem1().isValid("((({{{}}}[][][])))") << endl;
}

class Problem2 {
public:
    string simplifyPath(string path) {
        // step 1: replace multiple consecutive slashes with a single slash 
        for (int i = 0; i < path.length();) {
            while (i < path.length() && path[i] != '/') i++;
            int len = 0;
            while (i + len < path.length() && path[i + len] == '/') len++;
            path.erase(i, len - 1);
            i++;
        }
        if (path.back() == '/') path.pop_back();

        deque<string> dq;
        // step 2: obtain directories and add them into queue 
        for (int i = 0; i < path.length();) {
            while (i < path.length() && path[i] == '/') i++;
            int len = 0;
            while (i + len < path.length() && path[i + len] != '/') len++;
            string dir = path.substr(i, len);
            if (dir != "." && dir != "..") dq.push_back(dir);
            if (dir == ".." && !dq.empty()) dq.pop_back();
            i += len;
        }

        // step 3 : create path in unix style 
        string upath = "";
        while (!dq.empty()) {
            cout << dq.front() << " ";
            upath += "/" + dq.front();
            dq.pop_front();
        }

        if (upath == "") return "/";
        return upath;

        // Complexity analysis 
        // Time : O(N) ~ 
        // Space : O(N) 
    }
};

void p2() {
    // Problem 2 : Leetcode 71. Simplify Path - https://leetcode.com/problems/simplify-path/?envType=study-plan-v2&envId=top-interview-150 

    cout << Problem2().simplifyPath("/////home///user/....../Documents/./../Pictures") << endl;
}


int main() {
    // Day 16 of January 2025 

    p1();

    p2();


    return 0;
}