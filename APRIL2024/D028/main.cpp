#include <iostream>
#include <vector>

using namespace std;

bool canPlaceQueen(vector<vector<char>> &grid, int r, int c) {
    for (int it = 0; it < grid.size(); it++) {
        // check rows and cols both sides 
        if (grid[r][it] == 'Q') return false;
        if (grid[it][c] == 'Q') return false;

        // check diagonals all 4 sides 
        if (r + it < grid.size() && c + it < grid.size() && grid[r + it][c + it] == 'Q') return false;
        if (r - it >= 0 && c - it >= 0 && grid[r - it][c - it] == 'Q') return false;
        if (r + it < grid.size() && c - it >= 0 && grid[r + it][c - it] == 'Q') return false;
        if (r - it >= 0 && c + it < grid.size() && grid[r - it][c + it] == 'Q') return false;
    }

    return true;
}

void solve(int n, vector<vector<char>> &grid, int r, vector<vector<string>> &placements) {
    if (r == n) {
        vector<string> temp;
        for (int i = 0; i < n; i++) {
            string str;
            for (int j = 0; j < n; j++) str.push_back(grid[i][j]);
            temp.push_back(str);
        }
        placements.push_back(temp);
        return;
    }

    for (int c = 0; c < grid.size(); c++) {
        if (canPlaceQueen(grid, r, c)) {
            grid[r][c] = 'Q';
            solve(n, grid, r + 1, placements);
            grid[r][c] = '.';
        }
    }
}

vector<vector<string>> solveNQueens(int n) {
    vector<vector<string>> placements;
    vector<vector<char>> grid;
    vector<char> temp;
    for (int j = 0; j < n; j++) temp.push_back('.');
    for (int i = 0; i < n; i++) grid.push_back(temp);

    solve(n, grid, 0, placements);

    return placements;
}

void p1() {
    // Problem 1 : Leetcode 51. N-Queens - https://leetcode.com/problems/n-queens/ 

    int n = 9;

    vector<vector<string>> allPlacements = solveNQueens(n);
    for (int i = 0; i < allPlacements.size(); i++) {
        for (int j = 0; j < allPlacements[i].size(); j++) cout << allPlacements[i][j] << endl;
        cout << endl;
    }
}


int main() {
    // Day 28 

    p1();


    return 0;
}