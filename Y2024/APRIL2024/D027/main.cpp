#include <iostream>
#include <vector>

using namespace std;

vector<pair<int, int>> searchableCoordinates(int y, int x) {
    return {{y, x + 1}, {y + 1, x}, {y, x - 1}, {y - 1, x}};
}

bool searchPossible(int row, int col, int tRows, int tCols) {
    if (row < 0 || col < 0 || row >= tRows || col >= tCols) return false;
    return true;
}

bool solve(vector<vector<char>>& board, string word, int i, pair<int, int> lastStep) {
    if (i == word.length()) return true;

    vector<pair<int, int>> nextCoords = searchableCoordinates(lastStep.first, lastStep.second);

    for (int it = 0; it < nextCoords.size(); it++) {
        int r = nextCoords[it].first, c = nextCoords[it].second;
        if (!searchPossible(r, c, board.size(), board[0].size())) continue;
        if (board[r][c] != word[i]) continue;
        char ch = board[r][c];
        board[r][c] = '0';
        bool ex = solve(board, word, i + 1, {r, c});
        board[r][c] = ch;
        if (ex) return ex;
    }

    return false;
}

bool exist(vector<vector<char>>& board, string word) {
    for (int i = 0; i < board.size(); i++) {
        for (int j = 0; j < board[i].size(); j++) {
            if (board[i][j] != word[0]) continue;
            char ch = board[i][j];
            board[i][j] = '0';
            bool ex = solve(board, word, 1, { i, j });
            board[i][j] = ch;
            if (ex) return ex;
        }
    }

    return false;
}

void p1() {
    // Problem 1 : Leetcode 79. Word Search - https://leetcode.com/problems/word-search/ 

    vector<vector<char>> board = {{'A','B','C','E'},{'S','F','C','S'},{'A','D','E','E'}};
    string word = "ABCB";

    cout << exist(board, word);
}

int main() {
    // Day 27 

    p1();


    return 0;
}