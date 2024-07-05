#include <iostream>
#include <vector>

using namespace std;

bool canPlace(vector<vector<char>>& board, int r, int c, char ch) {
    // check horizontally and vertically 
    for (int i = 0; i < 9; i++) {
        if (board[r][i] == ch) return false;
        if (board[i][c] == ch) return false;
    }

    // check current sub grid 
    r = (r / 3) * 3, c = (c / 3) * 3;
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            if (board[r + i][c + j] == ch) return false;
        }
    }

    return true;
}

bool solve(vector<vector<char>>& board, int curr_row, int curr_col) {
    // found solution - exit recursion 
    if (curr_row == 9) return true;
    // update row 
    if (curr_col == 9) return solve(board, curr_row + 1, 0);
    // if col not empty 
    if (board[curr_row][curr_col] != '.') return solve(board, curr_row, curr_col + 1);

    for (int i = 1; i <= 9; i++) {
        char ch = '0' + i;
        bool check = canPlace(board, curr_row, curr_col, ch);

        if (check) {
            board[curr_row][curr_col] = ch;
            bool check_2 = solve(board, curr_row, curr_col + 1);
            if (check_2) return true;
            board[curr_row][curr_col] = '.';
        }
    }

    return false;
}

void solveSudoku(vector<vector<char>>& board) {
    solve(board, 0, 0);
}

void p1() {
    // Problem 1 : Leetcode 37. Sudoku Solver - https://leetcode.com/problems/sudoku-solver/ 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/solve-the-sudoku-1587115621/1 

    vector<vector<char>> board = {
        {'1', '.', '.', '2', '.', '.', '7', '.', '.'},
        {'.', '4', '6', '3', '.', '.', '.', '6', '.'},
        {'.', '.', '.', '5', '.', '.', '.', '1', '.'},
        {'.', '.', '.', '.', '.', '.', '.', '.', '.'},
        {'.', '.', '.', '6', '.', '.', '.', '.', '5'},
        {'.', '.', '5', '.', '.', '.', '.', '.', '8'},
        {'.', '.', '1', '.', '.', '.', '.', '.', '.'},
        {'.', '.', '.', '1', '.', '3', '4', '2', '9'},
        {'.', '6', '.', '.', '.', '.', '.', '.', '.'},
    };

    for (int i = 0; i < 9; i++) {
        for (int j = 0; j < 9; j++) cout << board[i][j] << " ";
        cout << endl;
    }
}

void solve(vector<string> &out, string exp, long long res, long long prev, int target, string num, int curr_index) {
    // cout << "num ::" << num << endl; // [ TLE, @param - num is also getting changed ]
    // answer - https://codeforces.com/blog/entry/97442 
    // cout << "num ::" << num; // this is working fine 

    int n = num.length();
    if (curr_index == n) {
        if (res == target) out.push_back(exp);
        return;
    }

    for (int i = curr_index; i < n; i++) {
        if (i > curr_index && num[curr_index] == '0') return;

        string sub = num.substr(curr_index, i - curr_index + 1);
        long long curr_number = stoll(sub);

        if (curr_index == 0) {
            solve(out, exp + sub, res + curr_number, curr_number, target, num, i + 1);
        } else {
            solve(out, exp + "+" + sub, res + curr_number, curr_number, target, num, i + 1);

            solve(out, exp + "-" + sub, res - curr_number, -curr_number, target, num, i + 1);

            solve(out, exp + "*" + sub, (res - prev) + (prev * curr_number), prev * curr_number, target, num, i + 1);
        }
    }
}

vector<string> addOperators(string num, int target) {
    vector<string> out;
    solve(out, "", 0, 0, target, num, 0);
    return out;
}

void p2() {
    // Problem 2 : Leetcode 282. Expression Add Operators - https://leetcode.com/problems/expression-add-operators/ 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/expression-add-operators/1 

    string num = "231";
    int target = 23;
    vector<string> exps = addOperators(num, target);
    for (int i = 0; i < exps.size(); i++) cout << exps[i] << endl;
}

int main() {
    // Day 5 

    p1();


    return 0;
}