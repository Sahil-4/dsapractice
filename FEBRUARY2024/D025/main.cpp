#include <iostream>
#include <bits/stdc++.h>

using namespace std;

bool find3Numbers(int A[], int n, int X) {
    // Your Code Here
    sort(A, A+n); // sorting array Tc = O(n * log(n)) 

    for (int i = 0; i < n; i++) {
        int j = i + 1;
        int k = n - 1;

        while (j < k) {
            int sum = A[i] + A[j] + A[k];
            if (sum == X) return true;
            else if (sum < X) j++;
            else k--;
        }

        return false;
    }
}

void p1() {
    // Problem 1 : Triplet sum - https://www.geeksforgeeks.org/problems/triplet-sum-in-array-1587115621/1 

    int arr []= {557, 217, 627, 358, 527, 358, 338, 272, 870, 362, 897, 23, 618, 113, 718, 697, 586, 42, 424, 130, 230, 566, 560, 933};
    int S = 986;
    int size = sizeof(arr) / sizeof(arr[0]);

    int status = find3Numbers(arr, size, S);
    cout << status << endl;
}


int main() {
    // Day 25 

    p1();


    return 0;
}