#include <iostream>
#include <vector>

using namespace std;

void inverseMatrix_opposite(vector<vector<int>>& matrix) {
    int n = matrix.size();
    n = n - 1;
    for (int r = 0; r <= n; r++) {
        for (int c = n - r; c >= 0; c--) {
            swap(matrix[r][c], matrix[n - c][n - r]);
        }
    }
}

void inverseMatrix(vector<vector<int>>& matrix) {
    int n = matrix.size();
    for (int r = 0; r < n; r++) {
        for (int c = r; c < n; c++) swap(matrix[r][c], matrix[c][r]);
    }
}

void reverseMatrix(vector<vector<int>>& matrix) {
    int n = matrix.size();
    for (int r = 0; r < n; r++) {
        for (int c = 0; c < n / 2; c++) swap(matrix[r][c], matrix[r][n - c - 1]);
    }
}

void rotate(vector<vector<int>>& matrix) {
    inverseMatrix(matrix);
    reverseMatrix(matrix);
}

void p1() {
    // Problem 1 : Leetcode 48. Rotate Image - https://leetcode.com/problems/rotate-image/ 
    // GeeksForGeeks - https://www.geeksforgeeks.org/problems/rotate-by-90-degree-1587115621/1 

    vector<vector<int>> matrix = {{1, 2, 3, 4, 5}, {6, 7, 8, 9, 10}, {11, 12, 13, 14, 15}, {16, 17, 18, 19, 20}, {21, 22, 23, 24, 25}};
    rotate(matrix);
    for (int i = 0; i < matrix.size(); i++) {
        for (int j = 0; j < matrix.size(); j++) cout << matrix[i][j] << " ";
        cout << endl;
    }
}

int main() {
    // Day 11 

    p1();


    return 0;
}