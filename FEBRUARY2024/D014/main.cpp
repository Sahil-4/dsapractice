#include <iostream>
#include <vector>

using namespace std;

int findZeroes(int arr[], int n, int m) {
    int ans = 0;

    int count = 0;
    int j = -1;

    for (int i = 0; i  < n; i++) {
        if (arr[i] == 0) count++;

        while (count > m) {
            if (arr[++j] == 0) count--;
        }

        int len = i - j;
        if (len > ans) ans = len;
    }

    return ans;
}

void p1() {
    // Problem 1 : Maximize Number of 1's - https://www.geeksforgeeks.org/problems/maximize-number-of-1s0905/1 

    // int arr[] = {1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1};
    int arr[] = {1, 1, 1, 0, 1};
    int n =  sizeof(arr) / sizeof(arr[0]);
    int m = 0;

    int ans = findZeroes(arr, n, m);
    cout << ans << endl;
}

int main() {
    // Day 14 

    p1();


    return 0;
}