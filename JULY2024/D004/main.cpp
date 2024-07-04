#include <iostream>
#include <vector>
#include <unordered_set>
#include <algorithm>

using namespace std;

bool canPlace(vector<string> board, int r, int c) {
    // '.' : default or clear 
    // 'Q' : queen is present 
    int n = board.size();

    // check out of bound indexes 
    if (r < 0 || r >= n) return false;
    if (c < 0 || c >= n) return false;

    for (int i = 0; i < n; i++) {
        // check horizontally and vertically 
        if (board[i][c] == 'Q') return false;
        if (board[r][i] == 'Q') return false;

        // check diagonally 
        if (r + i < n && c + i < n && board[r + i][c + i] == 'Q') return false;
        if (r - i >= 0 && c - i >= 0 && board[r - i][c - i] == 'Q') return false;
        if (r + i < n && c - i >= 0 && board[r + i][c - i] == 'Q') return false;
        if (r - i >= 0 && c + i < n && board[r - i][c + i] == 'Q') return false;
    }

    return true;
}

void solve(vector<vector<string>> &out, vector<string> &board, int curr_i, int n) {
    if (curr_i == n) {
        out.push_back(board);
        return;
    }

    for (int c = 0; c < n; c++) {
        if (canPlace(board, curr_i, c)) {
            board[curr_i][c] = 'Q';
            solve(out, board, curr_i + 1, n);
            board[curr_i][c] = '.';
        }
    }
}

vector<vector<string>> solveNQueens(int n) {
    vector<vector<string>> out;
    string str(n, '.');
    vector<string> board(n, str);

    solve(out, board, 0, n);

    return out;
}

void p1() {
    // Problem 1 : Leetcode 51. N-Queens - https://leetcode.com/problems/n-queens/ 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/n-queen-problem0315/1 

    int q = 5;
    vector<vector<string>> out = solveNQueens(q);
    for (int i = 0; i < out.size(); i++) {
        for (int j = 0; j < out[i].size(); j++) {
            cout << out[i][j] << endl;
        } cout << endl;
    }
}

// memoization 
unordered_set<string> memo;

bool solve(string s, vector<string>& wordDict) {
    int n = s.length();
    if (n == 0) return true;
    if (memo.find(s) != memo.end()) return false;

    for (int i = 1; i <= n; i++) {
        string sub = s.substr(0, i);
        if (memo.find(sub) != memo.end()) return false;

        if (find(wordDict.begin(), wordDict.end(), sub) != wordDict.end()) {
            string nextP = s.substr(i, n - i);
            bool check = solve(nextP, wordDict);

            if (check) return true;
            else memo.insert(nextP);
        }
    }

    memo.insert(s);
    return false;
}

bool wordBreak(string s, vector<string>& wordDict) {
    return solve(s, wordDict);
}

void p2() {
    // Problem 2 : Leetcode 139. Word Break - https://leetcode.com/problems/word-break/ 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/word-break1352/1 

    string s = "codeleetcode";
    vector<string> wordDict = {"leet", "code"};
    bool check = wordBreak(s, wordDict);
    cout << "check ::" << check << endl;
}


int main() {
    // Day 4 

    p1();

    p2();


    return 0;
}
