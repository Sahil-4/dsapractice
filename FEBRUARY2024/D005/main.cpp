#include <iostream>
#include <vector>

using namespace std;

// function to create transpose 
void transpose(vector<vector<int>>& matrix, int n) { 
    for (int i = 0; i < n; i++) {
        for (int j = i; j < n; j++) {
            int temp = matrix[i][j];
            matrix[i][j] = matrix[j][i];
            matrix[j][i] = temp;
        }
    }
}

//Function to rotate matrix anticlockwise by 90 degrees.
void rotateby90(vector<vector<int> >& matrix, int n) { 
    // code here 
    // first take transpose 
    transpose(matrix, n);
    
    // now swap arr[i][j] with arr[j][n - 1 - i]
    for (int i = 0; i < n/2; i++) {
        for (int j = 0; j < n; j++) {
            int temp = matrix[i][j];
            matrix[i][j] = matrix[n - 1 - i][j];
            matrix[n - 1 - i][j] = temp;
        }
    }
}

void p1() {
    // Problem 1 : Rotate array by 90 degree - https://www.geeksforgeeks.org/problems/rotate-by-90-degree-1587115621/1 

    vector<vector<int>> matrix = {
        {1, 2, 3}, 
        {4, 5, 6}, 
        {7, 8, 9}
        };

    // before 
    for (int i = 0; i < matrix.size(); i++) {
        for (int j = 0; j < matrix.size(); j++) {
            cout << matrix[i][j] << " ";
        }
        cout << endl;
    }

    rotateby90(matrix, matrix.size());

    // after 
    for (int i = 0; i < matrix.size(); i++) {
        for (int j = 0; j < matrix.size(); j++) {
            cout << matrix[i][j] << " ";
        }
        cout << endl;
    }
}

int main() {
    // Day 005 

    p1();


    return 0;
}