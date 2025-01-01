#include <iostream>
#include <vector>

using namespace std;

bool canbePlace(vector<vector<char>>& board, int y, int x, char c) {
    for (int i = 0; i < 9; i++) {
        // check in entire grid 
        if (board[y][i] == c || board[i][x] == c) return false;

        // check in current sub-grid 
        if (board[3 * (y / 3) + i / 3][3 * (x / 3) + i % 3] == c) return false;
    }

    return true;
}

bool solve(vector<vector<char>>& board, int y, int x) {
    // crossed the board - moved out of board - means we have put all numbers 
    if (y == board.size()) return true;

    if (board[y][x] != '.') {
        x++;
        if (x == board.size()) y++, x = 0;

        bool isDone = solve(board, y, x);
        if (isDone) return true;

        if (x == 0) x = board.size(), y--;
        x--;

        return false;
    }

    for (int i = 1; i <= 9; i++) {
        char ch = '0' + i;

        if (canbePlace(board, y, x, ch)) {
            board[y][x] = ch;
            x++;
            if (x == board.size()) y++, x = 0;

            bool isDone = solve(board, y, x);
            if (isDone) return true;

            if (x == 0) x = board.size(), y--;
            x--;
            board[y][x] = '.';
        }
    }

    return false;
}

void solveSudoku(vector<vector<char>>& board) {
    solve(board, 0, 0);
}

void p1() {
    // Problem 1 : Leetcode 37. Sudoku Solver - https://leetcode.com/problems/sudoku-solver/ 

    vector<vector<char>> board = {
        {'5', '3', '.', '.', '7', '.', '.', '.', '.'},
        {'6', '.', '.', '1', '9', '5', '.', '.', '.'},
        {'.', '9', '8', '.', '.', '.', '.', '6', '.'},
        {'8', '.', '.', '.', '6', '.', '.', '.', '3'},
        {'4', '.', '.', '8', '.', '3', '.', '.', '1'},
        {'7', '.', '.', '.', '2', '.', '.', '.', '6'},
        {'.', '6', '.', '.', '.', '.', '2', '8', '.'},
        {'.', '.', '.', '4', '1', '9', '.', '.', '5'},
        {'.', '.', '.', '.', '.', '8', '.', '7', '9'},
    };

    cout << "before solving" << endl;
    for (int i = 0; i < board.size(); i++) {
        for (int j = 0; j < board.size(); j++) {
            cout << board[i][j] << " ";
        } cout << endl;
    }

    solveSudoku(board);

    cout << "after solving" << endl;
    for (int i = 0; i < board.size(); i++) {
        for (int j = 0; j < board.size(); j++) {
            cout << board[i][j] << " ";
        } cout << endl;
    }
}

int main() {
    // Day 30 - Completed 4 Months (Jan, Feb, Mar, Apr) total 121 days 

    p1();


    return 0;
}