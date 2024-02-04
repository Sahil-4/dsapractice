#include <iostream>
#include <vector>
#include <string>

using namespace std;

void transpose(vector<vector<int> >& matrix, int n) { 
    // code here 
    // basically we have to change matrix[i][j] to matrix[j][i] 
    // and matrix[j][i] to matrix[i][j]

    for (int i = 0; i < n; i++) {
        for (int j = i; j < n; j++) {
            int temp = matrix[i][j];
            matrix[i][j] = matrix[j][i];
            matrix[j][i] = temp;
        }
    }
}

void p1() {
    // Problem 1 : Transpose of a Matrix - https://www.geeksforgeeks.org/problems/transpose-of-matrix-1587115621/1 

    // vector<vector<int>> matrix = {{1, 2, 3}, {1, 2, 3}, {1, 2, 3}};
    vector<vector<int>> matrix = {{1, 2}, {1, 2}};
    int n = matrix.size();

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cout << matrix[i][j] << " ";
        }
        cout << endl;
    }

    transpose(matrix, n);

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cout << matrix[i][j] << " ";
        }
        cout << endl;
    }
}

string longestCommonPrefix (string arr[], int N) {
    // find index of smallest string 
    int smallest_string_index = 0;
    for (int i = 0; i < N; i++) {
        if (arr[smallest_string_index].length() > arr[i].length()) smallest_string_index = i;
    }

    // assume lcp size as the size of smallest string 
    int lcp_size = arr[smallest_string_index].length();

    // match other string with smallest string and update the lcp size 
    for (int i = 0; i <  N; i++) {
        if (i == smallest_string_index) continue;
        int l = lcp_size;

        for (int j = 0; j < l; j++) {
            if (arr[smallest_string_index][j] != arr[i][j]) lcp_size = j; // in this if condition there is some problem 
        }
    }

    // no lcp 
    if (lcp_size == 0) return "-1";

    string ans = "";
    for (int i = 0; i < lcp_size; i++) {
        ans = ans + arr[0][i];
    }

    return ans;
}

void p2() {
    // Problem 2 : Longest Common Prefix - https://www.geeksforgeeks.org/problems/longest-common-prefix-in-an-array5129/1 

    string arr[] = {"hell", "hello", "hela", "helicopter"};
    int N = arr->size();

    string ans = longestCommonPrefix(arr, N);
    cout << ans << endl;
}


int main() {
    // Day 4 

    // p1();

    p2();


    return 0;
}