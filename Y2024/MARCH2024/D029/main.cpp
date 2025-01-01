#include <iostream>
#include <vector>
#include <string>
#include <stack>

using namespace std;

int findMax(vector<vector<int>>& mat, int c) {
    int r = 0;

    for (int i = 1; i < mat.size(); i++) {
        if (mat[r][c] < mat[i][c]) r = i;
    }

    return r;
}

vector<int> findPeakGrid(vector<vector<int>>& mat) {
    int c_size = mat[0].size();

    int low = 0, high = c_size - 1;

    int mid = low + (high - low) / 2;

    while (low <= high) {
        int r = findMax(mat, mid);
        int c = mid;

        if ((c == 0 || mat[r][c] > mat[r][c - 1]) && (c == c_size - 1 || mat[r][c] > mat[r][c + 1])) return {r, c};
        else if (c == 0 || mat[r][c] > mat[r][c - 1]) low = mid + 1;
        else high = mid - 1;

        mid = low + (high - low) / 2;
    }

    return {-1, -1};
}

void p1() {
    // Problem 1 : Leetcode 1901. Find a Peak Element II - https://leetcode.com/problems/find-a-peak-element-ii/  

    vector<vector<int>> mat = {{7,2,3,1,2},{6,5,4,2,1}};
    vector<int> coord = findPeakGrid(mat);

    cout << "i : " << coord[0] << " j : " << coord[1] << endl;
    cout << "element : " << mat[coord[0]][coord[1]] << endl;
}

string removeOuterParentheses(string s) {
    string ans = "";
    stack<char> stk;
    int start = 1;

    for (int i = 0; i < s.length(); i++) {
        if (s[i] == '(') stk.push(s[i]);
        else stk.pop();

        if (stk.empty()) ans += s.substr(start, i - start), start = i + 2;
    }

    return ans;

    // ! Can be optimised 
}

void p2() {
    // Problem 2 : LC 1021. Remove Outermost Parentheses - https://leetcode.com/problems/remove-outermost-parentheses/ 

    string str = "(()())(())(()(()))";

    string out = removeOuterParentheses(str);

    cout << out << endl;
}


int main() {
    // Day 29 

    p1();

    p2();

    return 0;
}