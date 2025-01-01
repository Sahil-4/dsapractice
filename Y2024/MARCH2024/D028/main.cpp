#include <iostream>
#include <vector>

using namespace std;

bool searchMatrix_1(vector<vector<int>>& matrix, int target) {
    int low = 0, high = matrix.size() * matrix[0].size() - 1;
    int mid = low + (high - low) / 2;

    // m = 9 [2, 1] 
    // [2, 1] = 9 / total_col, 9 % total_col
    // [2, 1] = 9 / 4, 9 % 4
    // [2, 1] = [2, 1]

    // m = 10 [2, 2] 
    // [2, 2] = 10 / total_col, 10 % total_col
    // [2, 2] = 10 / 4, 10 % 4
    // [2, 2] = [2, 2]

    while (low <= high) {
        int row = mid / matrix[0].size();
        int col = mid % matrix[0].size();
        int e = matrix[row][col];

        if (e == target) return true;
        else if (e < target) low = mid + 1;
        else high = mid - 1;

        mid = low + (high - low) / 2;
    }

    return false;
}

void p1() {
    // P1 LC 74. Search a 2D Matrix - https://leetcode.com/problems/search-a-2d-matrix/description/ 

    vector<vector<int>> matrix = {{1,3,5,7}, {10,11,16,20}, {23,30,34,60}}; 
    int target = 3;

    if (searchMatrix_1(matrix, target)) cout << "found" << endl;
    else cout << "not found" << endl;
}

bool searchMatrix(vector<vector<int>>& matrix, int target) {
    int row = 0, col = matrix[0].size() - 1;

    while (row < matrix.size() && col >= 0) {
        int e = matrix[row][col];

        if (e == target) return true;
        else if (e > target) col--;
        else row++;
    }

    return false;
}

void p2() {
    // Problem 2 : LC 240. Search a 2D Matrix II - https://leetcode.com/problems/search-a-2d-matrix-ii/ 

    vector<vector<int>> matrix = {{1,4,7,11,15}, {2,5,8,12,19}, {3,6,9,16,22},{10,13,14,17,24},{18,21,23,26,30}}; 
    int target = 5;

    if (searchMatrix(matrix, target)) cout << "found" << endl;
    else cout << "not found" << endl;
}

int main() {
    // Day 28 

    p1();

    p2();


    return 0;
}