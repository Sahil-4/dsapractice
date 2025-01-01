#include <iostream>
#include <vector>
#include <limits.h>

using namespace std;

int getMinLengthStringLength(vector<string> &strs) {
    int minLengthStr = INT_MAX;

    for (int i = 0; i < strs.size(); i++) {
        if (minLengthStr > strs[i].length()) {
            minLengthStr = strs[i].length();
        }
    }

    return minLengthStr;
}

string longestCommonPrefix(vector<string>& strs) {
    if (strs.size() == 1) return strs[0];
    string lcp = "";

    int minLengthStr = getMinLengthStringLength(strs);

    for (int i = 0; i < minLengthStr; i++) {
        bool check = true;
        char ch = strs[0][i];

        for (int j = 1; j < strs.size(); j++) {
            if (ch != strs[j][i]) {
                check = false;
                break;
            }
        }

        if (!check) break;
        else lcp += ch;
    }

    return lcp;
}

void p1() {
    // Problem 1 : Leetcode 14. Longest Common Prefix - https://leetcode.com/problems/longest-common-prefix/
    // GeeksForGeeks - https://www.geeksforgeeks.org/problems/longest-common-prefix-in-an-array5129/1 

    vector<string> strs = {};
    string lcp = longestCommonPrefix(strs);
    cout << "lcp :: " << lcp << endl;
}

int maxDepth(string s) {
    int depth = 0;
    int temp = 0;

    for (int i = 0; i < s.length(); i++) {
        if (s[i] == '(') temp++;
        else if (s[i] == ')') temp--;

        depth = max(temp, depth);
    }

    return depth;
}

void p2() {
    // Problem 2 : Leetcode 1614. Maximum Nesting Depth of the Parentheses - https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/ 
    // GeeksForGeeks - https://www.geeksforgeeks.org/problems/maximum-nesting-depth-of-the-parentheses/0 

    string s = "(1)+((2))+(((3)))";
    int d = maxDepth(s);
}

int main() {
    // Day 21 

    p1();

    p2();


    return 0;
}