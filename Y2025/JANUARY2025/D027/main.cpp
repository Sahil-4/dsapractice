#include <bits/stdc++.h>

using namespace std;

class Problem1 {
    // up, right, bottom, left
    int DR[4] = { -1, 0, +1, 0 };
    int DC[4] = { 0, +1, 0, -1 };

    void dfs(int i, int j, vector<vector<char>>& grid, vector<vector<bool>>& visited) {
        visited[i][j] = true;
        for (int k = 0; k < 4; k++) {
            int ni = i + DR[k], nj = j + DC[k];
            if (ni < 0 || nj < 0 || ni >= grid.size() || nj >= grid[0].size()) continue;
            if (grid[ni][nj] == '0') continue;
            if (visited[ni][nj]) continue;
            dfs(ni, nj, grid, visited);
        }
    }

    int solve1(vector<vector<char>>& grid) {
        int N = grid.size();
        int M = grid[0].size();

        vector<vector<bool>> visited(N, vector<bool>(M, false));
        int islands = 0;

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (grid[i][j] == '0' || visited[i][j]) continue;
                dfs(i, j, grid, visited);
                islands++;
            }
        }

        return islands;

        // Complexity analysis 
        // Time : O(N*N) 
        // Space : O(N*M) 
    }

    void bfs(int i, int j, vector<vector<char>>& grid, vector<vector<bool>>& visited) {
        stack<pair<int, int>> stk;
        visited[i][j] = true;
        stk.push({ i, j });

        while (!stk.empty()) {
            pair<int, int> top = stk.top(); stk.pop();
            int i = top.first, j = top.second;

            for (int k = 0; k < 4; k++) {
                int ni = i + DR[k], nj = j + DC[k];

                if (ni < 0 || nj < 0 || ni >= grid.size() || nj >= grid[0].size()) continue;
                if (grid[ni][nj] == '0') continue;
                if (visited[ni][nj]) continue;

                visited[ni][nj] = true;
                stk.push({ ni, nj });
            }
        }
    }

    int solve2(vector<vector<char>>& grid) {
        int N = grid.size();
        int M = grid[0].size();

        vector<vector<bool>> visited(N, vector<bool>(M, false));
        int islands = 0;

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (grid[i][j] == '0' || visited[i][j]) continue;
                bfs(i, j, grid, visited);
                islands++;
            }
        }

        return islands;

        // Complexity analysis 
        // Time : O(N*N) 
        // Space : O(N*M) 
    }

public:
    int numIslands(vector<vector<char>>& grid) {
        // return solve1(grid);

        return solve2(grid);
    }
};

void p1() {
    // Problem 1 : Leetcode 200. Number of Islands - https://leetcode.com/problems/number-of-islands/description/?envType=study-plan-v2&envId=top-interview-150 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/find-the-number-of-islands/1 

    vector<vector<char>> grid = { {'1','1','1','1','0'},  {'1','1','0','1','0'},  {'1','1','0','0','0'},  {'0','0','0','0','0'} };
    cout << Problem1().numIslands(grid) << endl;
}

class Problem2 {
    // top, right, bottom, left 
    int DDirections[4][2] = { {-1, 0}, {0, +1}, {+1, 0}, {0, -1} };
    int DD = 4;

    void markSave(int i, int j, vector<vector<char>>& board) {
        board[i][j] = '$';

        for (int k = 0; k < DD; k++) {
            int ni = i + DDirections[k][0], nj = j + DDirections[k][1];

            if (ni < 0 || nj < 0 || ni >= board.size() || nj >= board[0].size()) continue;
            if (board[ni][nj] != 'O') continue;

            markSave(ni, nj, board);
        }
    }

public:
    void solve(vector<vector<char>>& board) {
        int M = board.size(), N = board[0].size();

        // save all O's connected to edge (mark $) 
        for (int r = 0; r < M; r++) {
            int row_first = 0, row_last = N - 1;
            if (board[r][row_first] == 'O') markSave(r, row_first, board);
            if (board[r][row_last] == 'O') markSave(r, row_last, board);
        }
        // save all O's connected to edge (mark $) 
        for (int c = 0; c < N; c++) {
            int col_first = 0, col_last = M - 1;
            if (board[col_first][c] == 'O') markSave(col_first, c, board);
            if (board[col_last][c] == 'O') markSave(col_last, c, board);
        }

        // convert all O's to X 
        for (int i = 0; i < M; i++) {
            for (int j = 0; j < N; j++) {
                if (board[i][j] == 'O') board[i][j] = 'X';
            }
        }

        // convert all markes $'s to O 
        for (int i = 0; i < M; i++) {
            for (int j = 0; j < N; j++) {
                if (board[i][j] == '$') board[i][j] = 'O';
            }
        }

        // Complexity analysis 
        // Time : O(M*N) + O(2 * M*N) 
        // Space : O(1) + O(N*M) stack 
    }
};

void p2() {
    // Problem 2 : Leetcode 130. Surrounded Regions - https://leetcode.com/problems/surrounded-regions/?envType=study-plan-v2&envId=top-interview-150 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/replace-os-with-xs0052/1 

    vector<vector<char>> board = { {'X','X','X','X'},{'X','O','O','X'},{'X','X','O','X'},{'X','O','X','X'} };
    Problem2().solve(board);

    for (vector<char> v : board) {
        for (char c : v) cout << c << " ";
        cout << endl;
    }
}


int main() {
    // Day 27 of January 2025 

    p1();

    p2();


    return 0;
}