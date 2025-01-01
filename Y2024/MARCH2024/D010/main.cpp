#include <iostream>
#include <vector>
#include <set>

using namespace std;

void setRowZero(vector<vector<int>>& matrix, int row_number) {
    for (int c = 0; c < matrix[row_number].size(); c++) matrix[row_number][c] = 0;
}

void setColZero(vector<vector<int>>& matrix, int col_number) {
    for (int r = 0; r < matrix.size(); r++) matrix[r][col_number] = 0;
}

void setZeroes_Solution1(vector<vector<int>>& matrix) {
    vector<vector<int>> zeroesCoordintes;
    // Space = O(n * m)

    for (int r = 0; r < matrix.size(); r++) {
        for (int c = 0; c < matrix[r].size(); c++) {
            if (matrix[r][c] == 0) zeroesCoordintes.push_back({r, c, 0});
        }
    }
    // Tn = O(n * m)

    for (int i = 0; i < zeroesCoordintes.size(); i++) {
        setRowZero(matrix, zeroesCoordintes[i][0]);
        setColZero(matrix, zeroesCoordintes[i][1]);
    }
    // Tn = O(n * m)
}

void setZeroes_Solution2(vector<vector<int>>& matrix) {
    set<int> rows;
    set<int> cols;
    // Space = O(n + m)

    for (int r = 0; r < matrix.size(); r++) {
        for (int c = 0; c < matrix[r].size(); c++) {
            if (matrix[r][c] == 0) {
                if (rows.find(r) == rows.end()) rows.insert(r);
                if (cols.find(c) == cols.end()) cols.insert(c);
            }
        }
    }
    // Tn = O(n * m)

    for (int r : rows) {
        setRowZero(matrix, r);

        // Tn = O(n * m)
    }
    for (int c : cols) {
        setColZero(matrix, c);
        // Tn = O(n * m)
    }

    // Time = O(n * m) + O(n * m) + O(n * m) 
    // Space = O(n + m)
    // not best approach 
}

void p1() {
    // Problem 1 : Set matrix zeroes - https://leetcode.com/problems/set-matrix-zeroes/description/ 

    // vector<vector<int>> matrix = { {1, 1, 1}, {1, 0, 1}, {1, 1, 1} };
    // vector<vector<int>> matrix = { {1, 0, 1}, {1, 0, 1}, {1, 1, 1} };
    vector<vector<int>> matrix = { {0, 1, 1}, {1, 0, 1}, {1, 1, 1} };

    setZeroes_Solution2(matrix);

    for (int i = 0; i < matrix.size(); i++) {
        for (int j = 0; j < matrix[i].size(); j++) cout << matrix[i][j] << " ";
        cout << endl;
    }
}

int main() {
    // Day 10 

    p1();


    return 0;
}