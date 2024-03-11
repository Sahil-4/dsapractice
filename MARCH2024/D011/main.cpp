#include <iostream>
#include <vector>

using namespace std;

void rotate(vector<vector<int>>& matrix) {
    for (int i = 0; i < matrix.size(); i++) {
        for (int j = i; j < matrix.size(); j++) {
            swap(matrix[i][j], matrix[j][i]);
        }
    }
    // Time = O(n * n)

    for (int i = 0; i < matrix.size(); i++) {
        for (int j = 0; j < matrix.size() / 2; j++) {
            swap(matrix[i][j], matrix[i][matrix.size() - 1 - j]);
        }
    }
    // Time = O(n * n)

    // Total time = O(2 * n * n)
    // space = O(1)
}

void p1() {
    // Problem 1 : Rotate Image - https://leetcode.com/problems/rotate-image/description/ 

    vector<vector<int>> matrix = {
        {1, 2, 3, 4},
        {5, 6, 7, 8},
        {9, 10, 11, 12},
        {13, 14, 15, 16}
    };

    rotate(matrix);

    for (int i = 0; i < matrix.size(); i++) {
        for (int j = 0; j < matrix[0].size(); j++) {
            cout << matrix[i][j] << " ";
        }
        cout << endl;
    }
}

int main() {
    // Day 11 

    p1();


    return 0;
}