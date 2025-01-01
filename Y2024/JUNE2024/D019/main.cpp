#include <iostream>
#include <limits.h>
#include <vector>

using namespace std;

int getIthElement(int arr[], int n, int i) {
    if (i == -1 || i == n) return INT_MIN;
    return arr[i];
}

int peakElement(int arr[], int n) {
    // Your code here
    int ans_index = -1;
    int low = 0, high = n - 1;
    
    while (low <= high) {
        int mid = low + (high - low) / 2;
        
        if (getIthElement(arr, n, mid) >= getIthElement(arr, n, mid - 1) && getIthElement(arr, n, mid) >= getIthElement(arr, n, mid + 1)) {
            return mid;
        } 
        else if (getIthElement(arr, n, mid) >= getIthElement(arr, n, mid - 1)) low = mid + 1;
        else high = mid - 1;
    }
    
    return -1;
}

void p1() {
    // Problem 1 : Leetcode 162. Find Peak Element - https://leetcode.com/problems/find-peak-element/ 
    // GeeksForGeeks - https://www.geeksforgeeks.org/problems/peak-element/1 

    int arr[] = {1, 2, 3, 2, 0};
    int n = 5;
    int peak = peakElement(arr, n);
    cout << "peak :: " << peak << endl;
}

int findMaxElement(vector<int>& arr) {
    int badeWalaIndex = 0;

    for (int i = 1; i < arr.size(); i++) if (arr[badeWalaIndex] < arr[i]) badeWalaIndex = i;

    return badeWalaIndex;
}


vector<int> findPeakGrid(vector<vector<int>>& mat) {
    int n = mat.size();

    for (int r = 0; r < n; r++) {
        int idx = findMaxElement(mat[r]);
        if ((r == 0 || mat[r][idx] >= mat[r - 1][idx]) && (r == n - 1 || mat[r][idx] >= mat[r + 1][idx])) return {r, idx};
    }
}

void p2() {
    // Problem 2 : Leetcode 1901. Find a Peak Element II - https://leetcode.com/problems/find-a-peak-element-ii/ 

    vector<vector<int>> mat = {
        {7,2,3,1,2}, {6,5,4,2,1}
    };
    vector<int> peak = findPeakGrid(mat);
    cout << "peak :: " << mat[peak[0]][peak[1]];
}

int main() {
    // Day 19 

    p1();

    p2();


    return 0;
}