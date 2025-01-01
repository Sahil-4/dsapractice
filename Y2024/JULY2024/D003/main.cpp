#include <iostream>
#include <vector>

using namespace std;

bool isPalindrome(string &s, int l, int h) {
    while (l < h) {
        if (s[l] != s[h]) return false;
        l++, h--;
    }
    return true;
}

void solve(vector<vector<string>> &out, vector<string> &palinds, string &s, int start_index) {
    int n = s.length();
    if (start_index >= n) {
        out.push_back(palinds);
        return;
    }

    for (int i = 1; i <= n - start_index; i++) {
        bool check = isPalindrome(s, start_index, start_index + i - 1);

        if (check) {
            palinds.push_back(s.substr(start_index, i));
            solve(out, palinds, s, start_index + i);
            palinds.pop_back();
        }
    }
}

vector<vector<string>> partition(string s) {
    vector<vector<string>> out;
    vector<string> palinds;
    solve(out, palinds, s, 0);

    return out;
}

void p1() {
    // Problem 1 : Leetcode 131. Palindrome Partitioning - https://leetcode.com/problems/palindrome-partitioning/ 

    string s = "assbab";
    vector<vector<string>> out = partition(s);
    for (int i = 0; i < out.size(); i++) {
       for (int j = 0; j < out.size(); j++) cout << out[i][j] << " ";
       cout << endl;
    }
}

bool isOutOfBound(int row, int col, int n, int m) {
    // out of bound index 
    if (row < 0 || row >= n) return true;
    if (col < 0 || col >= m) return true;

    return false;
}

bool find(vector<vector<char>>& board, string &word, int curr_index, int row, int col) {
    // found all chars of word 
    if (curr_index >= word.length()) return true;

    // check next char in all 4 direction - nextPoints 
    vector<pair<int, int>> nextPoints = {{row, col + 1}, {row + 1, col}, {row, col - 1}, {row - 1, col}};

    for (int i = 0; i < 4; i++) {
        // next cell row, col 
        int r = nextPoints[i].first, c = nextPoints[i].second;

        // invalid index 
        if (isOutOfBound(r, c, board.size(), board[0].size())) continue;
        if (board[r][c] != word[curr_index]) continue;

        // mark the cell, considered 
        char ch = board[r][c];
        board[r][c] = '-1';

        bool check = find(board, word, curr_index + 1, r, c);
        board[r][c] = ch; // unmark the cell 

        // and return check result if true 
        if (check) return check;
    }

    // if no where found then return false
    return false;
}

bool exist(vector<vector<char>>& board, string word) {
    for (int i = 0; i < board.size(); i++) {
        for (int j = 0; j < board[i].size(); j++) {
            if (board[i][j] != word[0]) continue;

            char ch = board[i][j];
            board[i][j] = '-1';

            bool check = find(board, word, 1, i, j);
            board[i][j] = ch;

            if (check) return true;
        }
    }

    return false;
}

void p2() {
    // Problem 2 : Leetcode Leetcode 79. Word Search - https://leetcode.com/problems/word-search/ 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/word-search/1 

    vector<vector<char>> grid = {{'a', 'd', 'c', 'a'}, {'a', 'b', 'c', 'd'}};
    string word = "adbc";
    bool check = exist(grid, word);
    cout << check << endl;
}


int main() {
    // Day 3 

    p1();


    return 0;
}