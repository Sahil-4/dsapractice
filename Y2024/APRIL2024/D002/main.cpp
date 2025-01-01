#include <iostream>
#include <string>
#include <map>
#include <limits.h>

using namespace std;

int maxDepth(string s) {
    int maxCount = 0;
    int count = 0;

    for (int i = 0; i < s.length(); i++) {
        if (s[i] == '(') count++;
        if (s[i] == ')') count--;

        maxCount = max(count, maxCount);
    }

    return maxCount;
}

void p1() {
    // Problem 1 : Leetcode 1614. Maximum Nesting Depth of the Parentheses - https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/ 

    // string s = "(1+(2*3)+((8)/4))+1";
    string s = "(1)+((2))+(((3)))";

    int d = maxDepth(s);
    cout << d << endl;
}

int romanToInt(string s) {
    int ans = 0;
    int l = s.length() - 1;
    map<char, int> mp = {{'I', 1}, {'V', 5}, {'X', 10}, {'L', 50}, {'C', 100}, {'D', 500}, {'M', 1000}};

    for (int i = l; i >= 0; i--) {
        if (i == l || mp[s[i]] >= mp[s[i + 1]]) ans += mp[s[i]];
        else ans -= mp[s[i]];
    }

    return ans;
}

void p2() {
    // Problem 2 : Leetcode 13. Roman to Integer - https://leetcode.com/problems/roman-to-integer/ 

    // string s = "III";
    // string s = "VIII";
    string s = "IX";

    int number = romanToInt(s);
    cout << number << endl;
}

int myAtoi(string s) {
    int ans = 0;
    int sign = 1;
    int start = 0;

    while (start < s.length()) {
        if (s[start] == ' ') start++;
        else break;
    }

    if (start < s.length()) {
        if (s[start] == '-') {
            sign = -1;
            start++;
        }
        else if (s[start] == '+') {
            sign = 1;
            start++;
        }
    }

    for (int i = start; i < s.length(); i++) {
        if (s[i] >= '0' && s[i] <= '9') {
            int d = s[i] - '0';

            if (ans > (INT_MAX / 10) || ans == (INT_MAX / 10) && d > 7) {
                return sign == -1 ? INT_MIN : INT_MAX;
            }

            ans = (ans * 10) + d;
        } else break;
    }

    return ans * sign;
}

void p3() {
    // Problem 3 : Leetcode 8. String to Integer (atoi) - https://leetcode.com/problems/string-to-integer-atoi/ 

    // string strNum = "4545";
    // string strNum = "-4545";
    // string strNum = "    -4545";
    // string strNum = "df;sajfd -4545dfs a";
    string strNum = "-45 adjf 45";

    int intNum = myAtoi(strNum);
    cout << intNum << endl;
}


int main() {
    // Day 002 

    p1();

    p2();

    p3();


    return 0;
}