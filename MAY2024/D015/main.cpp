#include <iostream>
#include <stack>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

string postToPre(string post_exp) {
    // Write your code here
    stack<string> stk;

    for (int i = 0; i < post_exp.length(); i++) {
        if (isalnum(post_exp[i])) {
            stk.push(string(1, post_exp[i]));
        } else {
            string oprtr = string(1, post_exp[i]);
            string oprnd2 = stk.top(); stk.pop();
            string oprnd1 = stk.top(); stk.pop();
            string sExp = oprtr + oprnd1 + oprnd2;
            stk.push(sExp);
        }
    }

    return stk.top();
}

void p1() {
    // Problem 1 : Geeksforgeeks - Postfix to Prefix Conversion - https://www.geeksforgeeks.org/problems/postfix-to-prefix-conversion/1 

    string postExp = "ABC/-AK/L-*";
    string preExp = postToPre(postExp);
    cout << "prefix expression for :: " << postExp << " is :: " << preExp << endl;
}

vector<int> getPrefixMaxes(vector<int>& heights, int n) {
    vector<int> prefixMaxes;

    for (int it = 0; it < n; it++) {
        if (prefixMaxes.empty() || prefixMaxes.back() < heights[it]) prefixMaxes.push_back(heights[it]);
        else prefixMaxes.push_back(prefixMaxes.back());
    }

    return prefixMaxes;
}

vector<int> getSuffixMaxes(vector<int>& heights, int n) {
    vector<int> suffixMaxes;

    for (int it = n - 1; it >= 0; it--) {
        if (suffixMaxes.empty() || suffixMaxes.back() < heights[it]) suffixMaxes.push_back(heights[it]);
        else suffixMaxes.push_back(suffixMaxes.back());
    }

    reverse(suffixMaxes.begin(), suffixMaxes.end());
    return suffixMaxes;
}

int trap_Solution1(vector<int>& heights) {
    int n = heights.size();
    int totalWater = 0;

    vector<int> prefixMaxes = getPrefixMaxes(heights, n);
    vector<int> suffixMaxes = getSuffixMaxes(heights, n);

    for (int it = 0; it < n; it++) {
        totalWater += min(prefixMaxes[it], suffixMaxes[it]) - heights[it];
    }

    return totalWater;
}

int trap(vector<int>& heights) {
    int waterTrapped = 0;

    int n = heights.size();
    int r = n - 1, l = 0;
    int rightMax = 0, leftMax = 0;

    while (l < r) {
        if (heights[l] <= heights[r]) {
            if (heights[l] > leftMax) leftMax = heights[l];
            else waterTrapped += leftMax - heights[l];
            l++;
        } else {
            if (heights[r] > rightMax) rightMax = heights[r];
            else waterTrapped += rightMax - heights[r];
            r--;
        }
    }

    return waterTrapped;
}

void p2() {
    // Problem 2 : Leetcode 42. Trapping Rain Water - https://leetcode.com/problems/trapping-rain-water/ 

    vector<int> heights = {3, 4, 2, 1, 0, 0, 5, 2, 1, 2, 3, 4, 2, 1, 0, 0, 5, 2, 1, 2, 3};
    int water = trap(heights);
    cout << "water :: "<< water << endl;
}

int main() {
    // Day 15 

    p1();

    p2();


    return 0;
}